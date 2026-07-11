---
title: "How I Would Build an Options Portfolio From Scratch in 2025"
source: "https://www.youtube.com/watch?v=bQ00jjoh_b4"
channel: "Calculated Risk"
duration: "1:21:12"
summary_date: "2026-07-11"
---

# How I Would Build an Options Portfolio From Scratch in 2025

## TL;DR

Jim Schultz presents an 81-minute beginner course that moves from option mechanics to a Tasty-style portfolio process. His recommended progression is: understand calls/puts and Greeks, begin with small defined-risk OTM credit spreads around **45 DTE**, prefer **IV rank above 30**, risk **1–3% per spread**, then gradually learn iron condors/diagonals before considering undefined-risk short-premium trades.

The economic thesis is that option sellers collect theta and the volatility risk premium because implied volatility tends to exceed subsequent realized volatility. The missing half is that this premium compensates sellers for negative convexity, gaps, volatility expansion, and tail losses.

## Option foundations

An option contract specifies:

- underlying
- strike
- contract size, usually **100 shares**
- expiration
- option premium

Terminology:

- long = buyer
- short = seller
- call gives the long the right to buy shares at the strike
- put gives the long the right to sell shares at the strike
- the long and short payoff are opposing sides of the same contract

Moneyness:

- Call is ITM when stock price > strike.
- Put is ITM when stock price < strike.
- ATM means stock approximately equals strike.
- OTM means the option currently has no intrinsic value.

## Payoffs

- Long call: limited loss to premium, theoretically unlimited upside.
- Short call: limited premium income, theoretically unlimited upside loss.
- Long put: limited loss to premium, large downside profit potential.
- Short put: limited premium income, large downside loss potential down to stock price zero.

## Option pricing

He introduces the Black-Scholes inputs:

- stock price
- strike
- time
- implied volatility
- dividends
- interest rate

Every option premium consists of:

- **Intrinsic value:** current exercise value.
- **Extrinsic value:** time, volatility, and remaining model inputs.

OTM options consist entirely of extrinsic value. At expiration, all extrinsic value becomes zero.

## Three P&L drivers

He simplifies portfolio P&L to:

1. **Delta:** directional exposure.
2. **Theta:** passage of time.
3. **Vega:** implied-volatility exposure.

His framework is to spend less effort predicting exact direction and more effort structuring exposure to time and volatility.

## Bullish versus bearish exposure

Bullish advantage:

- Equities have long-run positive drift from the equity risk premium, economic growth, and innovation.

Bearish advantages:

- Downside moves are typically faster and larger because equity returns have negative skew.
- Short delta can hedge a short-premium portfolio because market declines usually coincide with volatility spikes.

This does not make short delta a complete hedge. Volatility expansion, skew changes, gaps, and nonlinear option exposure can overwhelm a simple directional offset.

## Why he prefers selling options

### Positive theta

Extrinsic value must decay to zero by expiration. An OTM option seller can profit if the option remains OTM, even without correctly predicting direction.

He prefers entering around **45 DTE**, where he says decay begins accelerating while enough time remains to manage the position.

### Short volatility

Option prices rise with implied volatility. He argues:

- volatility usually spends more time near the lower end of its range
- volatility is mean reverting after spikes
- implied volatility tends to exceed subsequent realized volatility

The implied-minus-realized spread is the seller's expected edge.

## Structural edge

> The market pays option sellers to supply insurance and liquidity and to warehouse volatility, gap, and tail risk. Implied volatility is often marked above subsequently realized volatility because buyers pay a premium for protection and convexity.

This is not free theta. It is compensation for adverse states where losses arrive quickly and correlations rise.

## Beginner trade recommendation

Start with OTM defined-risk vertical credit spreads:

- **Bullish:** short put spread.
- **Bearish:** short call spread.

These provide:

- positive theta
- negative vega
- fixed maximum loss
- a breakeven buffer
- higher probability of profit than pure directional stock exposure, in exchange for capped gains and asymmetric loss size

Guidelines:

- Risk **1–3% of account equity per spread**.
  - For a $10k account: **$100–$300 maximum risk**.
- Prefer **IV rank >30** to sell after some volatility expansion.
- Trade liquid names from established watchlists.
- Begin small and do not modify strikes in ways that increase predefined maximum risk.

## Proposed learning progression

1. Short vertical spreads.
2. Iron condors.
3. Diagonals and other defined-risk structures.
4. Only after substantial experience, undefined-risk strategies.

He argues that consistently successful traders often emphasize undefined-risk strategies. This should be treated as his opinion, not a required destination. Undefined-risk option selling can produce smoother win rates but carries severe gap, margin, and tail risk.

## Important caveats

- **Theta is not a standalone return.** Delta and vega losses can exceed months of decay in one move.
- **IV > realized is compensation for risk.** Variance-risk premium exists partly because short-volatility losses concentrate in bad states.
- **Mean reversion has no guaranteed timetable.** Volatility can remain elevated or rise further after entry.
- **POP is not expected value.** Credit spreads can win often while average losses exceed average wins.
- **1–3% per spread can aggregate dangerously.** Several positions can share the same market, sector, volatility, or crash factor.
- **Undefined risk is not necessary for success.** It demands stricter sizing, liquidity, stress testing, and buying-power reserves.
- **Options are zero-sum at contract payoff before fees, but portfolio outcomes also depend on hedging, financing, spreads, taxes, and risk premia.**

## Practical portfolio checklist

Before entering:

- Is the underlying liquid?
- Is IV elevated relative to its own history?
- What are delta, theta, vega, and gamma?
- What is maximum loss and portfolio-level correlated loss?
- Is this genuinely a new exposure or another version of the same short-vol trade?
- What happens under a gap, volatility spike, or margin expansion?
- What is the exit or adjustment rule?

## One-line summary

Start with small, liquid, OTM defined-risk credit spreads around 45 DTE and sell elevated implied volatility, but recognize that theta income is payment for warehousing nonlinear downside risk.
