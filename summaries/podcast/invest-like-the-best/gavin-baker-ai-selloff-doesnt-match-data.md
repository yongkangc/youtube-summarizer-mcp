---
title: "Gavin Baker: The AI Selloff Doesn't Match the Data"
source: "https://www.youtube.com/watch?v=NGsi2PC4y68"
video_id: "NGsi2PC4y68"
channel: "Invest Like The Best"
host: "Patrick O'Shaughnessy"
guest: "Gavin Baker"
upload_date: "2026-08-04"
date_summarized: "2026-08-04"
duration: "1:18:44"
tags:
  - artificial-intelligence
  - semiconductors
  - nvidia
  - memory
  - compute
  - investing
---

# Gavin Baker: The AI Selloff Doesn't Match the Data

[YouTube](https://www.youtube.com/watch?v=NGsi2PC4y68)

## Source note

Complete auto-generated transcript reviewed in contiguous fixed windows. Interview contains many forward-looking, private-market and anecdotal claims. Numbers below are Baker's claims unless independently stated otherwise. Several future model/company names may be imperfectly captioned.

## TL;DR

Gavin Baker argues July 2026's 40–60% AI-stock selloff resembled “2022 in a month,” but observable AI demand kept accelerating: GPU availability remained tight, rental prices rose, DRAM strengthened and token volume expanded. His structural edge thesis is that markets see public capex but miss private-lab and open-source revenues, while old compute contracts are materially below spot and should reprice upward.

The real risk is financing. If compute revenue and hyperscaler operating cash flow fail to catch capex, debt funding plus higher real yields could create classic capital-cycle unwind. Other kill tests: sustained GPU-price decline, falling aggregate lab/open-source usage, regulatory constraints and a discontinuity from sample-efficient continual learning.

## Why market sold off

Baker reconstructs a sequence of bearish interpretations:

1. **Meta renting compute** was read as excess capacity and looming capex cuts. He says Meta did not cut capex and argues it was testing monetization at spot-market premiums.
2. **Open-source models gained share** while a token-revenue index flattened. Market read this as weaker demand; Baker sees margin shifting from frontier labs toward lower-price tokens, not reduced compute use.
3. **China reportedly developed a DUV lithography tool**, triggering semicap selling. Baker considers this strategically meaningful but potentially decades behind leading EUV capability.
4. **Real yields, credit spreads and CDS rose.** This is the substantive concern because debt-financed buildouts can unwind quickly when supply exceeds demand.
5. **Fast systematic/AI-mediated trading** compressed narrative cycles. He claims capacitor stocks completed what might historically be a three-year boom/bust cycle in six weeks.

## Quantitative evidence cited

Baker says every demand lens he checked accelerated:

- GPU availability remained scarce;
- GPU rental pricing rose;
- DRAM spot prices increased;
- token growth accelerated;
- OpenAI and open-source inference clouds grew rapidly;
- Anthropic continued strong growth, though third-party data may show some trajectory softening.

He says operating cash-flow growth for Microsoft, Meta and Amazon accelerated from **28% to 32%**, or **35% excluding unusual one-time items**. Exact calculation and company aggregation are not independently documented in interview.

A startup reportedly rented several thousand B200 GPUs around the mid-**$2/GPU-hour** range, then expected to pay just under **$4/GPU-hour** seven months later: roughly **50–60%** increase. Another inference-cloud operator reportedly expected Blackwell rental expense to double when contract renewed. These are private anecdotes, not audited market series.

At recording, Baker says Nvidia traded at its lowest forward P/E in ten years, implying market expects significant overearning. This requires current valuation verification before use.

## Core compute-repricing thesis

During 2024–25, buyers signed long-term GPU contracts expecting hardware rental prices to decline. Instead, Baker says old GPU prices rose in 2026. Installed contracted compute therefore trades below spot.

Mechanism:

`contracts roll off → compute reprices toward spot → cloud operating cash flow rises → internal funding covers more capex → credit risk falls`

He says consensus effectively values future Blackwell and Rubin gigawatts at Ampere-era monetization. He contrasts approximately **$1.3–1.4T** hyperscaler operating cash flow under that framing with around **$2T** if new capacity monetizes below current Blackwell rates, potentially removing **$700B** of credit demand. These are model outputs, not verified forecasts.

### Why market may be missing it

Public investors see hyperscaler and semiconductor capex clearly but have less visibility into:

- Anthropic;
- OpenAI;
- open-source inference providers such as Fireworks, Baseten, Modal and Together;
- private AI-native customer usage;
- contract-versus-spot GPU economics.

Baker calls open source “dark matter” for public markets.

## Open source is not necessarily bearish for infrastructure

Baker separates model-layer margin from physical compute.

He claims frontier tokens may carry approximately **80–95%** inference margins versus perhaps **30%** for open-source tokens. A router can use customized open-source model first and frontier model for planning/checking, producing similar or better results at perhaps half user cost.

His mechanism:

`lower model margin → cheaper tokens → more token consumption → similar/more GPU-hours → infrastructure captures larger share`

A company's AI bill may stabilize while its physical compute use rises because it substitutes cheaper tokens and increases volume.

Caveat: “a token is a token” is directionally useful but technically imprecise. Compute/token varies with model size, architecture, context length, batching, quantization, sparsity, hardware utilization, cache hits and speculative decoding. Lower-priced tokens do not automatically require equal FLOPs or watts.

## Multi-model stack and software moat

Baker expects AI-native applications to combine:

- proprietary customer/task data;
- supervised fine-tuning or RL on an open model;
- router selecting specialized model;
- frontier model used for planning, orchestration or verification.

This can reduce dependence on single frontier vendor and make “wrapper” companies more defensible. He cites Fireworks' Nexus as example and says some firms moved frontier models to only **30–60%** of token use.

He thinks open-source models could process majority of tokens while frontier models retain majority of economic value, analogous to highly paid CEO orchestrating larger workforce. Cheap competent models may increase value of scarce frontier intelligence that coordinates them.

## Demand ceiling: knowledge work

Baker frames ultimate compute demand against approximately **$25T** of knowledge work. If token spend reached 20% of compensation, that represents **$5T**, funded through either labor substitution or faster growth.

He cites AI-forward companies spending approximately **20–25%** of compensation-equivalent on tokens, with anecdotes at **30%** and **50%**. Attribution and denominator are not standardized.

He prefers growth outcome: people plus AI create more output rather than mass layoffs. He notes founder-controlled companies have not broadly conducted major AI-driven layoffs after adjusting for prior overhiring, and AI-heavy companies appear to grow faster. He acknowledges cited indices may not control adequately for industry selection.

Adoption remains tiny in his framing: perhaps **250K–500K** people use agentic AI while compute is already scarce. Moving toward 100M or 500M users would create enormous demand, but user count and intensity are not independently verified.

## Memory as strategic bottleneck

Baker argues memory per unit of compute is critical to token throughput. Memory manufacturers are trading short-term pricing upside for long-term agreements (LTAs), often with prepayment and price floors/ceilings.

Game theory:

- accelerator market includes Nvidia, AMD, Google TPU and Amazon Trainium plus startups;
- supply allocation may determine market share;
- customer breaking LTA during oversupply risks losing allocation in next shortage;
- cyclicality makes relationship durability strategically valuable;
- suppliers accept capped upside in exchange for visibility and customer commitment.

His conclusion: LTAs can structurally reduce memory cyclicality and improve durability. But they do not abolish cycles; actual terms, take-or-pay provisions, customer concentration, capacity additions and technology transitions matter.

## Nvidia's expanding economic role

Baker sees Nvidia doing more than selling chips:

- GPUs remain easiest accelerator assets to finance;
- Nvidia helps match power, land, capital and operators;
- equity investments create upside in ecosystem growth;
- credit-wrapper structures may include revenue share above GPU-price floor;
- royalties can convert financing support into recurring cloud-like revenue;
- ecosystem support strengthens Nvidia's competitive position.

He explicitly says this is not classic vendor financing when third parties lend to GPU buyers, though fungibility means Nvidia equity capital still supports broader enterprise funding.

His suggested memory-company analogue: contribute capital to infrastructure deal in exchange for ongoing revenue share, extending LTA logic from durability toward royalty participation.

Caveat: interview does not provide contract documents, exposure, counterparty risk, accounting treatment or realized returns. Nvidia ecosystem investments could amplify losses if compute prices fall.

## Capital-allocation game theory

Baker argues labs cannot easily slow compute purchasing:

- buy too much and risk bankruptcy;
- buy too little and lose frontier position;
- rivals that secured compute regained model competitiveness;
- observing this makes every lab less willing to cut capacity.

This is an arms-race mechanism sustaining demand even before near-term financial ROI is proven. It is also risk: strategic overbuying can create industry-wide oversupply.

## China lithography

Baker treats reported Chinese DUV progress as a phase transition: indigenous capability exists where previously absent. Yet he analogizes it to technology perhaps 25 years behind EUV and says learning-by-doing cannot be teleported.

Balanced view:

- strategically significant;
- probably overreacted to in near-term Western semicap stocks;
- could affect ASML orders only years later;
- information from China is difficult to verify;
- US-China decoupling is becoming self-reinforcing.

He mentions unverified reports of smuggled EUV equipment and explicitly says he does not know whether true.

## Data-center politics and regulation

Baker calls regulation largest obvious AI risk, citing proposed data-center moratoria and poor industry communication.

He argues modern data-center agreements can:

- finance behind-the-meter generation;
- lower local power bills;
- fund community infrastructure;
- create ongoing electrical, plumbing, HVAC and maintenance work;
- support medical/scientific progress.

He says a widely repeated water-use estimate was wrong by **10,000×** and argues environmental/water effects are often overstated. This segment is advocacy. Claims that data centers “almost certainly” lower power bills or have “no impact” on water/environment are too broad and require project-specific evidence. Grid upgrades, rate design, generation mix, cooling design and water basin determine outcome.

## Inference architecture and SRAM

Baker sees opportunity in disaggregating inference:

- prefill on one accelerator;
- attention on HBM-heavy accelerator;
- feed-forward network on SRAM-based accelerator built on older nodes.

He argues SRAM can improve feed-forward performance and avoid some HBM/leading-node constraints. Flexible disaggregation may adapt better than fixed on-chip memory/compute ratio.

Caveat: this is architectural thesis, not benchmark. Interview gives no model, interconnect, latency, power, utilization, batch, precision or cost data. Data movement between accelerators may erase theoretical gains.

## SpaceX and orbital compute

Baker views SpaceX increasingly as compute company. He says it brought capacity online faster and cheaper than peers, while market absorbed new supply without visible price shock.

He discusses a public report that SpaceX might add **8 GW** in around 18 months, but repeatedly calls that implausible and says he does not expect anywhere near eight. Other claims:

- compute monetization around **$50B/GW**;
- consensus next-year estimate around **$73B**;
- Grok, Cursor and related activity might reach **$10B ARR** quickly;
- only hyperscalers, CoreWeave, Crusoe and SpaceX have added over **500 MW** in one year;
- orbital compute feels increasingly plausible;
- Benchmark's StarCloud investment offers outside validation.

These are speculative and partly based on unnamed/public secondary reports. Investment by smart VCs is not technical validation. Orbital compute must overcome launch economics, radiation, heat rejection, maintenance, networking and hardware-refresh constraints.

## Theory of edge

**Why market would pay this trade:** public equities may be pricing an AI capex bust using visible spending and lower model-layer prices, while missing private token demand, contract-to-spot compute repricing, infrastructure scarcity and operating-cash-flow acceleration.

Expression implicit in interview: own repriced AI infrastructure and scarce memory/power/networking assets when market assumes overearning.

This is an information-interpretation edge, not unique information. Many inputs are private anecdotes and may already be reflected in positioning.

## Kill tests

Baker gives or implies concrete falsifiers:

1. Hyperscaler operating cash flow stops accelerating.
2. Aggregate OpenAI + Anthropic + open-source usage plateaus or declines.
3. GPU rental prices fall materially and remain depressed.
4. GPU availability becomes easy and customers report excess inventory.
5. Compute repricing fails as contracts roll off.
6. Capex becomes dependent on debt while real yields/spreads remain elevated.
7. Long-term memory agreements are broken or capacity additions overwhelm demand.
8. Sample-efficient continual learning sharply reduces training requirements without enough inference elasticity.
9. Regulation delays power/data-center deployment.
10. Frontier model economics compress faster than token demand expands.

## What to monitor

- B200/Blackwell spot and contracted $/GPU-hour;
- old-GPU rental curves;
- hyperscaler operating cash flow versus capex;
- net debt, CDS and bond spreads;
- token volumes by frontier versus open-source provider;
- inference-cloud revenue, gross margin and utilization;
- HBM/DRAM contract duration, prepayment and price bands;
- memory supply growth and customer allocations;
- energized GW versus announced GW;
- power connection delays;
- Nvidia ecosystem investment/revenue-share disclosures;
- model routing mix and cost per successful task;
- local data-center rate/water outcomes;
- regulatory moratoria.

## Bottom line

Baker's bull case is internally coherent: compute demand and monetization are improving faster than public markets can observe, while contract repricing could convert capex into enough operating cash flow to avoid debt-led bust. Strongest evidence is physical scarcity and rental repricing. Weakest links are extrapolation from private anecdotes, coarse token-equals-compute reasoning, aggressive operating-cash-flow models and speculative SpaceX/orbital claims. Correct posture: bullish only while cash flow, utilization and executable compute prices confirm.