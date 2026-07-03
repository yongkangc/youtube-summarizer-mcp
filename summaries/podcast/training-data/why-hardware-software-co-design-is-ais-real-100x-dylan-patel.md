---
title: "Why Hardware-Software Co-Design Is AI's Real 100x: Dylan Patel of SemiAnalysis"
source: "Training Data"
url: "https://www.youtube.com/watch?v=f6D_aiy8qyU"
date: "2026-06-30"
duration: "1:09:46"
speakers:
  - Dylan Patel
  - Shaun Maguire
  - Sonya Huang
---

# Why Hardware-Software Co-Design Is AI's Real 100x: Dylan Patel of SemiAnalysis

Source: [YouTube](https://www.youtube.com/watch?v=f6D_aiy8qyU)

Source quality: YouTube captions. Some names are garbled; numbers were preserved where stable.

## TL;DR

Dylan Patel's core claim is that the next AI infrastructure edge is not a faster chip in isolation. The real leverage comes from co-designing model architecture, software stack, and hardware architecture together.

Investor read: AI bottlenecks keep rotating, but near-term scarce layers are inference compute, power, memory bandwidth, high-quality data-center execution, and the ability to co-design across the full stack. Nvidia remains structurally strong, but the moat is less "CUDA alone" and more ecosystem gravity, supply chain, model-shape compatibility, and a multipolar compute market.

## Main thesis

- Inference could become one of the largest markets in the world, potentially many percentage points of GDP.
- Static inference benchmarks are stale almost immediately because models, kernels, drivers, PyTorch, vLLM, SGLang-like stacks, and serving optimizations change constantly.
- SemiAnalysis built InferenceX to run daily benchmarks across current models, hardware, and configurations.
- Dylan says cost for equivalent model quality has fallen roughly 60x per year; power efficiency has improved closer to 40x.
- The important serving curve is throughput versus interactivity:
  - Slow batch workloads optimize for cost.
  - Interactive coding and agent workflows optimize for latency and may pay much more per token.
- Fast tokens have separate economics. If the human or agent feedback loop is expensive, customers may pay 4x more for speed. If a batch job can run overnight, cost dominates.

## Hardware-software co-design

Dylan argues GPU versus TPU versus ASIC cannot be evaluated in isolation.

- DeepSeek model shapes were optimized for Hopper; later shapes are optimized for Blackwell and Huawei chips.
- TPUs may be excellent for one model family and poor for another.
- OpenAI, Anthropic, and Google likely use meaningfully different model architectures.
- Matrix-multiply unit size, attention layout, expert shape, network topology, collectives, and arithmetic intensity all influence what hardware is best.
- Nvidia NVLink switch domain is around 72 GPUs.
- Google ICI can connect roughly 8,000 TPU chips, but with routing-through-chip tradeoffs because there is no equivalent switch.

Correct question is not "GPU or TPU better?" Correct question: which model and software stack is co-designed for which hardware?

## Nvidia moat, updated

The old lazy version of the Nvidia thesis is CUDA programmability. Dylan's version is sharper:

- CUDA and software moats are partly weakened because AI models can now write kernels and infrastructure software.
- Nvidia still benefits because much of the open model ecosystem is shape-optimized for Nvidia GPUs.
- Downstream inference providers, RL companies, and enterprise customization stacks inherit that Nvidia-optimized model gravity.
- Google's counter would be to open-source strong TPU-native models so external users have a reason to rent or buy TPUs.

Nvidia's moat is no longer just CUDA. It is model-architecture gravity plus supply chain plus ecosystem default status.

## Cerebras, Groq, and SRAM-based chips

Dylan likes fast-token niches but flags the risk.

- Cerebras and Groq can be strong for very fast inference.
- Best use cases are high-value, low-latency tasks: coding loops, agent workflows, and maybe financial trading.
- Risk: frontier models may keep getting much larger and longer-context.
- If models reach 10T+ parameters plus million-token context, SRAM-based chips may struggle.
- Revenue matters more than token volume. Labs make money from the best and most expensive models, not necessarily from the highest-volume cheap tokens.

## Memory and power bottlenecks

- Memory bandwidth is a major technical bottleneck.
- HBM has mostly improved by adding more and faster stacks.
- Next wave may be memory stacked directly on chip, which could materially increase bandwidth.
- Chips have historically sat near 1 watt per square millimeter.
- Dylan mentions current or coming chip power levels:
  - Current high-end chips around 1,400W.
  - Next-generation Nvidia Rubin-like chips around 2,000W.
  - Rubin Ultra-like chips possibly around 4,000W.
- Future improvement may come from pushing more power through silicon, reducing silicon area, and solving thermal or electrical-interference issues.
- Energy bottlenecks may be less impossible than consensus if practical generation hacks work, including natural-gas or converted diesel-engine generator approaches.

## Space data centers

Dylan's view is time-horizon dependent:

- Next 3 to 5 years: space data centers are basically irrelevant.
- By 2030: likely below 1% of inference compute.
- By 2040: possibly more than half of incremental compute goes to space.

Reason: if inference demand reaches terawatt scale, terrestrial power constraints become dominant.

He forecasts OpenAI and Anthropic together could exceed 100GW by 2030. That is the big aggressive assumption in the episode.

## Data-center economics

Most investable section.

- Trainium rental rate to Anthropic/OpenAI-like customers: below $10B per GW per year.
- GPU rental rate before the latest tightness: around $12B to $13B per GW per year.
- SpaceX/Google GPU deal mentioned around $25B per GW per year, or $25M per MW per year.
- Colocation/data-center pricing:
  - Old: around $60 per kW per month.
  - Current common range: around $120 to $160 per kW per month.
  - High-quality site with weaker-credit customer: up to around $200 per kW per month.
  - Weaker geographies or lower-quality sites: around $80 to $100 per kW per month.

Dylan says many data-center failures are not subtle. Weak teams get delayed, delayed again, then fail.

Important operator edge: Google can put roughly 1.5GW of hardware behind 1GW of utility capacity because it understands workload and power management deeply. Utilities may allow customers to draw 2GW most days if they can curtail on peak days. That requires batteries, gas, backup generation, workload control, and operational excellence.

## Compute glut risk

Dylan acknowledges the risk but thinks the current tide still favors buildout.

- Model capability and addressable work are expanding faster than compute supply.
- Every added GPU, TPU, or Trainium unit can still produce gross profit.
- If model progress stalls, compute pricing can break.
- People inside OpenAI and Anthropic still appear to believe model progress has line of sight.
- Models now help build the next model infrastructure, creating a pseudo-recursive engineering-velocity loop.

## Jensen's chess move

Dylan's Nvidia strategy read:

- Jensen wants a multipolar AI world.
- Bad world for Nvidia: only OpenAI, Anthropic, and Google models, with hyperscaler-owned compute dominating inference.
- Good world for Nvidia: many model labs, neoclouds, open ecosystems, and many GPU buyers.
- Nvidia backs labs and neoclouds because CoreWeave, Crusoe, and similar players weaken Google TPU and Amazon Trainium's strategic leverage.
- Many neoclouds and neolabs will fail, but enough survivors can become structurally important.

## Structural edge claim

The market pays for AI infrastructure exposure because model capability is expanding monetizable demand faster than compute and power supply can come online.

Edge sits with players that control scarce bottlenecks and execute faster:

- Accelerators.
- Memory bandwidth.
- Networking and optical interconnect.
- Power access.
- Data-center build speed.
- Full-stack model-hardware co-design.

## Investor read-through

- Nvidia: still strongest, but thesis should be ecosystem/model-shape gravity plus supply chain plus multipolar-market strategy, not CUDA-only moat.
- Google TPU: real contender where models are co-designed around TPU. Needs stronger open-source TPU-native ecosystem to pull outside demand.
- Amazon Trainium: not a toy. Anthropic involvement may make it genuinely useful; lower dollar-per-GW could be strategic.
- Memory/HBM/advanced packaging: central bottleneck. Watch direct memory-on-chip and bandwidth innovations.
- Optical/networking: co-packaged optics likely by late decade; timing matters materially for stock outcomes.
- Neoclouds: binary execution game. Winners have speed, power, and customer demand; losers drown in delays and leverage.
- Power/data centers: not every GW is equal. Better workload and power management makes the same grid allocation more valuable.
- ASIC startups: only compelling if they co-design silicon, software abstraction, and model layer. Chip-only startups likely fail.

## Kill tests

- Model progress slows, causing compute prices to break.
- Best models become too large or too long-context for SRAM/fast-token niche chips.
- Hyperscaler custom silicon captures too much inference share.
- Power and data-center bottlenecks ease faster than expected, compressing scarcity premiums.
- Open-source model ecosystem shifts away from Nvidia-optimized shapes.

## One-line summary

Dylan's AI-infra alpha is not "buy the fastest chip"; it is underwriting which bottleneck gets paid as model architecture, software, hardware, power, and supply chain co-evolve.
