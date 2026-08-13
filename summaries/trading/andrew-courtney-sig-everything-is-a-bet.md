# “I Think of Everything as a Bet” — Ex-SIG Quant Trader Andrew Courtney

Source: https://www.youtube.com/watch?v=MXDozNbr7Js

Note: YouTube captions were unavailable. Summary uses downloaded audio + local ASR; names and minor wording may be imperfect.

## TLDR

Former SIG quant market maker Andrew Courtney explains trading as decision-making under incomplete information: estimate probabilities, understand who is across from you, size for uncertainty, update from market response, and judge process rather than isolated outcomes. His prediction-market edge thesis is structural: new, obscure, weakly researched markets can briefly reward smart amateurs because prices are less informed and professional competition remains thin.

## Theory of edge

**Smart amateurs may get paid for researching neglected prediction markets where natural reference prices are absent, liquidity providers optimize for incentives rather than valuation, and institutions have not yet crowded the market.**

This edge is temporary. Growing liquidity and professional entry should compress it.

## SIG trading reality

- Electronic market making meant multiple monitors filled with prices, signals, and alerts.
- Most days were slow; danger came from not knowing when a market or strategy would suddenly break.
- Even while programming, trader kept one eye on live markets.
- No real lunch break: catered food, then immediately back to desk.
- Career produced a narrow, dense network of talented coworkers, unlike consulting/banking’s broad client network.
- Good fit requires enjoying constant pattern extraction, uncertainty, competition, and divided attention—not merely wanting compensation/status.

## Why SIG trains with poker

- Training included roughly **10 weeks** off-desk.
- Trainees played poker **1–2 hours daily** with peers and instructors.
- After interesting hands, everyone exposed cards and justified each decision quantitatively and qualitatively.
- Poker resembles markets more than chess:
  - incomplete information
  - uncertain opponent models
  - probabilistic outcomes
  - decisions can be correct even when result loses
  - sometimes uncertainty remains even after outcome
- Core habit: separate **decision quality** from **outcome quality**.

## “Everything is a bet”

He frames ordinary choices as decision trees:

- possible upside/downside
- probabilities
- cost of waiting
- value of new information
- shrinking opportunity as decision is delayed
- whether personal balance sheet can absorb variance

Example: public versus private schooling. Waiting one year reveals more about child and schools, but may reduce future benefit from switching. Optimal choice balances information gain against decaying payoff.

## Prediction-market efficiency

First question: **what anchors this price?**

- Fed markets inherit information from Fed funds futures.
- Sports markets inherit odds and research from sportsbooks.
- These prices already aggregate professional work, even if prediction-market volume itself looks low.
- Novel categories with little data, no natural reference market, and little analyst attention should be less efficient.

Second question: **who is on other side?**

- An obscure Grammy market had almost no volume but paid liquidity incentives.
- Quoters may primarily want daily rewards, not express informed fair value.
- Such quotes deserve less informational weight than prices backed by deep natural liquidity.

## LLM forecasting experiment

- Courtney used a reasoning LLM prompted as a “superforecaster” for obscure Grammy markets.
- He later became **less confident** in LLM forecasts.
- Results were highly prompt-sensitive and noisy.
- He now considers model quality weakest part of trade.
- More important:
  - market selection
  - weak counterparties
  - low cost if model is wrong
  - asymmetric payoff from even modest informational value
- If he had a genuinely researched view, he would discard LLM estimate and use research directly.

## Entry, sizing, and updating

- Direction alone insufficient once size grows; need fair value estimate.
- He views roughly **quarter-Kelly** as reasonable textbook sizing, but tiny market liquidity often binds before bankroll does.
- Each extra price level crossed requires more confidence because entry worsens.
- Order-book response is information:
  - take 1,000 offered and market disappears: counterpart may have been passive/incentive-driven
  - take 1,000 and 10,000 immediately reloads: informed seller may disagree strongly
- Reassess thesis after every market reaction. He calls this Bayesian updating.

## Behavioral opportunities

- Retail likes lottery-ticket long shots and parlays; house margins are large.
- Media salience can concentrate casual bettors on obvious side.
- Ask: **which side would a non-expert naturally want?** Then inspect opposite side.
- Contrarianism alone is not edge. Must compare price to probability and identify why flow is biased.

## Measuring whether edge is real

- Small, heterogeneous trade samples make statistical proof hard.
- Different contracts have different edge profiles and cannot be pooled cleanly.
- A Monte Carlo benchmark can simulate every trade assuming paid probability is fair, then compare actual P&L with distribution.
- Positive P&L alone proves little, especially before rare expensive favorites lose.
- Short-run priority: document a structural reason each trade should have edge.

## Prediction-market opportunity window

- Courtney says competent programmer + trading knowledge may currently build profitable one/two-person systems on Kalshi-style markets.
- Similar system would have no chance market-making Apple against mature firms.
- Prediction markets have lower entry barriers and less institutional saturation.
- This resembles early electronic/options eras when smart amateurs could compete.
- Window likely closes as professional firms scale resources.

## Best and worst use cases

Best:

- naturally binary events, especially elections
- information aggregation around news/geopolitics/public health
- direct event exposure where stocks/options are noisy proxies
- eventual risk transfer/insurance contracts, e.g. hurricane or earthquake risk

Weak/problematic:

- contracts duplicating cleaner instruments, e.g. S&P threshold when options already exist
- mention/word markets vulnerable to manipulation
- markets creating insider-trading incentives
- 15-minute crypto and sports products marketed as easy money

## Insider trading and adverse selection

Courtney rejects claim that insider trading improves prediction markets:

- may move price toward truth sooner in short run
- creates severe adverse selection
- liquidity providers widen/leave
- damages long-run efficiency
- creates corrosive incentives for employees, governments, and information custodians

A market is not a truth machine. It is a limited order book and one signal among many.

## Practical checklist

Before trade:

1. What structural reason makes market pay me?
2. Is there a mature reference market already anchoring price?
3. Who likely sits across from me: informed trader, retail gambler, or incentive farmer?
4. What is fair probability—not merely direction?
5. If estimate is garbage, how much can trade lose versus random?
6. How much liquidity exists before price destroys edge?
7. What market response would invalidate thesis?
8. Can portfolio absorb variance and tail loss?

## YK read

Strongest lesson: **counterparty + market structure often matter more than forecasting model sophistication.** LLM may improve research speed, but cannot manufacture edge in already efficient market. Best PM-alpha terrain is obscure contract, weak natural anchoring, biased/incentive-driven flow, bounded downside, and explicit invalidation from order-book reaction.

## One-line summary

Think in bets, identify who pays you and why, size below uncertainty, update from every fill, and expect amateur prediction-market edge to disappear once professionals arrive.
