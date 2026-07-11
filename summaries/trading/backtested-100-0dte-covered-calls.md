---
title: "We Backtested 100 0DTE Covered Calls To See What Would Happen"
source: "https://www.youtube.com/watch?v=UEFA3W3tImA"
video_id: "UEFA3W3tImA"
category: trading
created: "2026-07-11"
---

# We Backtested 100 0DTE Covered Calls To See What Would Happen

Source: https://www.youtube.com/watch?v=UEFA3W3tImA

## TL;DR

Tastylive compares holding 100 SPY shares and repeatedly selling a 25-delta 0DTE call versus selling a 25-delta 45DTE call. The 0DTE version performs better on ordinary flat-to-up days because the full daily premium decays quickly, but performs worse on down days and caps large rallies sooner.

## Theory of edge

Covered calls do not create free income. Long stock supplies bullish beta; short call sells upside convexity and volatility risk premium. 0DTE concentrates that sale into daily gamma and execution risk. Market pays premium because seller repeatedly gives buyers same-day upside convexity.

## Mechanics

- Position: long 100 SPY shares + short one call.
- Call selected around 25 delta.
- Covered call remains bullish, not neutral.
- Short call lowers cost basis and raises probability of profit, but caps upside.
- Their generic example says adding a 25-delta call raises POP from roughly 50% to 65%, while replacing unlimited upside with limited max profit.
- Comparison: sell a fresh 25-delta 0DTE call daily versus hold a 25-delta call around 45 DTE.

## Study setup

- Underlying: SPY, 100 shares.
- Tested one-day P&L after SPY moves approximately +$2, +$4, unchanged, -$2, -$4, and large up days over +$8.
- At SPY near $400 and IV around 19%, $4 is roughly a 1% move and $8 roughly 2%.
- Title states 100 0DTE covered-call observations.

## Results

- Ordinary up days: 0DTE covered calls produced roughly 20%–100% more P&L than 45DTE calls across scenarios shown.
- Their aggregate takeaway: around 50% better P&L on normal up days.
- Unchanged day example: 0DTE short call earned about $0.40 versus about $0.05 from one day of decay on 45DTE call.
- Down days: 0DTE structure lost roughly 25% more than 45DTE structure.
- Reason: 0DTE call rapidly falls toward zero, leaving position almost fully long 100 shares with little remaining hedge.
- Large up days around +2%: 45DTE covered call outperformed by almost 40% because its 25-delta strike began farther OTM. Daily 0DTE strike sat closer and capped rally earlier.

## Payoff interpretation

- Flat / modest rise: 0DTE benefits from rapid same-day decay.
- Moderate decline: both lose through long stock; 45DTE call retains more value and therefore provides more offset.
- Large decline: covered call offers only small premium cushion; stock downside dominates.
- Large rally: 0DTE gets called away / capped sooner; 45DTE retains more upside because strike is farther away.

## Trading read-through

- This is a bullish stock-overlay strategy, not standalone yield.
- 0DTE advantage depends on frequent ordinary days. It gives up both tails: worse downside cushioning and earlier upside truncation.
- Daily execution means more slippage, fees, taxes, monitoring, strike selection, and assignment handling than study headline captures.
- Comparing single-day scenario P&L is not enough to establish long-run edge. Need full distribution, regime split, transaction costs, realized assignment, tax treatment, and path-dependent compounding.
- Their “50% better good days vs 25% worse bad days” framing is incomplete without frequencies and dollar magnitudes. A few large gaps can dominate many small premium wins.

## Practical rule

Use daily 0DTE covered calls only when willing to hold underlying, mildly bullish rather than strongly bullish, and comfortable selling each day’s upside. Avoid when expecting breakout, major catalyst, or needing meaningful downside protection.

## One-line summary

0DTE covered calls monetize ordinary days faster, but leave nearly full stock downside and sell away large upside sooner.
