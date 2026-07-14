---
title: "This Video Will Change How You Pick Strikes Forever"
source: "https://www.youtube.com/watch?v=VsUIyZzL8WI"
video_id: "VsUIyZzL8WI"
speaker: "Jim Schultz"
channel: "tastylive"
duration: "10:21"
category: trading
---

# Picking short-option strikes: probability versus premium

[YouTube source](https://www.youtube.com/watch?v=VsUIyZzL8WI)

## TL;DR

Short-option strike selection trades probability against compensation. Far-OTM strikes win more often but collect little extrinsic value against large tail exposure; strikes nearer ATM collect more premium and provide a wider premium-adjusted breakeven, but lose more frequently. Schultz prefers roughly **25–35 delta** as a practical compromise for undefined-risk premium sales.

## Core mechanics

- Option sellers trade **extrinsic value**, which must decay to zero by expiration if all else stays constant.
- Lower-delta OTM short options generally have higher probability of expiring profitably but smaller credits.
- Nearer-ATM options carry more extrinsic value and larger credits, but greater directional exposure and lower probability of profit.
- Short-option probability of profit is measured against the **premium-adjusted breakeven**, not merely the strike. That is why an ATM short option can show POP above 50%.
- Delta's complement, `1 − |delta|`, is only a rough estimate of probability expiring OTM. It is not exact POP, exercise probability, or expected value.

## Tesla examples shown

Underlying was around **$394**, with roughly 39 days remaining:

- **340 put, ~15 delta:** heuristic predicts about 85% POP; platform showed 82%.
- **390 put, ~44 delta:** heuristic predicts about 56%; platform showed 63% because credit moves breakeven below strike.
- **300 put, ~5 delta:** roughly 95% POP for about **$1.60 / $160 credit**. Cash-secured maximum loss is approximately **$29,840**, with breakeven at **$298.40**. Credit is only **0.54% of maximum downside**.
- **355 put, ~23 delta:** platform showed about 75% POP and **$8.70 / $870 credit**. Cash-secured maximum loss is approximately **$34,630**, with breakeven at **$346.30**. Credit is **2.51% of maximum downside**.

Presenter warns naked Tesla positions require substantial account capital, suggesting well above $200K–$300K, though appropriate sizing depends on portfolio concentration, stress margin, and loss limit rather than account size alone.

## Why 25–35 delta

Schultz views this range as balance among:

- meaningful premium;
- probability above 50%;
- some distance from spot;
- enough credit and delta to support rolling or active management.

It is a process preference, not universal optimum. Best strike depends on volatility skew, IV rank, expected move, liquidity, catalysts, correlation, portfolio exposure, and management rule.

## Edge and risk

**Theory of edge:** Short options can earn volatility/insurance premium when implied volatility systematically exceeds subsequently realized volatility. Strike selection allocates that edge and tail risk; high POP itself is not edge.

Main cautions:

- POP ignores payoff asymmetry. Many tiny wins can be erased by one crash.
- Delta and platform POP are model outputs, not guarantees; both move with spot, time, and IV.
- “Undefined risk” short put has finite loss if underlying reaches zero, but loss is economically enormous versus credit. Naked short calls have theoretically unlimited loss.
- Initial buying-power requirement can expand sharply during selloffs and volatility spikes.
- Moving from 5 delta to 25–35 delta increases premium but also frequency and magnitude of challenged trades.
- Management cannot manufacture positive expectancy when options are fairly or cheaply priced after costs.

## YK read

Use 25–35 delta only as starting grid. Compare candidate strikes by expected value, premium per stressed loss, skew richness, liquidity, portfolio beta, and gap scenario. For every short option, write down breakeven, maximum/stress loss, margin expansion, management trigger, and exit before entry.

## One-line summary

Pick strikes by compensation for tail risk, not probability of winning.