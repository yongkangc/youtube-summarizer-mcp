---
title: "Vladimir Novakovski: Lighter, ZK Trading and Onchain Finance"
source: "https://www.youtube.com/watch?v=u8ezrAOjIbA"
video_id: "u8ezrAOjIbA"
duration: "34:41"
date_summarized: "2026-07-21"
category: "crypto"
---

# Vladimir Novakovski: Lighter, ZK Trading and Onchain Finance

## TLDR

Lighter founder Vladimir Novakovski argues that decentralized exchanges can surpass centralized exchanges by combining low latency and cost with verifiable execution and Ethereum settlement. Lighter's claimed technical edge is custom zero-knowledge circuits designed specifically for finance rather than general computation.

His broader lesson: technology, distribution and customer integration are complements. Fast infrastructure matters, but institutional adoption also requires forward-deployed engineers, liquidity partners and regulated distribution such as Robinhood.

The strongest investment caveat is token value capture. Novakovski says all economic value accrues to Lighter's token and equity receives no revenue or profit, but the interview does not specify fees, buybacks, burns, staking cash flows, token supply or unlocks. Treat value-accrual claim as an intention, not demonstrated economics.

## Background

- Began programming around age eight to build opponents for family card games.
- Competed in physics and informatics Olympiads.
- Entered Harvard at 16 and graduated in roughly two and a half years.
- Chose economics to learn what to build, having already developed strong programming skills.
- A 94 on his first microeconomics exam compared with a class average of 37 led directly to a research role.
- Joined Citadel around age 18 after Ken Griffin personally helped close the recruitment.
- Later worked in Silicon Valley at Quora and Addepar, then co-founded Lunchclub before pivoting it into Lighter.

## Citadel lessons

### Electronic markets rapidly consume visible alpha

Novakovski had researched and traded options strategies in college. Griffin told him some had worked historically but had already been arbitraged away.

Core lesson:

- A strategy's historical validity does not make it currently tradable.
- Once capital, data and automation target an anomaly, returns decay.
- Edge requires either new information, better execution, structural risk bearing or a market participants cannot efficiently enter.

He declined to disclose specific Citadel strategies.

### Madoff was suspicious years before collapse

During Novakovski's first week in 2004, Griffin reportedly dismissed Bernard Madoff's unusually smooth options-fund track record as a Ponzi scheme.

Novakovski says the SEC later failed to verify a fake DTCC account reference by making a basic confirmation call.

His blockchain argument:

- Madoff fabricated trades that never occurred.
- Onchain positions and settlements would be independently auditable.
- Zero-knowledge proofs could verify activity or solvency without publishing every position in real time.

Caveat: blockchain verifies recorded state, not necessarily asset custody, valuation, offchain liabilities, governance integrity or truthful oracle inputs. Transparency reduces one fraud vector; it does not eliminate fraud.

## Why Lighter exists

Novakovski left traditional quant trading because it optimized existing markets rather than creating new products and market structures. Lighter attempts to combine:

- low transaction cost;
- low execution latency;
- verifiable operation;
- security through Ethereum settlement.

These objectives usually conflict. More decentralization or proof generation can add latency and cost; centralized execution can be faster but less transparent.

## Claimed technical edge

Lighter uses custom zero-knowledge circuits designed for financial exchange logic instead of adapting general-purpose circuits.

Novakovski claims:

- proving finance-specific computation requires about 1% of the compute needed by a general-purpose approach;
- this allows lower cost and latency while retaining verifiability and Ethereum security;
- Lighter is stronger than competitors across cost, speed, verification and security.

These are founder claims. Interview provides no reproducible benchmark, throughput test, proof-generation cost, latency distribution, outage history or comparison under stressed volume.

## Theory of edge

**Lighter may earn market share if finance-specific ZK engineering lowers the decentralization tax enough that traders receive centralized-exchange speed while institutions retain verifiable Ethereum settlement.**

Who pays:

- Traders pay through fees, spread or token economics for execution and risk transfer.
- Integrators value faster time-to-market and interoperable settlement.
- Institutions may pay to reduce custody, reconciliation and counterparty risk.

Why market might reward Lighter:

- Specialized circuits may be difficult and slow for general-purpose chains to reproduce.
- Ethereum provides a trusted settlement layer without Lighter building equivalent security from scratch.
- Robinhood and Telegram Wallet can supply distribution Lighter would struggle to build directly.
- Integrated spot, perpetuals and options can improve collateral efficiency and liquidity concentration.

Why edge may disappear:

- Hyperliquid or other exchanges copy performance and product features.
- Traders prioritize liquidity and incentives over verification.
- Ethereum settlement costs or latency become limiting.
- Token subsidies create temporary volume mistaken for durable demand.
- Regulatory requirements favour conventional intermediaries.

## Technology and distribution are complements

Novakovski rejects the claim that technology no longer matters because distribution dominates.

Examples:

- Removing roughly 100 milliseconds can materially improve trading experience.
- Robinhood and Telegram Wallet performed technical diligence before integration.
- Institutional customers need engineers working directly with their teams.

He credits Joe Lonsdale and Palantir with the forward-deployed-engineer model: engineers become part of customer delivery rather than handing software over the wall.

Lighter combines:

- specialized exchange infrastructure;
- Ethereum interoperability;
- partner distribution;
- forward-deployed implementation support.

## Pivoting Lunchclub into Lighter

Roughly 80% of the engineering team stayed through the pivot.

Reasons given:

1. Management had accumulated trust.
2. Team participated in choosing the new direction.
3. Company ran an internal accelerator with three competing projects and a demo day.
4. Runway and investors remained healthy.
5. Engineers preferred cryptography, scaling systems and quantitative-finance problems.

Founder lesson: a pivot is easier when staff help choose it, survival is not immediately threatened, and new work better matches intrinsic motivation.

## Ethereum thesis

Novakovski views Ethereum as DeFi's equivalent of a clearinghouse:

- established security;
- stable operation;
- broad interoperability;
- credible settlement neutrality.

Moving away from Ethereum is not a meaningful roadmap priority. Lighter would reconsider only if another ledger became superior across relevant dimensions.

## Options roadmap

For Q3 2026, Lighter plans onchain options sharing one balance sheet and collateral system with perpetuals and spot.

Goal includes making options available through Robinhood.

Potential benefit:

- unified collateral;
- concentrated liquidity;
- lower operational friction;
- cross-product margining.

Risks:

- options require sophisticated market makers and robust volatility surfaces;
- liquidation and margin logic become materially harder;
- thin tails can create misleading marks and insolvency risk;
- regulatory treatment is more complex than spot or perpetuals;
- onchain speed does not itself create options liquidity.

## Token versus equity

Lighter is structured as a US C-corporation without a separate foundation.

Novakovski says:

- the pre-token venture round was Lighter's final equity raise;
- round was about five times oversubscribed;
- only about 1% of shareholders chose liquidity rather than accepting token-led economics;
- equity receives no revenue or profit;
- all value is intended to accrue to the token;
- long-term preference is for the token itself also to represent tokenized equity, subject to regulatory clarity.

Missing information:

- token supply and dilution;
- team and investor unlocks;
- fee schedule;
- whether fees are distributed, burned or retained;
- staking obligations and rewards;
- governance rights;
- legal claim on protocol assets;
- regulatory treatment;
- current organic volume after incentives.

Therefore, "all value accrues to the token" is not enough to value it. A token can receive narrative value without enforceable cash-flow rights.

## Evidence quality

Strongest evidence:

- founder's direct account of product architecture and company structure;
- named Robinhood and Telegram Wallet integrations;
- coherent explanation of finance-specific ZK design and forward deployment.

Weakest evidence:

- no audited performance benchmarks;
- no market-share, retention or organic-volume data;
- no comparison adjusted for incentives;
- no protocol revenue or token-capture mechanics;
- founder is selling Lighter's differentiation;
- host and participants may hold project exposure.

## YK read

Most useful idea is not "DEX beats CEX." It is that exchange advantage combines four layers:

1. **Execution:** latency, matching quality and uptime.
2. **Liquidity:** depth, spread and resilient market makers.
3. **Settlement:** custody, verification and counterparty risk.
4. **Distribution:** regulated customer access and integrations.

Lighter's technical story addresses execution and settlement. Robinhood/Telegram partnerships address distribution. Liquidity remains decisive and least evidenced in this interview.

Before underwriting token:

- separate gross volume from incentive-driven volume;
- measure spreads and depth during volatile periods;
- compare liquidation losses and downtime with Hyperliquid and major CEXs;
- verify real protocol revenue;
- map fee flow into tokenholder value;
- model unlocks and fully diluted valuation;
- test whether institutional integrations generate retained users;
- demand stress benchmarks for ZK proving and Ethereum settlement.

## Bottom line

Lighter offers plausible architecture: specialized ZK exchange computation on Ethereum, paired with large distribution partners. But architecture is only potential edge. Durable value requires liquidity, uptime, regulation and explicit tokenholder economics. Interview establishes technical ambition, not investable proof.