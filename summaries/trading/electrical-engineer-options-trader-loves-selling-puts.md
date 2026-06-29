# Electrical Engineer and Options Trader Loves Selling Puts

Source: https://www.youtube.com/watch?v=EG3kKNZxkBQ

## TL;DR

Tastylive interview with David, an electrical engineer who became a systematic short-premium trader. Core lesson: put-selling can scale only if treated as repeatable risk warehousing, not “high win rate = safe.” His process improved after 2018 drawdowns forced smaller sizing, explicit stops/roll rules, and simpler strategies he could track.

## Key Points

- Background: David studied electrical engineering at UVA and Princeton, followed markets around 2008–2009, then got pulled into options through a friend who introduced him to put selling and Tastylive.
- Early hook: he was intrigued by Tom/Tony’s view that holding to expiration to squeeze last premium is not worth path/tail risk; Tastylive’s 21 DTE management rule became part of his framework.
- 2017 mistake: tried to adopt delta-neutral / short-delta structures like strangles and iron condors in a strong bull grind. Frustration pushed him toward long delta late in the year, which worked until volatility returned.
- Feb 2018 stress test: market fell roughly 10%, VIX hit about 50, and he took drawdown but survived via rolling and reduced leverage.
- Dec 2018 lesson: short-put-heavy book got hit during violent Thanksgiving-to-Christmas selloff. He learned mental adjustments were too loose; needed more rigorous risk controls and smaller sizing.
- Process evolution: simplified strategies so results became trackable. Fewer moving parts made it easier to know what worked, what failed, and why.
- 2019 setup: trading while working full-time, on a meaningful account size. He describes current process as scalable/repeatable: 2–3 “bread and butter” trades, including a 5-delta short put with stop and re-establish/roll logic.
- Backtest discipline: built his own SPX short-put backtest with ~400 occurrences, configurable by delta 5/10/20/30 and stop levels 0x/1x/2x/3x.
- Win-rate math: without stop, 5-delta short puts showed roughly 97–98% win rate; 10-delta roughly 95%. He says numbers matched theory closely enough that live trading could build trust.
- Tom’s parallel: in futures options, small delta-neutral trades across 10–15 underlyings in 2019 kept about 25% of premium sold, close to expected math.
- Trading-as-life frame: David says trading improved non-trading decisions because everything becomes pot odds: quantify upside, downside, and tradeoff before acting.

## Trading Read-Through

- **Theory of edge:** short premium gets paid to warehouse downside path risk, volatility risk, and tail/gamma risk other participants want to shed. Market does not pay because 5-delta puts magically cannot lose.
- High win rate is not edge by itself. It is expected from far OTM options; edge lives in whether premium collected exceeds realized tail losses after costs, slippage, stops, and bad regimes.
- 5-delta short puts are psychologically seductive: many tiny wins, rare ugly losses. Need audited risk budget, not vibes.
- Stops reduce blow-up risk but can also convert temporary vol spikes into realized losses; re-entry logic matters as much as entry logic.
- “Go smaller” is real risk control. If trade can still damage you when sized small, structure is wrong.
- 21 DTE rule here is time/gamma risk management: avoid holding short options into expiration just for last pennies.

## Practical Checklist

- Define trade before entry: underlying, delta, DTE, stop, re-entry/roll rule, max portfolio exposure.
- Track every occurrence by strategy bucket; do not mix strangles, condors, naked puts, rolls, and discretionary hedges into one fuzzy PnL blob.
- Compare live win rate and average loss to backtest expectation; kill or resize if live tails exceed model.
- Stress-test against Feb 2018 / Dec 2018 style moves, not only calm bull-market samples.
- Keep full-time-job process simple: fewer strategies, repeatable rules, low monitoring burden.

## Best Lines

- “It’s not worth it because of the risk and we do 21 DTE.”
- “Making money is easy, but it’s how you handle losing that you learn.”
- “You can never get hurt by going smaller.”
- “Everything’s pot odds… always risk-reward, always a trade-off.”

## One-Line Summary

Short puts can be a scalable process only when sized and managed like tail-risk warehousing, not treated as free yield from high win rates.
