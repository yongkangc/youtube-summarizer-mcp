# Most Traders Buy the Dip on Any Red Day. This Tastylive Study Shows That Is the Wrong Approach

Source: https://www.youtube.com/watch?v=eK5Zh_VPVHU

## TL;DR

Tastylive tests whether selling 45-DTE SPY put spreads after red days works better than selling them every day. Result: buying/selling the dip on tiny red days underperforms; the sweet spot is larger down days, especially around 1–2% SPY drops. The edge is not that rebounds become more likely — it is that volatility/premium expands enough to pay better for the same tail risk.

## Setup

- Underlying: SPY / S&P proxy.
- Trade: short put spread.
- Structure: short ~30 delta put, long ~15 delta put.
- DTE: 45 days.
- Hold: to expiration, no management, to isolate tail outcomes.
- Signal tested: enter only after SPY red days by threshold:
  - down 0% to 0.5%
  - down 0.5% to 1%
  - down 1% to 2%
  - down >2%
- Benchmark: selling similar put spreads every day.

## Findings

- Selling put spreads after tiny red days is not useful.
  - Down 0% to 0.5% is mostly noise.
  - Down 0.5% to 1% also underperforms selling every day.
  - Removing bullish days and only trading mild red days can reduce returns.

- Larger dips improve average returns.
  - Down 1–2% starts to produce stronger performance.
  - Down >2% also looks richer, but happens less often.
  - Practical systematic zone: SPY down 1–2% because it occurs often enough and provides enough vol expansion.

- POP barely changes.
  - Probability of profit across thresholds stayed roughly in the 82–89/90% range.
  - Better performance did not come from trades winning materially more often.

- Directional rebound assumption is mostly wrong.
  - After SPY is down >2%, probability of rebound 45 days later is not meaningfully better than any random 45-day period.
  - The market does have long-term upward drift, but this short-term dip signal is not a strong directional forecast.

- Real driver is premium/volatility.
  - Larger down days push implied volatility/premiums higher.
  - You are getting paid more for roughly similar probability/risk profile.
  - CVaR/extreme-loss dollar value did not rise much as dips got larger, because higher premium offsets some tail loss.

## Trading Interpretation

- Do not treat every red day as a dip-buying edge.
- Mild red days are noise; they do not provide enough extra premium.
- If using price signals for short put spreads, wait for real vol expansion.
- Best process rule from this study:
  - no signal: trade normal systematic short premium
  - SPY down <1%: ignore as noise
  - SPY down 1–2%: better entry window
  - SPY down >2%: richer premium but lower frequency / event-risk context matters

## Theory of Edge

This is not a “markets bounce after red days” edge. The structural edge is **short-vol / liquidity provision after volatility expands**. You are being paid more premium to warehouse downside/tail/gamma risk when other traders demand protection.

## Risk Caveats

- Study holds to expiration; real Tastytrade process usually manages early, often around 21 DTE.
- Short put spreads remain negatively convex: rare big selloffs can dominate results.
- Down >2% days may include crisis regimes where vol is high for a good reason.
- SPY/index behavior does not generalize cleanly to single-name equities; single names have larger gap/idiosyncratic risk.

## One-Line Summary

Don’t sell put spreads on any red day; wait for enough downside move to lift premium — the edge is richer vol compensation, not better rebound odds.
