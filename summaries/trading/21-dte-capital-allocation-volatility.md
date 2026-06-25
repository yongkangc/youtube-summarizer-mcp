---
title: "How This Strategy Can Help You Manage Risk"
source: "https://www.youtube.com/watch?v=B665lnA0Oyo"
category: trading
summary_date: 2026-06-25
---

# How This Strategy Can Help You Manage Risk

Source: https://www.youtube.com/watch?v=B665lnA0Oyo

## TL;DR

Tastytrade compares three management styles for 45-DTE one-standard-deviation strangles: hold to expiration, take profits at **50% max profit**, or exit at **21 DTE**. Their conclusion: exiting at roughly half the original time-to-expiration produces the best volatility control and, in this study, the highest average return with the lowest daily volatility.

## Setup

- Strategy: **45 DTE, one-standard-deviation short strangles**
- Capital allocation: initially **25%** of total account value, then scaled to **35%**
- Portfolio is always invested / continuously redeployed
- Management rules compared:
  - Hold to expiration
  - Manage winners at **50% max profit**
  - Exit at **21 DTE**

## Key findings

### 1. 21 DTE had best return/volatility tradeoff

- Exiting at **21 DTE** generated the **highest average return** and **lowest volatility** among the three rules.
- Tony generalizes it as “exit at half the time”:
  - 45 DTE trade → exit around **21 DTE**
  - 30 DTE trade → exit around **15 DTE**
  - 10 DTE trade → exit around **5 DTE**
  - 1 DTE trade → exit around noon

### 2. 50% profit-taking helps return, but not volatility

- Managing winners at **50% max profit** improved returns versus holding to expiration.
- But it did not control volatility as well as 21-DTE exits.
- Their wording: 50% winners are “not bad,” but not where they want to be if the goal is smoother P/L.

### 3. Holding to expiration was weakest

- Holding to expiration had the worst return in this comparison.
- It also failed to control portfolio volatility as effectively.
- This supports their broader rule: avoid sitting in the last part of the expiration cycle where gamma/tail risk can dominate.

### 4. Scaling up capital increases portfolio volatility

They increased committed capital from **25%** to **35%**.

- Volatility rose for all three management strategies.
- This is intuitive: bigger size means bigger P/L swings.
- But the **21-DTE rule still contained the volatility increase best**.

### 5. 50% profit-taking produced the biggest profit jump after scaling, but also more volatility

- When scaling up, 50% profit-taking saw a larger jump in profitability.
- But volatility rose too.
- Their preference: reducing volatility is more valuable than chasing a higher jump in profitability.

## Trading read-through

This is a portfolio-control argument, not just a trade-management argument. The edge in short premium is harvesting volatility/risk premium repeatedly without letting gamma, size, or capital concentration dominate the book.

The 21-DTE rule works because it mechanically cuts exposure before the nastier late-cycle risk profile. It also forces capital recycling. The 50% profit rule is fine for harvesting winners, but it leaves risk exposure dependent on when profit arrives; 21 DTE is more robust as a portfolio volatility governor.

## Practical checklist

- For 45-DTE short premium, default exit around **21 DTE**.
- Think of 21 DTE as a **portfolio volatility control**, not just a trade exit rule.
- If scaling allocation from 25% to 35%, expect portfolio vol to rise mechanically.
- Don’t optimize only for profit; optimize for return per unit of P/L volatility.
- 50% profit-taking is useful, but weaker than 21 DTE for controlling volatility.
- If portfolio P/L curve feels too jumpy, reduce sizing first; size is the volatility dial.

## One-line summary

For short strangles, 21-DTE exits are less about squeezing max profit and more about keeping the portfolio’s volatility from becoming the trade.
