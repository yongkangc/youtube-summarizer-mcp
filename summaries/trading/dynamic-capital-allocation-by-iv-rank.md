---
title: "Dynamic Capital Allocation by IV Rank"
source: "https://www.youtube.com/watch?v=sko-HlCcxQk"
video_id: "sko-HlCcxQk"
duration: "14:23"
date_summarized: "2026-07-15"
category: "trading"
---

# Dynamic Capital Allocation by IV Rank

## TLDR

Sixteen-year short-strangle backtest found dynamic exposure produced profits closer to constant 50% allocation while keeping worst-tail CVaR closer to constant 25% allocation. Rule: maintain 25% allocated capital when IV rank is below 15, scale linearly, and reach 50% above IVR 30. Win rate barely changed; sizing altered dollars earned and lost, not trade-level accuracy.

## Backtest design

- Sample: 16 years.
- Strategy: sell symmetric `30Δ`, `20Δ`, `16Δ`, or `10Δ` strangles.
- Entry: 45 DTE.
- Management: close/manage at 21 DTE.
- Results normalized per `$10,000` initial capital.
- Compared:
  - constant 25% capital allocation;
  - dynamic 25–50% allocation based on IVR;
  - constant 50% allocation.
- Dynamic rule:
  - IVR below 15: 25% allocated;
  - IVR above 30: 50% allocated;
  - linear interpolation between thresholds.
- CVaR: average loss/risk in worst 5% of observations, as described in episode.

## Results

### 30-delta strangle

- Constant 25%: `$2.19/day`, `71%` wins, `$678` CVaR.
- Dynamic: `$3.52/day`, `72%` wins, `$762` CVaR.
- Constant 50%: `$4.38/day`, `71%` wins, `$996` CVaR.

### 20-delta strangle

- Constant 25%: `$1.96/day`, `78%` wins, `$598` CVaR.
- Dynamic: `$3.11/day`, `77%` wins, `$712` CVaR.
- Constant 50%: `$3.93/day`, `78%` wins, `$1,197` CVaR.

### 16-delta strangle

- Constant 25%: `$1.80/day`, `79%` wins, `$539` CVaR.
- Dynamic: `$2.92/day`, `78%` wins, `$672` CVaR.
- Constant 50%: `$3.61/day`, `79%` wins, `$1,079` CVaR.

### 10-delta strangle

- Constant 25%: `$1.42/day`, `82%` wins, `$407` CVaR.
- Dynamic: `$2.41/day`, `82%` wins, `$515` CVaR.
- Constant 50%: `$2.84/day`, `82%` wins, `$815` CVaR.

## Interpretation

- Constant 50% roughly doubles average P&L versus 25%, but tail risk rises substantially.
- Dynamic allocation captures much of higher-allocation profit without carrying maximum exposure continuously.
- Win rates remain nearly identical across sizing methods because position size does not change whether underlying stays inside strikes.
- Lower-delta strangles win more often and earn less per day; this says nothing by itself about risk-adjusted expectancy.
- Keeping reserve capital during low-IV periods preserves capacity for high-IV opportunities.

## Theory of edge

**Structural edge:** Option sellers receive variance/insurance premium for warehousing gap, convexity and liquidity risk. Dynamic allocation assumes compensation per unit of capital is better when IVR is elevated, so capital should be concentrated when option prices are richer.

Market pays more in high IV because actual risk is also higher. IVR is not free alpha; dynamic sizing works only if implied volatility rises more than subsequent realized/tail loss.

## Caveats

- IVR thresholds `15/30` and allocation `25/50%` were explicitly arbitrary.
- Episode does not identify underlying universe, exact dates, commissions, slippage, margin model, overlapping-position treatment or liquidation constraints.
- No out-of-sample validation or statistical significance shown.
- Average P&L/day and win rate can hide maximum drawdown, recovery time, skew and margin expansion.
- CVaR estimated from historical worst 5% may understate unseen crash regimes.
- Scaling up during high IV mechanically increases exposure during crises, when correlations and margin requirements also rise.
- A 50% short-strangle allocation can be dangerously aggressive in a correlated live portfolio even if backtest's standalone CVaR looks tolerable.

## Practical rule

- Keep more dry powder when IVR is low.
- Increase exposure gradually as IVR rises; do not jump from low to full size.
- Cap portfolio risk using stress loss and peak margin, not entry buying power.
- Scale aggregate correlated exposure, not every position independently.
- Require volatility premium after costs; IVR alone does not establish edge.

## Bottom line

Dynamic sizing beats always-small or always-large allocation in this backtest: risk capital should vary with opportunity quality. Useful principle; exact 25–50% schedule is not universally safe or proven.