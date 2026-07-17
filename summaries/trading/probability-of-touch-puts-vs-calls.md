---
title: "I Wish I Knew About This Metric 30 Years Ago"
source: "https://www.youtube.com/watch?v=HPZ84ku6XUE"
video_id: "HPZ84ku6XUE"
speakers:
  - "Tom Sosnoff"
  - "Tony Battista"
duration: "4:31"
category: trading
---

# Probability of Touch: 10-Delta Puts vs Calls

[Video](https://www.youtube.com/watch?v=HPZ84ku6XUE)

## TL;DR

Tastylive tests whether the rule of thumb `probability of touch ≈ 2 × probability of expiring ITM` matched history for 45-DTE, 10-delta options.

Across SPY, QQQ, Apple, Amazon, and Microsoft over roughly 10 years:

- 10-delta options theoretically implied ~20% touch probability.
- Puts touched only ~9% of the time.
- Calls touched ~19%, close to theoretical 20%.
- After a strike was touched, put positions finished profitable roughly 21 percentage points more often than calls, attributed to equity-market rebounds.

This describes a strong bull-market sample. It does not prove short puts are free money or establish expected return.

## Metric

Probability of touch estimates chance underlying reaches option strike at any point before expiry.

A touch means position becomes challenged; it does not mean final loss. Underlying can touch strike, reverse, and option still expire OTM.

Common shortcut:

- 10-delta option → roughly 10% probability expiring ITM;
- probability of touching strike → roughly 20%.

The `2×` relationship is approximation under restrictive diffusion assumptions, not identity. Delta, terminal ITM probability, and barrier-hitting probability diverge with drift, skew, jumps, dividends, rates, stochastic volatility, and American exercise.

## Study setup

- Entry: 45 DTE.
- Strike: 10-delta puts and calls.
- Underlyings: `SPY`, `QQQ`, `AAPL`, `AMZN`, `MSFT`.
- Holding: expiration.
- Window: described as roughly 10 years.
- Outcomes: actual touch frequency and win rate after touch.

Reported results:

- Put touch rate: ~9% average versus ~20% theoretical.
- Call touch rate: ~19% average; SPY/QQQ reached roughly 25%.
- Post-touch put win rates: around 50–60% for most names, with Apple lower.
- Put post-touch win rate exceeded call post-touch win rate by ~21 percentage points.

## Why puts looked better

Sample contains sustained positive equity drift and quick rebounds after drawdowns:

- upside drift moved call strikes toward spot;
- downside strikes were often avoided;
- temporary put breaches frequently recovered before expiration.

This is regime evidence, not timeless option law. Different result likely during prolonged bear market, volatility regime change, or single-name collapse.

## Theory of edge

> Short-put sellers earn premium for supplying crash insurance and committing liquidity when other investors fear or are constrained from holding downside risk.

Positive equity drift and implied-volatility risk premium may improve long-run short-put expectancy. Market pays seller because payoff is negatively skewed: many small premiums, occasional large loss. Low touch frequency is compensation evidence only when premium exceeds tail loss and friction—not edge by itself.

## Critical limitations

- Only five large, successful US equity underlyings.
- Bull-market and survivor-selection bias.
- Exact dates, sample count, overlap treatment, data source, and touch definition not shown.
- Intraday high/low versus closing-price touch unspecified.
- No transaction costs, spreads, assignment, margin, or management rules.
- Win rate ignores loss magnitude and expected value.
- Naked short-call risk is asymmetric and potentially unlimited; comparing win rates alone is especially misleading.
- Holding challenged trades to expiry differs from common management practice.

## Trading implications

Use probability of touch for **position-management planning**, not return forecasting:

- A 20% theoretical touch rate means prepare for challenges more often than expiration probability suggests.
- Touch is not automatic stop or loss.
- Evaluate post-touch conditional distribution, not only final win rate.
- Stress gap risk, margin expansion, and loss size.
- Compare premium earned against expected tail loss.
- Re-estimate by asset, regime, tenor, delta, and skew.

## YK read

Useful metric, weak standalone strategy argument. Main finding is really: positive equity drift made historical 10-delta puts less frequently challenged than symmetric model shortcut predicted.

The edge is not “puts rarely touch.” Edge, if any, is **getting adequately paid to warehouse downside insurance risk**. Need expected value, drawdown, margin stress, and crash-year decomposition before trading it.
