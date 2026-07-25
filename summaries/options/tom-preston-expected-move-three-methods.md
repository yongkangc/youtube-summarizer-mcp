---
title: "Tom Preston: Expected Move and Three Different Option-Market Estimates"
source: "https://www.youtube.com/watch?v=OcU_CmO6BP4"
video_id: "OcU_CmO6BP4"
duration: "14:30"
date_summarized: "2026-07-24"
category: "options"
---

# Tom Preston: Expected Move and Three Different Option-Market Estimates

## TLDR

Expected move estimates the magnitude—not direction—of a potential price change over a stated horizon. Tom Preston explains three platform numbers that may disagree because each uses different option data:

1. a weighted straddle/strangle estimate;
2. standard-deviation bands derived from an expiration-wide IVX volatility;
3. probability of expiring in the money derived from each option's own implied volatility.

They are risk-neutral, price-implied guides rather than forecasts of the stock's true distribution. Use them to frame strike selection, then require adequate credit and portfolio-level risk.

## Why expected move matters

Option value depends heavily on expected movement magnitude and the chance of finishing or becoming in the money. It does not encode a trader's subjective bullish or bearish opinion.

More precisely, option pricing incorporates forward price, rates, dividends and carry, but not an arbitrary directional forecast supplied by the trader.

Expected move helps answer:

- How large a move is priced over this expiration?
- Where do one- and two-standard-deviation reference levels sit?
- What probability does an individual strike imply?
- Does a spread's credit justify its width and tail exposure?

## Method 1: weighted straddle and strangles

The displayed plus/minus expected move uses:

$$
EM = 0.60(ATM\ straddle) + 0.30(first\ OTM\ strangle) + 0.10(second\ OTM\ strangle)
$$

Example from SPY:

- 60% × 12.92 at-the-money straddle;
- 30% × 11.93 first out-of-the-money strangle;
- 10% × 10.97 second out-of-the-money strangle;
- resulting displayed range: approximately **±12.21**.

This floor-trader heuristic uses observed option prices and updates as those prices change. It is not a directional call.

Important caveat: the weighted premium is a convention, not a guaranteed confidence interval or unbiased estimate of future realized movement.

## Method 2: IVX standard-deviation bands

IVX is a VIX-style volatility calculation for one underlying and expiration, using a broad set of available out-of-the-money calls and puts.

The platform converts that expiration-wide implied volatility into one- and two-standard-deviation price bands.

Under a normal-distribution approximation:

- about **68%** falls within ±1 standard deviation;
- about **95%** within ±2;
- about **99.7%** within ±3.

These are model approximations. Equity returns have skew, jumps and fat tails, especially around earnings or macro events. Real-world breach frequencies may exceed normal-distribution predictions.

## Method 3: individual-option probability

Each strike has its own implied volatility. The platform uses that strike-specific IV to calculate a model probability of expiring in the money.

Therefore, a put around the expiration-wide one-standard-deviation line need not display exactly a 16% in-the-money probability.

Preston's Meta example:

- expiration-wide IVX: approximately **49.9%**;
- individual 510 put IV: approximately **47.45%**;
- different volatility inputs produce different ranges and probabilities.

This is a direct consequence of volatility skew/smile and different calculation inputs.

Critical caveat: option-implied probability is generally a **risk-neutral**, model-dependent probability—not necessarily the market's true physical probability. Risk premia, skew and liquidity affect it.

## How to combine them

Preston's sequence:

1. Use weighted expected move for quick range orientation.
2. Inspect expiration-wide one-standard-deviation bands.
3. Examine strike-level probability and implied volatility.
4. Compare credit received with spread width and loss potential.
5. Move strike closer or farther only if reward/risk becomes acceptable.

For a short put spread, he asks whether the credit is roughly adequate relative to strike width. Probability alone does not justify a trade.

## Trading implication

The structural edge in short-premium trading, when present, is compensation for providing liquidity and warehousing volatility/tail risk. Expected move does not create that edge; it only describes current market pricing.

A complete decision still needs:

- implied versus expected realized volatility;
- volatility-risk-premium estimate;
- event calendar;
- skew and term structure;
- bid/ask spread and fill quality;
- maximum loss and portfolio correlation;
- scenario analysis beyond displayed standard-deviation bands.

## YK read

Best use: translate option-chain prices into comparable range and strike references.

Do not interpret expected move as:

- analyst forecast;
- hard support/resistance;
- guaranteed containment probability;
- evidence that selling outside the line has positive expected value;
- complete measure of jump or gap risk.

For earnings, compare the implied move with the stock's historical post-earnings absolute move and condition on current uncertainty. For ordinary expirations, compare implied volatility with a forward realized-volatility estimate. Then size against stressed moves, not only ±1σ.

## Bottom line

Three numbers can disagree without any being mechanically wrong because they answer related questions using different datasets. Expected move is useful navigation. Edge still comes from identifying mispriced volatility and surviving outcomes beyond the displayed range.