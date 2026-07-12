---
title: "Exact Moment to Roll a Credit Spread"
source: "https://www.youtube.com/watch?v=79_jXMpx_qg"
video_id: "79_jXMpx_qg"
channel: "tastylive"
speaker: "Mike Butler"
duration: "7:37"
date_summarized: "2026-07-11"
category: "trading"
---

# Exact Moment to Roll a Credit Spread

## TL;DR

If plan is to defend a credit spread by rolling out for flat price or credit, roll **before spread moves in the money**, meaning before underlying crosses short strike. Once spread is ITM, long option can hold more extrinsic value than short option, making same-width time roll likely require a debit.

This is not universal rule to always roll. It applies only when trade plan already calls for defense and available roll preserves acceptable risk/reward.

## Theory of edge

Credit spread earns compensation for selling implied volatility and accepting directional/tail risk. Long wing caps loss but also offsets much of short option's Greeks. Edge requires implied premium exceeding realized loss, slippage and adverse-selection costs over many trades.

## Vertical spreads can be nearly binary

Long and short legs carry opposite Greeks. When strikes sit close together relative to underlying price:

- deltas are similar;
- theta largely offsets;
- vega largely offsets;
- position moves slowly until underlying approaches/crosses strikes;
- terminal payoff dominates mark-to-market Greek behavior.

Example shown:

- `SPX` around `$7,200–$7,500`;
- 10-point vertical;
- sell around `$1.50`;
- risk around `$8.50` or `$850` per spread;
- about 50 DTE.

Without large move, trader may wait 20–30 days to capture only about `$0.75`. Narrow spread behaves mainly as binary “inside/outside strike at expiry” bet.

## Relative width matters—not nominal width

Five-point spread means different risk on different products:

- 5 points in `$7,500 SPX`: extremely narrow; little net Greek exposure.
- 5 points in `$25 DKNG`: 20% of stock price; much larger delta gap and Greek exposure.

Useful diagnostic: compare short-leg and long-leg delta.

`DKNG` example:

- short put around 37 delta;
- long put around 1 delta;
- wide 36-delta gap means meaningful directional exposure.

Spread width should be judged against underlying price and delta separation, not points alone.

## Optimize width against protection cost

Check whole option chain before accepting default wing.

`DKNG` example:

- 5-point-wide spread credits about `$0.68`;
- 2.5-point-wide spread credits about `$0.60`;
- giving up only `$0.08` premium cuts defined-risk width roughly 50%;
- approximate max risk falls from `$4.32` to `$1.90` before fees.

If far OTM protective wing costs only `$0.05–$0.10`, buy closer wing. Small premium sacrifice may remove hundreds of dollars of max loss.

Mirror logic for debit spreads: if short option reduces cost by only `$0.10–$0.20` but heavily caps upside, use different structure such as long option/ZEBRA rather than poor-value cap.

## Why roll before spread becomes ITM

While credit spread remains OTM:

- short option generally carries more extrinsic value than long wing;
- buying back near expiry and selling later-dated spread may produce credit or near-scratch.

After spread moves ITM:

- long wing may carry more extrinsic value than short option;
- short option has more total value mainly because of intrinsic value;
- closing both legs means paying to repurchase relatively rich long-wing extrinsic;
- rolling same structure outward likely requires debit.

Debit roll:

- reduces total max profit;
- increases cumulative max loss/capital committed;
- still requires favorable directional reversal.

Therefore, if defense is mandatory, trigger is **underlying approaching short strike / before short strike breach**, even at 40, 30 or 25 DTE. Fixed 21-DTE rule is secondary to moneyness for this specific roll objective.

## Gamma nuance

Generic tastytrade management often rolls near 21 DTE to avoid accelerating gamma. Mike argues narrow verticals have little net gamma because legs offset. Their bigger problem is losing ability to roll for credit after ITM transition.

Wider relative spreads retain more delta/gamma/theta/vega and behave more like naked short option with distant disaster hedge.

## Operator checklist

Before entry:

1. Define whether position will be defended or allowed to settle at max loss.
2. Compare width as percentage of underlying price.
3. Check delta gap between legs.
4. Compare credits across closer protective wings.
5. Calculate premium surrendered per dollar of max loss removed.
6. Confirm liquidity and slippage on all four roll legs.

During trade:

1. Monitor underlying distance to short strike.
2. Inspect intrinsic/extrinsic value by leg.
3. Price full roll, not isolated legs.
4. If roll for credit is plan, act before short strike breach.
5. Reject debit rolls unless revised thesis independently justifies added risk.

## Caveats

- Crossing short strike does not mechanically mean position should be rolled. Expected value may favor holding, closing, accepting loss or changing structure.
- “Before ITM” is path-dependent; overnight gaps can skip trigger.
- Roll credit is not profit. It extends duration and risk.
- Four-leg roll can carry meaningful bid/ask cost.
- American-style equity options add early-assignment risk, especially around dividends.
- SPX is European-style and cash-settled; mechanics differ from equity/ETF options.
- Max-loss reduction comparison must include changed credit, fees and fill quality.

## Bottom line

For defendable credit spreads, roll trigger is not automatically 21 DTE. It is loss of favorable extrinsic-value relationship as underlying approaches short strike. Roll before spread becomes ITM—or accept that later roll may require paying debit for same directional bet.