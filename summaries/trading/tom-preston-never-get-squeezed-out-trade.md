---
title: "Tom Preston Shows How to Never Get Squeezed Out of a Trade Again"
source: "https://www.youtube.com/watch?v=7zff_5jj36E"
video_id: "7zff_5jj36E"
category: "trading"
created: "2026-07-06"
---

# Tom Preston Shows How to Never Get Squeezed Out of a Trade Again

📺 Source: https://www.youtube.com/watch?v=7zff_5jj36E

## TL;DR

Tom Preston’s point: squeezes are not just price pain; they are forced-exit events caused by losses plus expanding margin / buying-power requirements. Defined-risk vertical spreads cap both max loss and capital requirement, so position survives adverse moves without broker/liquidity pressure forcing bad exits.

## Edge / Risk Premia

This is not a new edge by itself. It is risk-control for short-premium trades. Actual edge, if any, is still short-vol / liquidity provision / getting paid to warehouse downside or upside tail risk. Vertical spread converts uncapped/margin-expanding exposure into capped risk, sacrificing some premium for survival and cleaner sizing.

## Key Mechanics

- Short squeeze: short stock or short call exposure loses money as price rises; margin requirement rises; weak shorts must buy back, pushing price higher.
- Long squeeze: longs lose money as price falls; margin/capital pressure or pain forces selling, pushing price lower.
- Squeezes are not official market metrics. Preston says look for big price moves with volume spikes as clue.
- Main danger: forced trades. Broker / clearing margin rules can force exit at bad fills. Trader loses control of timing.

## Micron Example

- Stock around `1033`.
- Bullish naked short put example: sell `950 put` for about `$83–86`.
- Initial buying-power effect: about `$12,430`, rounded to `$12,500`.
- If Micron drops from `1033` to `950`, that `950 put` becomes ATM and behaves like current `1030/1035` ATM put.
- Buying-power requirement can jump from about `$12,500` to around `$20,700–24,000`.
- Problem: even if trader can tolerate mark-to-market loss, trader may not have capital to hold position. Then broker forces buyback.

## Vertical Spread Fix

- Instead of naked short `950 put`, sell `950/940 put spread`.
- Credit around `$4.40`.
- Width = `10 points` = `$1,000` max spread width.
- Buying-power effect = width minus credit = about `$560`.
- If Micron drops and short strike becomes ATM, buying-power stays around `$560–600`, not `$12.5k → $24k`.
- Max loss known at entry: about `$560–600` depending fill.
- Same principle on upside: instead of naked short call, use short call spread.

## Trading Read-Through

- This video is mostly about **liquidation risk**, not directional prediction.
- Naked short options on high-priced / volatile names carry two risks:
  - P&L loss.
  - Margin expansion exactly when trade is moving against you.
- Defined-risk spreads reduce forced-exit probability. That can be worth paying via lower credit / capped reward.
- Tight wings matter. Preston notes very wide spreads can start behaving more like naked short-option margin because broker may margin short leg, not pure width.
- Practical pre-trade test: simulate adverse move by dragging OTM short strike to ATM equivalent and checking buying-power requirement.

## Checklist

- Before selling naked option, ask: if underlying moves to short strike, what does BPR become?
- Can account hold new BPR without margin call?
- If answer no, use defined-risk spread or smaller size.
- For high-priced names, prioritize survival over premium maximization.
- Do not confuse lower BPR with free edge. Spread still loses if thesis wrong; it just prevents margin spiral.

## One-Line Summary

Use vertical spreads when naked short-option margin expansion can force you out; capped upside is price paid for staying alive.
