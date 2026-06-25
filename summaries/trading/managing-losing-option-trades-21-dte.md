---
title: "We Studied 15 Years of Losing Trades, This is What We Found Out | Market Measures"
source: "https://www.youtube.com/watch?v=YtQ8DSBnkOk"
category: trading
summary_date: 2026-06-25
---

# We Studied 15 Years of Losing Trades, This is What We Found Out | Market Measures

Source: https://www.youtube.com/watch?v=YtQ8DSBnkOk

## TL;DR

Tastytrade studies 15 years of SPY naked-option trades and compares holding losers to expiration versus managing at **21 DTE**. Holding gives losers more chance to recover, especially far-OTM options, but managing early sharply reduces the frequency of large losses, frees capital, and avoids the emotional/portfolio damage of tail moves.

## Setup

- Underlying: **SPY**
- Period: **15 years**
- Structures: naked individual options, not spreads
- Deltas tested:
  - **50-delta** puts/calls
  - **30-delta** puts/calls
  - **20-delta** puts/calls
- Compared:
  - Holding through expiration
  - Managing at **21 DTE**
- Loss thresholds tested relative to initial credit:
  - **0.5x credit** loss
  - **1.0x credit** loss
  - **1.5x credit** loss
  - **2.0x credit** loss

Example: if you sell an option for **$1**, then:

- 0.5x loss means buying back around **$1.50**
- 1.0x loss means buying back around **$2.00**
- 2.0x loss means buying back around **$3.00**

## Key findings

### 1. Managing at 21 DTE reduces tail-loss frequency

For **50-delta options**:

- Holding to expiration:
  - ~**30%** chance of reaching 0.5x loss
  - ~**11%** chance of reaching 1x loss
  - ~**3.5%** chance of reaching the larger outlier-loss bucket
- Managing at 21 DTE:
  - ~**11%** chance of reaching 0.5x loss
  - ~**4.5–5%** chance of reaching 1x loss
  - ~**2%** chance of the outlier-loss bucket

Main point: early management materially reduces the number of ugly-loss events.

### 2. Holding gives losers more chance to recover

For 50-delta options, when losses occurred and the trade was held to expiration, recovery happened a meaningful amount of the time:

- Around **44%**, **34%**, **27%**, and **28%** recovery rates across the loss-threshold buckets discussed.

But if you manage at 21 DTE, you are basically conceding that losing trade and moving on. The trade itself has much less chance to recover because you have exited.

### 3. 30-delta options show the same tradeoff

For **30-delta options**:

- Holding to expiration created much higher chances of touching loss thresholds — roughly **45%**, **26%**, **15%**, **9%** across the buckets mentioned.
- Managing at 21 DTE reduced those probabilities to a fraction of that.
- But if you held the trade instead, far-OTM options had meaningful recovery rates — in some cases more than half.

Speaker’s conclusion: even though recovery odds look tempting, they still prefer managing early because it controls tail risk and capital usage.

### 4. 20-delta options are closest to their preferred style

For **20-delta options**, which they say is closer to what they typically sell:

- Holding to expiration had loss-threshold touch probabilities in the broad **40–50%** range depending on threshold.
- Managing at 21 DTE lowered the odds of trouble sharply.
- Example cited:
  - Around **13%** chance of reaching a 1x loss by 21 DTE
  - Around **4.5%** chance of reaching a 2x loss by 21 DTE

This is why they like the strategy: if managed early, the probability of getting into serious trouble is relatively low.

### 5. Recovery vs risk control is the actual decision

The tradeoff:

- Hold to expiration:
  - Higher chance of loser recovering
  - Higher chance of large loss and wider P/L swings
  - More capital tied up
  - More psychological difficulty when the trade moves far against you
- Manage at 21 DTE:
  - Lower chance of major loss
  - Lower chance of recovery on that specific trade
  - Frees buying power for new trades
  - Keeps portfolio volatility and emotional load lower

Their bias: manage at **21 DTE** despite lower recovery odds.

## Trading read-through

This is not a “right answer” study. It is a variance preference study.

Holding losers to expiration can be mathematically defensible because short options often mean-revert enough to recover. But the cost is fatter left-tail exposure, larger drawdown swings, and capital lock-up. Managing at 21 DTE sacrifices some recovery optionality in exchange for lower tail risk, faster capital recycling, and cleaner process.

Edge framing: for short premium, you are being paid to warehouse volatility and adverse moves. The question is not “can this recover?” but “is the remaining recovery optionality worth the extra tail risk, buying-power usage, and psychological load?” Tasty’s answer: usually no; take the 21-DTE exit and redeploy.

## Practical checklist

- Decide your management rule before entry; don’t invent it when the trade is bleeding.
- If using Tasty-style short premium, **21 DTE** management is a tail-risk control rule, not a profit-maximizing rule for every individual trade.
- Holding losers longer increases recovery odds, but also increases outlier-loss exposure.
- Track buying-power opportunity cost: capital stuck in a loser cannot be used in a fresh setup.
- For far-OTM short options, recovery can be common — but a few non-recoveries can dominate P/L.
- Choose based on portfolio-level risk tolerance, not just single-trade recovery statistics.

## One-line summary

Holding losing short options gives them more time to recover; managing at 21 DTE gives the portfolio less time to get wrecked.
