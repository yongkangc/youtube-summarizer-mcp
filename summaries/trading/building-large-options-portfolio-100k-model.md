---
title: "Building a Large Options Portfolio: $100k Model"
source: "https://www.youtube.com/watch?v=whDUysN2XYc"
channel: "tastylive"
duration: "16:42"
summary_date: "2026-07-11"
---

# Building a Large Options Portfolio: $100k Model

## TL;DR

Tastylive builds a diversified, mostly undefined-risk short-premium portfolio for a **$100k account**, using **$50k buying power**, multiple liquid ETFs/futures, and options near **45 DTE**. The core idea is to spread small bullish, bearish, and neutral views across weakly correlated products rather than make one large market bet.

## Model portfolio

Market views used for illustration:

- bullish S&P 500
- bearish Nasdaq
- neutral Russell 2000
- bullish China equities
- bearish US dollar
- bearish crude oil / energy
- bullish digital assets

Products included `SPY`, `QQQ`, `IWM`, `FXI`, euro futures, `XOP`, and `BITO`.

They avoided crude-oil futures because one contract required roughly **$14k buying power**, too large for balanced sizing in a $100k account. `XOP` was used instead.

## Construction rules

- Account: **$100k**
- Buying-power usage: **50% / $50k**
- Entry duration: closest cycle to **45 DTE**
- Use liquid ETFs and futures rather than concentrating in single stocks
- Keep buying-power allocation roughly similar across positions
- Use **3–5 strategy types**; example uses:
  - short put
  - short call
  - short strangle
  - covered call
- Example has no meaningful defined-risk positions, although defined risk can be substituted

Important: buying-power reduction is **not maximum risk**. Undefined-risk short options can lose materially more than the displayed BPR.

## Portfolio Greeks

- Premium collected: approximately **$7,000**
- Initial theta: about **$189/day**, or **0.189% of account equity per day**
- Raw position deltas: about **290**
- SPY beta-weighted delta: **+113**
- At SPY near **$417**, equivalent directional exposure was approximately **$47k long SPY notional**
- Estimated cross-product portfolio correlation: **0.30**

The beta-weighting step is important: raw deltas from different products are not directly comparable. Converting them to SPY-equivalent deltas shows the portfolio's actual aggregate market bias.

## Their P&L expectations

With approximately +113 SPY beta-weighted deltas:

- Estimated daily directional move: about **±$465**
- One volatility-point move: about **±$200** from vega
- If SPY rises about **2%** in a month, directional gain could be roughly **$900–$1,000**
- If volatility also falls 1–2 points, another **$200–$400** could be gained
- Combined favorable directional/volatility contribution: roughly **1%–1.4%** of account equity

For theta, they assume keeping about **25% of collected premium** over the month:

- 25% × $7,000 = **$1,750**
- Equivalent to **1.75%** of the $100k account
- In a favorable price + volatility month, they suggest total return might reach roughly **3.25%**

These are scenario estimates, not reliable monthly yields. Direction, volatility expansion, correlation spikes, slippage, assignment, and tail losses can overwhelm theta.

## Product indifference

Their research claim is that the same short-premium structure produces broadly similar success rates across liquid products:

- IWM 16-delta strangle: about **80%**
- SPY 16-delta strangle: about **73%**
- FXI 16-delta strangle: about **74%**
- FXI iron condor: about **80%**
- XOP iron condor: about **74%**
- SPY iron condor: about **74%**

Their conclusion: strategy mechanics and portfolio construction matter more than finding one magical ticker.

## Edge and hidden risk

**Theory of edge:** earn the volatility risk premium by selling options across liquid, weakly correlated underlyings while diversifying directional views and retaining unused capital.

**Risk being warehoused:** short-volatility, gap, correlation, liquidity, and convexity risk. During a crisis, apparently diverse positions can become one trade: equities fall, volatility rises, correlations converge toward one, and buying-power requirements expand simultaneously.

The portfolio's **0.30 historical correlation** and **$50k BPR** can therefore give false comfort. Neither is a hard loss limit.

## Practical interpretation

Useful lessons:

- Allocate by risk/BPR rather than contract count.
- Reject products whose smallest contract is too large.
- Beta-weight the whole portfolio before calling it diversified.
- Mix bullish, bearish, and neutral exposures.
- Keep substantial free buying power.
- Diversify across genuinely different economic drivers.

What not to copy blindly:

- Treating 25% of premium as a dependable monthly return.
- Equating 50% BPR with 50% maximum risk.
- Assuming low normal-period correlations persist during stress.
- Scaling every position linearly when account size doubles.

## One-line summary

Build a short-premium portfolio from many small, liquid, differently directed trades, but judge diversification under stress because buying power and historical correlation understate undefined tail risk.
