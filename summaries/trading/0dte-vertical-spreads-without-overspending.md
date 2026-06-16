# How We Trade 0DTE Vertical Spreads (without over spending)

Source: https://www.youtube.com/watch?v=YH_hL1oRjU0

## TL;DR

Tastytrade’s point: 0DTE vertical spreads look cheap in buying power, but they are not “small risk.” Compared with similar 45 DTE spreads, they collect about **1/8 the credit** while carrying about **10x the intraday directional/gamma exposure**. Size them like a high-speed directional trade, not like a normal defined-risk income spread.

## Key points

- **Why use verticals:** naked SPX strangles can require roughly **$78k–$80k** buying power. Vertical spreads define risk and can reduce capital to hundreds/thousands depending on width.

- **Standard credit-spread heuristic:** sell a vertical for roughly **1/3 of strike width**. Example used:
  - Sell SPY 399 put / buy 390 put
  - Width: **$9**
  - Credit: **$2.17**
  - Max loss: **$6.83** per share, or **$683** per contract
  - Theoretical POP: **~62%**

- **0DTE example:** a 1-point SPY put spread around 0DTE:
  - Sell 404 put / buy 403 put
  - Credit: **$0.27**
  - Risk: **$0.73**
  - SPX equivalent: **$270 credit / $730 risk**
  - Theoretical POP: **~66%**

- **Study setup:** they compared short put verticals with:
  - Short leg: **35 delta**
  - Long leg: **25 delta**
  - Spread roughly **$10 wide**
  - 0DTE vs 45 DTE
  - P/L measured in first half of day if SPY moved +$2, +$1, unchanged, -$1, -$2

- **Main empirical takeaway:** same starting delta does not mean same risk. 0DTE spreads had about **10x the directional exposure** of 45 DTE spreads because gamma is much higher.

- **P/L sensitivity shown:** for short put spreads, as % of net credit:
  - SPY +$2: 0DTE **+70%** vs 45 DTE **+7%**
  - SPY +$1: 0DTE **+40%** vs 45 DTE **+3%**
  - Unchanged: 0DTE **+25%** vs 45 DTE **+1%**
  - SPY -$1: 0DTE **-15%** vs 45 DTE **-3%**
  - SPY -$2: 0DTE **-111%** vs 45 DTE **-7%**

- **Credit difference:** average credit for the same 35/25 delta structure:
  - 0DTE: **$27**
  - 45 DTE: **$217**
  - So 0DTE collects about **1/8 the credit**, but moves far faster.

- **Sizing implication:** one 0DTE spread can roughly match the day-to-day dollar risk of one 45 DTE spread, despite much lower credit. Do not scale contracts just because the credit or buying power looks small.

- **Width caveat:** making 0DTE spreads too narrow may not give enough room. In very short-dated options, many nearby OTM strikes can be nearly worthless unless direction is immediately right.

## Trading interpretation

This is not an “income” edge by itself. It is a gamma/directional trade with defined max loss. The market pays the seller because they warehouse very concentrated intraday path risk: small adverse moves can erase the credit fast.

Good use case:
- You have a strong intraday directional view.
- You want defined risk.
- You size by gamma exposure, not by premium collected.

Bad use case:
- Selling 0DTE spreads because the credit looks attractive annualized.
- Multiplying lots because buying power is small.
- Treating 0DTE like a 45 DTE tasty-style theta trade.

## Checklist before trading

- What is the directional view for today?
- What move invalidates it?
- Am I sizing as if this has **~10x** normal spread sensitivity?
- Is the credit enough for the width and execution cost?
- Do I have an exit rule if SPY moves against me by $1–$2?
- Am I okay with full max loss today?

## One-line summary

0DTE credit spreads are cheap to enter but expensive to be wrong in: roughly **1/8 the credit, 10x the speed of risk** versus 45 DTE spreads.
