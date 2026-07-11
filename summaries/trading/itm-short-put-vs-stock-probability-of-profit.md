---
title: "Why an In-the-Money Short Put Can Have Higher POP Than Stock"
source: "https://www.youtube.com/watch?v=KsIOYxkn9yU"
channel: "Calculated Risk"
duration: "11:06"
summary_date: "2026-07-11"
---

# Why an In-the-Money Short Put Can Have Higher POP Than Stock

## TL;DR

Jim Schultz argues that even an in-the-money short put can have a probability of profit above 50%, because the seller receives extrinsic value and the breakeven is therefore below the current stock price. That is mechanically correct, but the title overstates the conclusion: a higher probability of *some* profit does not mean a short put has a higher expected return than stock. The seller exchanges unlimited upside for premium and retains nearly all downside risk.

## Core mechanics

At expiration, a short put's P&L is:

`premium received − max(strike − terminal stock price, 0)`

Its breakeven is:

`strike − premium received`

An in-the-money put premium contains:

- **Intrinsic value:** `strike − current stock price`
- **Extrinsic value:** time value / volatility premium

Because the seller receives both components, the breakeven lands below the current stock price by approximately the extrinsic value. The stock can remain flat or decline slightly and the short put can still make money.

## Illustrative example

Using the video's SPY setup, suppose:

- SPY = **711**
- Short-put strike = **735**
- Hypothetical premium = **28**
- Intrinsic value = **24**
- Extrinsic value = **4**
- Breakeven = **707**

At expiration:

- SPY **650**: short put loses **57**; stock loses **61**.
- SPY **707**: short put breaks even; stock loses **4**.
- SPY **711**: short put gains **4**; stock is flat.
- SPY **735**: short put reaches max profit of **28**; stock gains **24**.
- SPY **760**: short put remains capped at **28**; stock gains **49**.

The exact premium in the live chain will differ; these numbers illustrate the payoff mechanics.

## Equivalent position

A cash-secured short put is economically equivalent, through put-call parity, to:

> long stock + short call at the same strike

That is why a deep in-the-money short put behaves much like stock below the strike but stops participating once the stock rises above the strike. It is effectively a covered-call payoff expressed through a put.

## What “higher probability of profit” really means

It means the short put has a lower breakeven than buying stock today. It does **not** mean free alpha.

The trade-off is:

- higher probability of a small/moderate profit
- capped maximum profit
- substantial downside exposure
- short-volatility / negative-convexity risk
- assignment and capital requirements

The option premium is compensation for warehousing downside and volatility risk. Under no-arbitrage assumptions, the short put does not dominate stock; the payoff distribution is reshaped.

## Important correction to the video

The statement that “every short-put strategy beats stock ownership” is misleading. The video demonstrates higher platform-estimated POP, not superior expected return, risk-adjusted return, or terminal wealth.

A short put outperforms stock when the underlying is flat, modestly down, or rises only up to the strike. Stock wins in a sufficiently strong rally. Both suffer in a major decline, with the short put only cushioned by the premium.

## Edge and risk

**Theory of edge:** systematic option selling may earn compensation for supplying liquidity and warehousing volatility/crash risk when implied volatility exceeds subsequently realized volatility.

**Hidden risk:** the strategy wins frequently and then suffers large losses during sharp declines. High win rate is partly the statistical signature of selling insurance, not proof of superior forecasting.

## Practical rule

Use an in-the-money short put when you are bullish but willingly cap upside in exchange for a lower breakeven and upfront premium. Do not choose it merely because the POP displayed by the broker exceeds 50%.

## One-line summary

An ITM short put has higher POP because extrinsic value pushes breakeven below spot, but that advantage is purchased by selling away upside while retaining most downside risk.
