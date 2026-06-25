# Tom Preston Shows How He Would Generate Income on a Million Dollar Account Using Only Theta

Source: https://www.youtube.com/watch?v=nu4wogE2MqI

## TL;DR

Tom Preston proposes a million-dollar short-premium portfolio built around daily theta, not stock picking or directional calls. The target is roughly **$1,500/day of positive theta**, accepting that a large portion will be given back through losers, adjustments, rolls, and volatility shocks.

## Strategy mechanics

- **Core idea:** generate returns by selling options with positive theta — collecting extrinsic value decay as time passes.

- **No directional thesis.** He explicitly avoids chart analysis, earnings calls, stock-picking, or predicting tops/bottoms. The strategy is built from high-probability short premium positions.

- **Preferred structures:**
  - SPX: short iron condor / defined-risk short strangle equivalent.
  - Large stocks: short strangles.
  - Futures like crude oil: short strangles.

- **Why high-priced underlyings:** higher-priced stocks/futures have higher dollar option premiums, hence more dollar theta. Not higher theta percentage necessarily, just bigger dollar decay per contract.

- **Example trades from transcript:**
  - SPX 0/1DTE-style iron condor: about **$11 credit**, around **$453 theta**, about **$1,300 buying power**.
  - META 39DTE short strangle: sell roughly **520 put / 620 call**, about **$70 theta**, around **$7,000 capital**.
  - MU high-IV short strangle: about **$320 theta**, around **$11–12k capital**, delta around **-5.7 shares**.
  - Crude oil short strangle: about **$130 theta**, around **$9,500 capital**, near-flat delta.

- **Portfolio construction:** use around **8 symbols**, mostly 1–2 contracts each, sized so most positions consume roughly **$10–12k** buying power. SPX is kept defined-risk because naked SPX strangles would require much more capital.

- **Target portfolio theta:** roughly **$1,500–1,600/day**.

- **Capital used:** example portfolio uses around **$86–87k** buying power on a **$1M** account. He stresses buying power is not max risk; it is only a risk/capital proxy.

## Math / return claim

- **Gross theta target:**
  - $1,500/day × 250 trading days = **$375,000/year** gross theta.

- **He assumes you do not keep all theta.** There will be bad days/weeks/quarters, losing strangles, and adjustments.

- **If you keep 60%:**
  - $375,000 × 60% = **$225,000**, or about **22.5%** on $1M.

- **If you give back 60% / keep 40%:**
  - $375,000 × 40% = **$150,000**, or **15%** on $1M.

- **Transcript inconsistency:** he says “give back 60%” and then quotes around **$225k**, which actually corresponds to keeping 60%, not giving back 60%. The broad point: he is underwriting a high-teens/20%ish return target, not claiming you keep all theta.

## Risk / caveats

- **This is short volatility / tail-risk warehousing.** The edge is not free yield. You are getting paid to sell convexity, provide liquidity, and absorb gap/volatility risk.

- **Buying power is not max loss.** Naked strangles can lose far more than displayed buying power in a shock. SPX iron condor is defined-risk; naked stock/futures strangles are not.

- **Theta is not P&L.** Theta is expected daily decay holding everything else equal. Delta moves, gamma, vega expansion, earnings, gaps, and correlation spikes can overwhelm theta quickly.

- **Needs active management.** He says you must check daily: is theta at target, do positions need adjustment/roll, do you need a new symbol, should winners be closed, etc.

- **Diversification can be fake in stress.** Eight symbols across equities/futures helps, but short premium books often become one correlated short-vol trade during market shocks.

- **Scaling down increases risk concentration.** He says the same concept can be tried on $500k or $200k, but that means risking more of the account to hit comparable income.

## YK trading read-through

- **Theory of edge:** short volatility / liquidity provision / convexity risk premium. Market pays you because you warehouse tail risk and provide option liquidity when others want protection or leverage.

- **Good part:** process-driven, delta-light, diversified short premium, explicit theta target, avoids pretending to forecast direction.

- **Dangerous part:** the video frames buying power gently. Real risk is not $86k; real risk is gap/vol expansion across a short-vol portfolio.

- **If adapting:** use hard portfolio limits: max notional short vega/gamma, per-underlying loss stop, event filters, defined-risk around earnings/binary events, correlation stress test, and explicit crash playbook.

- **For Scry/Fund framing:** this is a yield-like process only if risk controls are institutional. Otherwise it is “picking up nickels” with uncapped left-tail risk.

## One-line summary

Tom’s million-dollar theta plan targets **$1.5k/day gross theta** via diversified short premium, but the real trade is selling volatility and managing tail risk — theta income is the headline, convexity warehousing is the substance.
