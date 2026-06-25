---
title: "Ranking Option Strategies Based On Risk | Options Crash Course 2025"
source: "https://www.youtube.com/watch?v=RnZ485FB2Jg"
category: trading
summary_date: 2026-06-25
---

# Ranking Option Strategies Based On Risk | Options Crash Course 2025

Source: https://www.youtube.com/watch?v=RnZ485FB2Jg

## TL;DR

Jim Schultz’s core point: options are not automatically “high-risk leverage.” Depending on structure and sizing, options can reduce risk versus long stock, define risk exactly, or improve capital efficiency. The catch: the product gives flexibility, not free edge — bad sizing and hidden tail risk are still what kill you.

## Main framework

The video ranks option usage from lower-risk / risk-mitigating structures to higher-complexity structures:

1. Protective puts
2. Covered calls
3. Short puts / synthetic stock
4. Defined-risk spreads
5. Undefined-risk strategies
6. “Free butterfly” created by adjusting a ratio spread after the market moves

## Key points

### 1. Options are not inherently max-risk

- The myth he attacks: once “options” enters the conversation, people assume ultra-high-risk, max-leverage gambling.
- His correction: options can be used either to increase leverage or to reduce risk.
- Risk comes from structure, sizing, and portfolio context — not from the word “options.”

### 2. Protective puts reduce downside, but are often expensive

- Protective put = long stock portfolio + long puts, usually on SPY/QQQ, as crash insurance.
- Purpose: protect against violent downside events like dot-com bust, GFC, Covid crash.
- Tasty research on SPY from 2005–2019: buying **16-delta puts** for protection had average P/L around **-$57 per trade**, only protected around **7%** of the time, and was net negative over time.
- His read: useful as proof options can reduce risk, but not necessarily a good recurring strategy because insurance drag is real.

### 3. Covered calls are lower risk than long stock

Example: Microsoft at **$350**.

- Long 100 shares:
  - Profit above $350
  - Lose dollar-for-dollar below $350
  - Unlimited upside
- Covered call:
  - Long 100 shares at $350
  - Sell **45 DTE $370 call** for **$3**
  - Upside capped above $370
  - $3 credit buffers downside and turns flat stock into a profitable outcome

Conclusion: covered calls cap upside, but reduce risk versus pure long stock because collected premium lowers breakeven / cushions losses.

### 4. Short puts can be lower risk than long stock

Example: Amazon at **$140**, sell **$130 put** for about **$3.50**.

- If Amazon rises: long stock profits; short put expires worthless and keeps premium.
- If Amazon falls to **$135**: stock loses **$5/share**; short put still OTM, keeps premium.
- If Amazon falls to **$120**: stock loses **$20/share**; $130 short put has $10 intrinsic loss, offset by $3.50 premium, net loss about **$6.50**.

Conclusion: short puts cap upside, but can reduce downside versus buying stock outright.

### 5. Synthetic stock offers buying-power flexibility

Tony Batista clip: synthetic long stock = **short 50-delta put + long 50-delta call** at the same strike.

- Short put = roughly +50 delta.
- Long call = roughly +50 delta.
- Combined = roughly +100 delta, similar to 100 shares.
- Example in SPY: synthetic stock in a margin account used about **$9k buying power** versus about **$38k** to buy stock.
- In an IRA, adding a cheap far-OTM long put can convert it into a defined-risk structure while keeping near-stock delta; example reduced buying power from about **$39k** to **$8k**, while keeping around **95 deltas**.

Takeaway: options can replicate stock exposure with much less capital, but that also means leverage risk must be managed.

### 6. Defined-risk strategies give exact max loss

- Defined-risk strategies let you know maximum loss on entry.
- Examples:
  - Bullish: short put spread
  - Bearish: put diagonal spread
  - Neutral: iron condor
- Benefit: directional customization, positive theta exposure, higher probability-of-profit structures, and known downside.
- Main risk-control variable: position size.

Sizing rules he gives:

- For accounts around **$20k–$100k**: aim for **1–3% of net liq per defined-risk position**.
- For accounts > **$100k**: can often size below **1%** per trade.
- For accounts < **$20k**: may need to size higher, maybe **5–7%**, because products have minimum contract granularity.
- Avoid one trade becoming **15–40%** of account value. Even positive expectancy fails if one outcome dominates the book.

### 7. Undefined risk is not automatically worse

- Undefined-risk strategies have no built-in max-loss cap, unlike verticals/iron condors.
- But undefined risk must be judged relative to sizing and portfolio context.
- A naked short put can be less risky than long stock, as shown earlier.
- Tasty research from early 2023: using similar capital, portfolios of **iron condors** had higher long-term volatility than portfolios of **short strangles**, even though strangles have theoretically unlimited loss.
- His point: “defined risk” does not automatically mean lower realized portfolio risk; position size and structure matter more.

### 8. “Free butterfly” via ratio-spread adjustment

He demonstrates a staged trade using Disney options, around **30 DTE**:

Initial normal butterfly:

- Buy **93 put**
- Sell **2x 91 puts**
- Buy **89 put**
- $2-wide put butterfly
- Costs about **$0.25 debit**

Ratio spread version:

- Buy **93 put**
- Sell **2x 91 puts**
- Omit the **89 put** wing
- This creates a **1x2 put ratio spread** for around **$0.45–$0.50 credit**

Mechanic:

- The missing 89 put is the only difference between ratio spread and full butterfly.
- If Disney rallies or time passes, that far-OTM 89 put can decay from ~**$0.73–$0.74** to maybe **$0.40**.
- If you originally collected ~**$0.50** on the ratio and later buy the missing wing for **$0.40**, you complete the butterfly for a net **$0.10 credit**.
- Result: a “free butterfly” — worst case is keeping the small credit; best case is profit near the short strike.

Important caveat:

- It is not free at entry.
- You must first carry the undefined risk of the ratio spread.
- It becomes riskless only if the market cooperates enough for the missing wing to decay below the credit collected.

## Trading read-through

The real edge is not “options are safer” or “options are dangerous.” The edge/risk tradeoff is structural:

- Covered calls / short puts: you are selling upside/optionality and collecting premium. Edge, if any, is short-vol / liquidity provision / risk-premium harvesting, paid for warehousing downside or opportunity-cost risk.
- Protective puts: you buy convexity, but insurance drag is expensive unless timing or crash sensitivity is genuinely valuable.
- Defined-risk spreads: cleaner max loss, but small accounts can still over-concentrate because contracts are chunky.
- Undefined-risk spreads: can be reasonable if sized by stress scenarios, not theoretical max loss alone.
- Free butterfly: good adjustment tool, not free money. You get the “riskless” structure only after surviving the initial ratio-spread risk.

## Practical checklist

- Don’t rank strategies by label. Rank by actual dollar risk, sizing, convexity, liquidity, and portfolio correlation.
- Covered call / short put are lower downside than stock, but cap upside.
- Use defined-risk trades to control max loss, but keep position size small.
- For defined-risk trades, use **1–3% net liq** as a normal sizing anchor if account size permits.
- Do not let one options trade become the account’s main event.
- For undefined-risk trades, stress test real scenarios: gap moves, vol expansion, correlation spikes, margin expansion.
- Treat synthetic stock as leverage. Same delta with lower buying power can be useful or lethal.
- Treat “free butterfly” as an adjustment path, not a starting trade.

## One-line summary

Options are not inherently high risk; they are leverage/customization tools, and the real risk comes from sizing, structure, and whether you’re being paid enough to warehouse the tail.
