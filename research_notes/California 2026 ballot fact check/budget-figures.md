# California 2026–27 enacted budget figures

Scope: the hardcoded `budget2026` object and the surrounding claims on `ca-2026-ballot/index.html`. Snapshot date on the page is October 5, 2026. All dollar figures below are administration estimates of the *enacted* 2026 Budget Act unless noted. The LAO overview uses those administration estimates; it is not an independent LAO revenue forecast.

Primary documents opened:

- LAO, *The 2026-27 Budget: Overview of the Spending Plan*, August 26, 2026, HTML and PDF — [Report 5197](https://lao.ca.gov/Publications/Report/5197), [PDF](https://lao.ca.gov/reports/2026/5197/2026-27_Budget_Overview_of_Spending_Plan_082626.pdf). Every LAO table is footnoted: “Reflects administration estimates of budget actions taken through July 1, 2026.”
- Department of Finance, Schedule 8 (revenues), Schedule 9 (expenditures), and Schedule 10 (fund condition), all “AT 2026 BUDGET ACT,” header date June 2026, dollars in thousands — [Schedule 8](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH8.pdf), [Schedule 9](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH9.pdf), [Schedule 10](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH10.pdf).
- Department of Finance, *General Fund Multiyear Forecast, 2026 Budget Act*, dollars in millions — [MultiYearProjection.pdf](https://www.ebudget.ca.gov/reference/MultiYearProjection.pdf). Note on that PDF: “Totals may not add due to rounding.”
- Department of Finance, enacted Budget Summary introduction — [Introduction.pdf](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/Introduction.pdf).
- Department of Finance enacted overview (rendered page) — [2026-27 Budget Overview, enacted route](https://ebudget.ca.gov/budget/e/2026-27/BudgetOverview).

The page’s source link `https://ebudget.ca.gov/budget/m/2026-27/BudgetDetail` is a JavaScript app. A plain fetch returned no figures. On prior-year ebudget URLs, `m` is the May Revision (“Revised Budget Detail”) and `e` is enacted. The enacted overview that matches these numbers is the `e` route above, not the January proposal and not the May Revision.

## Do the revenue lines, net transfers, and annual resources match, and what is the $1 million gap?

### Takeaway

The four revenue components and the net-transfer line are the LAO Figure 4 millions, and `annualResources` of 226.754 is the official “revenues and transfers” total. Gross revenue plus net transfers does **not** equal 226.754 at the page’s displayed precision: the $0.001 billion ($1 million) gap is a rounding residual from adding figures already rounded to the nearest million. It is not a hidden beginning balance or another revenue line. At the unrounded Schedule 8 level, gross revenue plus transfers and loans equals revenues and transfers exactly.

### Cited Findings

- Schedule 8, 2026–27 General Fund, dollars in thousands — [Schedule 8](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH8.pdf):
  - Personal income tax (4116200): **145,608,654**
  - Corporation tax (4110800): **45,166,625**
  - Retail sales and use tax (4117000): **35,598,189**
  - Insurance gross premiums tax (4113400): **4,727,503**
  - Other General Fund major taxes: alcoholic beverage excise, beer and wine **145,861** + distilled spirits **269,491** = **415,352**; cigarette tax (4110400) **34,027**; mobilehome in-lieu tax (4114000) **972**; motor-vehicle license in-lieu, General Fund portion (4115300) **2**. Those four sum to **450,353**.
  - Total, major taxes and licenses: **231,551,324**. Check: 145,608,654 + 45,166,625 + 35,598,189 + 4,727,503 + 450,353 = 231,551,324.
  - Total, minor revenues: **5,807,505** (regulatory taxes and licenses, investment income, and miscellaneous). Investment-income total within that is **2,575,573**.
  - Total, revenues (gross, before transfers and loans): **237,358,829**. Check: 231,551,324 + 5,807,505 = 237,358,829.
  - Transfers and loans: loans **−1,005,300**; revenue transfers **−9,599,397**; total transfers and loans **−10,604,697**.
  - Total, revenues, transfers, and loans: **226,754,132**. Check: 237,358,829 + (−10,604,697) = 226,754,132.
- LAO Figure 4, “General Fund Revenue Estimates,” dollars in millions, enacted 2026–27 — [Report 5197](https://lao.ca.gov/Publications/Report/5197):
  - Personal income tax **$145,609**
  - Sales and use tax **$35,598**
  - Corporation tax **$45,167**
  - Total, major revenue sources **$226,373** (the three lines sum to **$226,374**; the printed subtotal is $1 million lower)
  - Insurance tax **$4,728**
  - Other revenues **$6,258**
  - Transfers and loans **−$10,605**
  - Totals, revenues and transfers **$226,754**
- Unrounded “other revenues” = other major taxes 450.353 + minor revenues 5,807.505 = **6,257.858 million**, which rounds to the LAO’s **$6,258 million**.
- Unrounded insurance + other = 4,727.503 + 6,257.858 = **10,985.361 million**. The page’s **10.986** is 4,728 + 6,258, the sum of the two already-rounded LAO lines, **$0.639 million higher** than Schedule 8.
- Schedule 10 General Fund, 2026–27, dollars in thousands — [Schedule 10](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH10.pdf): beginning reserve **57,221,020**; revenues **226,754,132**; expenditures **251,477,209**; ending reserve **32,497,943**. Check: 57,221,020 + 226,754,132 − 251,477,209 = 32,497,943.
- DOF enacted overview chart, dollars in millions — [enacted Budget Overview](https://ebudget.ca.gov/budget/e/2026-27/BudgetOverview): revenues total **$226,754**; personal income tax **$145,609**; corporation tax **$45,167**; sales and use tax **$35,598**; insurance tax **$4,728**; other **$5,614**; transfer to the BSA **−$3,574**; Projected Surplus Temporary Holding Account **−$6,388**. Those chart lines sum to 226,754. The chart’s “Other” of $5,614 is **not** the LAO’s “other revenues” of $6,258. It is a residual plug: rounded big-three-plus-insurance ($231,102 million) subtracted from revenues before the BSA and holding-account transfers ($236,716 million). The plug nets miscellaneous revenue together with the transfers and loans that are **not** the BSA or the holding account (about **−$643 million**). The page does not use that plug. It follows LAO Figure 4.
- DOF multiyear, dollars in millions — [MultiYearProjection.pdf](https://www.ebudget.ca.gov/reference/MultiYearProjection.pdf), 2026–27: revenues/transfers **$236,716** (before the two lines below); transfer to the BSA **−$3,574**; transfer to the Surplus Account **−$6,388**. Check: 236,716 − 3,574 − 6,388 = **226,754**.
- Page arithmetic, values as stored, billions: 145.609 + 45.167 + 35.598 + 10.986 = **237.360**. Then 237.360 + (−10.605) = **226.755**. Stored `annualResources` is **226.754**. Gap = **$0.001 billion = $1 million**.

### Inferences

- Verdicts versus Schedule 8 (exact thousands) and versus the LAO millions the page actually stored:
  - Personal income tax 145.609: **ROUNDED**. Schedule 8 is $145,608.654 million. Nearest million, and the LAO line, is $145,609 million. Page is **$346,000 high**.
  - Corporation tax 45.167: **ROUNDED**. Schedule 8 is $45,166.625 million. Nearest million and the LAO line are $45,167 million. Page is **$375,000 high**.
  - Sales and use tax 35.598: **ROUNDED**, but only by the amount already inside the nearest million. Schedule 8 is $35,598.189 million. Page matches the LAO’s $35,598 million and is **$189,000 low**.
  - Insurance + other revenue 10.986: **ROUNDED**. Faithful combination of LAO insurance tax $4,728 million and LAO other revenues $6,258 million. Schedule 8 sum of those concepts is $10,985.361 million. Page is **$639,000 high**. Combining is acceptable; the total matches the LAO split, not a separate DOF “other” of $5,614 million.
  - What was combined into “Insurance + other revenue,” using Schedule 8: insurance gross premiums tax; the small General Fund major taxes (beer and wine, distilled spirits, cigarettes, mobilehome in-lieu, and a $2,000 vehicle-license residue); and all minor revenues (regulatory fees and licenses, pooled-money and other investment income, miscellaneous revenue such as abandoned property). Cannabis excise tax is in special funds, not this General Fund line.
  - Net transfers −10.605: **ROUNDED**. Schedule 8 transfers and loans are −$10,604.697 million. Nearest million and the LAO line are −$10,605 million. Page is **$303,000 too negative**. The line is all transfers and loans, not only the BSA and the holding account. Those two are −$3,574 million and −$6,388 million. The rest of the −$10.605 billion is other revenue transfers and loans.
  - `annualResources` 226.754: **ACCURATE** at the million the page stores, **ROUNDED** versus Schedule 8’s $226,754.132 million (page is **$132,000 low**). This is “revenues, transfers, and loans,” not total resources.
  - Implied gross revenue 237.36: **ROUNDED**. It is the sum of the rounded LAO lines ($237,360 million). Schedule 8 gross revenue is $237,358.829 million. The displayed gross is **$1.171 million high**. The enacted overview and the Senate Republican Caucus summary both describe 2026–27 General Fund revenues as about **$237 billion**, which is this gross figure, not the $226.754 billion after transfers — [Republican Caucus highlights, September 30, 2026](https://src.senate.ca.gov/content/highlights-and-analysis-2026-27-enacted-budget).
- The $1 million discrepancy is the major-tax rounding residue. The three rounded tax lines sum to $226,374 million, but LAO’s own subtotal is $226,373 million, and $226,373 + $4,728 + $6,258 − $10,605 = $226,754 exactly. Adding the page’s four displayed revenue lines ($237,360 million) to −$10,605 million produces $226,755 million, one million above the official revenues-and-transfers total. Annual resources **are** gross revenue plus net transfers and loans. No beginning balance was collapsed into that line. The beginning balance is a separate $57,221.020 million.
- `moneyB` displays values of $10 billion and up to one decimal. The revenue sentence therefore reads “After **$10.6B** in net transfers and loans, current-year resources are **$226.8B**.” The donut subtitle “gross revenue” is the right concept (Schedule 8 “TOTALS, REVENUES,” before transfers). The donut total displays as **$237.4B**.

### Gaps

- Minor revenues were not itemized below the Schedule 8 category totals (regulatory / investment / miscellaneous). The category total is verified; individual minor lines other than investment income were not copied into this note.
- The BSA and holding-account amounts are published in millions ($3,574 million and $6,388 million), not in the Schedule 8 thousands detail as separate rows. Their sum is not equal to all of “transfers and loans.”

## Do the six spending categories equal enacted General Fund spending, and how are agencies grouped?

### Takeaway

Higher education and corrections match Schedule 9 to the thousand. Health and human services and K–12 match the Department of Finance enacted budget-detail regrouping, which moves two Schedule 9 “executive” departments into those programs. The other two page categories are the page’s own labels on the remaining official agency rows. They sum **$5,000 above** enacted General Fund expenditures because “Other agencies & programs” is rounded from $9,017.995 million to $9.018 million. The sankey uses that six-category sum. The donut uses 251.477. Both display as $251.5B.

### Cited Findings

- Schedule 9 grand total, 2026–27 General Fund expenditures: **251,477,209 thousand dollars** ($251,477,209,000) — [Schedule 9](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH9.pdf). The same figure is on Schedule 10 and, rounded to millions, in LAO Figure 3 (**$251,477 million**) and the DOF multiyear (**Total Expenditures $251,477**).
- Schedule 9 section totals, 2026–27 General Fund, thousands, before moving secretaries:
  - Legislative, Judicial, and Executive **8,180,866**
  - Business and Consumer Services **15,700**
  - Housing and Homelessness **1,685,232** (this section total includes the Civil Rights Department, org 1700, **63,364**)
  - Transportation **554,201** (does **not** include the Transportation secretary)
  - Natural Resources **4,887,666** (does **not** include the Natural Resources secretary)
  - Environmental Protection **267,821**
  - Health and Human Services **93,394,388** (does **not** include the agency secretary)
  - Corrections and Rehabilitation **14,447,846**
  - K–12 Education **90,902,498**
  - Higher Education **26,691,050**
  - Labor and Workforce Development **1,019,679**
  - Government Operations **5,109,670** (does **not** include the Government Operations secretary)
  - General Government **4,320,592**
  - These thirteen sections sum to **251,477,209**. Department-level totals also sum to **251,477,209**. Nothing in Schedule 9 is outside these sections.
- Two departments inside the Schedule 9 executive block are moved in the public summary grouping:
  - 0530 Health and Human Services Agency, Secretary: **280,615**. 93,394,388 + 280,615 = **93,675,003**. That is the page’s Health & Human Services figure exactly, and the enacted overview chart’s “Health and Human Services: $93,675” million.
  - 0954 ScholarShare Investment Board: **189,252**. 90,902,498 + 189,252 = **91,091,750**. That is the page’s K–12 figure exactly, and the chart’s “K-12 Education: $91,092” million. The LAO higher-education write-up lists ScholarShare separately from the segment totals and shows about $189 million — [Higher education spending plan](https://lao.ca.gov/Publications/Report/5202). The page puts it in K–12, which matches the DOF chart, not the LAO higher-education table.
- Corrections page value 14.447846 = Schedule 9 **TOTALS, CORRECTIONS AND REHABILITATION, 14,447,846** exactly. Higher education page value 26.691050 = Schedule 9 **Totals, Higher Education, 26,691,050** exactly.
- Enacted budget-detail style rollup, General Fund, thousands. Secretaries are placed with their agencies. ScholarShare is in K–12. The HHS secretary is in HHS. These rows sum to 251,477,209. They were reconstructed from Schedule 9 and match the agency rows on the enacted Budget Detail display (General Fund column, dollars in thousands; total on that display is 251,477,209):
  - Business and Consumer Services **15,700**
  - Environmental Protection **268,656** (= 267,821 + secretary 0555 **835**)
  - Housing and Homelessness **1,689,848** (= 1,685,232 + secretary 0516 **4,616**)
  - Labor and Workforce Development **1,022,247** (= 1,019,679 + secretary 0559 **2,568**)
  - Natural Resources **4,949,343** (= 4,887,666 + secretary 0540 **61,677**)
  - Transportation **1,072,201** (= 554,201 + secretary 0521 **518,000**)
  - Legislative, Judicial, and Executive **7,083,302** (Schedule 9 LJE 8,180,866 minus the secretaries and ScholarShare moved above, and minus the Government Operations secretary)
  - Government Operations **5,149,671** (= 5,109,670 + secretary 0511 **40,001**)
  - General Government **4,320,592** (unchanged)
  - Health and Human Services **93,675,003**
  - K–12 **91,091,750**
  - Higher Education **26,691,050**
  - Corrections **14,447,846**
- Page “Government, courts & executive” **16,553,565** = LJE 7,083,302 + Government Operations 5,149,671 + General Government 4,320,592. Exact.
- Page “Other agencies & programs” stored as **9,018,000**. The six program rows sum to 15,700 + 268,656 + 1,689,848 + 1,022,247 + 4,949,343 + 1,072,201 = **9,017,995**. The page is **5 thousand dollars ($5,000) high**, which is what you get by rounding $9,017.995 million to the nearest million.
- Six-category sum, billions: 93.675003 + 91.091750 + 26.691050 + 14.447846 + 16.553565 + 9.018000 = **251.477214**. In dollars that is **$251,477,214,000**.
  - Versus Schedule 9 expenditures **$251,477,209,000**: six-category sum is **$5,000 high**.
  - Versus the donut / `allFunds` General Fund value **251.477** ($251,477,000,000): six-category sum is **$214,000 high**.
- `moneyB` rounds anything at or above $10 billion to one decimal, so both 251.477214 and 251.477 display as **$251.5B**. The sankey “Total General Fund” node and the spending KPI use the six-category sum. The all-funds donut uses 251.477. The hero and the overview tile hardcode **$251.5B**. The method line hardcodes **$251.477B**. There is a real data inconsistency, and it is not visible in the $251.5B labels.
- Share math uses the six-category sum as the denominator (`pct`), not 251.477. At two-decimal percents the $5,000 does not change a displayed share.

What sits inside the two page-invented labels (faithful to the official rows above, not to the plain-language labels):

- **Government, courts & executive ($16,553.565 million)** is three official rows, not a custom mix of departments:
  - Legislative, Judicial, and Executive, **$7,083.302 million**, after the moves above. Still inside this row: the Legislature (Senate 206,258; Assembly 271,769; Legislative Counsel 185,033; legislators’ retirement 1,074); the judicial branch (Judicial Branch 3,829,217; Commission on Judicial Performance 7,388; judges’ retirement 306,104; subtotal **4,142,709**); and the remaining executive offices. Large executive pieces include the Office of Emergency Services **653,303**, Department of Justice **518,444**, Governor’s Office of Service and Community Engagement **213,513**, School Finance Authority **184,788** (left here, not moved to K–12), State Controller **168,871**, Secretary of State **126,333**, and the Office of the Inspector General **53,941** (CDCR oversight; it is not in the corrections total).
  - Government Operations, **$5,149.671 million**. The dominant pieces are the Public Employees’ Retirement System state contribution **3,018,000**, Franchise Tax Board **1,145,171**, Department of General Services **391,559**, and the Department of Tax and Fee Administration **384,714**, plus the agency secretary **40,001**.
  - General Government, **$4,320.592 million**. This is not “courts.” It includes retiree health and dental benefits **3,205,158**, supplemental pension payments **556,000**, Department of Veterans Affairs **597,452**, the federal per-diem offset for veterans’ housing **−89,371**, Department of Food and Agriculture **274,170**, Military Department **175,400**, tax relief **403,001**, local government financing **161,929**, statewide Proposition 98 reconciliation **−1,066,131**, statewide general-administrative pro rata **−1,300,503**, and the Arts Council **51,807**.
- **Other agencies & programs** is the other six official rows: business and consumer services, environmental protection, housing and homelessness (including Civil Rights), labor and workforce development, natural resources, and transportation, each including its agency secretary. Sum **$9,017.995 million**, stored on the page as **9.018**.

Notable placements that are easy to misread, but that follow the official table rather than a double count:

- ScholarShare is in the page’s K–12 bar, not higher education. School Finance Authority stays in the government/executive row.
- The Proposition 98 reconciliation of **−$1,066.131 million** is in General Government, so it reduces the government bar. It is not also deducted from the K–12 bar. K–12 on the page is the Schedule 9 K–12 total plus ScholarShare, which is what the DOF chart labels “K-12.”
- Community-college retirement costs are **−365,916** inside the K–12 section and **+365,916** inside higher education (org 6878). They offset. Both are inside the page’s matching bars. No double count.
- No agency row is omitted. The thirteen detail rows sum to the expenditure grand total.

### Inferences

- Health & Human Services 93.675003: **ACCURATE** against the enacted detail regrouping (Schedule 9 HHS plus the HHS secretary). It is **not** the raw Schedule 9 section total of 93,394,388.
- K–12 91.091750: **ACCURATE** against that same regrouping (Schedule 9 K–12 plus ScholarShare). It is **not** the raw section total of 90,902,498.
- Higher education 26.691050: **ACCURATE**.
- Corrections 14.447846: **ACCURATE**. Includes CDCR 14,191,395, Board of State and Community Corrections 165,961, Safe Neighborhoods and Schools Act 89,060, and smaller corrections items. It does not include the Inspector General.
- Government, courts & executive 16.553565: **ACCURATE** as the sum of Legislative/Judicial/Executive + Government Operations + General Government on the enacted detail rollup. The **label is MISLEADING**. The bar includes agriculture, veterans, the military, the arts, retiree health ($3.205 billion), pension payments, tax relief, and a −$1.066 billion Proposition 98 reconciliation. A reader who hears “courts and executive” will not expect those.
- Other agencies & programs 9.018000: **ROUNDED**. Official sum of the six remaining agency rows is $9,017.995 million. The page rounds to the nearest million and pads zeros, which is the entire **$5,000** overstatement of enacted spending.
- Six-category sum versus 251.477: **not equal**. Gap versus the number in the donut is **$214,000**. Gap versus Schedule 9 expenditures is **$5,000**. Displayed sankey total and displayed donut General Fund slice are both **$251.5B**, so the inconsistency is in the data and in any unrounded use of the sum, not in the hero text.
- Nothing material is double-counted. The $5,000 is rounding, not a second inclusion of an agency.

### Gaps

- The enacted Budget Detail web table was recovered as rendered text associated in search with an ebudget budget-detail URL whose year token did not consistently read 2026–27. Every row used here was recomputed from Schedule 9 and ties to the 251,477,209 grand total, so the grouping does not depend on that URL. A CSV download of the detail table was not opened.
- Individual department amounts inside natural resources, environmental protection, and labor were read and sum-checked only at the section level, not reprinted department by department in this note.

## Is 251.477 General Fund expenditures, and do the all-funds figures match?

### Takeaway

251.477 is enacted 2026–27 General Fund **expenditures**, rounded to the nearest million from $251,477.209 million. It is not revenues and it is not a different “appropriations” control total. The four all-funds slices match LAO Figure 5. Bond funds and federal funds are expenditures in Schedule 9, but they are not in the LAO’s “Budget Totals,” and federal funds are not part of the Department of Finance’s “total state funds.” The page’s “state spending” (General Fund plus special funds only) matches the LAO and excludes the bond funds that the Department of Finance includes in “total state funds.”

### Cited Findings

- LAO Figure 3, millions, 2026–27 enacted: revenues and transfers **226,754**; expenditures **251,477** — [Report 5197](https://lao.ca.gov/Publications/Report/5197). The line is labeled “Expenditures,” not revenues.
- LAO Figure 5, “Total State and General Fund Expenditures,” millions, 2026–27 enacted:
  - General Fund **$251,477**
  - Special funds **$95,129**
  - Budget Totals (those two only) **$346,606**
  - Bond funds **$5,104**
  - Federal funds **$187,190**
  - LAO prose: “General Fund spending is projected to total $252 billion in 2026–27.” “Including special funds, total state spending reaches $347 billion. Accounting for bond funds and federal funds as well, all-funds spending totals roughly $539 billion in 2026–27, with federal funds—at $187 billion.”
- Schedule 9 grand total, 2026–27, thousands — [Schedule 9](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH9.pdf):
  - General Fund **251,477,209** → $251,477.209 million → rounds to **$251,477 million**
  - Special funds **95,129,056** → $95,129.056 million → rounds to **$95,129 million**
  - Selected bond funds **5,103,532** → $5,103.532 million → rounds to **$5,104 million**
  - Budget total (General Fund + special + selected bond) **351,709,797** → **$351.710 billion**
  - Federal funds **187,189,993** → $187,189.993 million → rounds to **$187,190 million**
  - Check: 251,477,209 + 95,129,056 + 5,103,532 = 351,709,797. Adding federal funds: 351,709,797 + 187,189,993 = **538,899,790 thousand** = **$538,899.790 million**.
- The Schedule 9 bond column is titled **“Selected Bond Funds.”** The enacted overview uses that column as its bond-fund total.
- DOF enacted overview — [Budget Overview](https://ebudget.ca.gov/budget/e/2026-27/BudgetOverview): “The budget spends **$351.7 billion in total state funds**, consisting of approximately **$251.5 billion from the General Fund**, **$95.1 billion from special funds**, and **$5.1 billion from bond funds**.” Expenditures on the same chart: **$251,477 million**. Revenues on that chart: **$226,754 million**. So the $251.5 billion is the expenditure side.
- Page `allFunds` sum: 251.477 + 95.129 + 5.104 + 187.190 = **538.900**. `moneyB` displays **$538.9B**. Official four-way sum is $538,899.790 million. The page’s sum is **$210,000 high**, all of it from rounding the four lines to the nearest million (the bond line alone is $468,000 high; federal is $7,000 high; special funds are $56,000 low; General Fund is $209,000 low).
- Page “state spending” = General Fund + special funds = 251.477 + 95.129 = **346.606**, displayed as **$346.6B**. That equals the LAO “Budget Totals” line of **$346,606 million**. It excludes bond funds.
- January Governor’s Budget, for contrast only, was a different vintage: about **$248.3 billion** General Fund and **$348.9 billion** total state funds — [proposed overview](https://ebudget.ca.gov/budget/p/2026-27/BudgetOverview). May Revision General Fund spending was **$246.6 billion** — [May Revision full summary](https://ebudget.ca.gov/2026-27/pdf/Revised/BudgetSummary/FullBudgetSummary.pdf). The page is on the enacted totals, not those earlier ones.
- The deficit sentence calls  the spending total “total appropriations.” The official line is expenditures. No separate appropriations total different from $251,477 million was found in the LAO overview or the DOF schedules.

### Inferences

- General Fund 251.477: **ACCURATE** as enacted General Fund **expenditures** rounded to the nearest million ($209,000 below Schedule 9). **Not revenues** (those are $226.754 billion after transfers, or $237.359 billion before). The same number is the General Fund slice of all-funds spending. Using one number in both places is correct.
- Hero “Budget baseline $251.5B General Fund” and the overview “$251.5B 2026–27 General Fund”: **ROUNDED**, and the year is the **2026–27 enacted** expenditure total. 251.477 to one decimal is 251.5. Verdict on the hero as a baseline label: **ACCURATE** in year and concept, **ROUNDED** in digits.
- Special funds 95.129: **ACCURATE** at the LAO million; **ROUNDED** versus $95,129.056 million.
- Bond funds 5.104: **ROUNDED**. Schedule 9 selected bond funds are $5,103.532 million. The page matches the LAO’s $5,104 million and is **$468,000 high**. They are expenditure estimates of bond proceeds, in the same expenditure statement, but they are borrowed funds. General Fund debt service is already inside General Fund expenditures, so bond-fund spending is not the same thing as the cost to the General Fund.
- Federal funds 187.190: **ROUNDED** by **$7,000** above $187,189.993 million. Matches the LAO’s $187,190 million. These are federal dollars estimated to be spent through the state budget, not state revenue. Schedule 9 keeps them in their own column. They are “spending” in the expenditure-statement sense and are **not** part of DOF “total state funds.”
- All-funds sum 538.900: **ROUNDED**. Matches the LAO’s “roughly $539 billion.” Official sum of the four Schedule 9 columns is $538,899.790 million.
- “State spending alone—General Fund plus special funds—is $346.6B”: **ACCURATE** relative to LAO Figure 5 “Budget Totals” and to the LAO sentence that puts bond funds outside “total state spending.” **MISLEADING** relative to the Department of Finance term “total state funds,” which is **$351.7 billion** and **includes $5.1 billion of bond funds**. The page does say, in the same sentence, that bond and federal funds sit on top of that state-spending figure. The label still will not match anyone who looks up the official $351.7 billion state-funds total. The Senate Republican Caucus summary also describes total state spending as about **$352 billion**, which is the DOF state-funds concept rounded, not $346.6 billion — [Republican Caucus highlights](https://src.senate.ca.gov/content/highlights-and-analysis-2026-27-enacted-budget).

### Gaps

- No document was found that prints an all-funds total of exactly $538,900 million. The $538.9 billion figure is the sum of four rounded lines. The exact four-column sum is $538,899.790 million.
- “Selected” bond funds may exclude some bond accounts. DOF’s own $5.1 billion / $351.7 billion state-funds statement uses this column, so it is the official summary figure even if the word “selected” means the column is not every bond dollar in the state.

## Is the operating deficit $18.5 billion, and is the enacted budget balanced cumulatively?

### Takeaway

The administration’s published operating deficit for 2026–27 is **−$18,335 million**, not $18.5 billion. The LAO rounds that administration figure to “$18.5 billion” and uses the term “operating deficit.” The page copies the LAO’s rounding and the LAO’s term. The enacted budget is balanced in the constitutional sense: the Special Fund for Economic Uncertainties is positive. That balance is cumulative because the state spends down a large prior-year balance. The simple revenue-versus-spending gap is **$24.723 billion**, and it equals that balance drawdown. It is larger than the operating deficit by the **$6.388 billion** holding-account deposit.

### Cited Findings

- DOF multiyear, line “Operating Surplus/Deficit with BSA Transfer,” 2026–27: **−$18,335 million**. Later years: **−$10,485 million**, **−$8,643 million**, **−$8,430 million** — [MultiYearProjection.pdf](https://www.ebudget.ca.gov/reference/MultiYearProjection.pdf).
- That line equals expenditures minus revenues after the BSA transfer and **before** counting the transfer to the Surplus Account. In the published millions: revenues/transfers $236,716 − BSA $3,574 = $233,142; expenditures $251,477 − $233,142 = **$18,335**. The holding-account deposit of $6,388 million is excluded from this definition.
- LAO, “Multiyear” section — [Report 5197](https://lao.ca.gov/Publications/Report/5197): “As shown in Figure 6, the administration estimates an **$18.5 billion operating deficit** in 2026–27—somewhat larger than the amount of solutions needed to balance the enacted budget. This difference arises largely because **the enacted budget is balanced on a cumulative basis**: as discussed earlier in this report, it draws down the elevated fund balance carried over from 2025–26 and prior years. The operating deficit, by contrast, evaluates each year in isolation—comparing the revenues the state collects that year against the costs it incurs that year. Viewed this way, the state’s 2026–27 ongoing revenues fall well short of its ongoing spending.” The LAO then says the administration’s operating deficit narrows to **$10.4 billion** in 2027–28, **$8.7 billion** in 2028–29, and **$8.3 billion** in 2029–30. Those out-year LAO figures do not match the DOF line (−$10.485, −$8.643, −$8.430) at the tenth-of-a-billion. Figure 6 is a chart image; the prose is the citable LAO number.
- LAO on the budget window, same report: the state ends 2026–27 with **$4.5 billion** in the SFEU. “In other words, the state has a **structural imbalance in 2026–27, even though the enacted budget is balanced**.”
- DOF introduction — [Introduction.pdf](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/Introduction.pdf): a balanced budget is “measured by maintaining a positive balance in the state’s Special Fund for Economic Uncertainties.” The Budget Act “project[s] a positive balance in 2026–27 and a positive balance in the SFEU in 2027–28,” specifically **$4.5 billion** and **$403 million**. The introduction says the out-year structural deficits are less than half those in the Governor’s Budget. It does not print “$18.5 billion.” It does say the Budget Act “largely maintains the May Revision framework, which balances the budget in both the 2026–27 and 2027–28 fiscal years.”
- Fund condition, LAO Figure 3, millions, 2026–27: prior-year fund balance **$57,221**; revenues and transfers **$226,754**; expenditures **$251,477**; ending fund balance **$32,498**; encumbrances **$27,998**; SFEU **$4,500**. Prior-year SFEU **$29,223**. Drawdown of the fund balance: 57,221 − 32,498 = **24,723**. Drawdown of the SFEU: 29,223 − 4,500 = **24,723**. Encumbrances are unchanged, so the entire drawdown comes out of the SFEU.
- Same identity in Schedule 10 thousands: 57,221,020 − 32,497,943 = **24,723,077** thousand dollars, and 251,477,209 − 226,754,132 = **24,723,077**. The expenditure gap and the balance drawdown are the same number.
- Page code: `balanceUse = totalSpending − annualResources`. Using the six-category sum, 251.477214 − 226.754 = **24.723214**, which `moneyB` displays as **$24.7B**. Using the donut’s 251.477 instead, 251.477 − 226.754 = **24.723**, which also displays as **$24.7B**. The callout text therefore says the structural gap “is not the same as the simple **$24.7B** difference between this year’s revenues and transfers and total appropriations.”
- Why $24.723 billion and $18.335 billion differ: 24,723 − 18,335 = **6,388**, the Surplus Account / Temporary Surplus Holding Account deposit. That deposit is inside “revenues and transfers” (it makes the simple gap larger) and is excluded from the operating-deficit definition (the money is set aside to be withdrawn in 2027–28). LAO: the budget “deposits $6.4 billion into the TSHA, to be withdrawn in 2027–28.” “Neither our office nor the Department of Finance considers this account to be a reserve.”
- Page wording that current-year revenues and transfers do not cover enacted spending, and that the budget uses prior-year balances to close the gap: this matches the LAO (“drawing down that elevated 2025–26 balance … allows the state to cover costs in 2026–27 that would not otherwise be covered by that year’s revenues on their own”) and the arithmetic above. The extra words “and other one-time resources” / “other resources” go beyond the accounting identity. The $24.723 billion gap is closed entirely by the prior-year balance, specifically the SFEU. Budget solutions (the suspended BSA true-up, the Proposition 98 settle-up, fund shifts, revenue solutions) are already inside the revenue and spending totals; they are not a second plug on top of the $24.7 billion.
- Reserves, LAO Figure 3, end of 2026–27: BSA **$15,070 million**; SFEU **$4,500 million**; safety net **zero**; total of those reserves **$19,570 million**. LAO prose: “General Fund Reserves Nearly $20 Billion Under Spending Plan. Combined, under the spending plan, the BSA ($15.1 billion) and SFEU ($4.5 billion) would total **$19.6 billion** at the end of 2026–27. … The state’s Safety Net Reserve … is now fully depleted. … the state would also end 2026–27 with **$9.2 billion** in the Public School System Stabilization Account.”
- Schedule 10, BSA (fund 1011), 2026–27 ending reserve: **15,070,422 thousand** ($15,070.422 million) — [Schedule 10](https://ebudget.ca.gov/2026-27/pdf/Enacted/BudgetSummary/BS_SCH10.pdf).
- DOF multiyear “Total Reserves” 2026–27: **$28,765 million** = BSA 15,070 + SFEU 4,500 + PSSSA **9,195**. DOF introduction rounds the same concept to **$28.8 billion** (BSA $15.1 billion + SFEU $4.5 billion + school reserve $9.2 billion) and says that adding the holding account brings amounts “set aside” to about **$35.2 billion**. The introduction is explicit that the holding account is not described as part of reserves in the same way; the LAO says it is not a reserve.
- The page’s Proposition 2 card says “Current broadly usable reserves are about $20B.” That matches the LAO’s “nearly $20 billion” of BSA + SFEU ($19.6 billion), not the $28.8 billion that includes the school reserve, and not the $35.2 billion that includes the holding account. “Broadly usable” is a fair gloss: the school reserve is limited to schools, and both DOF and the LAO refuse to call the holding account a reserve.

### Inferences

- `operatingDeficit` 18.5: **ROUNDED**. The official DOF cell is **−$18.335 billion**. The LAO text says **“$18.5 billion.”** The page attributes the figure to the LAO, which is right as a citation of that sentence and wrong if a reader thinks the LAO independently measured $18.5 billion or that the administration printed $18.5 billion. Nearest tenth of a billion would be **$18.3 billion**, so the LAO’s rounding is loose by **$165 million**. The page did **not** invent the label. “Operating deficit” is the LAO’s heading and the DOF row name (“Operating Surplus/Deficit with BSA Transfer”). The LAO also says “structural imbalance” for the same budget year; the page’s “structural gap” follows that usage.
- The page is correct that the operating deficit is not `balanceUse`. `balanceUse` displays as **$24.7B**. The precise gap is **$24,723.077 million**.
- “The enacted budget is balanced cumulatively”: **ACCURATE**, as a close paraphrase of the LAO. DOF’s definition of balance is a positive SFEU. The SFEU is **$4.5 billion** in 2026–27 and **$403 million** in 2027–28. It turns negative in the forecast after that (−$8,241 million in 2028–29 and −$16,671 million in 2029–30 on the multiyear). “Balanced” does not mean current-year revenues cover current-year spending.
- “Current-year revenues and transfers do not cover enacted spending on their own. The budget uses prior-year balances and other one-time resources to close the accounting gap.” The first sentence is **ACCURATE**. The prior-year-balance part is **ACCURATE**. “Other one-time resources” as an additional closer of the $24.7 billion accounting gap is **MISLEADING**. That entire gap is the SFEU drawdown.

### Gaps

- Figure 6 is an image. The bar labels were not independently read off the image; the $18.5 / $10.4 / $8.7 / $8.3 billion figures are from the LAO prose beside the figure. The out-year mismatch with the DOF multiyear is unresolved beyond “the LAO rounded.”
- No thousands-level restatement of the −$18,335 million operating-deficit cell was found. It lives on a millions table that warns that totals may not add.

## Do the date, source-link, and reserve claims hold?

### Takeaway

“Administration estimates through July 1, 2026” is the LAO’s own cutoff for the enacted package, not the January budget or the May Revision. As of October 5, 2026, the LAO’s later spending-plan posts had not replaced these statewide totals. Report 5197 is the right overview. The page’s ebudget link uses the `m` route, which is the wrong vintage code for the enacted budget on this site.

### Cited Findings

- LAO introduction: the publication “reflects the administration’s estimates of legislative actions taken through the end of June 2026.” Table note: “Reflects administration estimates of budget actions taken through **July 1, 2026**.” Publication date on the HTML page: **August 26, 2026** — [Report 5197](https://lao.ca.gov/Publications/Report/5197).
- LAO Figure 8 is titled “Budget-Related Legislation Passed On or Before July 1, 2026.” The narrative says the Legislature passed the amended budget act and trailer bills on **June 29, 2026**. The Governor had presented the May Revision on **May 14, 2026**, and the January budget on **January 9, 2026**.
- DOF schedules are headed “June 2026” and “AT 2026 BUDGET ACT.” The enacted introduction describes the 2026 Budget Act, not a proposal.
- Later LAO posts in the same series, including natural resources on **October 5, 2026**, discuss program detail. None of the documents opened replaces the statewide General Fund totals of $226,754 million and $251,477 million — [Natural resources post](https://lao.ca.gov/Publications/Report/5207).
- Report 5197’s title is “The 2026-27 Budget: Overview of the Spending Plan.” Headline figures in it are the ones quoted above: General Fund expenditures $251,477 million, revenues and transfers $226,754 million, SFEU $4.5 billion, BSA $15.1 billion, reserves $19.6 billion, operating deficit described as $18.5 billion, all-funds spending roughly $539 billion.
- The page links to `https://ebudget.ca.gov/budget/m/2026-27/BudgetDetail`. The enacted overview that contains the signed-budget language and the $251,477 million / $226,754 million chart is `https://ebudget.ca.gov/budget/e/2026-27/BudgetOverview`. The PDF schedules live under `https://ebudget.ca.gov/2026-27/pdf/Enacted/`. A prior-year `m` route is titled “Revised Budget Detail” and compares January with the May Revision — [2024–25 revised detail](https://ebudget.ca.gov/publication/m/2024-25/BudgetDetail). The 2026–27 `m` URL did not return numbers to a non-browser fetch.

### Inferences

- “Figures: 2026–27 enacted budget, administration estimates through July 1, 2026.” **ACCURATE**. July 1, 2026 is the LAO cutoff for enacted actions, not an earlier May or January date. The page is not using a stale pre-enactment vintage. No post–July 1 revision of these statewide totals was found as of the October 5, 2026 snapshot.
- Source link to Report 5197: **ACCURATE**. It is the LAO overview of the 2026–27 spending plan.
- Source link to `/budget/m/2026-27/BudgetDetail`: **MISLEADING** as a citation for the enacted budget. The enacted route on this site is `e`. Whether the 2026–27 `m` app still shows May Revision numbers could not be verified from the page shell.
- “3 direct bond measures” was not checked. The General Fund figure beside it is the 2026–27 enacted expenditure total.

### Gaps

- The rendered contents of `https://ebudget.ca.gov/budget/m/2026-27/BudgetDetail` were not visible without the site’s JavaScript. The vintage warning is from the site’s own `e` versus `m` naming, not from a side-by-side of 2026–27 May Revision versus enacted numbers inside that app.

## Official figures for a verification tool

Dollars are exact where the source is in thousands. Millions-only sources are marked. “Page verdict” uses the page’s stored value.

### General Fund revenues, 2026–27

| Item | Official amount | Source | Page value | Verdict |
| --- | --- | --- | --- | --- |
| Personal income tax | $145,608,654,000 | Schedule 8, 4116200, 2026–27 GF | $145.609 billion | ROUNDED (LAO $145,609 million) |
| Corporation tax | $45,166,625,000 | Schedule 8, 4110800 | $45.167 billion | ROUNDED (LAO $45,167 million) |
| Sales and use tax | $35,598,189,000 | Schedule 8, 4117000 | $35.598 billion | ROUNDED (LAO $35,598 million) |
| Insurance gross premiums tax | $4,727,503,000 | Schedule 8, 4113400 | included in 10.986 | ROUNDED to LAO $4,728 million |
| Other GF major taxes | $450,353,000 | Schedule 8: alcohol $415,352,000; cigarettes $34,027,000; mobilehome in-lieu $972,000; vehicle license in-lieu GF $2,000 | included in 10.986 | part of LAO “other revenues” |
| Minor revenues | $5,807,505,000 | Schedule 8, TOTALS, MINOR REVENUES | included in 10.986 | with the $450,353,000, rounds to LAO other revenues $6,258 million |
| Insurance + other, unrounded | $10,985,361,000 | sum of the three rows above | $10.986 billion | ROUNDED; $639,000 high |
| Gross revenues | $237,358,829,000 | Schedule 8, TOTALS, REVENUES | implied $237.360 billion | ROUNDED; $1,171,000 high |
| Transfers and loans | −$10,604,697,000 | Schedule 8; loans −$1,005,300,000; revenue transfers −$9,599,397,000 | −$10.605 billion | ROUNDED (LAO −$10,605 million) |
| Of which BSA transfer | −$3,574 million | DOF chart and multiyear, millions | inside net transfers | not shown separately; ACCURATE as part of the net |
| Of which surplus holding account | −$6,388 million | DOF chart and multiyear, millions | inside net transfers | not shown separately; ACCURATE as part of the net |
| Revenues, transfers, and loans | $226,754,132,000 | Schedule 8 and Schedule 10 | $226.754 billion | ACCURATE at the million; $132,000 low versus thousands |

Identity that holds: 237,358,829,000 + (−10,604,697,000) = 226,754,132,000. Identity that does not hold on the page: 237.360 + (−10.605) = 226.755 ≠ 226.754.

### General Fund expenditures by program area, 2026–27

Agency amounts are General Fund, thousands of dollars, enacted budget-detail regrouping (secretaries with their agencies; ScholarShare in K–12; HHS secretary in HHS), built from Schedule 9.

| Page category | Official amount | What it contains | Page value | Verdict |
| --- | --- | --- | --- | --- |
| Health & Human Services | $93,675,003,000 | Schedule 9 HHS section $93,394,388,000 + HHS secretary $280,615,000 | 93.675003 | ACCURATE |
| K–12 education | $91,091,750,000 | Schedule 9 K–12 section $90,902,498,000 + ScholarShare $189,252,000 | 91.091750 | ACCURATE |
| Higher education | $26,691,050,000 | Schedule 9 higher education section | 26.691050 | ACCURATE |
| Corrections | $14,447,846,000 | Schedule 9 corrections section | 14.447846 | ACCURATE |
| Government, courts & executive | $16,553,565,000 | LJE $7,083,302,000 + Government Operations $5,149,671,000 + General Government $4,320,592,000 | 16.553565 | ACCURATE as a sum; MISLEADING label |
| Other agencies & programs | $9,017,995,000 | BCS $15,700,000 + Environmental Protection $268,656,000 + Housing and Homelessness $1,689,848,000 + Labor $1,022,247,000 + Natural Resources $4,949,343,000 + Transportation $1,072,201,000 | 9.018000 | ROUNDED; $5,000 high |
| Sum of six | $251,477,209,000 if other agencies is unrounded; page sum $251,477,214,000 | Schedule 9 grand total $251,477,209,000 | sankey uses the page sum; donut uses $251.477 billion | page sum is $5,000 high |
| General Fund expenditures | $251,477,209,000 | Schedule 9 and Schedule 10; LAO $251,477 million | 251.477 and hero $251.5 billion | ACCURATE at the million; hero ROUNDED |

### All-funds expenditures, 2026–27

| Fund | Official amount | Source | Page value | Verdict |
| --- | --- | --- | --- | --- |
| General Fund | $251,477,209,000 | Schedule 9 | 251.477 | ACCURATE at LAO million; this is expenditures |
| Special funds | $95,129,056,000 | Schedule 9 | 95.129 | ACCURATE at LAO million |
| Selected bond funds | $5,103,532,000 | Schedule 9 | 5.104 | ROUNDED (LAO $5,104 million) |
| Federal funds | $187,189,993,000 | Schedule 9 | 187.190 | ROUNDED (LAO $187,190 million) |
| LAO budget totals (GF + special) | $346,606 million | LAO Figure 5 | page “state spending” $346.606 billion | ACCURATE vs LAO; MISLEADING vs DOF “total state funds” |
| DOF total state funds (GF + special + bond) | $351,709,797,000 | Schedule 9 budget-total column; DOF text “$351.7 billion” | not shown; page’s state-spending label excludes the $5.104 billion of bonds | label gap, not a wrong addend |
| Four-column sum | $538,899,790,000 | Schedule 9 | 538.900 | ROUNDED; LAO says roughly $539 billion |

### Reserves, end of 2026–27

| Item | Official amount | Source | Page claim | Verdict |
| --- | --- | --- | --- | --- |
| BSA | $15,070 million; Schedule 10 ending reserve $15,070,422,000 | LAO Figure 3; Schedule 10 fund 1011 | inside “about $20B” | ACCURATE as part of that claim |
| SFEU | $4,500 million | LAO Figure 3; DOF multiyear | inside “about $20B” | ACCURATE as part of that claim |
| BSA + SFEU | $19,570 million | LAO: “nearly $20 billion” | “about $20B” broadly usable reserves | ROUNDED; right concept |
| Safety Net Reserve | $0 | LAO and DOF multiyear | not stated | depleted |
| Public School System Stabilization Account | $9,195 million (DOF); LAO “$9.2 billion” | DOF multiyear; LAO prose | not in the $20B claim | correctly omitted if “broadly usable” means general-purpose |
| Total reserves including the school reserve | $28,765 million | DOF multiyear | not what the page says | do not substitute this for the $20B claim |
| Temporary Surplus Holding Account | $6,388 million deposited, withdrawn in 2027–28 | DOF multiyear; LAO “$6.4 billion” | not a reserve | LAO and DOF both say it is not a reserve |

### Structural gap

| Item | Official amount | Definition | Page value | Verdict |
| --- | --- | --- | --- | --- |
| Operating deficit, 2026–27 | −$18,335 million | DOF “Operating Surplus/Deficit with BSA Transfer”: expenditures minus (revenues/transfers after the BSA transfer, ignoring the holding-account transfer and ignoring the prior-year balance) | 18.5 | ROUNDED. LAO prose says the administration estimates “$18.5 billion.” Label is the LAO’s and DOF’s, not invented |
| Simple gap / balance drawdown | $24,723.077 million | Expenditures minus revenues and transfers, which equals the fall in the fund balance and the fall in the SFEU | code displays $24.7B | ACCURATE at one decimal |
| Difference between those two gaps | $6,388 million | The holding-account deposit, which widens the simple gap and is excluded from the operating deficit | page says they differ, without this arithmetic | the claim that they differ is ACCURATE |

Prior-year General Fund balance **$57,221,020,000**. Ending balance **$32,497,943,000**. Encumbrances stay **$27,998 million**. SFEU goes from **$29,223 million** to **$4,500 million**.
