# California 2026 ballot fact check

Snapshot date: October 5, 2026. Page checked: `ca-2026-ballot/index.html`. The ballot conclusions on that page were not changed. The only edit is a sentence in “How this guide was built” that links to the research record.

The certified ballot, the election date, and the headline dollar ranges from the Legislative Analyst’s Office are real. The errors that would change a reader’s understanding are the wealth-tax base, two poll cards that hide published results, one bond mislabeled as a revenue bond, chart endpoints the LAO never published, and two coalition colors that flatten a split.

## What was checked against

- Secretary of State certification, June 25, 2026: [14 measures for November 3, 2026](https://www.sos.ca.gov/administration/news-releases-and-advisories/2026-news-releases-and-advisories/california-secretary-state-shirley-n-weber-phd-certifies-measures-november-3-2026-general-election-ballot).
- LAO, *The 2026–27 Budget: Overview of the Spending Plan*, August 26, 2026, administration estimates through July 1, 2026: [Report 5197](https://lao.ca.gov/Publications/Report/5197).
- Department of Finance enacted Schedules 8, 9, and 10, and the [2026–27 budget overview](https://ebudget.ca.gov/budget/e/2026-27/BudgetOverview).
- LAO ballot analyses opened for this check: [Proposition 1](https://lao.ca.gov/BallotAnalysis/Proposition?number=1&year=2026), [Proposition 3](https://lao.ca.gov/BallotAnalysis/Proposition?number=3&year=2026), [Proposition 38](https://lao.ca.gov/BallotAnalysis/Proposition?number=38&year=2026), [Proposition 45](https://lao.ca.gov/BallotAnalysis/Proposition?number=45&year=2026), and [Proposition 40](https://lao.ca.gov/BallotAnalysis/Proposition?number=40&year=2026).
- PPIC Statewide Survey, *Californians and Their Government*, fieldwork September 4–10, 2026, 1,103 likely voters, margin ±3.8 points: [publication](https://www.ppic.org/publication/ppic-statewide-survey-californians-and-their-government-september-2026/).
- Voter-guide titles, summaries, and argument signers, plus Berkeley IGS Release #2026-20 (September 25, 2026), as quoted in `research_notes/California 2026 ballot fact check/`.

The June 25 qualification estimates and the final voter-guide analyses are not the same documents. Where they differ, the voter-guide LAO analysis is the one the page should follow. It does, on the items below.

## Material errors

### Proposition 40 taxes net worth, not only the slice above $1 billion

The one-line summary says the measure “taxes covered wealth above $1B at up to 5%.” The LAO says billionaires who were California residents on January 1, 2026, pay “a one-time state tax equal to 5 percent of their net worth.” Real estate, pensions, and retirement accounts are generally excluded. The Attorney General title says “up to 5%” on taxpayers and trusts whose covered assets are valued over $1 billion, and it lists those exclusions.

A 5 percent tax on a $2 billion net worth is about $100 million. A 5 percent tax on only the dollars above $1 billion is about $50 million. The official yes statement is “equal to 5 percent of their wealth.” The page’s yes box is closer to that sentence than the one-liner is. The one-liner is the sentence that needs to change.

The LAO does not publish a phase-in table. Secondary readings of the text describe a rate that reaches 5 percent at $1.1 billion and declines toward $1 billion. That schedule was not re-read from the proposed-law PDF here, so it is not treated as established. “Up to 5%” is the official trace of a rate that is not flat.

### Propositions 41 and 43 hide poll results PPIC published

PPIC likely voters, September 2026, read by me from the publication:

- Proposition 41: 51 percent yes, 44 percent no, 5 percent don’t know. The card says the no share was not published.
- Proposition 43: 43 percent yes, 51 percent no. The card says the exact topline was unpublished and that support is “below majority.” The yes share is below 50 percent. The topline itself is published, and the no side is ahead.

The other twelve yes/no pairs match the pollster named on the card. PPIC likely-voter figures confirmed from the narrative: Proposition 1, 55/43; 2, 60/39; 4, 42/53; 5, 35/59; 37, 61/35; 38, 55/42; 42, 54/43; 44, 34/61; 45, 49/46. Proposition 3 on PPIC is 58/40; the card’s 54/34 is the Berkeley figure, not a misquote of PPIC. The same is true of Proposition 39 (PPIC 43/55, card Berkeley 39/52) and Proposition 40 (PPIC 52/46, card Berkeley 45/42).

Where the published yes, no, and don’t-know sum to 99 or 101 because of rounding, the page’s `100 - yes - no` remainder is off by one point. That affects Propositions 3, 5, 37, 42, and 44.

Berkeley’s September 15–20 wave (Release #2026-20, likely voters, released September 25) is later than PPIC and was public before this snapshot. The page uses it for 3, 39, and 40, and uses the earlier PPIC wave for 4, 41, 42, and 43. On Proposition 42 that is the difference between PPIC’s 54 percent yes and Berkeley’s 43 percent yes. The card does not say another major poll exists.

### Proposition 1’s veterans piece is a general-obligation bond

The LAO says Proposition 1 lets the state sell $11.25 billion in general-obligation bonds: $10 billion repaid by the General Fund and $1.25 billion repaid by veterans’ home-loan payments. Those payments have always covered that debt service. The flow chart still labels the $1.25 billion a “CalVet revenue bond.” The proposed-law text pledges the full faith and credit of the state for that piece. The big-number card, which calls the whole $11.25 billion a general-obligation bond, matches the LAO.

Proposition 37’s “revenue bond” label is the correct one. Its bonds are payable from borrower payments and are not a state debt.

### Two charts turn LAO phrases into dollar endpoints

The LAO did not publish $20 million, $300 million, $80 million, or $110 million.

- Proposition 39: “tens of millions of dollars to low hundreds of millions of dollars” a year, state and local, “less than one-quarter of 1 percent (0.25 percent)” of the General Fund. The page draws $20–$300 million and prints “roughly 0.01–0.12% of the General Fund.” Unrounded, $20 million is about 0.008 percent of $251.477 billion. The page’s `toFixed(2)` turns 0.00795 into 0.01. The costs are state and local. The chart title calls the row a General Fund effect.
- Proposition 45: initial state and local costs “likely in the high tens of millions of dollars annually, potentially exceeding $100 million annually,” partly covered by fees, for the first several years. The page draws $80–$110 million. The LAO gives no floor and no ceiling. After the initial period, some costs are likely to decline. The longer-term effect is uncertain and could be larger than the startup cost.

Propositions 1 and 38 do have LAO ranges of $500–$600 million a year. The LAO calls each about 0.25 percent of the General Fund. The page’s 0.20–0.24 percent is $500–$600 million divided by the $251.477 billion expenditure total. The dollars match. The percentage is the page’s arithmetic. The LAO’s 0.25 percent is a rounder statement of the same cost, not a higher debt-service estimate. Proposition 3’s $5–$15 billion is the LAO range. “About 2–6 percent” is $5 billion and $15 billion divided by $251.477 billion (1.99 percent and 5.96 percent). The LAO did not publish that percentage.

## Budget figures

These enacted 2026–27 figures match LAO Report 5197 and the Department of Finance schedules. Values in the LAO tables are millions of dollars.

| Item | Official figure | Page |
| --- | --- | --- |
| Personal income tax | 145,609 | 145.609 |
| Corporation tax | 45,167 | 45.167 |
| Sales and use tax | 35,598 | 35.598 |
| Insurance tax + other revenues | 4,728 + 6,258 = 10,986 | 10.986 |
| Transfers and loans | −10,605 | −10.605 |
| Revenues and transfers | 226,754 | 226.754 |
| General Fund expenditures | 251,477 | 251.477 |
| Special funds | 95,129 | 95.129 |
| Selected bond funds | 5,104 | 5.104 |
| Federal funds | 187,190 | 187.190 |
| K–12 | 91,092 on the DOF chart; 91,091.750 in the agency rollup | 91.091750 |
| Health and Human Services | 93,675 | 93.675003 |
| Higher education | 26,691 | 26.691050 |
| Corrections | 14,448 | 14.447846 |

Schedule 8, in thousands, is slightly different because the LAO rounds each line to the nearest million: personal income tax $145,608.654 million, corporation tax $45,166.625 million, gross revenue $237,358.829 million, transfers −$10,604.697 million, revenues and transfers $226,754.132 million. Adding the page’s already-rounded lines produces $226.755 billion. The page stores the official total, $226.754 billion. That $1 million gap is in the rounded source table.

The six spending bars sum to $251,477,214,000. Schedule 9 expenditures are $251,477,209,000. The extra $5,000 is “Other agencies & programs,” rounded from $9,017.995 million to $9.018 billion. The hero and the donut both display $251.5 billion. The sankey’s unrounded total is the six-bar sum.

The Department of Finance overview chart’s “Other” expenditures are $25,571 million. The page splits that remainder into $16.553565 billion and $9.018 billion. Those two totals match the enacted agency rollup. The label “Government, courts & executive” does not. That $16.554 billion is Legislative, Judicial, and Executive, plus Government Operations, plus General Government. General Government includes retiree health and dental ($3.205 billion), supplemental pension payments ($0.556 billion), veterans, agriculture, the military, and a Proposition 98 reconciliation of −$1.066 billion.

“State spending” on the page is the General Fund plus special funds, $346.606 billion. That is the LAO budget total. The Department of Finance’s “total state funds” is $351.7 billion because it also counts bond funds. Both definitions are official. The page should keep saying which one it is using.

The simple gap between expenditures and revenues-and-transfers is $24.723 billion (251,477 − 226,754). That equals the draw on the prior-year balance. The Special Fund for Economic Uncertainties falls from $29.223 billion to $4.500 billion.

The administration’s operating-deficit cell is −$18,335 million. The arithmetic is 251,477 − (226,754 + 6,388) = 18,335. The $6,388 million added back is the deposit into the Temporary Surplus Holding Account, which is set aside for 2027–28 and is not counted in that deficit definition. The LAO prose calls the administration’s estimate “an $18.5 billion operating deficit” and says the enacted budget is balanced on a cumulative basis. The page repeats the LAO’s $18.5 billion. Nearest-tenth rounding of $18.335 billion is $18.3 billion. The label “operating deficit” is the LAO’s and the Department of Finance’s. The page is right to keep it separate from the $24.7 billion balance draw. A reader who wants the unrounded administration figure needs $18.335 billion.

End-of-2026–27 reserves in the LAO table are a Budget Stabilization Account of $15.070 billion and a Special Fund for Economic Uncertainties of $4.500 billion, together $19.570 billion. The page’s “about $20 billion” of broadly usable reserves matches that pair. The Public School System Stabilization Account, $9.2 billion, is separate. The figure is an end-of-year estimate under the enacted budget, not cash on hand on October 5.

Proposition 2’s rules, confirmed in the same LAO report: the Budget Stabilization Account cap would rise from 10 percent to 20 percent of General Fund tax revenues, and the extra debt-payment requirement now set to expire in 2030 would run through 2040.

## Legal effects that are off by a real condition

The ballot is exactly Propositions 1, 2, 3, 4, 5, 37, 38, 39, 40, 41, 42, 43, 44, and 45. The Secretary of State certified 14 measures, five from the Legislature and nine from initiatives. November 3, 2026, is the statewide general election.

These official conditions are missing or stronger than the LAO:

- Proposition 4. The existing public-financing exception covers charter cities and charter counties. The no-vote line says charter cities only. The cost line, a few hundred thousand dollars a year for Fair Political Practices Commission guidance, matches the LAO. There is no overall cap on future programs.
- Proposition 5. The official title says statewide officers, and the page follows it. The amended section is Article II, section 15, and the LAO also applies the new vacancy rules to legislative recalls. Succession to the lieutenant governor is the governor rule. Early in a gubernatorial term, that successor serves until a special election. The recalled officer cannot be appointed to the vacancy.
- Proposition 39. Mail voters must supply the last four digits of the specific ID number they designated at registration. A mismatch means the ballot does not count. The page’s “ID digits” line does not say that a mismatch voids the ballot.
- Proposition 40, conflict. California Constitution, Article II, section 10(b): if provisions of two approved measures conflict, the provisions of the measure with the highest number of affirmative votes prevail. Propositions 41 and 42 each say a conflicting measure on the same ballot is void if they receive more yes votes. The LAO’s sentence is narrower: if 41 or 42 receives more yes votes, Proposition 40 “could be stopped” because “the courts could find” a conflict. The overview box states the block as certain. The fail-state lines are right that a defeated rival cannot block Proposition 40.
- Proposition 41. The Attorney General summary prohibits new state taxes that exclude their revenue from the 1979 spending limit. The LAO yes statement says the state “might not be able” to exclude new special-tax spending. “Revenue stays under the Gann Limit” follows the Attorney General and is stronger than the LAO. The audits are pre-election for voter initiatives and every four years afterward. Recommendations are not binding. The measure does not name Proposition 40.
- Proposition 42. The date is taxes enacted or taking effect on or after January 1, 2026, not only taxes “enacted after” that date. The LAO fiscal line is only that future revenue may not rise as much. “Progressive revenue options,” in the con box, is wider than a ban on new personal-property taxes and defined retroactive taxes.
- Proposition 43. The two-thirds rule applies to voter-proposed local special taxes approved after January 1, 2027, including increases and extensions. It is a legislative constitutional amendment, ACA 22. The voter guide prints Senate 35–1 and Assembly 68–2.
- Proposition 44. The 90 percent rule, the shortfall penalty, fee-funded enforcement in the low tens of millions, waivers, and a five-year penalty refund match the LAO. The cost line omits uncertain Medi-Cal and closure costs. The LAO says these clinics currently report spending about 80 percent of revenue on health care.
- Proposition 45, yes line. Opt-in is accurate. The LAO also says the measure limits alternatives, freezes the standards used in the review to those in place when the application is filed, narrows tribal consultation to federally recognized tribes, caps how long comments are accepted, and limits what a court can consider and stop. “Faster CEQA review” does not carry those changes. The pro-box claim that the measure keeps environmental standards is in tension with that LAO list.

Proposition 1’s debt service, $500–$600 million a year for about 25 years, matches the LAO. The LAO’s unit estimate is up to 40,000 multifamily rentals, about 2,500 farmworker units, about 1,200 university beds, and up to 40,000 homeownership households. “Tens of thousands” is that estimate. Proposition 38’s $8.4 billion, $500–$600 million a year for about 20 years, half to one institute and half to grants, 2 percent administration cap, 20 percent California price discount, and 10 percent revenue share match the LAO analysis. The June 25 qualification blurb for that bond said about $500 million a year for 25 years. The page follows the later voter-guide analysis, which is the right one.

Proposition 3 makes the Proposition 30 rates permanent instead of letting them expire in 2031. The LAO says the top 2 percent of California taxpayers pay those rates. Roughly 40 percent of the maintained revenue would go to schools and community colleges, and the rest to other state programs, part of it to reserves. That is not a dedication of health-care funding. No one’s rate changes before 2031 under either outcome.

## Neutrality

The method note says lean labels describe coalitions, and that the pro and con boxes are each side’s case. The problems below are in the color, the type tag, or a sentence a reader can take as a finding.

- Proposition 40 is colored Democratic. The California Democratic Party is recorded as Yes. Governor Newsom, a Democrat, is a signer of the opposition case, along with the California Teachers Association, the building trades, carpenters, firefighters, the California Medical Association, and business groups. SEIU-UHW and the state labor federation are on the yes side. The sentence “progressive-labor support” describes part of the yes coalition and skips the labor split. The color treats the split as a Democratic measure.
- Proposition 43 is colored Republican. The campaign is taxpayer and business groups against labor, and the state parties are Republican Yes and Democratic No. The measure was ACA 22, authored by Assemblymember Buffy Wicks, a Democrat, and the floor votes were 68–2 and 35–1. The sentence discloses the bipartisan referral. The red color drops it.
- Proposition 5’s “election-integrity opposition” is a frame the official no signers do not use. They are Senate Minority Leader Brian Jones and Assemblymember Joe Patterson. The support side, the League of Women Voters and California Common Cause, matches “good-government.”
- Proposition 45’s Republican color matches a California Republican Party Yes and a California Democratic Party No. The named yes argument is a children’s-hospital association, a water association, and an affordable-housing council. “Developer” is a shorthand. The color is not invented. The interest-group sentence is the fairer description.
- The type tags “countermeasure to Prop 40” on Propositions 41 and 42 sit outside the argument boxes. Both measures are written as general rules. Each can void Proposition 40 if it passes and receives more yes votes. “Countermeasure” is a purpose claim. The official opposition arguments do say the measures were written to undo the billionaire tax. That belongs in the argument box, where “poison pill” already sits.
- “Without evidence of widespread voter fraud” is in Proposition 39’s con box. The LAO analysis does not discuss fraud. The official argument against does not use that sentence either. It is the page’s own argument.
- “Keeping environmental standards,” in Proposition 45’s pro box, conflicts with the LAO changes listed above.

Propositions 38 and 44 are correctly left uncolored. On 38, both major parties are recorded as Yes and the only official opponent in the voter guide is one individual, with Howard Jarvis and the League of Women Voters also opposed. On 44, both major parties are No and the fight is labor against provider groups. Propositions 1, 2, 3, 4, and 39 match the party and signer record closely enough to keep. Proposition 1 is the soft case: the California Republican Party is recorded as neutral, and no argument against was filed. Howard Jarvis is the organized conservative opponent.

The glossary definitions of the LAO, PPIC, Berkeley IGS, the FPPC, CEQA, CalHFA, CalVet, SEIU, the General Fund, the Gann Limit, and K–12 are not false. “Gann Limit” is a common name, not the name used in the official summaries.

## What the page gets right

Fourteen statewide measures, election day November 3, 2026, and the proposition numbers. The $251.477 billion General Fund expenditure total, the revenue lines, the transfer line, the all-funds slices, and the four large program totals. The separation of the $18.5 billion operating deficit from the $24.7 billion balance draw. Proposition 1 and 38 debt service, Proposition 3’s $5–$15 billion, Proposition 37’s $25 billion revenue-bond ceiling and “no direct state or local cost,” Proposition 40’s “tens of billions” and “under $1 billion” income-tax risk, and the refusal to add those unlike numbers into one total. The 90/10 health split on Proposition 40 is the Attorney General’s allocation. The LAO puts administration of the tax inside the non-health share.

## Gaps

- The Proposition 40 phase-in formula and the trust threshold were not quoted from the proposed-law PDF.
- Berkeley IGS Release #2026-20 was read in the polling pass. The HTML item page returned empty on a later fetch. The PPIC yes/no figures above were read directly.
- Campaign-committee dollar rankings were not pulled from the FPPC. Coalition judgments use voter-guide signers, the quick-reference supporter lines, and the IGS endorsement grid.
- A later Independent Voter Project survey was published October 4. It was not used here as a replacement topline because the questionnaire was not re-read in the final pass.
- Figure 1 of the Proposition 45 analysis, the full eligible-project list, was not transcribed.

## Checker

`tools/verify_fiscal/verify_fiscal.py` reads the page and compares it with `tools/verify_fiscal/official_fiscal_2026.json`. It does not use the network. Refresh the JSON if the Department of Finance or the LAO revises a table.

```bash
python3 tools/verify_fiscal/verify_fiscal.py
```

The current run exits 1. The failure is the “CalVet revenue bond” label. Warnings cover the $18.5 billion rounding, the government-bar label, and the Proposition 39 and 45 endpoints. Notes cover the $1 million revenue residual, the $5,000 spending residual, and the page-computed percentages.

## Edits not made

The six content edits below were not applied. Any of them would change what the guide tells a voter and needs a yes before it is applied:

1. Rewrite the Proposition 40 one-liner to a 5 percent tax on net worth, with real property and some retirement accounts excluded, and describe the 41/42 interaction as a conflict the courts could find.
2. Publish the PPIC toplines for Propositions 41 (51/44) and 43 (43/51), and show the other poll when PPIC and Berkeley disagree.
3. Relabel the veterans bond as general-obligation, and rename the $16.554 billion bar so it does not say only courts and executive.
4. Remove the $20–$300 million and $80–$110 million endpoints, and label state-and-local costs as state and local.
5. State the operating deficit as $18.3 billion, or keep $18.5 billion and attribute it as the LAO’s rounding of the administration’s $18.335 billion.
6. Drop the Democratic color on Proposition 40 and the Republican color on Proposition 43, and replace “election-integrity” and the “countermeasure” type tags.
