#!/usr/bin/env python3
"""Check the financial claims in the California 2026 ballot explainer.

Reads ca-2026-ballot/index.html and compares it with tools/verify_fiscal/official_fiscal_2026.json.
Those pins are the enacted 2026-27 budget and the Legislative Analyst's Office ballot analyses.
The script does not use the network. Re-pin the JSON when the source documents change.

Exit status is 1 when any check is FAIL. WARN and NOTE do not fail the run.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "ca-2026-ballot" / "index.html"
PIN = Path(__file__).resolve().parent / "official_fiscal_2026.json"

# A displayed billion is accepted when it is within this many dollars of the pin.
MILLION = 1_000_000


class Check:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    def add(self, level: str, name: str, detail: str) -> None:
        self.rows.append((level, name, detail))

    def fail(self, name: str, detail: str) -> None:
        self.add("FAIL", name, detail)

    def warn(self, name: str, detail: str) -> None:
        self.add("WARN", name, detail)

    def note(self, name: str, detail: str) -> None:
        self.add("NOTE", name, detail)

    def ok(self, name: str, detail: str) -> None:
        self.add("PASS", name, detail)


def slice_const(html: str, name: str) -> str:
    key = f"const {name}="
    i = html.index(key) + len(key)
    while html[i].isspace():
        i += 1
    start = i
    depth = 0
    in_str = False
    quote = ""
    j = i
    while j < len(html):
        c = html[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == quote:
                in_str = False
            j += 1
            continue
        if c in "'\"":
            in_str = True
            quote = c
            j += 1
            continue
        if c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
            if depth == 0:
                return html[start : j + 1]
        j += 1
    raise ValueError(f"unbalanced {name}")


def js_to_data(src: str):
    """Convert the page's data object, which uses single quotes and bare keys, to JSON."""
    out: list[str] = []
    i = 0
    while i < len(src):
        if src[i] == "'":
            buf: list[str] = []
            i += 1
            while i < len(src):
                if src[i] == "\\":
                    buf.append(src[i + 1])
                    i += 2
                    continue
                if src[i] == "'":
                    i += 1
                    break
                buf.append(src[i])
                i += 1
            out.append(json.dumps("".join(buf)))
            continue
        out.append(src[i])
        i += 1
    text = "".join(out)
    text = re.sub(r"([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2":', text)
    text = re.sub(r"(?<=[:\s])\.(\d)", r"0.\1", text)
    return json.loads(text)


def billions(value: float) -> int:
    """Page figures are in billions. Return the nearest dollar."""
    return round(value * 1_000_000_000)


def money_b(value: float) -> str:
    """Reproduce the page's moneyB display."""
    if value >= 10:
        return f"${value:.1f}B"
    text = f"{value:.2f}".rstrip("0")
    if text.endswith("."):
        text += "0"
    return f"${text}B"


def near(actual: int, expected: int, tolerance: int = MILLION) -> bool:
    return abs(actual - expected) <= tolerance


def main() -> int:
    html = PAGE.read_text()
    pin = json.loads(PIN.read_text())
    budget = js_to_data(slice_const(html, "budget2026"))
    impacts = js_to_data(slice_const(html, "annualImpacts"))
    large = js_to_data(slice_const(html, "largeFiscalEffects"))
    checks = Check()

    gf = pin["general_fund_millions"]
    funds = pin["all_funds_millions"]
    spend_pin = pin["spending_thousands"]

    revenue = budget["revenueSources"]
    spending = budget["spending"]
    all_funds = budget["allFunds"]
    gross = sum(item["value"] for item in revenue)
    spend_sum = sum(item["value"] for item in spending)
    all_sum = sum(item["value"] for item in all_funds)
    transfers = budget["netTransfers"]
    resources = budget["annualResources"]
    balance_use = spend_sum - resources

    # Revenue lines follow LAO Figure 4, in millions.
    revenue_pins = {
        "Personal income tax": gf["personal_income_tax"]["lao"],
        "Corporation tax": gf["corporation_tax"]["lao"],
        "Sales & use tax": gf["sales_and_use_tax"]["lao"],
        "Insurance + other revenue": gf["insurance_tax"]["lao"] + gf["other_revenues"]["lao"],
    }
    for item in revenue:
        expected = revenue_pins[item["label"]] * MILLION
        actual = billions(item["value"])
        if actual == expected:
            checks.ok(
                item["label"],
                f"stored ${item['value']:.3f}B matches LAO Figure 4 (${revenue_pins[item['label']]:,} million). "
                f"The page displays {money_b(item['value'])}.",
            )
        else:
            checks.fail(item["label"], f"page {actual:,} dollars; LAO {expected:,} dollars")

    gross_dollars = billions(gross)
    lao_gross = (
        gf["personal_income_tax"]["lao"]
        + gf["corporation_tax"]["lao"]
        + gf["sales_and_use_tax"]["lao"]
        + gf["insurance_tax"]["lao"]
        + gf["other_revenues"]["lao"]
    ) * MILLION
    schedule_gross = (
        gf["personal_income_tax"]["schedule_8_thousands"]
        + gf["corporation_tax"]["schedule_8_thousands"]
        + gf["sales_and_use_tax"]["schedule_8_thousands"]
        + gf["insurance_tax"]["schedule_8_thousands"]
        + gf["other_revenues"]["schedule_8_thousands"]
    ) * 1000
    if gross_dollars == lao_gross:
        checks.ok(
            "Gross revenue",
            f"sum of the four LAO lines is ${gross:.3f}B, displayed as {money_b(gross)}. "
            f"Schedule 8 gross revenue is ${schedule_gross/1e9:.3f}B.",
        )
    else:
        checks.fail("Gross revenue", f"page sum {gross_dollars:,}; LAO lines {lao_gross:,}")

    implied = gross + transfers
    gap = round((implied - resources) * 1_000_000_000)
    if gap == MILLION:
        checks.note(
            "Revenues and transfers",
            "Rounded LAO lines sum to $226.755B. The page stores the official total $226.754B. "
            f"The $1 million gap is the same rounding residual in LAO Figure 4. Schedule 8 is ${gf['revenues_and_transfers']['schedule_8_thousands']*1000:,}.",
        )
    elif gap == 0:
        checks.ok("Revenues and transfers", money_b(resources))
    else:
        checks.fail(
            "Revenues and transfers",
            f"gross {gross:.3f} plus transfers {transfers:.3f} is {implied:.3f}; page stores {resources:.3f}",
        )

    if billions(transfers) == gf["transfers_and_loans"]["lao"] * MILLION:
        checks.ok("Net transfers and loans", f"{money_b(abs(transfers))} matches LAO Figure 4")
    else:
        checks.fail("Net transfers and loans", f"page {transfers}; LAO {gf['transfers_and_loans']['lao']}")

    if billions(resources) == gf["revenues_and_transfers"]["lao"] * MILLION:
        checks.ok("Current-year resources", "$226.754B matches LAO revenues and transfers")
    else:
        checks.fail("Current-year resources", f"page {resources}")

    spend_map = {item["label"]: item["value"] for item in spending}
    for key, spec in spend_pin.items():
        label = spec["page_key"]
        actual = billions(spend_map[label])
        official = spec["official"] * 1000
        if actual == official:
            checks.ok(label, f"${actual:,} matches the Schedule 9 rollup")
        elif near(actual, official):
            checks.note(label, f"page ${actual:,}; Schedule 9 rollup ${official:,}; difference ${actual-official:,}")
        else:
            checks.fail(label, f"page ${actual:,}; official ${official:,}")

    gov = spend_pin["government_courts_executive"]
    part_sum = sum(gov["parts_thousands"].values()) * 1000
    if part_sum == gov["official"] * 1000 and "Government, courts & executive" not in html:
        checks.ok("Government bar label", "The $16.554B bar is labeled as more than courts and executive offices")
    elif part_sum == gov["official"] * 1000:
        checks.warn(
            "Government, courts and executive label",
            "The $16.554B total matches Legislative, Judicial, and Executive plus Government Operations plus General Government. "
            "General Government includes retiree health ($3.205B), supplemental pension payments ($0.556B), and a Proposition 98 reconciliation (−$1.066B). "
            "The label describes courts and executive offices only.",
        )
    else:
        checks.fail("Government bar parts", f"parts sum ${part_sum:,}; pin ${gov['official']*1000:,}")

    other = spend_pin["other_agencies"]
    other_sum = sum(other["parts_thousands"].values()) * 1000
    if other_sum == other["official"] * 1000:
        checks.ok(
            "Other agencies rollup",
            "Business, environment, housing, labor, natural resources, and transportation sum to $9,017,995,000",
        )
    else:
        checks.fail("Other agencies rollup", f"parts ${other_sum:,}; pin ${other['official']*1000:,}")

    enacted = gf["expenditures"]["schedule_9_thousands"] * 1000
    page_spend = billions(spend_sum)
    if page_spend - enacted == 5000:
        checks.note(
            "Six-category spending sum",
            f"Page sum ${page_spend:,} is $5,000 above Schedule 9 expenditures ${enacted:,}, "
            "because other agencies is rounded from $9,017.995 million to $9.018 billion. "
            f"The donut uses {budget['allFunds'][0]['value']} and both displays round to {money_b(budget['allFunds'][0]['value'])}.",
        )
    else:
        checks.fail("Six-category spending sum", f"page ${page_spend:,}; Schedule 9 ${enacted:,}")

    fund_pins = {
        "General Fund": funds["general_fund"]["lao"],
        "Special funds": funds["special_funds"]["lao"],
        "Bond funds": funds["bond_funds"]["lao"],
        "Federal funds": funds["federal_funds"]["lao"],
    }
    for item in all_funds:
        expected = fund_pins[item["label"]] * MILLION
        actual = billions(item["value"])
        if actual == expected:
            checks.ok(item["label"], f"{money_b(item['value'])} matches LAO Figure 5")
        else:
            checks.fail(item["label"], f"page {actual:,}; LAO {expected:,}")

    state_only = billions(
        next(i["value"] for i in all_funds if i["label"] == "General Fund")
        + next(i["value"] for i in all_funds if i["label"] == "Special funds")
    )
    dof_state_funds = (
        funds["general_fund"]["schedule_9_thousands"]
        + funds["special_funds"]["schedule_9_thousands"]
        + funds["bond_funds"]["schedule_9_thousands"]
    ) * 1000
    checks.note(
        "State spending label",
        f"The page's state-spending total, General Fund plus special funds, is ${state_only/1e9:.3f}B. "
        f"That matches the LAO budget total. The Department of Finance total-state-funds figure is ${dof_state_funds/1e9:.3f}B because it also includes bond funds.",
    )

    simple_gap = gf["expenditures"]["lao"] - gf["revenues_and_transfers"]["lao"]
    deficit = budget["operatingDeficit"]
    dof_deficit = gf["operating_deficit"]["dof_millions"]
    reconstructed = gf["expenditures"]["lao"] - (
        gf["revenues_and_transfers"]["lao"] + gf["tsha_deposit"]["dof_chart_millions"]
    )
    if reconstructed != dof_deficit:
        checks.fail(
            "Operating-deficit arithmetic",
            f"reconstruction {reconstructed} does not equal the pinned DOF cell {dof_deficit}",
        )
    else:
        checks.ok(
            "Operating-deficit arithmetic",
            f"251,477 − (226,754 + 6,388) = {dof_deficit} million dollars",
        )
    if deficit == gf["operating_deficit"]["lao_prose_billions"] and "rounds the administration’s $18.3B estimate to $18.5B" in html:
        checks.ok(
            "Operating deficit displayed as $18.5B",
            "The page attributes $18.5B to the LAO's rounding of the administration's $18.3B estimate",
        )
    elif deficit == gf["operating_deficit"]["lao_prose_billions"]:
        checks.warn(
            "Operating deficit displayed as $18.5B",
            "The page matches the LAO sentence, which rounds the administration's figure to $18.5 billion. "
            f"The Department of Finance cell is ${dof_deficit/1000:.3f}B. "
            f"The simple spending-minus-revenue gap is ${simple_gap/1000:.3f}B and equals the draw on the prior-year balance. "
            f"The page's sankey bridge is {money_b(balance_use)}.",
        )
    else:
        checks.fail("Operating deficit", f"page {deficit}; LAO prose {gf['operating_deficit']['lao_prose_billions']}")

    reserves = gf["reserves_bsa_plus_sfeu_millions"]
    checks.note(
        "Broadly usable reserves",
        f"Budget Stabilization Account ${gf['bsa_end_2026_27_millions']/1000:.3f}B plus the Special Fund for Economic Uncertainties "
        f"${gf['sfeu_end_2026_27_millions']/1000:.3f}B is ${reserves/1000:.3f}B at the end of 2026-27. "
        f"The school reserve is a separate ${gf['school_reserve_billions']}B. The page says about $20B.",
    )

    # Proposition ranges. Endpoints the LAO did not publish are warnings, not silent passes.
    by_prop = {item["prop"]: item for item in impacts}
    props = pin["propositions"]

    def displayed_pct(billions_value: float) -> str:
        return f"{(billions_value / spend_sum * 100):.2f}%"

    for number, low, high, years in ((1, 0.5, 0.6, 25), (38, 0.5, 0.6, 20)):
        row = by_prop[number]
        spec = props[str(number)]
        if row["low"] == low and row["high"] == high and spec["years"] == years:
            unrounded_low = low / 251.477 * 100
            checks.note(
                f"Prop {number} share of the General Fund",
                f"The LAO annual cost is ${spec['annual_cost_millions'][0]}–${spec['annual_cost_millions'][1]} million for about {years} years, "
                f"and the LAO calls that about 0.25 percent. The page's {displayed_pct(low)}–{displayed_pct(high)} "
                f"is ${low*1000:.0f}–${high*1000:.0f} million divided by the $251.477B expenditure total "
                f"({unrounded_low:.3f} percent at the low end, unrounded).",
            )
        else:
            checks.fail(f"Prop {number} annual cost", f"page {row}; LAO {spec['annual_cost_millions']} over {years} years")

    if "CalVet revenue bond" in html:
        checks.fail(
            "Prop 1 CalVet instrument",
            "The flow chart calls the $1.25B veterans piece a revenue bond. "
            "The LAO and the bond statute call the entire $11.25B general-obligation bonds. "
            "Veterans' payments have covered that debt service. Full faith and credit still applies.",
        )
    else:
        checks.ok("Prop 1 CalVet instrument", "The page does not call the veterans bond a revenue bond")

    p3 = props["3"]
    card = next(item for item in large if item["prop"] == 3)
    if card.get("range") == p3["annual_revenue_maintained_billions"]:
        low, high = card["range"]
        checks.note(
            "Prop 3 share of the General Fund",
            f"The LAO range is ${low}–${high} billion a year and does not state a percentage. "
            f"Against $251.477B, that is {low/251.477*100:.2f}–{high/251.477*100:.2f} percent. The page says about 2–6 percent.",
        )
    else:
        checks.fail("Prop 3 revenue range", f"page {card.get('range')}")

    p39 = by_prop[39]
    if "low" not in p39 and p39.get("approx") and p39.get("pctText"):
        checks.ok("Prop 39 bar endpoints", "No dollar endpoints are printed; the label quotes LAO wording and the bar is marked approximate")
    else:
        checks.warn(
            "Prop 39 bar endpoints",
            f"The page draws ${p39['low']*1000:.0f}–${p39['high']*1000:.0f} million and its percent function prints "
            f"{displayed_pct(p39['low'])}–{displayed_pct(p39['high'])}. "
            f"Unrounded, ${p39['low']*1000:.0f} million is {p39['low']/spend_sum*100:.4f} percent, which toFixed(2) turns into "
            f"{displayed_pct(p39['low'])}. The LAO published no dollar endpoints. It says tens to low hundreds of millions "
            "of state and local costs, less than 0.25 percent of the General Fund.",
        )

    p40 = by_prop[40]
    if p40["high"] == 1 and p40.get("uncertain"):
        checks.note(
            "Prop 40 ongoing loss",
            "The bar tops out at $1B. The LAO says the ongoing income-tax loss would probably be less than $1B a year, "
            "and that one-time revenue is tens of billions with no tighter official range.",
        )
    else:
        checks.fail("Prop 40 ongoing loss", str(p40))

    p45 = by_prop[45]
    if "low" not in p45 and p45.get("approx") and p45.get("pctText"):
        checks.ok("Prop 45 bar endpoints", "No dollar endpoints are printed; the label quotes LAO wording and the bar is marked approximate")
    else:
        checks.warn(
            "Prop 45 bar endpoints",
            f"The page draws ${p45['low']*1000:.0f}–${p45['high']*1000:.0f} million. "
            "The LAO says initial state and local costs likely in the high tens of millions and potentially over $100 million, "
            "partly fee-funded, with no floor or ceiling. Costs are for the first several years.",
        )

    if "revenue bond" in html and "Up to $25B" in html:
        checks.ok("Prop 37 instrument", "The $25B authorization is labeled a revenue-bond authority")

    counts = {level: sum(1 for row in checks.rows if row[0] == level) for level in ("FAIL", "WARN", "NOTE", "PASS")}
    print(f"Fiscal check of {PAGE.relative_to(ROOT)}")
    print(f"Pins: {PIN.relative_to(ROOT)}")
    print(
        f"{counts['PASS']} passed, {counts['NOTE']} notes, {counts['WARN']} warnings, {counts['FAIL']} failures"
    )
    print()
    for level, name, detail in checks.rows:
        print(f"[{level}] {name}")
        print(f"    {detail}")
        print()
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
