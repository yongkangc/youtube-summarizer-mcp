---
title: "0DTE SPX Iron Condors: Does Legging Out Improve Results?"
source: "https://www.youtube.com/watch?v=rCPBeBIenWQ"
video_id: "rCPBeBIenWQ"
duration: "9:39"
date_summarized: "2026-07-24"
category: "options"
---

# 0DTE SPX Iron Condors: Does Legging Out Improve Results?

## TLDR

Tastylive tested whether closing the nearly worthless side of a 0DTE SPX iron condor improves results while leaving the tested side open. With a 25% whole-position profit target already applied, legging out did not materially improve win rate or tail risk. Holding the full condor until the profit target or expiration produced the strongest average and cumulative results, though with more P&L volatility.

Closing one side only when it had already captured roughly 90% of its maximum value produced comparable returns with somewhat lower volatility. Earlier leg removal sacrificed too much remaining decay.

## Test design

- Underlying: **SPX**
- Expiration: **0DTE**
- Entry: **8:30 a.m. Central**, approximately the cash-market open
- Short strikes: approximately **20 delta**
- Wings: **$20 wide**
- Sample: daily data from **2023 onward**
- Intraday observations: approximately every **10 minutes**
- Whole-position profit target: close after capturing **25% of original credit**

Baseline:

- Hold complete iron condor until 25% profit target or expiration.

Legging-out variants:

- Buy back either call spread or put spread after its value decays to a threshold.
- Leave the other vertical spread open.
- Close remaining position if whole-trade 25% profit target is reached.
- Otherwise hold remaining defined-risk spread to expiration.

Explicit thresholds listed were **$0.75, $0.50 and $0.25** per spread. The discussion also references a **$1** threshold, creating a minor specification inconsistency.

## Results

### Win rate

All approaches clustered around approximately **89.9%**.

Legging out did not materially increase win rate. The existing 25% profit target dominated the management effect by removing many profitable positions early.

### Typical trade

Median P&L remained approximately **$140** across strategies.

This suggests legging out changed tail and path outcomes more than the ordinary trade experience.

### Average and cumulative P&L

Holding the complete condor produced:

- strongest average return;
- highest cumulative P&L;
- more P&L volatility.

Closing one side earlier forfeited additional theta. The roughly **$0.50–$0.75** thresholds appeared to offer a middle ground: respectable cumulative growth with less volatility than baseline.

Closing only near **$0.25**, when most premium had already decayed, produced results close to baseline.

### Tail risk

Legging out did not meaningfully improve worst-case outcomes. Baseline had the smallest average loss among the worst **5%** of observations in the displayed analysis.

The position was already defined-risk. Legging out could remove a side whose value might later change during an intraday reversal, while the remaining side stayed exposed.

## Interpretation

A short vertical's remaining upside is capped at its remaining premium. Once roughly 90% of that side's premium has been captured, keeping it open earns little while preserving some operational and reversal exposure. Buying it back cheaply can therefore be reasonable.

Closing at a high residual value is different: the trader pays away meaningful remaining edge without materially changing the tested-side risk.

The 25% portfolio profit target already performs most of the useful early-exit function. Adding another management rule creates little incremental value.

## Theory of edge

**Volatility/liquidity risk premium:** the 0DTE iron-condor seller earns premium for warehousing intraday convexity, jump risk and liquidity demand.

Legging out is not an independent edge. It adds value only if reduced tail exposure or P&L variance exceeds:

- premium paid to close;
- bid/ask spread;
- commissions and fees;
- lost theta;
- adverse execution during fast markets.

## Methodological limitations

The study is suggestive, not deployment-grade:

- **2023 onward** is a short and regime-specific sample.
- Ten-minute snapshots miss intrabar target ordering, fast gamma moves and executable quotes.
- Transaction costs, slippage and spread-crossing assumptions were not presented in the video.
- Exact strike-selection and missing-data rules were not shown.
- No volatility-regime, trend-day, macro-event or day-of-week breakdown.
- No comparison of return on buying power, drawdown duration or risk-adjusted return.
- The profit target and legging thresholds may have been selected after inspecting results.
- SPX expiration and settlement mechanics need explicit implementation detail.

A one- or two-tick execution difference can materially affect frequent 0DTE strategies.

## YK read

Practical rule:

> Do not leg out merely because one side is profitable. Close it only when residual premium is trivial relative to fees, spread and operational risk.

Before trading:

1. Rebuild with one-minute bid/ask data.
2. Use conservative marketable fills.
3. Include commissions and exchange fees.
4. Split results by VIX level, trend days and scheduled macro events.
5. Compare baseline, full-close target and leg-out rules on CAGR, max drawdown, CVaR and buying-power return.
6. Test thresholds as a percentage of original side credit, not fixed dollars only.
7. Hold out recent data and avoid tuning on full sample.

## Bottom line

Within this setup, simple management won: keep the complete defined-risk condor until its 25% profit target or expiration. Legging out offered no clear return or tail-risk advantage. Cheaply removing a nearly exhausted side may reduce volatility, but aggressive legging mostly pays away remaining premium.