# Stop Selling In the Money Spreads. Do This Instead.

Source: https://www.youtube.com/watch?v=L-nr6AFx7OU

## TL;DR

Mike from tastytrade argues that most traders should avoid using in-the-money vertical spreads when the same payoff can be built with out-of-the-money options. The risk graph is synthetically equivalent, but OTM options usually have tighter bid/ask spreads and more liquidity, so the trade is cleaner and cheaper to execute over many repetitions.

## Core definitions

- **Out-of-the-money option:** pure extrinsic value. If it stays OTM through expiration, it goes to zero.
- **In-the-money option:** intrinsic value plus extrinsic value.
- **Intrinsic value:** distance between strike and current underlying price.
- ITM options retain intrinsic value as long as they remain ITM; the intrinsic component transfers roughly one-for-one across expirations.

## Buying options: OTM vs ATM/ITM

- Buying OTM calls/puts gives higher percentage upside if the underlying moves toward the strike, because the option gains extrinsic value.
- Buying ATM/ITM options can still make money, but percentage gain is lower because the option gains intrinsic while losing some extrinsic.
- OTM options can go to zero if the expected move does not happen.

## Main point: avoid ITM spreads when possible

Mike focuses on traders selling ITM put spreads to express a bullish view.

Example:

- Sell 750 put / buy 745 put, both ITM or near ITM.
- This creates a bullish vertical payoff.
- But those ITM options have wider markets and less activity.

Equivalent alternative:

- Buy the 745/750 OTM call spread using the same strikes.
- Same risk graph / same payoff profile.
- Better liquidity and tighter bid/ask in most cases.

In the SPY example shown:

- ITM put spread market: around **2.50 / 2.70**, about **20-cent wide**.
- OTM call spread market: around **2.45 / 2.55**, about **10-cent wide**.
- OTM calls had much larger open interest: roughly **20k–23k** contracts vs only **1.9k–3.6k** on the ITM puts.

## Synthetic equivalences

Same strikes, same expiration:

- **Selling an ITM put spread** ≈ **buying the equivalent OTM call spread**.
- **Buying an ITM call spread** ≈ **selling the equivalent OTM put spread**.

The payoff is effectively the same, but the OTM expression usually has better markets.

## Why this matters

This is not about changing your market view. It is about reducing execution drag.

If two structures have the same risk profile, prefer the one with:

- tighter bid/ask
- more open interest
- more volume
- less slippage
- simpler fills

Over one trade, the difference may look small. Over hundreds or thousands of trades, liquidity drag compounds.

## Caveat: synthetic stock / covered call replacement

Mike gives one caveat where an ITM option can make sense:

- Instead of buying 100 shares and selling a call, you can sell an ITM put.
- That creates a similar risk profile to a covered call.
- It may use far less buying power.

In his SPY example, selling the ITM put saved more than **$20,000** in buying power compared with stock + short call, while the max-loss profile was effectively the same.

So the rule is not “never trade ITM options.” The rule is:

- For **vertical spreads**, use the OTM synthetic version when possible.
- For **stock-like exposure**, an ITM option may be more capital efficient.

## YK trading translation

For your SpaceX / IPO-vol bullish spread question:

- If you want bullish defined risk and are tempted to sell an ITM put spread, check the equivalent OTM call spread.
- If the OTM call spread has better bid/ask and open interest, use that instead.
- If you want to collect premium/theta specifically, an OTM bull put spread is still fine, but do not force ITM strikes just to get more credit.
- ITM put spread = more directional, worse liquidity, less clean theta trade.

## One-line summary

When a vertical spread can be replicated with OTM options, use the OTM version: same payoff, usually tighter markets, less slippage, better long-run execution.
