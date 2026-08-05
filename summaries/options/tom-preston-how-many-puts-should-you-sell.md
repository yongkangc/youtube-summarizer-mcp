---
title: "Tom Preston: How Many Puts Should You Sell?"
source: "https://www.youtube.com/watch?v=zAfFNEZiLis"
video_id: "zAfFNEZiLis"
channel: "tastylive"
speaker: "Tom Preston"
upload_date: "2026-08-04"
date_summarized: "2026-08-05"
duration: "6:59"
tags:
  - options
  - short-puts
  - delta
  - position-sizing
---

# Tom Preston: How Many Puts Should You Sell?

[YouTube](https://www.youtube.com/watch?v=zAfFNEZiLis)

## TL;DR

Choose short-put quantity from desired **delta exposure and downside capacity**, not premium income. One 33-delta put begins around +33 stock deltas; three begin near +99, locally resembling 100 shares. But this equivalence is temporary: as stock falls, put deltas rise and three contracts can become exposure to 300 shares.

## Example

Preston uses Nvidia options around 45 DTE:

- sell one 200 put;
- approximately 33 delta;
- approximately $740 credit;
- approximately $12.69/day theta;
- approximately $5,200 initial buying-power reduction.

One put gives less initial exposure, risk and upside opportunity than 100 shares. To target roughly +100 initial deltas:

- sell three 33-delta puts;
- initial position delta approximately +99;
- credit approximately $2,220;
- initial buying-power reduction approximately $15,600.

Alternative: two 50-delta puts also begin around +100 deltas.

## Critical payoff mechanics

Delta-matching is local, not payoff equivalence.

- **100 shares:** constant +100 delta; uncapped upside; downside equals stock price paid.
- **Three short 200 puts:** start near +99 delta; upside capped at $2,220 total credit; downside exposure increases as stock falls.
- Around strike, each put would ordinarily approach approximately 50 delta, so three short puts would be nearer +150 deltas, not +300, all else equal.
- Deep in the money, each short put approaches +100 delta; total approaches +300.

Using video's $7.40 premium per share:

- breakeven: **$192.60**;
- one-put maximum loss if NVDA goes to zero: **$19,260**;
- three-put maximum loss: **$57,780**;
- initial buying-power reduction is not maximum loss and can expand sharply.

Preston's statement that P&L will be “roughly the same” as 100 shares applies only to small near-term moves around entry. It is not true across larger moves because short puts have gamma, capped upside and nonlinear downside.

## Process suggested

For long-term bullish exposure:

- enter around 45 DTE;
- manage or roll around 21 DTE;
- repeatedly reset strikes/deltas to maintain target exposure;
- retain enough capital for adverse movement and possible assignment.

For weaker/speculative conviction, one put may be enough. If capital is constrained, Preston suggests defining risk with a vertical, such as short 200 put plus long 180 put.

Rolling can defer assignment but does not erase economic loss or downside exposure. A roll closes one losing position and opens another with later expiry.

## Theory of edge

Short-put seller is paid to warehouse downside, volatility, liquidity and gap risk. Delta matching alone creates no edge. The trade requires implied volatility/premium to exceed realized downside and tail losses after costs.

## Practical rule

Before selling puts, choose maximum acceptable exposure under three states:

1. **At entry:** contract delta × 100 × contracts.
2. **At strike:** stress near 50 delta × 100 × contracts.
3. **Deep ITM/assignment:** 100 shares × contracts.

Size from state 3, not entry buying power or theta.

## Bottom line

Three 33-delta puts may mimic 100 shares initially, but can morph into 300-share downside while retaining capped upside. Use delta for initial exposure; use assignment quantity and stressed loss for position sizing.