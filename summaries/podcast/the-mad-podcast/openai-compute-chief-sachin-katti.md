---
title: "OpenAI's Compute Chief: We Can't Build Fast Enough"
source: "https://open.spotify.com/episode/6ICX16Sv77eh7hZCMNm6Xt"
spotify_episode_id: "6ICX16Sv77eh7hZCMNm6Xt"
show: "The MAD Podcast with Matt Turck"
host: "Matt Turck"
guest: "Sachin Katti"
published: "2026-07-16"
duration_seconds: 2636
date_summarized: "2026-08-10"
transcript_source: "Full RSS audio enclosure transcribed locally with Whisper tiny.en. ASR quality was adequate for thematic and mechanistic coverage; uncertain proper nouns and host-supplied figures are not treated as verified facts."
---

# OpenAI's Compute Chief: We Can't Build Fast Enough | Sachin Katti

Source: [Spotify](https://open.spotify.com/episode/6ICX16Sv77eh7hZCMNm6Xt)

## Source notes

- Spotify episode resolved to *The MAD Podcast with Matt Turck*.
- Guest: Sachin Katti, OpenAI Head of Industrial Compute; formerly Stanford professor, startup founder, and Intel CTO.
- RSS feed exposed the complete 43:56 MP3. I downloaded and transcribed all 2,636 seconds locally.
- Claims are Katti/OpenAI claims unless independently identified otherwise. This is a strategic interview, not audited capacity or financial disclosure.

## TLDR

OpenAI sees compute scarcity, not overbuild, as the binding risk. It is becoming an industrial infrastructure operator: securing land, power, shells, chips, networking, financing, and operations across hyperscalers, neoclouds, chip partners, and self-designed systems. The durable metric is moving from GPU count to **tokens per watt**, while the bottleneck rotates outward from accelerators into power generation, transformers, cooling, networking reliability, permitting, and skilled trades.

## Core architecture

### AI data centers are factories converting electrons into tokens

Katti describes modern AI sites as giant, tightly coupled supercomputers rather than ordinary cloud data centers.

- Scale is the main difference.
- Accelerators, network links, cables, transformers, and power equipment all generate heat.
- Air cooling is insufficient for the densest systems; liquid cooling extends from chips into broader system infrastructure.
- Better heat transfer lets chips run harder, improving memory bandwidth and compute throughput.
- Cooling innovation is therefore economically coupled to intelligence output, not just facility efficiency.

The useful output metric is not installed GPU count. It is **tokens delivered per watt**, adjusted for workload, reliability, and utilization.

### Power stack

OpenAI says it prefers grid-connected power but increasingly funds the infrastructure required to add load:

- New generation.
- Transmission.
- Transformers.
- Substations.
- Local distribution.

Katti claims OpenAI commits not to take existing power away from communities and instead funds incremental supply. Treat that as company framing requiring local project-level verification.

Where grids cannot add capacity quickly enough, the company considers **behind-the-meter generation**. In the US, the practical current answer is often gas turbines because natural gas is dense, transportable, and available.

He is strongly positive on nuclear: dense, clean, scalable energy that `can't come soon enough`, but notes most countries have substantial execution catch-up.

## Project Jalapeño: OpenAI custom silicon

Why OpenAI wants its own chips:

- Inference is now a very large, perhaps majority, share of compute.
- Training itself increasingly contains inference: synthetic-data generation, post-training, and evaluation/testing.
- OpenAI knows its future model/workload better than a general merchant-chip vendor.
- Model/hardware co-design can eliminate unnecessary generality and maximize tokens per watt.

Katti says Jalapeño went from design to tape-out in roughly **nine months**, unusually fast. Reasons he gives:

- Experienced team, including people who previously designed Google TPUs.
- Broadcom partnership and ASIC delivery capability.
- OpenAI's visibility into future model requirements.
- AI tools accelerating design-space exploration and optimization.

He expects recursive co-design: AI increasingly helping design the chips and systems used to train the next AI generation.

## Why OpenAI rejects the overbuild thesis

Katti's position:

- Demand currently outstrips compute supply.
- New capacity is consumed immediately.
- Research scaling continues.
- AI-assisted research expands experiment count beyond the human-researcher bottleneck.
- Every time OpenAI thought it could slow compute acquisition, it later regretted it.

Thus his feared surprise is **failure to commission enough compute**, not stranded capacity. The physical world moves more slowly than model demand: factories, permitting, generation, transmission, skilled labor, and supply chains cannot compound at software speed.

This is OpenAI's operating thesis, not independent proof that industry-wide returns on capital will be attractive.

## Industrial compute as a capability

Katti's organization manages the full compute lifecycle:

1. Forecast workload, chip type, location, and capacity needs.
2. Source land, power, buildings/shells, accelerators, and networking.
3. Structure financing for real estate, facilities, and chips.
4. Commission and operate the infrastructure reliably.
5. Allocate scarce capacity across research, training, and products.

Capacity is multidimensional: not merely `more compute`, but where it is, which chip, interconnect topology, and which workloads it can serve.

## Portfolio strategy and Stargate

OpenAI avoids one sourcing channel. Katti describes a portfolio spanning:

- Microsoft.
- AWS.
- Google.
- Neoclouds such as CoreWeave.
- Chip partners supplying systems.
- Design/build partners.
- Increasing OpenAI participation in designing, operating, or potentially building systems directly.

He frames **Stargate** as an evolving umbrella for OpenAI taking greater control over compute design and delivery, not one static joint venture.

Examples discussed:

- Oracle facilities, including Abilene and additional US sites.
- SoftBank collaboration on facility shells and energy.
- OpenAI deploying or operating its own chips in partner-built sites.

On financing, Katti says OpenAI generally acts as the committed tenant/compute buyer while partners finance and own the infrastructure. That shifts upfront capex away from OpenAI but leaves it with potentially large long-duration purchase commitments.

## Networking: MRC and 100,000-GPU reliability

At 100,000-GPU scale, link, switch, NIC, and routing failures are normal rather than exceptional. A training job cannot depend on every component remaining healthy.

Katti describes MRC as a multipath routing approach:

- Traffic can be sprayed across multiple routes.
- The network masks individual failures.
- Training sees a reliable abstraction rather than stopping for every broken path.
- Goal: availability and graceful degradation at extreme cluster scale.

The moat is therefore not chips alone. Useful compute requires resilient fabrics, schedulers, operations, and model-aware system design.

## Current physical bottlenecks

Katti says there is no single bottleneck. Scarcity rotates through:

- Permitting and suitable land.
- Grid interconnection and generation.
- Gas turbines.
- Transformers.
- Transmission/substations.
- Liquid cooling.
- Networking and reliability.
- Electricians, plumbers, construction labor, and other skilled trades.

Manufacturing capacity for turbines and transformers was not built for the abrupt demand shock; adding factories takes years. Skilled trades may become more constrained as every lab and hyperscaler builds simultaneously.

## Data-center community claims

Katti argues rural data centers create:

- Property-tax revenue.
- School and hospital funding.
- New grid investment.
- Construction and skilled-trade jobs.

On water, he says liquid-cooling loops recycle water and net consumption is much lower than commonly portrayed.

Caveat: those statements are broad company claims. Water use depends materially on cooling architecture, climate, evaporative losses, power-generation water, and whether reported metrics count withdrawals versus consumption. Local tax subsidies, electricity pricing, emissions, and long-term operating employment also require site-specific diligence.

Site-selection factors:

- Plentiful, remote land.
- Fast permitting.
- Strong grid and gas access.
- Available construction labor, electricians, and plumbers.

Texas scores well across these dimensions, but OpenAI is building across multiple US states.

## Guaranteed capacity: intelligence as a contracted supply unit

OpenAI is offering enterprises guaranteed capacity, which Katti equates with reserved dollars/tokens of intelligence.

His thesis:

- Intelligence becomes a critical enterprise input.
- Compute scarcity makes token availability uncertain.
- Enterprises may contract forward to avoid supply disruption.

This begins to resemble cloud reserved instances, take-or-pay energy capacity, or industrial commodity offtake. It can finance infrastructure and lock in demand, but may also create minimum-commitment and pricing risks for customers if token costs fall rapidly.

## Space data centers

Katti expects orbital compute to become technically feasible and perhaps one component of supply, not the dominant solution. Preconditions:

- Much cheaper launch.
- Hardware cheap enough to discard when it fails.
- Economics that compensate for repair difficulty and orbital constraints.

He treats it as plausible engineering, not a near-term primary plan.

## Investor read-through

### Theory of edge

The market may pay investors who identify the **next binding physical constraint** before headline AI demand translates into vendor backlog and margins. The edge is bottleneck underwriting, not simply buying all AI exposure.

### Potential beneficiaries

- Fast, incremental power: gas turbines, generation developers, grid equipment.
- Transformers, switchgear, transmission, and substations.
- Direct liquid cooling, pumps, heat exchangers, and thermal materials.
- Broadcom/custom ASIC ecosystem and advanced packaging.
- High-availability networking, optical/copper interconnect, NICs, and switches.
- Engineering/construction firms and scarce skilled labor.
- Hyperscalers/neoclouds able to finance and commission capacity quickly.

### Strategic implications

- OpenAI is vertically integrating into workload-aware silicon and systems, potentially reducing dependence on any single GPU supplier at inference.
- Nvidia's risk is not immediate demand loss; it is long-run workload-specific substitution if custom silicon materially wins tokens per watt.
- Broadcom gains from hyperscaler/frontier-lab ASIC proliferation.
- Power and commissioning speed may be more defensible bottlenecks than nominal chip orders.
- Tenant-backed infrastructure financing can accelerate deployment while obscuring economic leverage in long-term purchase commitments.

## Risks and kill tests

- **Promotional bias:** OpenAI benefits from persuading investors, suppliers, governments, and communities that scarcity is permanent.
- **Demand elasticity fails:** token demand may not absorb capacity if applications cannot monetize inference.
- **Efficiency outruns demand:** model compression, routing, quantization, better utilization, and custom silicon could reduce power per useful task faster than workload expands.
- **Partner-credit risk:** infrastructure owners depend on OpenAI/hyperscaler offtake and financing durability.
- **Orphaned assets:** workload/chip architecture may change faster than facilities and power contracts.
- **Local opposition:** permitting, power prices, emissions, water, subsidies, or community resistance can slow projects.
- **Custom-chip execution:** nine-month tape-out does not prove yield, software readiness, production ramp, reliability, or superior lifecycle economics.
- **Overbuild evidence:** falling accelerator rental prices, rising idle capacity, delayed/cancelled sites, weaker reserved-capacity pricing, and poor partner ROIC would invalidate the scarcity thesis.

## KPIs to track

- Commissioned megawatts, not announced gigawatts.
- Time from land/power agreement to productive tokens.
- Tokens per watt and tokens per dollar by workload.
- Utilization and reserved-capacity pricing.
- OpenAI inference demand and enterprise contract conversion.
- Transformer/turbine lead times and supplier backlog conversion.
- Jalapeño production yield, software support, deployment volume, and cost advantage.
- Partner capex, debt, take-or-pay commitments, and return on invested capital.
- Local electricity prices, subsidies, water consumption, and emissions.

## Bottom line

OpenAI's compute thesis is Jevons-style: efficiency and AI-assisted research create more experiments and more token demand, so useful compute remains scarce. The investable question is not whether AI uses more compute; it is **which layer constrains commissioned, reliable tokens next, who captures scarcity rent, and whether customer revenue ultimately covers the enormous physical capital bill**.
