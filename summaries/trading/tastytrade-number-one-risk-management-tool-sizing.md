# I May Have Just Found My #1 Risk Management Tool

Source: https://www.youtube.com/watch?v=zBd_DBZL-6E

## TL;DR

The video argues that for short-premium/options portfolios, the most important risk-control rule is **stay small** — especially limiting total portfolio capital allocated to short premium. Greeks and diversification matter, but both can fail in turbulent markets; sizing is the risk lever you actually control at entry.

## Core claim

If a new options trader follows only one risk-management rule, it should be:

- **Keep trade size small.**
- More importantly: **cap total short-premium allocation at the portfolio level.**

Reason: at order entry, you can choose underlying, duration, strategy, and Greeks, but the one thing that most directly limits how much capital is exposed is **size**.

## Three risk controls discussed

- **Sizing:** limiting individual position size and total portfolio allocation to short premium.
- **Underlying diversification:** spreading exposure across sectors, asset classes, and markets.
- **Greek management:** monitoring portfolio/position Greeks such as beta-weighted delta and theta.

Their ranking: all matter, but sizing is most robust when markets break.

## Why Greeks are not enough

- Greeks estimate expected option behavior under model assumptions.
- Beta-weighted delta estimates portfolio move for a $1 move in benchmark, usually SPY.
- Portfolio theta estimates daily time decay.
- But Greeks come from models like Black-Scholes, which assume smooth price moves and relatively stable volatility.
- In highly volatile regimes, those assumptions break down.

YK read: Greeks are useful dashboard instruments in normal markets, not crash airbags.

## Why diversification is not enough

Diversification helps against **idiosyncratic risk**:

- Apple has a bad day.
- One sector sells off.
- One company-specific event hits.

But it does not fully protect against **systemic risk**:

- In a market-wide selloff, correlations rise.
- During 2020, SPY and sector ETFs saw 30-day correlations converge toward 1.
- Even defensive sectors like utilities became more correlated with the broad market.

So diversification still helps, but less when you most need it.

## Defensive assets are imperfect hedges

They discuss gold and bonds as examples of assets that may become inversely correlated with equities during stress.

But:

- inverse price correlation is not guaranteed;
- you can be on the wrong side of a big move in gold or bonds;
- options vol can spike across markets even if prices diverge;
- high vol is high vol — short options can lose from implied-vol expansion even when underlyings are not price-correlated.

This is the options-specific trap: price diversification can fail because **implied volatility correlations remain high**.

## Compounding loss example

From *The Unlucky Investor’s Guide to Options Trading*:

- SPY + QQQ strangles: compounding loss probability around **67%** because underlyings are highly correlated.
- SPY + gold strangles: compounding outlier / 2x loss probability around **36%** in the dataset.

36% is lower than 67%, but still meaningful. Diversification reduces risk; it does not eliminate short-vol regime risk.

## Why sizing wins

Position and portfolio sizing directly limit exposed capital:

- Defined-risk trades have a strict max-loss cap.
- Undefined-risk trades do not have a true cap, but smaller notional/contract sizing still limits capital at risk relative to account size.
- Total portfolio allocation to short premium is most resilient against market-wide turbulence.

They especially emphasize **portfolio capital allocation to short premium**, not just individual trade size.

## Allocation guidance mentioned

They reference a short-premium allocation guide based on VIX / volatility regime.

In the current example, with VIX in the **20–30** range:

- Conservative case: around **35% max allocation** to short-premium positions.
- Moderate case: about **30–35% more**, roughly **47–50%**.
- Aggressive case: another **30–35% more**, roughly **64–65%**.

The video stresses that the shown **35%** is the conservative case, not the only possible number.

## Why reserve capital matters

The point of lower allocation is not idle purity. It is to keep dry powder for stress:

- withstand large market moves;
- avoid forced liquidation when vol spikes;
- deploy into better opportunities after premium expands;
- avoid being maxed out exactly when expected returns improve.

This is the practical reason sizing beats Greek micromanagement.

## YK trading read-through

- **Theory of edge:** short premium earns volatility/liquidity/convexity risk premium, but the market pays you because you warehouse crash/vol-spike risk. Sizing is how you survive long enough to collect it.

- **Most useful rule:** cap total short-premium buying power / margin / risk allocation before caring about fancy adjustments.

- **Greeks are state-dependent.** In normal regimes, useful. In discontinuous regimes, stale.

- **Diversification is regime-dependent.** Helps with single-name/sector risk; weakens sharply under systemic stress.

- **Vol correlation is the hidden killer.** Even if underlyings move differently, implied vol can rise everywhere, hurting multiple short options positions together.

- **Reserve capital is edge capital.** It lets you sell premium when IV is high instead of defending over-sized trades opened when IV was lower.

## Checklist

- Keep individual positions small.
- Cap total portfolio allocation to short premium.
- Treat defensive-asset strangles as still short-vol, not true hedges.
- Watch beta-weighted delta and theta, but do not trust Greeks as crash protection.
- Assume correlations rise and vol correlations rise in stress.
- Keep enough cash/buying power to act after vol expands.

## One-line summary

For short-premium trading, sizing is the only risk lever that still works when Greeks get stale and diversification correlations collapse — stay small so you survive the vol spike and can deploy after it.
