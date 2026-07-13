---
title: "Why 10% of Max Profit on 0DTE Is What I Aim For"
source: "https://www.youtube.com/watch?v=EJR7fKzPul8"
channel: "tastylive"
duration: "6:39"
summary_date: "2026-07-11"
---

# Why 10% of Max Profit on 0DTE Is What I Aim For

## TL;DR

Tastylive tests same-day iron flies and finds that taking only **10–15% of the initial credit** often produces similar average P&L with materially higher win rates than waiting for large profits. Their practical recommendation is to enter shortly after the open, take a small gain quickly, and avoid holding the position while 0DTE gamma risk intensifies.

The result is not free money. Wider wings increase credit and win rate but also make the trade resemble an undefined-risk short straddle. One large loss can overwhelm many small 10% winners.

## Strategy

A short iron fly consists of:

1. Selling an at-the-money call.
2. Selling an at-the-money put.
3. Buying an OTM call wing.
4. Buying an OTM put wing.

It is a defined-risk short straddle:

- positive theta
- short volatility
- negative gamma
- maximum profit if the underlying expires near the short strike
- maximum loss limited by wing width minus credit

## Study design

- More than two years of 0DTE data
- Entry at **9:00 a.m. Chicago time**
- Wing widths from **$10 to $60**
- Profit targets from **10% to 75% of maximum profit**
- Backtest assumes execution at the option-chain midpoint

The midpoint assumption is important: live 0DTE multi-leg execution can be materially worse after bid/ask spread, latency and commissions.

## Main findings

The presenters highlight:

- $10 wings: approximately **70% winning trades** at the aggressive target.
- $20 wings: approximately **78% win rate** at 10%; waiting for larger gains reportedly reduced the hit rate substantially without meaningfully improving average P&L.
- $30 wings: approximately **83% win rate** at 10%.
- $60 wings: approximately **90% win rate** at 10%, but the position increasingly resembles a short straddle.

Across many wing widths, waiting for 30–75% of maximum profit did not add enough average P&L to compensate for the lower win rate and additional intraday exposure.

Their preferred implementation is therefore:

- target **10%**, maximum around **15%**
- close immediately when reached
- do not turn a quick morning trade into an all-day gamma bet

## Why a small target can work

Soon after entry, the trade can benefit from:

- rapid same-day time decay
- normalization of opening implied volatility
- the underlying remaining temporarily near the short strike

Waiting longer exposes the iron fly to rapidly increasing gamma. A small directional move can then overwhelm the remaining theta.

The small target is therefore less a return-maximization rule than a **risk-duration rule**: harvest the easiest portion of decay and stop warehousing intraday convexity.

## Example

Suppose a $20-wide iron fly collects **$5.00**:

- 10% target = **$0.50**, or **$50 per contract** before costs.
- Exit debit = **$4.50**.
- Maximum loss = `(20 − 5) × 100` = **$1,500**.

The target earns only **3.3% of maximum loss**. Many successful trades are therefore needed to offset a full loss.

## Theory of edge

> Earn opening volatility and intraday variance-risk premium by supplying liquidity and insurance, then exit before late-session gamma dominates the remaining theta.

The market pays this premium because the seller accepts path, gap and short-gamma risk during a highly compressed expiry window.

## Important caveats

- **Win rate is not expectancy.** A 90% win rate can still lose money if the remaining 10% contains sufficiently large losses.
- **Wider wings are not automatically safer.** They increase credit and win rate but also increase capital at risk and tail exposure.
- **Mid-price fills are optimistic.** Four-leg 0DTE spreads can suffer meaningful slippage.
- **Two years is a limited regime sample.** Results may depend on volatility, trend and event mix.
- **No risk-adjusted comparison is shown.** Similar dollar P&L across wing widths does not imply similar return on capital or drawdown.
- **Opening execution is competitive.** The apparent edge may decay after realistic latency, commissions and adverse selection.
- **Intraday monitoring is mandatory.** This is not a passive income position.

## Practical rule

If using the setup:

- trade only highly liquid underlyings
- use limit orders and record actual slippage
- size against maximum loss, not target profit
- avoid major scheduled events unless explicitly included in the model
- automate the 10–15% exit
- define a loss/time exit before entry
- test tail loss, drawdown and return on buying power, not only win rate

## One-line summary

A 10% target works by reducing time exposed to 0DTE gamma, not by improving the trade's payoff asymmetry; it converts the strategy into many tiny wins financed by occasional much larger losses.
