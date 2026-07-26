---
title: "Bigger Option Credits Aren't Always Better: The DTE Trap"
source: "https://www.youtube.com/watch?v=rrBFHgIBNkw"
video_id: "rrBFHgIBNkw"
channel: "tastylive"
speaker: "Jim Schultz"
duration: "8:02"
episode_date: "2026-07-25"
date_summarized: "2026-07-25"
category: "trading"
---

# Bigger Option Credits Aren't Always Better

## TLDR

Longer-dated short options collect more dollars because they contain more extrinsic value, but that value usually decays more slowly per day. Shorter DTE accelerates theta but increases gamma/path risk. Schultz prefers roughly `45 DTE`, with `30–60 DTE` acceptable, as compromise among total credit, daily decay and directional risk.

## Mechanism

### Long DTE `[0:40]`

A `90 DTE` OTM option has more time for adverse movement, therefore more extrinsic value and larger headline credit than comparable `30 DTE` option.

But extrinsic value is spread across wider time window:

- larger total credit;
- lower daily theta;
- slower early decay;
- longer capital/risk exposure.

Big credit is not free edge. Seller warehouses risk for longer.

### Short DTE `[2:50]`

As expiration approaches:

- theta generally accelerates;
- gamma rises;
- delta changes faster after underlying moves;
- adjustment window shrinks.

Thus moving from `90` to `7 DTE` does not create free theta. It exchanges duration risk for stronger gamma and gap risk.

### Preferred zone `[3:10]`

Schultz's operational range:

- preferred entry: approximately `45 DTE`;
- acceptable: `30–60 DTE`;
- avoid `80–100+ DTE` for foundational short-premium trades because decay is too slow;
- avoid very short DTE because gamma dominates.

## Examples

On platform, he compares similar/same strikes across expirations:

- IWM: longer expiration shows larger credit but lower theta; shorter cycles show smaller credit and faster decay.
- MCD `255P`: long cycle around `34 delta` shows roughly `$7.30` credit and `$6.70/day` theta; nearer cycle roughly `$5.45` credit and `$8/day` theta. Shortest cycle shows lowest credit and highest theta.

Numbers are platform snapshot, not backtest or executable study.

## Theory of edge

> Short-vol seller earns volatility/liquidity risk premium by warehousing uncertainty. DTE choice should maximize compensation per unit of capital and risk—not headline premium.

Correct comparison should include:

- theta per day;
- theta per buying-power dollar;
- credit / defined max loss;
- IV versus forecast realized volatility;
- gamma and gap loss;
- vega exposure;
- expected holding period and turnover;
- slippage/fees;
- drawdown and tail expectancy.

## Audit / caveats

- Theta is model estimate assuming spot, IV and rates unchanged; real P&L rarely follows theta cleanly.
- Same strike across expirations is not same risk: delta, IV, vega, probability ITM and expected move differ.
- Absolute theta is not enough; normalize by margin/capital and tail loss.
- `45 DTE` is heuristic, not universal optimum. Earnings, macro events, skew, term structure and liquidity can dominate.
- Longer DTE provides lower gamma and more management time; video underweights these benefits.
- Shorter DTE may show faster theta but much worse tail-adjusted expectancy.
- No historical P&L, drawdown, fees or statistical test proves `30–60 DTE` superior.

## YK rule

Never choose expiration because credit looks bigger. Compare **theta/margin + IV/RV edge + gamma/tail risk**. If no structural volatility premium, DTE optimization cannot rescue trade.