# Stop Selling In the Money Spreads. Do This Instead.

Source: https://www.youtube.com/watch?v=L-nr6AFx7OU

## TL;DR

Mike’s point: don’t trade in-the-money vertical spreads when the out-of-the-money equivalent creates the same payoff. The OTM version usually has tighter bid/ask, more open interest, more volume, and less slippage — same risk graph, better execution.

## Key mechanics

- Out-of-the-money options are pure extrinsic value.
- In-the-money options contain:
  - intrinsic value: distance between strike and current price
  - extrinsic value: remaining option premium above intrinsic
- If an ITM option is 5 points in the money, it keeps roughly 5 points of intrinsic value as long as spot stays there, regardless of expiration.

## Option-buying note

- Buying OTM options can generate higher percentage returns if spot moves toward/through the strike, because the option gains extrinsic value as it approaches ATM.
- Buying ATM/ITM options may retain more absolute value if the move happens, but percentage return is lower because intrinsic rises while extrinsic can fall.
- OTM = more explosive upside percentage, but can go to zero.
- ITM = more durable value, but more capital and usually worse percentage return.

## Main spread lesson

Example from SPY:

- Selling an ITM put spread, e.g. short 750 put / long 745 put, expresses a bullish spread.
- Buying the OTM call spread with the same strikes, e.g. long 745 call / short 750 call, creates the same risk/reward profile.
- They are synthetically equivalent.

But execution differs:

- ITM put spread had wider markets, roughly 20 cents wide in his example.
- OTM call spread had tighter markets, roughly 10 cents wide.
- OTM calls also showed much higher open interest: around 20k–23k contracts vs lower ITM put open interest.

## Rule of thumb

For vertical spreads, prefer the OTM side when it creates the same payoff:

- Instead of selling an ITM put spread, buy the OTM call spread.
- Instead of buying an ITM call spread, sell the OTM put spread.
- Instead of selling an ITM call spread, buy the OTM put spread.
- Instead of buying an ITM put spread, sell the OTM call spread.

Reason: same risk graph, usually better liquidity.

## Why it matters

The edge is not directional — the payoff is the same. The edge is execution quality:

- narrower bid/ask
- less slippage
- easier fills
- more open interest
- better repeatability over many trades

This matters more over many occurrences. A few cents saved per trade compounds if you run the strategy hundreds or thousands of times.

## Caveat: synthetic covered calls / stock replacement

He gives one exception:

- Buying 100 SPY shares and selling a call creates a covered-call payoff.
- Selling an ITM put can synthesize a similar covered-call / long-stock-with-short-call profile.
- This may use much less buying power, even if max loss is similar.
- In that case, accepting a slightly wider ITM option market may be worth it because the trade is replacing stock exposure and improving capital efficiency.

## Practical checklist

Before placing an ITM spread:

- Check whether the OTM counterpart has the same risk graph.
- Compare bid/ask width.
- Compare open interest and volume.
- Prefer the OTM version if payoff is equivalent.
- Only use ITM options deliberately when they improve capital efficiency or replicate stock exposure.

## My trading read

This is a microstructure/execution-cost point, not a strategy-edge point. If two option structures are synthetic equivalents, the better trade is the one with tighter markets and more depth. ITM spreads often look attractive psychologically because you “sell premium,” but the OTM equivalent often gives the same exposure with less slippage.

## One-line summary

If the payoff is identical, trade the out-of-the-money equivalent — same risk, usually better liquidity and less execution drag.
