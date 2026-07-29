---
title: "You Kaichao: vLLM, Open-Source Infrastructure and Model Co-Design"
source: "https://www.youtube.com/watch?v=ifniRXf467I"
video_id: "ifniRXf467I"
channel: "Zhang Xiaojun Podcast"
speakers: ["You Kaichao", "Zhang Xiaojun"]
published: "2026-07-28"
duration: "2:59:03"
date_summarized: "2026-07-29"
category: "ai"
---

# You Kaichao: vLLM, Open-Source Infrastructure and Model Co-Design

## TLDR

You Kaichao, vLLM maintainer and Inferact co-founder/chief scientist, argues AI progress has moved from isolated algorithm novelty toward **systems, hardware and model co-design**. An algorithm survives only if hardware and software can execute it efficiently.

vLLM's original PagedAttention idea was simple: manage KV cache like virtual memory pages. Its durable value became much broader—absorbing complexity across hundreds of model architectures, accelerators and workloads behind one open inference layer.

Inferact's commercial edge is not selling engineer-hours. It wants to charge against value created: more tokens per machine and lower inference cost. Its moat is community legitimacy, technical leadership, pre-release access to new models/hardware and position as neutral coordinator across competing vendors.

Open-source dominance and “Linux of AI inference” remain founder theses, not established outcomes. Monetization, competition, cluster-scale performance and customer conversion still need proof.

## Source context

- Full manually created English transcript read: `5,066` segments.
- Interview language/subtitles may contain translation errors.
- Company descriptions and investment numbers are speaker/host claims unless independently evidenced.
- Host states Inferact raised a `$150M` seed round earlier in 2026.

## 1. Why You moved from algorithms to systems `[02:18–37:56]`

Three reasons:

1. **Academic incentive decay.** He became disillusioned with paper-review novelty games.
2. **Scale dominates small algorithm tweaks.** A `1–2%` method improvement could be erased next year by replacing base model with larger pre-trained model.
3. **Algorithms depend on systems.** Large experiments, data pipelines, kernels, caches and hardware adaptation often determine whether an idea works.

His systems metric became:

- how many people use software;
- measured speed/cost improvement;
- reproducibility;
- direct user feedback.

He contrasts “accuracy improved 2% in one setting” against “system is 2× faster for understandable reasons.” Systems gave clearer cumulative feedback.

Career lesson: work at layer where contribution is measurable and deployable, not where scarce compute/resources prevent proving idea.

## 2. Birth of vLLM `[37:56–55:00]`

vLLM began around 2022–23 as UC Berkeley research project under Ion Stoica. Original paper introduced **PagedAttention**.

### PagedAttention

Autoregressive generation stores keys and values for prior tokens in KV cache. Sequence lengths vary, creating allocation waste/fragmentation.

PagedAttention borrows operating-system virtual-memory design:

- divide KV cache into blocks/pages;
- map logical token positions to non-contiguous physical blocks;
- allocate on demand;
- share/cache prefixes more flexibly;
- reduce memory waste and increase concurrent sequences.

You calls idea simple and low-novelty. SOSP reviewers criticized simplicity; paper survived because team built early and ran extensive reproducible experiments.

Core lesson:

> Timely, complete execution of obvious idea can matter more than academic novelty.

### vLLM became more than paper

Modern vLLM includes:

- PagedAttention;
- continuous batching;
- request scheduling;
- model/hardware abstractions;
- distributed serving;
- quantization/operators;
- speculative decoding;
- prefix caching;
- support for changing attention/state architectures.

Value is not one algorithm. Value is maintained integration surface.

## 3. From prototype to production `[50:00–67:00]`

### 2024: V0 → V1 refactor

Prototype needed production architecture while preserving user-facing compatibility. Models and hardware changed underneath; users still expected same deployment API.

You describes vLLM as always refactoring because it shields users from:

- new model architectures;
- new attention types;
- new chips;
- changing kernels;
- distributed-cluster requirements.

### 2025: cluster scale and Chinese models

Open-model center shifted toward China with DeepSeek V3/R1 and others. You returned to China and built local community/relationships through Chinese-language channels and direct company visits.

DeepSeek had used vLLM internally and added extensive optimization. vLLM maintainers then learned from DeepSeek's stronger production infra.

Maintainer constraint changed from single GPU/server to clusters. Volunteer project lacked:

- stable full-time staff;
- large clusters;
- legal entity for NDAs;
- procurement/contracting capability;
- predictable access to pre-release models/hardware.

This forced company formation.

## 4. Open-source governance `[60:00–95:00]`

vLLM became top-level PyTorch Foundation project. Foundation owns trademark/governance shell and guarantees continued open-source status. It does not make normal technical decisions.

Governance tiers:

- several “benevolent dictators” with final call;
- roughly dozen core maintainers;
- several dozen committers;
- wider contributor/user community;
- corporate contributors including NVIDIA, AMD, Red Hat and cloud vendors.

Examples of hard prioritization:

- removed Beam Search because maintenance complexity no longer matched main LLM workload;
- deprioritized tiny recommendation models;
- prioritized large models, clusters and mainstream hardware/workloads.

### AI-generated contribution problem

Speaker says vLLM ranked most active GitHub project by contributor activity in 2025 and had `2,000+` contributors.

Coding agents made code cheap but review scarce. Problems:

- resume-padding PRs;
- bots submitting many low-context patches;
- maintainers drowning in “AI slop.”

Likely community evolution:

- users provide bug reports, traces and feature needs;
- trusted maintainers/institutions supply architecture/context;
- coding agents implement;
- human maintainers own direction and long-term coherence.

Lesson: when code generation commoditizes, **problem selection, context and trusted review** become scarce.

## 5. Why company became necessary `[90:00–112:00]`

Ion Stoica's argument: major open-source infrastructure eventually needs dedicated company—Linux/Red Hat, Spark/Databricks, PyTorch/Meta, Kubernetes/Google.

Large incumbent alone is poor neutral steward because:

- existing product/hardware bias;
- competitors resist control;
- internal priorities override community;
- volunteer support remains peripheral.

Independent founder-led company can coordinate rivals while funding shared layer.

### Founder sacrifice claims

- founders reportedly rejected lucrative jobs;
- Woosuk Kim considered xAI, Thinking Machines and Google DeepMind opportunities;
- speaker claims top tech company offered four founders `$20M annual salary each` to join instead;
- they chose vLLM because project failure would create lifelong regret.

These are interview claims, not independently audited.

### Inferact state

- `$150M` seed round, per host;
- around `30–40` employees;
- demand for investment allegedly exceeded amount accepted;
- founders say customer demand exceeds support capacity.

Company wants fundraising to follow milestones, not capital availability.

## 6. Business model

Target: pay-per-use/value model—not consulting.

Value proposition:

`more useful tokens per GPU-hour + lower cost/machine + faster model/hardware support`

Potential products/services implied:

- managed/hosted inference;
- enterprise deployment/support;
- strategic co-optimization;
- cluster-scale orchestration;
- rapid pre-release model/hardware enablement.

Company says it rejects customers whose requests conflict with community direction.

## 7. Model–infrastructure co-design `[112:56–135:00]`

Analogy:

- hardware = wind/water/solar resource;
- model = generator;
- inference engine = grid delivering tokens.

Generator must fit resource conditions. Model architecture sets performance ceiling; system cannot rescue architecture hostile to available hardware.

### Hardware lottery

Moore's Law no longer gives broad automatic speedups. Accelerators specialize around matrix multiplication. Algorithms that map cleanly onto those units survive.

Examples:

- Transformer won GPU lottery through parallel matrix multiplication.
- Capsule Networks lacked GPU-friendly implementation.
- RoPE paired cleanly with FlashAttention because it can be applied outside attention kernel; alternatives requiring kernel modification lost ecosystem momentum.

Best organization: algorithm and infra teams co-located, understanding each other's constraints. Too much infra control can damage model quality; too much algorithm control creates unservable designs.

## 8. Speculative decoding

Autoregressive decoding normally generates one token at a time. Speculative decoding guesses several tokens, then target model verifies them together.

Speaker discusses:

- Eagle/MTP: shorter `3–5` token guesses, higher acceptance;
- DFlash family: guesses around `16` tokens; higher parallelism, more rejected work;
- DSpark: predicts which guesses are unreliable and skips verifying them;
- vLLM/NVIDIA DFlash implementation reportedly exceeds `1,000 tokens/s` on some models/configurations.

Caveat: no model, hardware, quality or benchmark setup supplied in interview. Number is not general serving throughput.

Core economics:

`speedup = accepted tokens per verification / added draft + verification cost`

## 9. MoE challenges `[135:00–145:00]`

Three main problems:

1. **Fine-grained experts:** small GEMMs underutilize GPU.
2. **Dynamic routing:** token-dependent data flow is harder than static GPU computation.
3. **Expert parallelism:** trillion-parameter sparse models require heavy communication and load balancing.

DeepSeek contributions cited:

- DeepEP for expert-parallel communication;
- DeepGEMM for expert computation;
- system support for fine-grained MoE.

MoE “shuffle” therefore stresses kernels plus inter-GPU/network communication.

## 10. Attention-state management

vLLM's central job is managing model state.

- Full attention: relatively small per-token state, append-only growth; fits PagedAttention.
- Linear attention: larger recurrent state that is modified; needs different state manager.
- Hybrid/cross-attention: more complex state patterns.

Speaker says vLLM supports around `200–300` model architectures and is pruning obsolete ones. Strategy: optimize mainstream models × mainstream hardware × mainstream workloads, not preserve every historical feature.

## 11. Harness–infra co-design for agents `[140:00–150:00]`

Agentic inference consists of many short calls with growing shared history. Prefix cache becomes critical.

Bad harness behavior:

- changing tool definitions at prompt front each turn;
- deleting/reordering prior reasoning;
- inserting current date/time into system prompt;
- scheduling every agent exactly on hour.

These invalidate prefix cache and synchronize traffic spikes.

Better design:

- keep stable prompt prefix;
- append changing state;
- expose current date/time through tool only when needed;
- jitter recurring jobs;
- coordinate memory/harness design with cache behavior.

This is direct systems lesson: token count alone misses recomputation. **Prompt-layout stability** affects inference cost.

## 12. FP8 and chip co-design `[148:00–155:00]`

Hopper FP8 matrix operations offer up to roughly 2× raw throughput versus FP16, but naïve global FP8 can hurt accuracy.

Speaker credits DeepSeek with large-scale approach using:

- block-wise weight quantization;
- per-channel activation quantization;
- higher-precision/vector accumulation alongside matrix units.

Claim: model and kernel design jointly captured FP8 speed without material quality loss.

Caveat: chronology in translated transcript (`A100 → H100 from 2024–25`) is inaccurate/loose; A100 and H100 launched earlier. Treat as architectural illustration, not release timeline.

## 13. First-principles performance engineering

Don't benchmark patches without causal model. Understand:

- continuous batching;
- attention shapes under batch/context regimes;
- FlashAttention implementation;
- GPU thermals, power and clock;
- memory hierarchy;
- communication topology;
- numerical precision;
- kernel programming model.

You's example: knowing GPU execution model led him to seek existing CUDA coredump support for illegal-memory-access debugging.

Rule:

> If engineer cannot explain why speedup occurs and under what workload it disappears, result may be lottery win, not durable optimization.

## 14. Technical predictions `[155:00–170:00]`

### Context ceiling

Hot take: human-facing models may plateau around **one million tokens**. Specialized science may need `10M–100M`. Long-horizon work likely handled through:

- external memory;
- skills;
- tools;
- subagents;
- retrieval.

This is falsifiable prediction, not consensus.

### China/US constraint asymmetry

Speaker view:

- China: constrained high-end accelerators; more land/power; stronger pressure for efficiency and domestic-chip adaptation.
- US: more high-end chips; tighter land/power; infrastructure focus shifts toward electricity.

### Open-source models

You predicts open-source models ultimately win and model capability commoditizes. Claimed reasoning:

- model outputs reveal behavior;
- users collect task data;
- organizations can build training flywheels;
- advantage depends on iteration speed, not static model lead.

Counterpoint: API outputs do not reveal weights, full training corpus, post-training process or frontier-scale compute. Data flywheel may clone narrow task behavior without replicating frontier model. Closed models can retain distribution, compute and feedback advantages.

## 15. “Systems, not algorithms” thesis

Examples:

- exact FlashAttention displaced many approximate attention algorithms;
- PagedAttention + continuous batching made autoregressive serving economical;
- speculative decoding reduces serial-token bottleneck;
- chunk-parallel kernels make some linear-attention designs viable.

Broader principle:

> Algorithm only survives if systems implementation wins hardware lottery.

But systems and algorithms are complements, not substitutes. Better system cannot create intelligence absent model/data; better model can be economically unusable absent system.

## Theory of edge

> Inferact gets paid because rapid fragmentation across models, accelerators and workloads creates integration complexity no single vendor-neutral customer wants to maintain; vLLM converts that complexity into more deployable tokens per machine.

Structural advantages:

- founder/maintainer credibility;
- community standard position;
- broad model/hardware compatibility;
- pre-release NDA relationships;
- vendor neutrality;
- performance expertise and fleet feedback;
- foundation-backed open-source continuity.

## Bull case

- open models gain share;
- vLLM remains default serving layer;
- model/hardware fragmentation rises;
- inference spend exceeds training spend;
- agents create repeated, cache-sensitive calls;
- managed deployment/per-use model scales;
- performance gains remain measurable and shared with customer;
- foundation neutrality keeps chip/cloud vendors cooperating.

## Risks and counter-thesis

- hyperscalers/model labs keep superior internal engines;
- TensorRT-LLM, SGLang, cloud runtimes or new architecture displace vLLM;
- open-source software commoditizes company differentiation;
- community forks after commercial conflicts;
- foundation trademark limits company control;
- GPU/cluster cost consumes seed capital;
- supporting `200–300` architectures becomes maintenance drag;
- benchmark leadership fails at large scale/P99;
- customers prefer bundled cloud inference;
- business model never exceeds support/consulting economics;
- open models fail to match frontier quality.

## KPIs

- production tokens served through vLLM;
- share of new open models supported at release;
- time from model/hardware disclosure to support;
- P50/P99 latency and throughput by workload;
- tokens/GPU-hour and cost per accepted/useful token;
- prefix-cache hit rate for agent workloads;
- cluster utilization and failure rate;
- enterprise paying customers, retention and net revenue expansion;
- recurring/platform revenue versus services;
- gross margin after compute;
- maintainer concentration and review backlog;
- trusted contributor/institution growth;
- performance versus SGLang/TensorRT-LLM/cloud runtimes.

## Kill tests

Re-underwrite if:

- leading open models launch without vLLM support;
- performance gap against internal/proprietary engines widens;
- commercial customers require community-hostile forks/features;
- revenue remains engineer-time services;
- per-use unit economics fail after compute/support;
- core maintainers leave or governance fragments;
- model architecture shifts make current state-management foundation obsolete;
- open-source models lose sustained quality/adoption share.

## Operator learnings

1. Choose measurable bottleneck, not fashionable abstraction.
2. Simple idea + early complete system beats novel paper without deployment.
3. Code cheap; context, prioritization and review scarce.
4. Prune features aggressively to preserve architecture.
5. Stable prompt prefixes and jittered schedules reduce agent serving cost.
6. Co-locate algorithm, systems and hardware understanding.
7. Explain speedup causally before trusting benchmark.
8. Open-source infrastructure needs neutral governance plus dedicated economic sponsor.

## Bottom line

vLLM's durable insight is not merely PagedAttention. It is that inference is integration problem across changing models, state patterns, GPUs, networks and workloads. Neutral abstraction layer can become valuable infrastructure if it keeps performance leadership while monetizing without betraying community.

Inferact owns strongest possible starting position, but `$150M` seed and “Linux of inference” framing set very high bar. Proof must be scalable recurring economics, not stars, contributors or technical prestige alone.