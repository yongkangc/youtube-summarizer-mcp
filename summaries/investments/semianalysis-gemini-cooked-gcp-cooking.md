---
title: "Gemini Is Cooked but GCP Is Cooking"
source: "https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking"
publication: "SemiAnalysis"
authors:
  - Max Kan
  - Joey Brookhart
  - Doug O'Laughlin
  - Dylan Patel
published_date: "2026-08-07"
archived_date: "2026-08-07"
topics:
  - Google
  - DeepMind
  - Gemini
  - Google-Cloud
  - TPU
  - AI-infrastructure
  - Anthropic
---

# Gemini Is Cooked but GCP Is Cooking

## Source

- Article: https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking
- Publication: SemiAnalysis
- Authors: Max Kan, Joey Brookhart, Doug O'Laughlin and Dylan Patel
- Published: August 7, 2026
- Access: complete article body reviewed

## One-sentence thesis

SemiAnalysis argues that Google has effectively chosen to monetize its scarce TPU capacity through Google Cloud rather than reserve it for DeepMind, sacrificing Gemini's long-term frontier competitiveness in exchange for a near-term GCP revenue, margin and EPS surge.

## Theory of edge

> Consensus models GCP primarily as recurring cloud revenue and underestimates gross-recognized TPU system sales, a large accelerator backlog and the transfer of compute from first-party Gemini research to external AI labs.

The proposed variant perception has two sides:

1. **Gemini downside:** talent departures, weak model releases, decelerating first-party token growth and inadequate compute allocation reduce the probability that DeepMind returns to the frontier.
2. **GCP upside:** the same compute can be contracted or sold to Anthropic, Meta and other customers, creating immediate revenue, backlog and earnings.

## Leadership change

The article interprets Google's August 5 leadership overhaul as evidence of a failed DeepMind strategy:

- Demis Hassabis is reportedly leaving day-to-day operations.
- Jeff Dean is leaving to start Discovery Loop.
- Sanjay Ghemawat, Quoc Le and Oriol Vinyals are joining him.
- Koray Kavukcuoglu becomes the remaining Gemini leader and replaces Demis operationally.

SemiAnalysis describes Jeff Dean, Sanjay Ghemawat and Quoc Le as among Google's highest-impact technical contributors. It places these departures alongside earlier losses including Noam Shazeer and John Jumper.

The authors' conclusion that DeepMind is "no longer a frontier lab" and has zero probability of returning to SOTA is an opinion, not an established consequence of the organizational changes.

## Why SemiAnalysis thinks Gemini peaked

### Model quality

SemiAnalysis says Gemini 3 Pro was arguably the best model in November 2025, but claims subsequent releases fell behind:

- Gemini 3.5 Flash was weak.
- Gemini 3.5 Pro was allegedly cancelled.
- Gemini 3.6 Flash reportedly trails several US and Chinese models.
- Current Gemini is characterized as eighth or ninth depending on benchmark methodology.
- The authors do not expect Gemini 4 to reverse the decline.

Some of these claims rely on proprietary notes, benchmark snapshots and industry chatter rather than Google disclosures.

### Token-growth deceleration

The article cites Gemini first-party API throughput:

- `1Q26`: `10B → 16B` tokens per minute, or `60%` growth.
- `2Q26`: `16B → 22B` tokens per minute, or `38%` growth.

SemiAnalysis interprets the slower sequential growth as a corresponding slowdown in Gemini first-party API revenue growth.

Token throughput is an input/activity measure. It does not directly reveal revenue, price, margins, user value or model quality.

### Enterprise platform is stronger than Gemini itself

Gemini Enterprise Agent Platform, formerly Vertex, is reportedly performing better because it distributes third-party models such as Claude.

This supports the core distinction:

- first-party Gemini model economics may weaken;
- Google's distribution, compute and cloud economics may strengthen anyway.

## Compute allocation as strategy

The article argues that frontier model progress requires both talent and massive reserved compute. A lab can monetize unused capacity while preserving contractual rights to reclaim it; the authors say Meta and SpaceX follow versions of this model.

Google instead allegedly committed scarce TPU capacity to external customers through long-term contracts that cannot be clawed back for DeepMind.

Key SemiAnalysis estimates:

- More than `20%` of all TPU shipments from `3Q26–4Q27` will be sold directly to Anthropic.
- This excludes hundreds of thousands of TPUs already rented to Anthropic.
- It also excludes further commitments to Anthropic and Meta over the next six quarters.

Google Cloud CEO Thomas Kurian is framed as viewing TPUs as general-purpose infrastructure and GCP as a neutral platform, even when customers compete directly with Gemini.

The leadership overhaul is therefore interpreted as an internal political victory for the cloud monetization strategy.

## Talent flywheel benefits GCP

The article describes a new loop:

1. Top researchers leave Google.
2. They create externally funded "neolabs."
3. Venture and strategic investors supply billions.
4. New labs buy Nvidia GPU or TPU capacity through GCP.
5. Google loses frontier research talent but monetizes their new companies as cloud customers.

Discovery Loop is compared with David Silver's Ineffable Intelligence. The authors see bureaucracy, slow decision-making and fear of disrupting Google's core businesses as the root cause—not any individual DeepMind leader.

## Financial model

### Gemini versus external cloud opportunity

SemiAnalysis estimates:

- Gemini ARR: `$12B` in `2Q26`.
- GCP third-party AI ARR from IaaS/TaaS: more than `$73B` by end-2027.
- TPU system sales: another `$120B` by end-2027.
- Combined external sales opportunity: approximately `$200B` at high-30s EBIT margins.

The comparison is meant to explain management's incentive: monetize external demand now rather than protect a much smaller first-party model business.

### Current GCP growth decomposition

The article says:

- Reported GCP growth in the latest quarter was `82%`.
- TPU system sales contributed an estimated `$1.2B` in `2Q26`.
- Excluding those sales, core GCP growth was in the low `70%` range.
- TPU systems are recognized gross at approximately `$35B/GW`.

The gross accounting treatment matters. Physical system sales can produce very large reported revenue without having the same recurrence, incremental margin or valuation quality as cloud consumption revenue.

### Backlog and forecast

SemiAnalysis estimates:

- More than `$150B` of current TPU-system backlog.
- GCP 2027 growth reaches the mid-`100%` range versus sell-side consensus of `64%`.
- System-sale EBIT margins are in the low `30%` range.
- Total GCP EBIT margins remain mid-to-high `30%`.
- More than `$250B` of additional TPU bookings may enter remaining performance obligations in coming quarters.
- The acceleration adds approximately `$3` to Alphabet's 2027 EPS.

These are proprietary SemiAnalysis estimates, not Alphabet guidance or audited disclosures.

## Investment implications

### Near-term Alphabet bull case

- Scarce compute is monetized immediately at attractive margins.
- Anthropic and other labs absorb large amounts of TPU capacity.
- Gross system sales create unusually rapid GCP revenue growth.
- Backlog and RPO may provide visible forward demand.
- Enterprise distribution can succeed even when Gemini is not the leading model.
- SemiAnalysis's model implies material 2027 EPS upside.

### Medium- and long-term bear case

- Selling capacity to competitors can weaken Gemini's model quality and first-party economics.
- Google may surrender control of the application/model layer while becoming infrastructure underneath rivals.
- Long-term TPU commitments reduce flexibility if DeepMind later needs more compute.
- Talent departures can become self-reinforcing.
- A cloud platform can grow while the strategic value of its first-party AI product erodes.

## What to watch

### Confirming the GCP thesis

- GCP growth accelerating above sell-side expectations.
- TPU system sales disclosed or inferable from revenue mix.
- RPO and backlog expanding through multi-GW customer commitments.
- GCP EBIT margins staying in the mid/high 30s despite hardware mix.
- Anthropic and Meta TPU deployment growth.
- Continued strength in Vertex/Gemini Enterprise through third-party models.
- Alphabet EPS revisions approaching the claimed `$3` uplift for 2027.

### Confirming the Gemini bear case

- Continued senior research departures.
- Gemini model rankings remain outside the frontier.
- First-party token and API-revenue growth continue to decelerate.
- Model launches are delayed, cancelled or framed around smaller bridge releases.
- DeepMind receives insufficient training compute relative to OpenAI and Anthropic.

### Kill tests

- Gemini 4 returns clearly to SOTA across credible, contamination-resistant evaluations.
- New DeepMind leadership rebuilds the RL team and secures frontier-scale compute.
- TPU system backlog is smaller or less firm than estimated.
- Gross system sales carry materially lower margins or create working-capital/capex drag.
- Customers delay deployment, renegotiate contracts or shift to GPUs/Trainium.
- GCP revenue growth decelerates toward consensus rather than the mid-100s forecast.
- TPU sales merely pull forward future cloud economics instead of adding durable earnings.

## Critical caveats

1. **Most important numbers are proprietary estimates.** Alphabet has not validated the `$150B` backlog, `$250B` prospective bookings, `$120B` 2027 TPU sales or `$3` EPS impact in this article.
2. **Revenue quality differs.** Gross hardware/system revenue deserves a different multiple from recurring cloud consumption.
3. **Bookings are not revenue or free cash flow.** Delivery timing, acceptance, financing and cancellation terms matter.
4. **Token growth is not value growth.** Tokens per minute do not reveal realized pricing, margins or customer ROI.
5. **Benchmark rank is unstable.** Model rankings vary by evaluator, task mix, release timing and test methodology.
6. **"Zero odds" is rhetoric.** Google retains substantial capital, infrastructure, distribution and research capacity.
7. **Customer concentration matters.** Large Anthropic/Meta contracts could make growth more dependent on a handful of labs.
8. **Compute monetization may not be irreversible.** Contracts, future TPU generations and new capacity could change internal allocation later.

## My read

The strongest insight is not that Gemini is permanently dead. It is that Alphabet can lose at the frontier-model layer while winning financially at the infrastructure and distribution layers.

The variant perception is potentially material because gross TPU system sales can make GCP growth look dramatically stronger than a standard recurring-cloud model predicts. But that same accounting composition deserves a lower valuation multiple unless backlog converts with sustained margins, cash flow and follow-on consumption.

Near term, the article is bullish Alphabet earnings. Strategically, it is bearish Alphabet's control over the model layer. The key question is whether Google is temporarily renting out excess compute or permanently financing the competitors that will own the highest-value AI relationship.
