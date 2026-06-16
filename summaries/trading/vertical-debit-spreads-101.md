# Vertical Debit Spreads 101

Source: https://www.youtube.com/watch?v=ptxT5wdWfJQ

## TL;DR

Mike from tastytrade explains vertical debit spreads as a way to take directional exposure with defined risk and better probability than buying naked options. You give up the “home run” upside, but reduce cost, move breakeven closer or even slightly in your favor, and get controlled exposure to expensive underlyings.

## When debit spreads make sense

Use debit spreads when:

- You have a directional view.
- IV is low enough that buying premium is not insanely expensive.
- The underlying is too expensive to buy shares outright.
- You want defined max loss.
- You want better probability than buying a naked call/put.

They are not ideal if you need unlimited upside. They cap profit by design.

## Call debit spread setup

Example stock price: **100**

Structure:

- Buy 95 call
- Sell 105 call
- Width: **10 points**

Pricing example:

- 95 call costs **$7.50**
  - $5 intrinsic value
  - $2.50 extrinsic value
- Sell 105 call for **$2.50**
- Net debit: **$5.00**

Trade math:

- Max loss: **$5.00**, or **$500/contract**
- Max profit: width - debit = **$5.00**, or **$500/contract**
- Breakeven: **100**, same as current stock price
- Return on capital if max profit: **100%**
- Probability of profit: roughly **50%** because debit is half the width

## Why straddle the stock price

For debit spreads, Mike says he generally does not buy fully OTM debit spreads or fully double-ITM debit spreads. He prefers to **straddle spot**:

- Long option slightly ITM
- Short option OTM
- Stock price between the strikes

Reason:

- Keeps breakeven near current price.
- Gives directional exposure immediately.
- Reduces the extrinsic value you need to overcome.
- Caps upside, but increases probability vs naked long option.

## Debit spread vs naked long option

Naked long call:

- Unlimited upside.
- Needs a large, fast move.
- Breakeven is above current stock price because you must overcome premium paid.
- Lower probability, higher payoff if right big.

Call debit spread:

- Upside capped.
- Lower cost basis because short call offsets premium.
- Breakeven can move down to current stock price.
- Higher probability, lower max payoff.

His phrasing: you are giving up the home run and going for a single/double.

## Put debit spread example

For bearish exposure, flip the structure.

Example stock price: **100**

Structure:

- Buy 107 put
- Sell 95 put

Pricing example:

- 107 put costs **$8.20**
  - $7.00 intrinsic
  - $1.20 extrinsic
- Sell 95 put for **$1.45**
- Net debit: **$6.75**

Trade math:

- Long put is $7 ITM.
- You pay only $6.75 for the spread.
- If stock stays at 100 through expiration, the 107 put is worth about $7.
- So breakeven is slightly favorable: stock can stay flat and the spread can make about **$0.25**.
- Max profit: **$5.25**
- Max loss: debit paid = **$6.75**

## More ITM long option = higher POP, lower ROC

Moving the long option deeper ITM:

- Raises the debit paid.
- Moves breakeven in your favor.
- Increases probability of profit.
- Reduces return on capital because you pay more to make less.

So there is a tradeoff:

- Pay less = higher ROC, lower POP.
- Pay more = lower ROC, higher POP.

## Key takeaways

- Vertical debit spreads are directional trades with defined risk.
- They remove the “home run” upside of naked options.
- In exchange, they improve breakeven and probability of profit.
- Best construction usually straddles current spot: buy ITM, sell OTM.
- Max loss is always the debit paid.
- Max profit is spread width minus debit paid.
- Breakeven can be near spot or even slightly favorable if long leg is deeper ITM.
- Useful for expensive stocks where shares are too capital-intensive.

## YK trading translation

For a SpaceX-style bullish hype trade:

- **Call debit spread** fits if your thesis is “it rips upward.”
- It is cleaner than a naked call because you reduce premium paid.
- It is cleaner than an ITM put spread if the OTM call spread has better liquidity.
- But it is not theta income. You need directional upside.
- If IV is insanely high, debit spreads still suffer because you are buying net premium, but selling the upper call helps offset that.

Practical structure:

- Buy slightly ITM or near-ATM call.
- Sell OTM call near your realistic target.
- Pay debit you are willing to lose fully.
- Choose spread where breakeven is close to current spot, not far above it.

## One-line summary

Debit spreads trade away jackpot upside for cheaper, defined-risk directional exposure with a better breakeven and higher probability than naked long options.
