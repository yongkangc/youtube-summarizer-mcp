# Managing 0 DTE Options Risk — Zero Days to Expiration Crash Course

Source: https://www.youtube.com/watch?v=MBmGDAbMdJ4

## TLDR

Tastytrade segment on using **0DTE SPX butterflies** as a defined-risk intraday range trade. The key point is not that butterflies have magic edge. It is that 0DTE makes butterflies tradable because gamma is high and prices move intraday. The research says butterfly pricing is basically efficient across volatility regimes: higher expected move makes the fly cheaper, lower expected move makes it more expensive, but the probability of making a fixed percentage of debit intraday stays roughly similar.

## Strategy discussed

They are trading **daily SPX call butterflies**:

- At-the-money body
- Around **30-point-wide wings**
- Often entered 0DTE or 1DTE
- Typically buying flies around **$4.50–$7.25 debit**, depending on volatility
- Taking profits at **25–50% of debit paid**
- Not holding to expiry / settlement

Example mentioned:

- Buy butterfly for **$3.60**
- Sell next morning for **$5.10**
- Profit: **$1.50**, about **42% of debit**

They prefer SPX over SPY because SPX is cash-settled, though they note it does not matter much if they close before the end of the day.

## Why 0DTE changes butterflies

They say they rarely discussed butterflies for normal 45DTE options because flies barely move when there is lots of time left.

With 0DTE:

- gamma is high
- the day’s expected move matters immediately
- the fly can move enough to scalp
- max loss is known upfront
- buying power is low vs naked or ratio structures

The trade is basically:

> “Can SPX stay near this range long enough for the fly to appreciate intraday?”

## Pricing mechanics

They study **SPX 0DTE at-the-money call butterflies with 30-wide wings** across expected-move regimes:

- expected move less than **$25**
- expected move **$25–$50**
- expected move greater than **$50**

Main observation:

- Bigger expected move → butterfly is cheaper
- Smaller expected move → butterfly is more expensive

Reason:

- If implied move is high, probability of landing inside the wings by expiry is lower, so the market charges less for the fly.
- If implied move is low, probability of staying inside the wings is higher, so the fly costs more.

Approx example prices from the segment:

- Low expected move: around **$9.50** for a 30-wide fly
- Mid expected move: around **$7.25**
- High expected move: lower than that

Live example in the video:

- Same-day expected move around **40 points**
- 30-wide ATM SPX fly priced roughly around **$6–$8 market**, about **$7 mid**

## Important research takeaway

Their key claim:

**The probability of making a certain percentage of debit intraday is roughly the same regardless of the day’s expected move.**

In other words:

- On high-vol days, you pay less, but the fly has lower probability of finishing inside the range.
- On low-vol days, you pay more, but the range is more likely to hold.
- The market prices this pretty efficiently.

So there is no obvious free lunch from saying:

> “Today’s fly is cheaper, so it is better.”

It may simply be cheaper because volatility / expected move is higher.

## Profit target guidance

They like taking **25–50% of debit paid**.

Reason:

- Holding to expiration is basically a coin-flip-ish bet depending on strike/range.
- But taking smaller intraday profits should have >50% probability if entry is fair.
- The fly can be held for a better target than naked long options because theta/premium bleed is less brutal.

Example:

- Buy for **$4.00**
- Target profit **$1–$2**
- Sell around **$5–$6**

This is more like defined-risk scalping than lottery-ticket expiry gambling.

## Why they like it versus naked options

Compared to buying naked 0DTE calls/puts:

- lower premium drag
- less tail risk
- defined max loss
- easier to set mechanical profit targets
- less need to predict a large directional move

Compared to short/riskier 0DTE structures:

- much lower buying power
- no naked tail exposure
- easier for smaller accounts

They mention SPX ratio spreads can require around **$70k+ buying power**, which is out of reach for many traders. Butterflies are cheaper and defined-risk.

## Main caveat

This is not edge by itself.

They explicitly say the market is pricing these efficiently. The edge, if any, is execution/process:

- getting a good fill
- choosing sensible body/wing width
- not overpaying relative to expected move
- taking profits mechanically
- sizing small
- not turning a defined-risk scalp into an expiry lottery

## My trading read

Useful framework, but I would treat it as **variance-contained entertainment / execution practice**, not a scalable edge unless we can prove fills and slippage are favorable.

Theory of edge if trading it:

> Retail often mismanages 0DTE by buying naked options and holding too long. A defined-risk butterfly with mechanical 25–50% profit targets may monetize intraday mean reversion/range behavior while capping blow-up risk.

But the structural edge is weak unless:

- realized intraday pin/range behavior is underpriced
- fills are consistently better than model mid
- trader exits winners faster than losers without bad expectancy leakage
- body placement has signal, not vibes

## Practical rules if YK experiments

- Use **SPX**, not SPY, if avoiding assignment/settlement mess.
- Keep size tiny; assume frequent full-debit losses.
- Enter only at fair/mid-ish price; do not chase wide markets.
- Target **25–50% of debit**, not max profit.
- Close before expiry; do not let it become a settlement gamble.
- Track every trade: debit, expected move, wing width, body distance from spot, time entered, time exited, realized SPX path, fill quality.
- Backtest by entry-time and body-placement rule before increasing size.

## One-line summary

0DTE SPX butterflies are a defined-risk way to scalp intraday expected range, but pricing is efficient; any edge must come from disciplined entries, fills, body placement, exits, and sizing — not from the structure itself.
