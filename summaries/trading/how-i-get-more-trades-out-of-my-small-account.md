# How I Get More Trades Out Of My Small Account

Source: https://www.youtube.com/watch?v=UdBYC1vnCyQ

Speaker/show: tastylive / Tasty Bites

## TL;DR

The video explains how to use synthetic option positions instead of stock to get directional exposure with less buying power. Core idea: long call + short put is synthetic long stock; short call + long put is synthetic short stock. You can use ATM options for near-100-delta stock replacement, or OTM options for lower delta, lower buying power, and higher probability of profit, but synthetics require active management because they expire and delta changes.

## Mechanics

- **Synthetic long stock / combo:** buy call + sell put, same expiry, usually same strike. This creates a forward-like payoff: bullish, high positive delta, similar to owning shares.
- **Synthetic short stock / combo:** sell call + buy put, same expiry, usually same strike. This creates a bearish forward-like payoff: similar to shorting shares.
- **Not a straddle:** a straddle buys both call + put, or sells both call + put. A synthetic stock position buys one option and sells the other. The sign is the whole difference.
- A same-strike ATM synthetic behaves nearly one-for-one with 100 shares by expiration because long call delta plus short put delta approximates +100 shares.
- If the call and put use different OTM strikes, this is better described as a **risk reversal / OTM combo**, not a pure stock replacement. It gives lower delta and lower BPR, but has a flat/no-profit zone between strikes and different expiry behavior.
- Tasty’s preference: enter for a **credit** where possible so you are not paying time value.

## Example numbers from the video

- Buying 100 shares of Amazon at **$225/share** requires **$11,250** in a regular margin account, assuming 50% stock margin.
- Nvidia at **$171/share** would require roughly **$17,000** cash or **$8,500** with margin — too large for a **$10,000** account.
- Amazon ATM synthetic BPR: about **$5,600**, roughly half the long-stock buying power requirement.
- Amazon 30-delta OTM synthetic BPR: about **$3,900**.
- OTM synthetic example has about **75 delta** rather than 100 delta.
- OTM synthetic probability of profit rises to about **65%**, versus roughly **50%** for stock or ATM synthetic exposure.

## Why it helps small accounts

- Frees buying power versus stock.
- Lets a small account get multiple positions instead of tying up most capital in one 100-share lot.
- Allows configurable directional exposure rather than binary “own 100 shares / short 100 shares”.
- Can improve probability of profit if using OTM structures entered for credit.

## Trade-offs / risk

- Stock is simpler: no expiration, constant 100 delta for 100 shares.
- Synthetic options expire, so you must close or roll.
- Delta is not constant. It changes with stock price and time.
- At expiration, delta collapses toward either 0 or 100 depending on where the stock closes versus the strikes.
- OTM synthetics have a different payoff shape: they may require stock to move above the long strike to be profitable at expiration.
- Less buying power does not mean less risk automatically; it can encourage oversizing if you treat margin relief as free leverage.

## Practical checklist

- Use liquid underlyings/options only.
- Decide desired directional delta first, not just “I want stock exposure.”
- Prefer credit entry when possible.
- Check BPR, max directional risk, and expiration behavior.
- Plan the roll/exit before entry.
- Track what you are synthetically long or short by looking at the whole option position, not each leg in isolation.

## One-line summary

Synthetic options let small accounts rent stock-like directional exposure with less buying power, but the cost is expiration, moving delta, and the need for active management.
