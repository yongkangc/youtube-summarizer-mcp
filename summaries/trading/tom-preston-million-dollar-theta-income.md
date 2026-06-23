# Tom Preston Shows How He Would Generate Income on a Million Dollar Account Using Only Theta

Source: https://www.youtube.com/watch?v=nu4wogE2MqI

## TL;DR

Tom Preston lays out a theta-income framework for a $1M account: target about $1,500/day of positive theta by selling high-probability out-of-the-money premium across large, liquid underlyings. The edge/theory is short-vol/liquidity provision: you are paid to warehouse option convexity/tail risk and collect extrinsic decay, not to predict direction.

## Core idea

- Don’t try to pick tops/bottoms or guess direction.
- Build a diversified book of short premium positions.
- Sell out-of-the-money calls and puts, usually around roughly 70% probability of expiring worthless.
- Use high-priced, liquid underlyings because their options have larger dollar extrinsic value and thus larger dollar theta.
- Maintain a target daily theta number, then manage/roll/replace positions as needed.

## Example structures mentioned

- SPX: short iron condor / defined-risk version of a short strangle.
  - He sketches a 0DTE / 1DTE-type trade.
  - Example credit around $11.
  - Theta shown around $453.
  - Buying power around $1,300.

- META: 39 DTE short strangle.
  - 39 DTE chosen as a balance between credit and theta decay.
  - Example: sell 520 put and 620 call.
  - Theta around $70.
  - Capital requirement around $6,900–$7,000.

- MU / Micron: high IV, high-priced stock, short strangle.
  - Example around 70% probability options.
  - Theta around $320.
  - Capital requirement around $11k–$12k.
  - Delta around -5.7 shares, i.e. mostly non-directional.

- Crude oil futures options: short strangle.
  - Example 24 DTE.
  - Theta around $130.
  - Capital requirement around $9,500.
  - Very low delta; framing is premium collection, not oil direction.

- He also references LLY and a total grid of around eight symbols, one or two contracts each, targeting balanced capital usage.

## Portfolio math

- Target: $1,500/day theta.
- Trading days assumption: 250/year.
- Gross theta generated: $1,500 × 250 = $375,000/year, or 37.5% of a $1M account.
- He says you won’t keep all of it because of bad days/weeks/quarters and losing trades.
- There is a transcript/math inconsistency:
  - If you give back 60%, you keep $150,000, or 15%.
  - If you give back 40%, you keep $225,000, or 22.5%.
  - Later he frames 60% of the theta as retained, which maps to about $225,000 and a ~20%+ return.

## Risk framing

- The sample book uses around $86k–$90k of buying power/capital requirement against a $1M account.
- He explicitly says this is not max risk; it is a rough risk/capital metric.
- Hidden risk is tail/convexity risk: large underlying moves, vol expansion, gap risk, assignment/margin stress, and correlated losses across symbols.
- The strategy is not “free income.” Higher return requires taking more risk.

## Management caveat

He does not cover management rules in this video. He explicitly punts on:

- when to close, e.g. 50% profit
- when/how to roll
- when to adjust existing positions
- when to add new symbols
- how to handle losers

That is the important missing piece. Generating theta is easy; surviving the left-tail and managing breached strangles is the real strategy.

## Practical checklist

- Pick liquid, high-priced underlyings or use more smaller symbols.
- Sell OTM calls and puts with high probability of expiring worthless.
- Use defined-risk iron condors where naked strangles consume too much capital or tail risk is too large.
- Track total daily theta against a target.
- Keep buying power usage small relative to the full account.
- Review daily: theta target, breached sides, rolling needs, new opportunities.
- Don’t scale beyond risk comfort.

## My read

Good as a conceptual income-generation framework, but incomplete as a tradable process. The real edge is being structurally short volatility and providing liquidity across diversified underlyings; the real danger is pretending daily theta is income before marking tail risk, margin expansion, and bad-path management.

## One-line summary

Preston’s plan is a diversified short-premium book targeting ~$1,500/day theta on $1M, but the actual trade is selling convexity/tail risk—not harvesting risk-free yield.
