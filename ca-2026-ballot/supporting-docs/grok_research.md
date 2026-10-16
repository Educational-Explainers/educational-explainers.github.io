# Research record: California 2026 ballot explainer

Record date: October 5, 2026.  
Page under review: `ca-2026-ballot/index.html`.  
This file is the chain of reasoning behind the fact-check. It separates what a document says from what a person must still judge. The public version of the same conclusions is `ca-2026-ballot/supporting-docs/index.html`.

The explainer’s ballot text was not edited. The guide links to this record from “How this guide was built.”

## 1. The question

The explainer says it states what a Yes or No vote does, the strongest case on each side, coalition signals, and fiscal scale, without telling the reader how to vote. The check asked four questions of every claim that could be true or false:

1. Does a primary document say this?
2. If the page computed a number, does the arithmetic follow from the inputs it names?
3. If the page interpreted a document, is there another reading a fair person could hold?
4. Does the presentation treat a judgment as if it were a measurement?

A claim survived when the answer to (1) or (2) was yes and the answer to (4) was no.

## 2. Method

### 2.1 What was extracted

Every sentence and number a reader can see was treated as a claim. That includes the hero, the budget charts, the fourteen cards, the yes/no lines, the fiscal-scale lines, the flow diagrams, the pro and con bullets, the poll figures, the coalition labels, the color assigned in code, the glossary, and the source links.

The pro and con boxes are labeled on the page as each side’s case. A bullet inside those boxes was graded as a false finding only when it stated a document fact that the cited document does not support. A value judgment inside a labeled argument box was left as argument.

Text outside those boxes — titles, one-liners, cost lines, type tags, chart labels, colors, and the overview — was held to the standard of a neutral description.

### 2.2 Source order

Sources were used in this order. A lower source was not allowed to override a higher one.

1. The statute or constitutional text, and the official title and summary prepared for the ballot.
2. The Legislative Analyst’s Office ballot analysis and the LAO overview of the enacted 2026–27 budget (Report 5197, August 26, 2026).
3. Department of Finance enacted schedules and the public budget overview. These are the administration’s estimates through July 1, 2026. Report 5197 uses those estimates and says so.
4. The pollster’s own release: question wording, population, dates, sample size, and topline.
5. Official argument signers in the voter guide, and published endorsement lists.
6. News and advocacy pages, used only to identify who said something, and labeled as secondary.

The June 25, 2026 Secretary of State qualification press release prints an earlier fiscal estimate for several initiatives. The voter-guide analysis is later. Where the two differ, the voter-guide analysis is the estimate a ballot explainer should use. The page does that on the items checked.

### 2.3 Evidence grades

- **A.** The page or the primary document was opened in this review, and the quotation below is from that opening.
- **B.** The quotation was recorded from the primary document during the same review and was not re-opened while this file was written. The citation is still the primary document. A fact-checker should open it.
- **C.** Arithmetic recomputed here from grade A or B inputs. The arithmetic is checked by repeating the operation. It does not add a new source.

### 2.4 What “fact” and “judgment” mean here

**Fact,** in this file, means a statement that is settled by looking at a named document or by repeating a named calculation. Two people who open the same page should get the same sentence and the same quotient.

**Judgment** means a conclusion that depends on how language is read, how much weight to give one fact beside another, or how a chart should be drawn when the source gave words instead of endpoints. A judgment can be well supported and still be something a reasonable person can decline.

The file does not call a judgment a fact. It also does not treat every disagreement as a judgment. If the source prints “44 percent no” and the page says that share was not published, that mismatch is a fact.

### 2.5 How the arithmetic was done

Page figures stored in billions were converted to dollars by multiplying by 1,000,000,000 and rounding to the nearest dollar. LAO table figures are in millions of dollars. Schedule 8 and Schedule 9 figures are in thousands of dollars. Those units are named at each step.

Percentages use the page’s own expenditure total unless a step says otherwise. The page function is:

```text
pct(value) = (value / totalSpending * 100).toFixed(2)
```

`toFixed(2)` rounds to two decimal places. It does not preserve a leading zero that would show a third decimal. That behavior is part of the finding on Proposition 39.

The checker that repeats these tests is `tools/verify_fiscal/verify_fiscal.py`. It reads the page and compares it with `tools/verify_fiscal/official_fiscal_2026.json`. It does not download anything. On October 5, 2026 it exited with status 1. The only failure was the words “CalVet revenue bond.” Warnings covered the $18.5 billion rounding, the government-bar label, and the Proposition 39 and 45 endpoints.

## 3. Chain of reasoning

### 3.1 Proposition 40: what the 5 percent applies to

**Page text (grade A).** The one-line summary says: “Taxes covered wealth above $1B at up to 5%, mainly for health care.” The yes box says: “California collects a one-time 5% wealth tax from covered billionaires and trusts.”

**Question.** Is the tax 5 percent of the amount above $1 billion, or 5 percent of net worth?

**Step 1.** Open the LAO analysis for Proposition 40 (grade A), [lao.ca.gov/BallotAnalysis/Proposition?number=40&year=2026](https://lao.ca.gov/BallotAnalysis/Proposition?number=40&year=2026). The proposal section says:

> Under Proposition 40, billionaires who were residents of California on January 1, 2026 would have to pay a one-time state tax equal to 5 percent of their net worth. The tax would be due in 2027. Taxpayers would have the option to spread the payments over five years but would have to pay more to do so. Real estate, pensions, and retirement accounts generally would be excluded from the tax.

The official yes statement on that page says: “The state would collect a one-time tax from billionaires equal to 5 percent of their wealth.”

**Step 2.** Open the Secretary of State certification press release of June 25, 2026 (grade A). It prints the Attorney General title circulated at qualification:

> Imposes one-time tax of up to 5% on taxpayers and trusts with covered assets valued over $1 billion; covered assets include businesses, securities, art, collectibles, and intellectual property, but exclude real property and some pensions and retirement accounts.

“Up to 5%” and “trusts” are in that title. The LAO narrative says “5 percent of their net worth” and does not spell out a phase-in table.

**Step 3.** Compare the bases with an illustration. The illustration is not an official tax bill. It shows why the two English readings are different amounts.

```text
Reading A, whole net worth:  0.05 × $2,000,000,000 = $100,000,000
Reading B, only the excess:  0.05 × ($2,000,000,000 − $1,000,000,000) = $50,000,000
Difference:                   $50,000,000
```

Near $1.1 billion the two readings differ by much more than half, because the excess is small and the whole fortune is not. The exclusions matter on top of either reading. A fortune held as real estate is largely outside the tax under both official summaries. The one-liner does not say that.

**Conclusion.** The LAO base is net worth. The page’s “above $1B” phrase is the sentence that invites the excess-only reading. The yes box is closer to the official yes statement, and it adds trusts, which the Attorney General title includes and the LAO yes statement does not.

**Fact.**

- The LAO sentence is “5 percent of their net worth.”
- The Attorney General title is “up to 5%” on taxpayers and trusts with covered assets over $1 billion, with stated exclusions.
- The one-liner says “covered wealth above $1B at up to 5%.”
- The illustration’s two products are $100 million and $50 million.

**Judgment.** Whether every reader must take “above $1B” to mean “only the dollars above $1 billion.” The fair defense is that “above $1B” identifies who is taxed, and “up to 5%” is the rate on covered wealth. That defense still leaves out the exclusions, and it has to fight the ordinary English reading of “tax above $1 billion at 5 percent,” which is a tax on the excess. The correction is to use the LAO’s own words: 5 percent of net worth, real estate and some retirement accounts excluded.

**Not established here.** The exact phase-in between $1 billion and $1.1 billion. Secondary descriptions of the proposed law give that schedule. The proposed-law PDF was not re-read for this file. “Up to 5%” is the official sign that the rate is not described as flat in the Attorney General title. The LAO analysis that voters are pointed to says 5 percent of net worth and does not print the phase-in.

### 3.2 Proposition 40 and the conflict with 41 and 42

**Page text (grade A).** The overview says: “Prop 40 creates the billionaire tax. Props 41 and 42 can block it. If conflicting measures pass, the one with more Yes votes controls.” The flow says that if 41 or 42 has more yes votes, Proposition 40 revenue is $0 and the tax is void.

**Step 1.** California Constitution, Article II, section 10(b), as displayed by the Legislature’s code site (grade A):

> If provisions of two or more measures approved at the same election conflict, the provisions of the measure receiving the highest number of affirmative votes shall prevail.

The rule is the highest number of yes votes, not the higher yes-vote percentage, and not whichever measure was chaptered later. It applies to conflicting provisions of measures that were approved. A measure that fails does not enter the comparison.

**Step 2.** The same LAO Proposition 40 analysis (grade A) says:

> If Proposition 41 or 42 on this same ballot receive more “yes” votes than Proposition 40, then Proposition 40 could be stopped from becoming law even if it gets yes votes from a majority of voters. This is because the courts could find that Proposition 41 or 42 conflict with Proposition 40.

**Step 3.** The Attorney General summaries of Propositions 41 and 42, recorded from the voter guide in this review (grade B), each say that another measure on the same ballot is void if it conflicts and if this measure receives more affirmative votes. Those sentences are the measures’ own instructions. They still depend on a conflict existing.

**Conclusion.** The page is right about the direction of the rule and right that a defeated 41 or 42 cannot block 40. It states the block as automatic. The LAO states it as something a court could find.

**Fact.** Section 10(b) uses the highest number of affirmative votes. The LAO uses “could” twice: “could be stopped” and “the courts could find.”

**Judgment.** How certain to sound before a court has ruled. A reader who wants the measures’ own text can say the voiding clause is written as mandatory once a conflict and a higher yes-vote total exist. A reader who wants the LAO’s uncertainty can say the conflict itself is what a court has to find. Both sentences should be available. The overview currently gives only the certain version.

### 3.3 Propositions 41 and 43: the poll numbers are published

**Page text (grade A).**

- Proposition 41: yes 51, no left blank, note “PPIC, Sept. 2026; No share not published.”
- Proposition 43: both shares blank, note “PPIC: below majority; exact topline unpublished.”

**Step 1.** Open the PPIC publication (grade A), fieldwork September 4–10, 2026, [ppic.org publication](https://www.ppic.org/publication/ppic-statewide-survey-californians-and-their-government-september-2026/). The methodology block on that page: 1,745 adults; the likely-voter margin is ±3.8 percentage points for 1,103 likely voters. Proposition questions are labeled likely voters only.

**Step 2.** Read the likely-voter narrative on that page.

- Proposition 41: “would vote yes (51%, 44% no).” The questionnaire block on the same page prints `51% yes`, `44% no`, `5% don’t know`.
- Proposition 43: “Forty-three percent of likely voters say they would vote yes … 51 percent would vote no.”

**Step 3.** Compare. The 51 on Proposition 41 matches. The statement that the no share was not published does not. “Below majority” is true of Proposition 43’s yes share (43 is less than 50). “Exact topline unpublished” is not true of this publication.

**Conclusion.** Both notes are false as descriptions of the PPIC release. This does not depend on which side one favors. The numbers are on the page the card cites.

**Fact.** PPIC likely voters: Proposition 41, 51 / 44 / 5 don’t know. Proposition 43, 43 / 51. The card’s notes deny that those no, and those exact, shares were published.

**Judgment.** None about whether the shares exist. There is a separate editorial judgment, discussed in section 3.10, about whether a card that cites one pollster must also show another pollster.

### 3.4 The other twelve poll pairs

**Step 1.** From the same PPIC narrative (grade A), likely voters:

| Proposition | PPIC yes | PPIC no | Card | Card’s named source |
| --- | --- | --- | --- | --- |
| 1 | 55 | 43 | 55 / 43 | PPIC |
| 2 | 60 | 39 | 60 / 39 | PPIC |
| 3 | 58 | 40 | 54 / 34 | Berkeley IGS |
| 4 | 42 | 53 | 42 / 53 | PPIC |
| 5 | 35 | 59 | 35 / 59 | PPIC |
| 37 | 61 | 35 | 61 / 35 | PPIC |
| 38 | 55 | 42 | 55 / 42 | PPIC |
| 39 | 43 | 55 | 39 / 52 | Berkeley IGS |
| 40 | 52 | 46 | 45 / 42 | Berkeley IGS |
| 42 | 54 | 43 | 54 / 43 | PPIC |
| 44 | 34 | 61 | 34 / 61 | PPIC |
| 45 | 49 | 46 | 49 / 46 | PPIC |

Where the card names PPIC, the yes and no match this narrative. Where the card names Berkeley, the yes and no do not match PPIC. That is what should happen if the card is citing Berkeley rather than miscopying PPIC.

**Step 2.** Berkeley IGS Release #2026-20, September 25, 2026, fieldwork September 15–20, was read from the release PDF in this review (grade B). The recorded likely-voter toplines were: Proposition 3, 54 yes / 34 no / 13 undecided; Proposition 39, 39 / 52 / 9; Proposition 40, 45 / 42 / 13. Those are the three Berkeley cards. The release was not re-opened while this file was written. The eScholarship item the page cites is `3w14s99c`, and the review identified that item as Release #2026-20.

**Step 3.** The page computes a remainder with `Math.max(0, 100 - yes - no)` when both shares are numbers (grade A, the `pollMarkup` function). PPIC’s own note says numbers may not add to 100 because of rounding. Where the published three-way sum is 99 or 101, the page’s remainder is one point away from the published don’t-know or undecided. The review recorded that for Propositions 3, 5, 37, 42, and 44.

**Fact.** The PPIC column above was read from the publication. The Berkeley cards match the release as recorded in the review. The one-point remainder is a property of the code plus ordinary rounding.

**Judgment.** Whether a one-point rounding remainder needs a correction. It is visible, and it is small relative to a ±3.8 point margin. It is not the same kind of error as saying a published number was unpublished.

### 3.5 Proposition 1: general-obligation bond, including the veterans piece

**Page text (grade A).** The flow chart contains the label “CalVet revenue bond” with the subtitle “$1.25B.” A separate card says “Prop 1 · $11.25B · General-obligation bond” and “General Fund repays most debt service.” The cost line says “$500–600M a year for about 25 years” and “CalVet loans are borrower-repaid.”

**Step 1.** Open the LAO analysis (grade A), [Proposition 1](https://lao.ca.gov/BallotAnalysis/Proposition?number=1&year=2026). It says:

> Proposition 1 allows the state to sell $11.25 billion in general obligation bonds for housing purposes. This amount consists of (1) a $10 billion bond for a variety of state housing programs that would be repaid by the General Fund and (2) a $1.25 billion bond that would be repaid by veterans’ payments on their home loans.

The fiscal section says the General Fund cost of the $10 billion housing bond would be “$500 million to $600 million annually for about 25 years,” and that this is “about one-quarter of 1 percent (0.25 percent) of the state’s total General Fund budget.” On the veterans piece it says payments “have always covered the amount owed on the bonds, meaning the program has always operated at no direct cost to the state.”

The background section of that analysis says the existing veterans program “sells general obligation bonds.”

**Step 2.** The proposed-law review in this project (grade B) recorded Military and Veterans Code section 998.754(a): the veterans bonds “shall be and constitute a valid and legally binding general obligation of the State of California, and the full faith and credit of the State of California is hereby pledged.” That PDF was not re-opened for this file. The LAO sentences in Step 1 are enough to reject the label “revenue bond.” The statute citation is the additional pledge language.

**Step 3.** Compare with Proposition 37, whose LAO analysis was recorded in this review (grade B) as authorizing revenue bonds, with a statutory legend that the bond is payable from program funds and is not a debt or a pledge of the state’s faith and credit. The page calls Proposition 37 a revenue-bond authority. That label matches. The same words on the Proposition 1 veterans piece do not.

**Conclusion.** Both pieces of Proposition 1 are general-obligation bonds. Veterans’ payments have covered the $1.25 billion piece in practice. The General Fund repays the $10 billion piece. The flow label uses the legal name of a different instrument.

**Fact.** The LAO calls the $11.25 billion general-obligation bonds and splits repayment $10 billion / $1.25 billion. The page’s flow says “CalVet revenue bond.”

**Judgment.** Whether a loose label is harmless because the subtitle says the money is repaid by borrowers. The practical repayment is real. The legal form is still a general-obligation bond. The page already has a revenue-bond measure, Proposition 37, so using the same words for both teaches the wrong distinction. The big-number card, which says general-obligation, should be the label on the flow as well.

### 3.6 Debt-service percentages for Propositions 1, 3, and 38

**Page text (grade A).** Propositions 1 and 38: “about 0.20–0.24% of the General Fund.” Proposition 3: “about 2–6% of today’s General Fund.” The method note says annual cost is compared with the “$251.477B enacted 2026–27 General Fund.”

**Step 1.** The LAO dollar ranges are grade A.

- Proposition 1: $500 million to $600 million a year for about 25 years, “about 0.25 percent.”
- Proposition 38, [LAO analysis](https://lao.ca.gov/BallotAnalysis/Proposition?number=38&year=2026): “$500 million to $600 million annually for about 20 years,” also “about one-quarter of 1 percent (0.25 percent).”
- Proposition 3, [LAO analysis](https://lao.ca.gov/BallotAnalysis/Proposition?number=3&year=2026): “between $5 billion and $15 billion each year.” The analysis does not print a percentage of the General Fund. It says “the top 2 percent of California taxpayers pay these higher rates,” and “Roughly 40 percent of the funding would go to schools and community colleges. The rest would go to other state programs.”

**Step 2.** Divide the LAO dollar ranges by the page’s $251.477 billion expenditure total (grade C).

```text
500,000,000 / 251,477,000,000 = 0.00198825 = 0.1988%, which rounds to 0.20%
600,000,000 / 251,477,000,000 = 0.00238590 = 0.2386%, which rounds to 0.24%
5,000,000,000 / 251,477,000,000 = 0.0198825 = 1.99%, which the page calls about 2%
15,000,000,000 / 251,477,000,000 = 0.0596476 = 5.96%, which the page calls about 6%
```

**Step 3.** Ask what 0.25 percent of that baseline would be.

```text
0.0025 × 251,477,000,000 = 628,692,500
```

So the LAO’s “about 0.25 percent” is a round description of a cost whose top is $600 million, not a statement that debt service runs up to $629 million. Using revenue ($226.754 billion) instead of spending would make $600 million about 0.26 percent. The page’s choice of the expenditure total matches the method note and the LAO’s habit of comparing bond cost with the General Fund budget.

**Conclusion.** The dollars match the LAO. The 0.20–0.24 and 2–6 percentages are the page’s quotients. They are not printed in the LAO analyses. They are close to the LAO’s “about 0.25 percent” for the two bonds. They should be labeled as the page’s comparison.

**Fact.** The quotients above. The LAO phrases “0.25 percent,” “$5 billion and $15 billion,” and “top 2 percent of California taxpayers.”

**Judgment.** Whether printing a more precise quotient beside the LAO’s round “0.25 percent” is a defect. It is a defect only if a reader thinks the LAO published 0.20–0.24. The underlying cost is the same.

**Separate vintage note, grade A.** The June 25 qualification press release said the immunology bond would cost “about $500 million annually for 25 years.” The voter-guide analysis opened for this check says $500–$600 million for about 20 years. The page follows the voter-guide analysis. That is the later document written for this ballot.

### 3.7 Proposition 39 and Proposition 45: endpoints the LAO did not publish

**Page data (grade A).** In `annualImpacts`:

```text
Proposition 39: low 0.02, high 0.3, label “Tens to low hundreds of millions / year”
Proposition 45: low 0.08, high 0.11, label “High tens of millions; possibly over $100M / year”
```

The units are billions. So 0.02 is $20 million, 0.30 is $300 million, 0.08 is $80 million, and 0.11 is $110 million.

**Step 1.** Proposition 39. The fiscal review recorded this LAO sentence (grade B): state and local costs “each year by tens of millions of dollars to low hundreds of millions of dollars,” representing “less than one-quarter of 1 percent (0.25 percent)” of the General Fund. The June 25 qualification press release (grade A) uses the same annual range and also mentions one-time preparation costs in the tens of millions. Neither document prints $20 million or $300 million.

**Step 2.** Apply the page’s percent function (grade C). The six spending categories sum to 251.477214 billion dollars:

```text
93.675003 + 91.091750 + 26.691050 + 14.447846 + 16.553565 + 9.018000
= 251.477214
```

```text
0.02 / 251.477214 × 100 = 0.007953
toFixed(2) of 0.007953 = "0.01"
0.30 / 251.477214 × 100 = 0.11930
toFixed(2) of 0.11930 = "0.12"
```

The card’s “roughly 0.01–0.12%” is what that function prints. The unrounded low end is about 0.008 percent. The LAO’s only percentage is “less than 0.25 percent,” which on this baseline is just under $629 million. The page’s $300 million high end is inside that description and narrower than it. The costs are state and local. The chart heading calls the rows “General Fund effects.”

**Step 3.** Proposition 45. The LAO analysis was opened (grade A), [Proposition 45](https://lao.ca.gov/BallotAnalysis/Proposition?number=45&year=2026):

> These costs likely would be in the high tens of millions of dollars annually, potentially exceeding $100 million annually.

The same section says the costs are initial, for state and local governments including courts, that fees would cover some of them, and that after the initial period some costs likely decline. The longer-term effect is “uncertain but potentially more significant.” There is no $80 million floor and no $110 million ceiling.

**Conclusion.** The words on the labels track the LAO. The bar endpoints are the page’s translations of those words. For Proposition 39 the translation also becomes a General Fund percentage the LAO did not publish, and the rounding makes the low end look twice as large as the unrounded quotient (0.01 printed, 0.008 actual).

**Fact.** The LAO sentences. The four endpoints appear in the page’s script and not in those sentences. The `toFixed` result.

**Judgment.** A chart has to have a width. Choosing $20 million and $300 million as a picture of “tens to low hundreds” is an illustration. Drawing it as if those were the LAO’s bounds, on a chart titled as General Fund effects, is the step that overclaims. The same is true of stopping Proposition 45 at $110 million when the LAO said the cost could exceed $100 million and did not give a top.

### 3.8 The 2026–27 budget totals

**Page data (grade A).** The script stores, in billions: personal income tax 145.609, corporation tax 45.167, sales and use tax 35.598, insurance plus other 10.986, net transfers −10.605, current-year resources 226.754, General Fund in the all-funds list 251.477, special funds 95.129, bond funds 5.104, federal funds 187.190, operating deficit 18.5.

**Step 1.** Open LAO Report 5197 (grade A), [Overview of the Spending Plan](https://lao.ca.gov/Publications/Report/5197), August 26, 2026. Figure 3, 2026–27 enacted, in millions:

```text
Revenues and transfers    226,754
Expenditures              251,477
```

Figure 4, 2026–27, in millions:

```text
Personal income tax        145,609
Sales and use tax           35,598
Corporation tax             45,167
Insurance tax                4,728
Other revenues               6,258
Transfers and loans        −10,605
Totals, revenues and transfers  226,754
```

Figure 5, 2026–27, in millions:

```text
General Fund     251,477
Special funds     95,129
Bond funds         5,104
Federal funds    187,190
```

The report says these are administration estimates of actions through July 1, 2026. That is the vintage the page names.

**Step 2.** Add Figure 4 (grade C).

```text
145,609 + 35,598 + 45,167 + 4,728 + 6,258 = 237,360
237,360 + (−10,605) = 226,755
```

The total line in the same figure is 226,754. The components, after rounding to the million, are $1 million higher than the total line. The page stores both the rounded components and the official total. Their difference is that $1 million. It is not a missing tax.

Schedule 8, in thousands, was read in the budget review (grade B): gross revenue $237,358.829 million, transfers −$10,604.697 million, revenues and transfers $226,754.132 million. At that precision, gross revenue plus transfers equals revenues and transfers. The $1 million gap appears only after the lines are rounded.

**Step 3.** Add Figure 5 (grade C).

```text
251,477 + 95,129 = 346,606
346,606 + 5,104 = 351,710
351,710 + 187,190 = 538,900
```

The LAO text says total state spending, including special funds, reaches about $347 billion, and all-funds spending is roughly $539 billion. The Department of Finance overview (grade B, the public chart) says total state funds are about $351.7 billion and counts bond funds in that phrase. The page’s “state spending” is General Fund plus special funds, $346.606 billion. That matches the LAO budget-total idea. It does not match the Department of Finance phrase “total state funds,” which includes the $5.104 billion of bond funds. The page says which two pieces it is adding. The label is easy to confuse with the other official total, so the sentence has to keep the definition.

**Step 4.** Spending categories. The Department of Finance overview chart (grade B) lists K–12 $91,092 million, Health and Human Services $93,675 million, higher education $26,691 million, corrections $14,448 million, and other $25,571 million.

```text
91,092 + 93,675 + 26,691 + 14,448 + 25,571 = 251,477
```

The page’s four large categories match those lines at the million. Its two “other” bars are 16.553565 and 9.018000.

```text
16.553565 + 9.018000 = 25.571565
```

That is $0.565 million above the chart’s $25,571 million “other,” before the $5,000 rounding described next.

The budget review reconstructed the bars from Schedule 9 (grade B). Health and Human Services on the page is the Schedule 9 section plus the agency secretary: 93,394,388 + 280,615 = 93,675,003 thousand dollars. K–12 is the section plus ScholarShare: 90,902,498 + 189,252 = 91,091,750 thousand dollars. Higher education is 26,691,050 thousand. Corrections is 14,447,846 thousand. Those four match the page exactly.

“Government, courts & executive” is three groups: Legislative, Judicial, and Executive 7,083,302; Government Operations 5,149,671; General Government 4,320,592.

```text
7,083,302 + 5,149,671 + 4,320,592 = 16,553,565 thousand dollars
```

General Government, in that reconstruction, includes retiree health and dental 3,205,158, supplemental pension payments 556,000, and a Proposition 98 reconciliation of −1,066,131, among other items. The dollar total matches. The words “courts & executive” do not describe retiree health, pensions, agriculture, veterans, or a negative school-funding reconciliation.

“Other agencies” is six groups that sum to 9,017,995 thousand dollars. The page stores 9.018 billion, which is that sum rounded to the nearest million. The extra $5,000 is why the six page bars sum to $251,477,214,000 while Schedule 9 expenditures are $251,477,209,000. Both screen displays round to $251.5 billion.

**Fact.** The LAO millions match the page’s stored budget lines. The $1 million revenue residual and the $5,000 spending residual are rounding. The $16.554 billion equals the three agency groups named above.

**Judgment.** Whether “Government, courts & executive” is an acceptable short name. “Government” can be read broadly. “Courts & executive” cannot carry retiree health and a Proposition 98 reconciliation. Renaming the bar is the correction. Changing the $16.554 billion would make the bar wrong.

### 3.9 Two deficits, and the reserve figure

**Page text (grade A).** `operatingDeficit` is 18.5. The sankey’s balance bridge is spending minus current-year resources. The visible copy says the LAO describes an operating shortfall and that this is different from the gap between this year’s revenues and transfers and total appropriations. Proposition 2’s cost line says current broadly usable reserves are about $20 billion.

**Step 1.** From Figure 3 (grade C):

```text
251,477 − 226,754 = 24,723 million dollars = $24.723 billion
```

That is the gap between enacted spending and revenues and transfers. The page’s bridge displays as $24.7 billion. Report 5197 says the budget draws down the elevated prior-year balance. The Special Fund for Economic Uncertainties goes from $29,223 million at the end of 2025–26 to $4,500 million at the end of 2026–27.

```text
29,223 − 4,500 = 24,723
```

The simple gap and the reserve draw are the same number.

**Step 2.** Report 5197 (grade A) says “the administration estimates an $18.5 billion operating deficit in 2026–27” and says the enacted budget “is balanced on a cumulative basis” because it uses the prior-year balance. The same report says the budget deposits $6.4 billion into the Temporary Surplus Holding Account, to be withdrawn in 2027–28, and that neither the LAO nor the Department of Finance treats that account as a reserve.

**Step 3.** The Department of Finance multiyear row “Operating Surplus/Deficit with BSA Transfer” was recorded as −$18,335 million (grade B). Rebuild it from the LAO millions plus the $6,388 million holding-account deposit printed on the Department of Finance overview chart (grade B):

```text
226,754 + 6,388 = 233,142
251,477 − 233,142 = 18,335
```

The $6,388 million is inside “revenues and transfers” as a negative transfer, so it widens the simple gap. The operating-deficit definition adds it back. The simple gap is larger than the operating deficit by that deposit:

```text
24,723 − 18,335 = 6,388
```

**Step 4.** Rounding. $18,335 million is $18.335 billion. The nearest tenth of a billion is $18.3 billion. The LAO prose says $18.5 billion. The difference is $165 million. The page copies the LAO sentence, which is a real sentence, and attributes it to the LAO, which is the right attribution. It is a loose rounding of the administration’s cell.

**Step 5.** Reserves in Figure 3 at the end of 2026–27 (grade A): Budget Stabilization Account $15,070 million, Special Fund for Economic Uncertainties $4,500 million.

```text
15,070 + 4,500 = 19,570 million dollars = $19.570 billion
```

The same section says the school reserve would be $9.2 billion. “About $20 billion” matches the first pair. It does not match that pair plus the school reserve ($28.8 billion). The figure is an end-of-year estimate under the enacted plan, not a cash count on October 5.

Proposition 2’s rule change is also in Report 5197 (grade A): the cap would rise from 10 percent to 20 percent of General Fund tax revenues, and extra debt payments set to expire in 2030 would run through 2040. The page’s description of those two rules matches.

**Fact.** $24.723 billion, $18.335 billion, $6.388 billion, and $19.570 billion, and the LAO sentence “$18.5 billion.”

**Judgment.** Which deficit to put in the headline. Both are real and they measure different things. The page already says they differ. The remaining choice is whether the headline should stay at the LAO’s $18.5 billion or show the administration’s $18.335 billion beside it. Showing both is the version that does not make the reader pick a rounding.

### 3.10 Conditions the short lines drop

These are smaller than the items above. Each one is a fact about a document, plus a judgment about whether the short line is still fair.

**Proposition 4 (grade B).** The Attorney General summary says the current ban on public financing has an exception “in charter cities and counties.” The page’s no-vote line says “charter cities.” Counties are omitted. The LAO cost, “a few hundred thousand dollars each year” for Fair Political Practices Commission guidance, matches the page. The measure sets no program and no overall dollar cap. That part of the con box matches the LAO.

**Proposition 5 (grade B).** The official title says statewide officers. The page repeats the title. The amended constitutional section is Article II, section 15, and the LAO analysis also describes the vacancy rules for legislative seats. Lieutenant-governor succession is the rule for the governor. If the recall falls early in the term, a special election follows. The short line is right about the title and incomplete about the offices.

**Proposition 39 (grade B for the LAO mechanics, grade A for the qualification summary).** Mail voters must provide the last four digits of the identification number they designated at registration. The Attorney General summary uses a mismatched number — Social Security digits when the registration designated a driver-license number — as an example of a ballot that would not count. The page says “ID digits” and does not say a mismatch voids the ballot.

**Proposition 42 (grade B).** The Attorney General date is taxes that are “enacted or take effect on or after January 1, 2026.” The page says “enacted after Jan. 1, 2026.” Taking effect on that date is part of the trigger. The LAO fiscal line is that future revenue may not rise as much. “Progressive revenue options,” in the con box, is wider than a ban on new taxes on personal property and on defined retroactive taxes. That width is a characterization in an argument box.

**Proposition 43 (grade B).** The LAO says the two-thirds threshold applies beginning January 1, 2027, to new, increased, or extended local special taxes proposed by voters. The page says the bar rises from a majority to two-thirds. The start date and the coverage of extensions are omitted. The voter guide prints the legislative vote on ACA 22 as Senate 35–1 and Assembly 68–2.

**Proposition 44 (grade B).** The 90 percent rule, a penalty equal to the shortfall, fee-funded enforcement “in the low tens of millions,” waivers, and a refund if the clinic complies within five years match the official summaries. The LAO also says other state and local costs are uncertain, including higher Medi-Cal costs and possible closures, and that these clinics currently report spending about 80 percent of revenue on health care. The page’s cost line is the enforcement piece only.

**Proposition 45’s yes line (grade A).** The LAO says applicants may use the new procedures or the existing ones. That supports “may opt into.” The same analysis, opened for this check, also says the measure limits the agency to one alternative developed by the applicant, assesses impacts under the rules in place when the application is submitted, limits tribal consultation to federally recognized California tribes, limits how long comments are accepted, and limits what a court can consider and can stop. “Faster” is true as far as deadlines. It does not carry those other changes.

**Fact.** Each omitted or extra condition above is a sentence in the named official summary.

**Judgment.** A one-line summary cannot carry every condition. The ones listed here change who is covered, what voids a ballot, or when a rule starts. They belong in the yes/no line or the sentence under it. Leaving them out is an editorial cut, and it is a cut that a fact-checker can name.

### 3.11 Coalition colors

The page says party-lean labels describe coalitions, not the content of a measure. The color is assigned in `partyLean` (grade A). A color is a judgment about a set of public positions. The positions themselves are facts when a signer list or an endorsement list shows them.

The endorsement grid below was recorded from the UC Berkeley IGS compilation checked September 28, 2026, and from voter-guide signer lists (grade B). It was not re-opened while this file was written. Y is support, N is opposition, NP is a stated neutral.

| Group | 40 | 43 | 45 | 1 | 5 | 44 |
| --- | --- | --- | --- | --- | --- | --- |
| California Democratic Party | Y | N | N | Y | Y | N |
| California Republican Party | N | Y | Y | NP | N | N |

**Proposition 40.** Facts recorded from the voter-guide arguments: the yes argument is signed by an SEIU-UHW leader, a Planned Parenthood patient-access worker, and a member of an AFT local. The no argument is signed by the California Medical Association, the California Primary Care Association, and the California School Boards Association, and it names Governor Gavin Newsom, the Democratic and Republican candidates for governor, the California Teachers Association, the building trades, carpenters, and firefighters among the opponents. The state Democratic Party is recorded as Yes. The color in the code is Democratic.

The defense of the color is that it follows the state party endorsement. The criticism is that the Democratic governor and several Democratic-aligned unions and health groups are on the other side, so one color describes a split as a party measure. The sentence on the card, “progressive-labor support,” also misses the labor split. Those are judgments about emphasis. The signer list is the fact.

**Proposition 43.** Facts: ACA 22, author Assemblymember Buffy Wicks, a Democrat; Assembly 68–2; Senate 35–1 (grade B, voter guide and bill history). The campaign supporters named in the quick reference are taxpayer and business groups. The named opponents are labor organizations. The state parties are Republican Yes and Democratic No. The card’s sentence discloses a bipartisan referral. The color is Republican.

The defense is that the color describes who is campaigning now. The criticism is that a red card on a measure placed on the ballot by a near-unanimous, Democratic-authored referral tells the reader the origin was partisan. The sentence tries to hold both facts. The color keeps one.

**Proposition 5.** Facts: the no argument is signed by Senate Minority Leader Brian Jones and Assemblymember Joe Patterson (grade B). Their argument, as recorded, does not use the phrase “election integrity.” The yes argument is signed by the League of Women Voters, California Common Cause, and a former Fair Political Practices Commission chair. “Election-integrity” is a frame added by the page. Naming the offices is the description that does not adopt a slogan.

**Proposition 45.** Facts: the state Republican Party is recorded as Yes and the state Democratic Party as No. The quick-reference supporters are the California Children’s Hospital Association, the California Water Association, and the California Council for Affordable Housing. The opponents include environmental organizations. The Republican color matches the party split. “Developer” is a shorthand for a coalition whose named supporters are hospitals, water, and affordable housing. The color is a judgment that tracks the parties. The interest-group sentence is the more specific fact.

**Proposition 1.** The state Republican Party is recorded as neutral, and no argument against was filed (grade B). Howard Jarvis Taxpayers Association is recorded as opposed. “Conservative opposition” is real and narrower than a party campaign. The Democratic color describes the support side. It is the softest of the Democratic colors.

**Propositions 38 and 44.** Both are uncolored in the code. On 38, both major parties are recorded as Yes. On 44, both are recorded as No, and the fight is labor against provider groups. Leaving them uncolored matches those records.

**Fact.** The signer names, the vote counts, and the party grid, at grade B.

**Judgment.** Which fact the color should emphasize when the party, the governor, the author, and the donors are not on the same side. A single color cannot carry a split. The correction is to drop the color where the split is the story, and to keep the names.

### 3.12 Argument-box sentences that conflict with the Analyst

These sit in boxes the page identifies as arguments. They are listed because a reader can still treat them as findings.

**Proposition 45, pro box (grade A for the LAO, grade A for the page).** “Could get housing and infrastructure built faster while keeping environmental standards.” The speed clause is a possible result, not a measured one. “Keeping environmental standards” conflicts with the LAO list in section 3.10: one alternative, standards frozen at the application date, narrower tribal consultation, a capped comment period, and a narrower remedy. A defender can say CEQA still applies, so the standards are kept in that sense. The LAO’s list is the more specific account of what changes.

**Proposition 39, con box (grade B).** “Without evidence of widespread voter fraud.” The LAO analysis does not discuss fraud incidence. The official argument against, as recorded, calls the measure costly and unnecessary. It does not use the fraud sentence. The sentence is the page’s argument, inside an argument box. It is not an LAO finding.

**Proposition 40, pro box (grade A for the LAO, grade B for the campaign line).** “After federal cuts” is not in the LAO analysis or the Attorney General bullets opened for this check. The quick-guide pro argument uses that rationale. Inside a pro box, it is campaign reasoning. It should not migrate into the neutral summary.

**“Poison pill” and “countermeasure” (grade A for where they sit).** “Poison pill” is in the con box. “Countermeasure to Prop 40” is in the type tag, which is outside the argument boxes. The measures are written as general rules. Each can affect Proposition 40 if it passes with more yes votes. Whether they were designed for that purpose is what the official opposition arguments assert. That purpose claim belongs with the arguments. The type tag currently states it as classification.

## 4. What survived

These were checked and match the document named.

- November 3, 2026 is the statewide general election. The Secretary of State certified 14 measures on June 25, 2026: Propositions 1, 2, 3, 4, 5, 37, 38, 39, 40, 41, 42, 43, 44, and 45. Five were placed by the Legislature and nine qualified as initiatives (grade A).
- The stored budget lines in section 3.8 match LAO Figures 3, 4, and 5.
- Proposition 1’s $11.25 billion, the $10 / $1.25 split, and $500–$600 million a year for about 25 years.
- Proposition 2’s cap, from 10 percent to 20 percent, and extra debt payments extended from a 2030 expiration through 2040.
- Proposition 3’s $5–$15 billion, the 2031 expiration in the LAO yes/no statement, the top 2 percent, and the roughly 40 / 60 split between schools and community colleges and other state programs. The LAO does not dedicate the 60 percent to health care.
- Proposition 37’s ceiling of $25 billion in revenue bonds, loans up to 17 percent of the price, and the LAO finding of no direct state or local cost.
- Proposition 38’s $8.4 billion, $500–$600 million a year for about 20 years, about half to one institute and half to grants, a 2 percent state administration cap, a 20 percent California price discount, and 10 percent of discovery revenue to the state until the bonds are repaid.
- Proposition 40’s “tens of billions” over several years and a possible ongoing income-tax loss of less than $1 billion a year. The LAO publishes no tighter range. The 90 percent health-care share is in the LAO analysis. The LAO puts administration of the tax inside the other 10 percent, together with education and food assistance.
- Proposition 1’s “tens of thousands” of homes. The LAO says up to 40,000 multifamily rental units, about 2,500 farmworker units, about 1,200 university beds, and up to 40,000 homeownership households.
- The glossary’s short definitions of the named agencies and of the Gann Limit are not false. “Gann Limit” is a common name. The official summaries say “state spending limit.”

## 5. What this record does not settle

- The Proposition 40 phase-in formula and the trust-by-trust threshold, until the proposed-law PDF is quoted section by section.
- Berkeley Release #2026-20’s toplines, until that PDF is opened again. They are grade B.
- Schedule 8 and Schedule 9 row titles, until those PDFs are opened again. The sums in this file were re-added from the recorded rows and match the page and the LAO millions. They are grade B on the row names and grade C on the addition.
- Which committees raised the most money. No FPPC dollar ranking was pulled.
- Any poll released after the PPIC and Berkeley waves other than as a reminder that snapshots move. An October 4 survey was reported in the polling review and was not re-read for this file, so its toplines are not used as corrections.
- How anyone should vote.

## 6. How to repeat the check

1. Open `ca-2026-ballot/index.html` and search for the sentence named in the finding.
2. Open the URL in that finding and search for the quotation.
3. Repeat the arithmetic in the same units.
4. Decide whether the remaining step is a fact about those two texts or a judgment about emphasis.
5. Run `python3 tools/verify_fiscal/verify_fiscal.py` for the budget lines, the bond label, and the chart endpoints.

A correction that cannot survive steps 2 and 3 should be dropped. A judgment that is labeled as a fact should be relabeled, even when the judgment is reasonable.
