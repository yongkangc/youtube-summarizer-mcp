---
title: "Bad Bloom Energy 1x2 Put Ratio Spread"
source: "https://www.youtube.com/watch?v=XUkwGEJyVmk"
video_id: "XUkwGEJyVmk"
duration: "4:15"
date_summarized: "2026-07-13"
category: "trading"
---

# Bad Bloom Energy 1x2 Put Ratio Spread

## TLDR

Speaker deliberately enters a poor-quality Bloom Energy (`BE`) 1×2 put ratio spread to illustrate what not to do: illiquid stock/options, wide spreads, weak fill and extreme implied volatility. Structure earns a small credit across most outcomes but hides naked downside below the lower strike.

## Setup

At approximately `BE $280`, 43 DTE:

- Buy 1 July `$165` put
- Sell 2 July `$150` puts
- Net credit: `$1.50` = `$150`
- Initial delta: approximately `+3`
- IV rank: `72`
- Monthly IV: approximately `120%+`
- Long put only around `6–8 delta`, versus speaker's usual approximately `20 delta`

Speaker calls it “omnidirectional,” but economically it is a bullish put ratio spread: one defined-risk bear-put spread plus one naked short `$150` put.

## Payoff at expiry

- `BE ≥ $165`: keep `$150` credit
- `BE = $150`: maximum profit **$1,650**
- `$133.50 < BE < $150`: still profitable, but profit falls as stock declines
- Lower breakeven: **$133.50**
- `BE < $133.50`: losses grow dollar-for-dollar
- `BE = $0`: loss **$13,350**

The displayed `95% probability of profit` does not make trade safe. It describes frequent small-profit outcomes while ignoring severity of rare left-tail loss.

## Why speaker says trade is bad

- Stock volume under 3M shares two hours into session.
- Option bid-ask spreads wide.
- Filled at `$1.50` credit while displayed midpoint approached `$1.70`.
- Entry slippage matters because trader controls entry, not future price.
- `120%+` IV signals enormous expected movement; speaker describes stock as capable of doubling or approaching zero over a year.
- Position's extra short put creates large downside obligation exactly when liquidity may worsen.

## Theory of edge

Potential edge is selling extremely expensive downside volatility and earning liquidity/convexity premium. But trade execution undermines it: poor liquidity transfers edge to market maker through spread, while tiny credit inadequately compensates for naked crash exposure.

## Better process

- Skip illiquid underlyings/options.
- Require tight bid-ask spread and meaningful stock/options volume.
- Price tail loss before looking at probability of profit.
- Use defined-risk 1×1 spread if unwilling to own shares below effective breakeven.
- Compare ratio spread against simply selling one `$150` put; added long put reshapes payoff but does not remove naked downside.
- Size from worst plausible gap, not attractive max-profit peak at `$150`.

## Bottom line

High win probability plus tiny entry credit can hide ugly negative skew. Here trader receives `$150` unless stock falls hard, can earn `$1,650` only near a precise pin, and risks up to `$13,350` at zero—inside an illiquid product with `120%+` IV.