---
title: "Position Sizing, Explained in One Sitting"
source: "https://www.youtube.com/watch?v=tBia3DWL2UI"
video_id: "tBia3DWL2UI"
channel: "More Tom Sosnoff"
upload_date: "2026-10-15"
date_summarized: "2026-10-16"
---

# Tom Sosnoff: Position sizing rules, with a risk audit

Compilation of One Lucky Dog and interview excerpts, not a single internally consistent sizing lecture. Reviewed all 1,829 caption segments in contiguous windows through approximately 63:30; metadata runtime 63:28. Figures are speaker rules of thumb, not validated risk limits.

## Theory of edge first

Potential short-option compensation is volatility/insurance premium earned by warehousing convexity, gap and tail risk, plus any demonstrated directional or execution advantage. High win rate, collecting theta, making many trades and cheap margin are not independently an edge. Sosnoff initially defines edge narrowly as execution below theoretical value and argues retail cannot obtain it against professional market makers. That does not settle whether a particular strategy has positive net expected value. The law of large numbers cannot turn negative expectancy positive; correlated trades do not create independent repetitions.

## Distilled rules worth applying

1. Size to survive being wrong, not to maximize the next premium receipt. Avoid increasing size merely after a winning streak.
2. Treat initial buying-power reduction (BPR) as a funding requirement, not maximum loss or a risk budget. Track net liquidation value, notional, stress loss and stressed margin separately.
3. Reduce contracts first when discomfort prevents clear thinking. An elaborate roll does not substitute for removing exposure.
4. Close when the thesis changes, volatility-premium opportunity disappears, remaining reward is trivial relative to capital/tail risk, or the trade breaches your risk budget.
5. Scale total deployment with opportunity, not an income quota. Sosnoff deploys less in low volatility and more in high volatility. Higher IV alone does not establish cheap risk.
6. Diversify causal exposures, underlyings and expiration dates. Different option structures on correlated equities can remain one short-volatility trade.
7. Keep liquidity outside initial margin to survive simultaneous losses and margin expansion. Cash supporting short puts is encumbered risk capital, not automatically a safe reserve.
8. Judge a roll as closing one trade and opening another. Credit versus debit does not determine whether the resulting position has better expected value or lower risk.
9. Trim a winning asset that becomes dominant in net worth. Do not let gratitude for past gains determine future risk.
10. Never rely on a stop order as a guaranteed gap-loss cap. Small size and appropriate defined-risk/hedging structures are complementary protections.

## Speaker sizing numbers: preserve definitions and contradictions

- **05:33, $200K account:** defined-risk trades approximately $1K–$2K, occasionally $3K; undefined-risk trades approximately $7.5K–$15K **initial BPR**, explicitly not notional or maximum loss.
- **08:42:** roughly **0.3–1.5%** per defined-risk trade versus **3–7%**, sometimes **up to 10%**, initial BPR per undefined-risk trade. He suggests up to 15% in very small accounts. Elsewhere he says roughly 0.5–2% defined and 3–7% undefined. These are not one consistent universal rule.
- **08:42:** defined-risk allocation of roughly **25–40%** is described as a maximum allocation, but denominator language shifts between capital and available buying power. Do not apply it as a precise portfolio constraint without clarification.
- **23:16:** a $20K-account weekly-spread caller is told **10–15%** per defined-risk trade is acceptable at the top end. This conflicts materially with the earlier small-position ranges. Do not adopt this as a safe default.
- **Portfolio margin/futures options:** repeatedly recommends using **25–35% less BPR** than conventional listed options. One example is $35K versus $50K on a $100K account. This is a heuristic, not stress-risk equivalence.
- **55:52:** theta around **0.1–0.2% of net liq**, sometimes up to **0.3%**, with **0.5%** deemed excessive. Theta is model-estimated daily decay, not promised daily income; raising it increases gamma/vega/tail exposure.
- **60:36:** for a portfolio-margin account consisting only of short puts, **40–50% BPR usage is his upper range**, not a target. Caller proposals of 50–80% are discouraged. A broker/portfolio-specific stress test may require a much lower ceiling.

## Management mechanics

### 12:19–23:16: deployment and rolling

He favors longer duration in low IV and shorter duration in higher IV; the specific example is 60 versus 30 DTE. Longer duration can reduce near-expiry gamma while increasing vega and capital duration, so it is not uniformly lower risk.

He prefers keeping rolled puts within roughly 90 DTE. He and Scott characterize assignment as avoidable by rolling, but American-option holders retain exercise rights; early assignment can occur before an intended roll. Closing or rolling early reduces practical exposure, not the legal right of exercise.

He describes rolling the untested side inward for a credit, or buying back an overcompressed short strangle and selling wider strikes for a debit (“buy the guts, sell the wings”). The latter reopens room but does not erase realized losses. Inward rolls can worsen reversal risk and reduce diversification between sides.

### 23:16–34:04: discomfort, market changes and concentration

Reduce size as the quickest intervention. Close if the underlying thesis changes or residual reward is too small—for example, continuing to tie up thousands in capital for a near-worthless short option. Evaluate percentage/volatility-normalized moves rather than treating a bigger dollar move at a higher index level as inherently more abnormal. Trim large crypto/net-worth concentrations; his personal “decade rule” is anecdotal, not a valuation method.

### 34:04–39:56: verticalized collar

For long-dated, in-the-money **long call spreads**, he proposes selling OTM call spreads above the expected move and using the credit to buy OTM put spreads below it, with similar duration and potentially narrower hedge widths. This is a defined-risk bearish overlay, not free protection. Existing long call spreads have capped upside, so naked short calls would be especially dangerous. Match total contracts, widths and stressed payoff across the combined position; hedge put spreads also cap the protection they provide. Account for basis risk and dividend-related early assignment.

### 39:56–43:05: Treasury curve pair

Example: **long one /ZB, short two /ZN**, or **long one /ZB, short four /ZF**. Intended thesis: long-end yields fall relative to intermediate yields. He calls this roughly an 80% risk reduction and suggests a $1K–$1.2K worst case. Neither is a guaranteed bound: futures losses are not capped at that amount. Hedge ratios require current DV01, delivery/cheapest-to-deliver and curve analysis, not a permanent contract-count rule.

### 43:05–55:52: drawdowns and futures

He urges small positions, not abandoning a process solely after a drawdown, and selling puts selectively after red/oversold moves. “Oversold” is not a standalone edge or permission to average down. His claim that there has been no prolonged downtrend since 2008–09 overlooks meaningful later bear periods and is not relied on here.

He emphasizes futures contract specifications and early management. The transcript conflates tick size and point value in examples; verify exchange specifications rather than reusing the clip. Futures options are not universally ten times equity options. SPAN and portfolio margin improve initial capital efficiency, not economic safety.

## Claims not to copy literally

- **“Buying power will never change”: incorrect as a general rule.** Naked-option, SPAN and portfolio-margin requirements can rise as volatility, prices, concentrations and broker house rules change.
- **“True risk” approximately 5% CVaR or at most 20% capital:** not substantiated. No horizon, confidence level, positions or scenario assumptions are provided. Delta-neutral is not gamma/vega-neutral and neither percentage caps realized loss.
- **Higher POP implies profitability:** false without loss severity, costs and expected-value analysis.
- **A short put always has higher POP than a covered call:** cannot follow from the structure alone. Matched-strike/maturity covered calls and cash-secured puts have equivalent terminal payoffs subject to financing/dividends and implementation differences.
- **Size is the only way to manage outliers:** too strong. Size matters greatly, but defined-risk structures, liquidity reserves and appropriately priced hedges can also control tail exposure.
- **Trade often:** only when opportunities retain positive net expectancy after fees/slippage. Repetition otherwise compounds costs.

## YK pre-trade checklist: adapted, not speaker-prescribed

- Why does the market pay me for this risk?
- What are entry BPR, total notional, defined max loss or explicit stress loss, and stressed margin?
- What happens if correlated positions move against me together?
- Can I survive the gap without a stop filling or a roll being available?
- What invalidates the thesis, and when will I cut size or exit?
- Is there enough remaining reward to justify the capital and tail exposure?

**Bottom line:** size from portfolio stress and survival first; use platform margin and theta only as secondary operating metrics. This video is valuable behavioral advice, not a complete quantitative risk model.
