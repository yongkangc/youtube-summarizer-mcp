---
title: "Eric Jablonski Coded a Futures Trading Bot With AI"
source: "https://www.youtube.com/watch?v=kK-sBFJuwMw"
video_id: "kK-sBFJuwMw"
channel: "tastylive"
duration: "7:39"
date_summarized: "2026-07-11"
category: "trading"
---

# AI-Coded Opening-Range Breakout Futures Bot

## TL;DR

Eric used Claude Code to implement a simple opening-range breakout bot for `ES` and `NQ`: TradingView creates alerts, TradersPost routes them to broker execution. Bot had only **~1.5 months live history**, no stressed-regime evidence and no performance statistics.

## Mechanics

- Products: S&P 500 and Nasdaq futures (`ES`, `NQ`).
- Signal: mark first **30-minute opening range**.
- Break above range: buy.
- Break below range: short.
- Code generation: Claude Code.
- Signal engine: TradingView.
- Automation bridge: TradersPost.
- Execution: broker API through TradersPost.

Eric trades separately by hand using hourly levels and multi-timeframe analysis. Bot trades opening hour even though he personally avoids it.

## AI’s actual role

AI did not discover edge. It translated a human-specified rule into code and integration logic. Value: faster prototyping, easier API implementation and automation.

## Theory of edge required

Opening-range breakout can work if early order flow reveals persistent intraday information/trend and payoff from occasional large trends exceeds repeated false-break losses.

Video provides no evidence this condition holds after fees/slippage. Eric explicitly says he would be surprised if such a simple strategy stayed profitable forever.

## Missing evidence

- Entry/exit and stop rules.
- Position sizing and max daily loss.
- Overnight versus intraday holding.
- Contract choice (`ES` vs micro contracts).
- Backtest period and out-of-sample split.
- Net returns after commissions/slippage.
- Drawdown, hit rate, average win/loss and profit factor.
- Behavior in 5–10% selloffs or volatility spikes.
- Alert duplication, outage and broker-reconciliation controls.

## Required validation

1. Define full deterministic rules.
2. Backtest across low/high-volatility, trend and mean-reversion regimes.
3. Use realistic spread, commissions and stop slippage.
4. Walk-forward/out-of-sample test.
5. Paper trade, then micro contracts.
6. Add daily loss cap, position cap, duplicate-order guard and kill switch.
7. Reconcile TradingView alerts against broker fills.

## One-line summary

Claude made bot construction easy; whether opening-range breakout has durable edge remains completely unproven.