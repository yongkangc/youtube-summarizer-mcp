---
title: "Covered Calls: Close When Remaining Premium Stops Paying"
source: "https://www.youtube.com/watch?v=giz_xCcrzdE"
video_id: "giz_xCcrzdE"
duration: "7:52"
date_summarized: "2026-08-11"
category: "options"
channel: "tastylive"
---

# Covered Calls: Close When Remaining Premium Stops Paying

## TLDR

Tom Preston’s rule: keep a covered call only while its remaining premium is still worth the time and risk. Use today’s shorter-dated option at the same strike as a rough forward map; once much of original credit is captured, buy it back and sell a fresh 39–46 DTE call.

## Example

- Long 100 IBM shares near $236.20.
- Sell 39-DTE $250 call around $6.55.
- If stock and volatility stay roughly unchanged:
  - after two weeks, comparable 25-DTE call suggests ~$4.60–$4.80 value: ~$1.75–$1.95 profit, 27–30% of credit captured;
  - after three weeks, comparable 18-DTE call suggests ~$3.12: $3.43 profit, 52.4% captured.
- Ask: “Would I newly sell this 18-DTE call for $3.12?” If not, close and reopen farther out, possibly same strike.

## Edge and risk

A covered call is `long stock + short call`: premium reduces effective basis, but trader sells upside convexity and still bears almost all stock downside. Edge exists only if sold implied volatility/premium exceeds realized opportunity cost and losses—not merely because theta decays.

Speaker’s “no upside risk” means no additional cash loss above strike; it ignores opportunity cost when stock rallies far through $250. Rolling lower after a drop can also crystallize a worse upside cap and create whipsaw risk.

Shorter-dated current prices are only scenario proxies. The mapping fails when stock, IV, rates, dividends, skew, or earnings timing changes.

## Practical rule

1. Define desired stock exit price before selling call.
2. Track credit captured versus days and upside remaining.
3. Re-evaluate short call as if opening it fresh today.
4. Close when residual premium no longer compensates for cap/assignment risk.
5. Roll only if new call is independently attractive—never merely to “keep generating income.”

## Bottom line

Useful management heuristic, not evidence of alpha. Covered-call success must be judged against unhedged stock on total return, including foregone upside, downside, fees, tax, assignment and executable fills.