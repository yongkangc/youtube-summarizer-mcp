# It Took Us 15,000 Trades To Find Our Preferred Delta

Source: https://www.youtube.com/watch?v=-2TM3Jaz9dQ

## TL;DR

Tastytrade’s study looks at probability of touch for SPY short options across common out-of-the-money deltas. The headline: theoretical probability of touch is roughly **2x delta**, but realized touch rates are much lower when positions are entered around **45 DTE** and managed/closed at **21 DTE**. This supports their preferred zone around **15–25 delta** and their recurring rule: manage early.

## Core mechanics

- **Probability of touch** = chance the underlying touches the strike at any point before expiration.
- Back-of-envelope theory: **probability of touch ≈ 2 × delta**.
  - A 20 delta option theoretically has about **40%** probability of touch.
- They compare this theory with realized outcomes for SPY puts/calls.
- Trades were:
  - Out-of-the-money puts and calls
  - Delta range: **10 to 45 delta**
  - Initiated around **45 DTE**
  - Managed/closed at **21 DTE**

## 20 delta example

For 20 delta options:

- Theoretical touch probability: **~40%** for both puts and calls.
- In the last 10 years / bull-market sample:
  - Puts touched only around **20%** if held toward expiration.
  - Calls touched closer to **40%**.
- If managed at 21 DTE:
  - Puts touched only around **10%–11%**.
  - Calls touched around **14%**.

Their point: early management massively reduces how often short strikes get tested.

## Put side findings

- Across deltas, actual probability of touch was below the theoretical **2x delta** rule.
- Closing at **21 DTE** reduced touch rates sharply across all deltas.
- The study is most useful for true OTM options, especially **10–25 delta**.
- Higher-delta options naturally get touched more often; the gap between theoretical and realized narrows as delta rises.
- They explicitly say the 40–45 delta area is less relevant because those are too close to ATM and will be touched often.

## Call side findings

- Calls touched more often than puts in the sample, likely because the period was a bull market.
- But even on calls, managing at 21 DTE kept realized touch probabilities much lower than the theoretical estimate.
- Mentioned call-side 21 DTE touch rates:
  - 10 delta: about **3%**
  - 15 delta: about **7%**
  - 20 delta: about **14%**
  - 25 delta: about **24%**

## Practical takeaway

Their preferred short-option delta range is basically **15–25 delta**, not because there is magic edge in the exact delta, but because this zone balances:

- enough premium to matter
- lower probability of touch
- manageable testing risk
- strong benefit from closing early at 21 DTE

They say it “didn’t really matter” which delta within the reasonable OTM zone was used; what mattered more was avoiding too-high deltas and managing early.

## Trading interpretation

This is a mechanics edge, not a free-money edge. The market pays option sellers for taking tail/path risk. The process edge is:

- sell OTM options where realized touch rates are lower than naive theory suggests
- avoid selling too close to ATM
- manage at 21 DTE instead of waiting for expiration
- reduce the number of times positions get tested
- smooth the P&L curve by taking risk off early

## YK notes

For actual trade design:

- **15–25 delta** is the clean default zone for short premium.
- **20 delta** is a reasonable center point.
- Calls may be touched more often in bull regimes, so call-side shorts need more respect.
- Early management is doing real work; the edge deteriorates if you hold to expiration.
- This applies better to 45 DTE short-premium trades than to 0DTE gamma trades.

## One-line summary

For 45 DTE short options, **15–25 delta + close around 21 DTE** keeps realized touch risk far below the simple **2×delta** rule and helps flatten P&L.
