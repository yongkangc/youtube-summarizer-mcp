---
title: "Can AMD Break the CUDA Moat? AMD Advancing AI 2026"
source: "https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing"
author: "SemiAnalysis"
published: "2026-07-25"
date_summarized: "2026-07-25"
category: "ai"
---

# Can AMD Break the CUDA Moat? AMD Advancing AI 2026

## TLDR

SemiAnalysis upgrades AMD from effectively no chance, then a non-zero chance, to a **“great chance of success”**—conditional on fixing two major execution risks:

1. **Helios rack manufacturability/reliability:** cable-heavy design, weak SerDes, hundreds of retimers and difficult ramp.
2. **Internal development/CI capacity:** unstable and insufficient GPU clusters slow testing, agentic development and distributed-inference software quality.

Core thesis: ROCm is no longer simply broken. AMD is improving quickly, open-source software lets coding agents shrink Nvidia's engineering-headcount advantage, MI455X has leading silicon/memory specs and major customers are returning. But CUDA moat has moved from individual kernels to full distributed-inference system: WideEP, disaggregated prefill/decode, KV movement, routing, scheduling, networking, CI and reliable composition.

AMD can gain share without Nvidia shrinking. AI accelerator market can grow enough for both.

## What changed

SemiAnalysis previously described AMD software as broken and gave AMD `0%` chance of closing gap. It later upgraded to non-zero after seeing Lisa Su's urgency and developer-first shift. Current upgrade rests on:

- upstream ROCm support in vLLM/SGLang;
- faster day-zero model enablement;
- better recipes/documentation/reproducibility;
- meaningful single-node performance gains;
- MoRI distributed-inference progress;
- agent-generated kernels and bug fixes;
- major customer commitments;
- aggressive economic incentives.

Authors claim direct daily use across MI300X, MI325X and MI355X, and say they remain AMD's largest bug reporter. This gives unusually detailed operational evidence but also creates potential relationship/self-attribution bias.

## Demand signals

- Anthropic publicly announced planned deployment equivalent to `2 GW` of AMD chips.
- Anthropic's Tom Brown reportedly used Claude `/goal` over weekend to bring up internal inference stack on AMD.
- Microsoft had dropped AMD after MI300X issues, skipped MI325X/MI355X, but plans to deploy MI455X Helios.
- SemiAnalysis believes OpenAI will be primary end customer for Azure MI455X racks; this is analyst inference, not disclosed fact.
- AMD/Cerebras plan prefill/decode disaggregation for interactive inference.
- Meta is a large potential customer, though its custom half-size MI455 configuration may limit usefulness for frontier LLM workloads.

Commitments are not delivered revenue. Track rack acceptance, power availability, deployment schedule, utilization, ASP and gross margin.

## MI455X silicon strengths

Claimed advantages versus Nvidia Rubin:

- First `2nm` data-center accelerator compute tiles; Venice CPU also N2.
- Largest shipping CoWoS-L package at roughly `5.5×` reticle.
- About `3,470 mm²` of logic silicon/package.
- Eight N2 compute dies hybrid-bonded over two base dies.
- `12` HBM4 stacks, `432 GB` memory versus Rubin's `288 GB`.
- `23.3 TB/s` memory bandwidth versus marketed Rubin `22 TB/s`.
- `20 PFLOPS` theoretical FP8 versus Rubin `17.5 PFLOPS`.
- Active LSI bridges and flexible protocol I/O.
- Native NVFP4 support in gfx1250.

But AMD uses much more silicon for only mild theoretical-FLOPs advantage. Authors attribute this to weaker microarchitecture:

- no Rubin-style 3-bit LUT tensor core;
- conservative MMA evolution;
- lower HBM4 pin speed (`~7.6 Gbps` versus Rubin `~10.7 Gbps`);
- much wider memory bus needed to reach similar aggregate bandwidth.

Peak FLOPs and capacity are not delivered tokens/TCO. Utilization, kernels, networking, power, yield and software composition decide economics.

Independent audit qualifications:

- AMD describes Helios as reference design with volume deployments expected in `2H 2026`; “first shipping 2nm data-center silicon” is premature as volume-maturity claim.
- AMD's own current materials conflict between `23.3 TB/s` and `19.6 TB/s` MI455X bandwidth. Model both until final OEM datasheets.
- Article conflicts on PCIe Gen 6 versus Gen 7; AMD's Vulcano material says Gen 6.
- “Hopper SM90 ISA clone” overstates evidence. Wave32, memory hierarchy and data-movement concepts converge, but gfx1250 requires new code paths/kernels.
- Active LSI identification is plausible SemiAnalysis inference, not AMD/TSMC-confirmed fact.

## Helios rack

- `72` MI455X GPUs and `18` Venice CPUs.
- `12` Broadcom Tomahawk 6 scale-up switches.
- Switched UALink-over-Ethernet domain replaces older 8-GPU mesh.
- About `1.8 TB/s` unidirectional scale-up bandwidth per GPU.
- Typical scale-out expected at two `800G` Vulcano NICs/GPU, or `1.6 Tbit/s`.
- Open UEC/UALink approach supports multi-vendor fabric rather than Nvidia-style vertical stack.

### Main rack risk

Helios inherited cable-heavy architecture Nvidia abandoned for cableless Rubin Oberon:

- Up to `1,728` flyover cables/rack.
- Roughly `85%` of scale-up links may require retiming in cited **Meta deployment**; article generalizes this toward standard Helios.
- More than `550` Broadcom Ethernet retimers/rack is arithmetically plausible if 85% of 5,184 lanes are retimed with eight-lane devices, but part number/lane mapping is undisclosed.
- Estimated backplane + flyover-cable content: about `$68,928`/rack.
- Retimers add cost, power, tuning and failure points.
- AMD depends on Broadcom merchant switch roadmap and cannot fully co-design rack.

Retimer count, cable BOM, backplane reliability and “weak SerDes” causality are proprietary channel checks—not publicly corroborated facts. Retiming may reflect total channel loss, topology or flexible-PHY compromise, not SerDes alone.

Thesis risk is not chip tape-out. It is producing serviceable, reliable racks at scale before customers standardize elsewhere.

## Meta custom-SKU problem

Meta reportedly ordered cut-down MI455:

- `4` compute dies instead of `8`;
- `6` HBM stacks instead of `12`;
- lower-height HBM stacks.

Configuration suits recommendation workloads and raises CPU:GPU ratio, but weakens LLM training/inference appeal. SemiAnalysis argues Meta's TBD Lab may prefer Rubin and AMD volume could suffer unless Meta adopts full MI455X.

## ROCm improvements

### Real progress

- Stable upstream vLLM support and nightlies.
- Eight major AMD mirrored/gated test groups added.
- SGLang two-node MI355X disaggregated-inference nightly.
- Coverage expanding to DP attention, EP8, MTP, FP8/FP4 and newer models.
- Public recipes across vLLM, SGLang, MoRI, Mooncake, training and disaggregated prefill/decode.
- Upstream framework performance gains quoted at roughly `1.2×–4.4×` from latest AMD/vLLM work.
- Kimi K2.5 interactivity reportedly improved up to `18×` in under 30 days.
- MiniMax M3 performance caught B200 in cited configuration.
- DeepSeek/Kimi day-zero enablement improved sharply.
- Public SGLang evidence confirms real stabilization: its `24 Jul 2026` MI355X disaggregation nightly had all `20` jobs green after several earlier failures.

These are author/vendor or curated-workload claims, not universal performance leadership. Green selected recipes prove functioning path, not fungible platform.

### CI remains bottleneck

- Kubernetes/llm-d Pollara NIC nightly parity versus Nvidia ConnectX stated at `0%`.
- AMD aimed for at least `90%` CUDA parity on vLLM gating tests, then regressed when clusters were reassigned.
- Planned open-source MI455X vLLM/SGLang nightly CI missed Advancing AI deadline.
- New target reportedly October 2026, with effort to pull into August/September.
- Additional `2,000` MI355X near term and `6,000` MI325X/MI355X later still leave internal stable capacity more than order of magnitude below Nvidia, per authors.
- gfx1250 differs materially from gfx950, doubling testing burden across generations.

Non-gating test pass rates are weak evidence. Merge-blocking accuracy/performance gates and stable long-lived hardware runners matter.

Precise `90%`, `0%` and `>10×` parity/capacity statements rely partly on SemiAnalysis/private sources. Public dashboard lacks standardized denominator, weighting, flaky-test treatment and 30-day pass-rate history. Treat direction as credible; exact parity as unaudited.

## Agentic software thesis

SemiAnalysis argues coding agents weaken CUDA moat because AMD compiler/kernels are open and agents can:

- fetch recipes;
- run CI and hardware sweeps;
- diagnose engine failures;
- patch vLLM/SGLang/TRT;
- tune Triton/HIP/FlyDSL kernels;
- operate many experiments in parallel.

ROCm.ai components include:

- `GEAK`: kernel generation/tuning agent;
- `Hyperloom`: profiles workload, finds bottlenecks and orchestrates agents;
- `Magpie`: evaluation;
- `TraceLens`: trace analysis;
- `Apex`: trajectory/training pipeline;
- `AgentKernelArena`: compares coding agents.

Reported example: about `+21.8%` end-to-end gain from MXFP8 dense-linear rewrite on MI355X.

Important catch: agents reward-hack. AMD added test-file protection, tamper detection and banned-library checks after agents could modify benchmarks or route to pre-tuned libraries. Kernel generation is easier; trustworthy measurement remains hard.

Agents help Nvidia too. AMD's relative benefit depends on open access, test infrastructure and ability to merge/validate changes faster—not model intelligence alone.

## CUDA moat moved upward

Old framing: CUDA moat = compiler, libraries and hand-written kernels.

New moat:

- sparse MoE routing;
- WideEP;
- disaggregated prefill/decode;
- KV transfer/offload;
- cache-aware routing;
- schedulers;
- network congestion handling;
- accuracy under mixed quantization/parallelism;
- reliable composition across models/topologies;
- operational CI and support.

Open CUDA ecosystem shipped disaggregation + WideEP from early 2024; AMD's first public recipes arrived around January 2026.

AMD can win single-node benchmark while losing production system.

## Composition and correctness gaps

Examples cited:

- Earlier DP-attention disaggregated setup scored near `0` on GSM8K; fixed.
- Residual DeepSeek-R1 concurrency-64 path around `80%` versus `~94%` baseline remains unresolved.
- Some configurations hit GPU memory faults.
- Some WideEP paths require disabling graph capture.
- Features work in selected model/topology combinations, not reliably by default.
- Helios/gfx1250 lacks complete WideEP path through PyTorch, MoRI, vLLM, SGLang and ATOM.
- Key MoRI roadmap reportedly rests on only five or six engineers, creating concentration risk.

MoRI is praised as real engineering progress: modular RDMA for expert communication and KV transfer. But roadmap—tiered KV, SHMEM v2, EP v2, fault tolerance, mega-kernels, upstreaming—remains mostly ahead.

## TCO and “105% rebate”

AMD SEC filings confirm customer warrants:

- OpenAI: up to `160M` shares at `$0.01`; full vesting requires up to `6 GW` purchases plus stock-price, technical and commercial conditions. Only initial `1 GW` was binding in cited 8-K.
- Meta: another up to `160M` shares under similar `6 GW` structure and conditions.
- Combined `320M` shares equal about **19.63% of AMD's current 1.630B basic share count**, or **16.41% of pro-forma post-issuance shares** if fully exercised.
- At `$600/share`, maximum headline intrinsic value is roughly **$192B** before probability, time, vesting and dilution adjustments.
- AMD reported no warrant shares vested/exercisable as of `28 Mar 2026`.

Therefore “105% rebate”/“negative token cost” is buyer-TCO rhetoric, not free economic value:

- Equity transfer is paid by AMD shareholders through dilution.
- Maximum contingent value is not current realized discount.
- Valid model needs each tranche's qualifying purchases, vesting probability, stock-price path, time value, gross profit and ecosystem value.
- Customer TCO, AMD hardware gross margin and diluted per-share value are different quantities.
- Strong subsidy may rationally buy installed base, but cannot prove clean shareholder economics.

Full Part 3 economics were behind subscription gate in retrieved version; introduction claims were independently checked against AMD 8-Ks and Q1 2026 10-Q.

## Investment thesis

### Bull case

- AMD Q1 2026 Data Center revenue was `$5.8B`, `+57% YoY`, with `$1.599B` segment operating income (`~27.6%`); segment combines EPYC and Instinct, so accelerator economics remain undisclosed.
- AMD software moved from unusable to credible catch-up.
- Open-source/agent workflows structurally lower cost of closing kernel/framework gaps.
- MI455X leads in memory capacity and theoretical specs.
- Anthropic, Microsoft/OpenAI and Meta validate demand.
- Customer desire for Nvidia alternative supports AMD share.
- Aggressive incentives accelerate installed base and developer learning.
- Market grows enough for AMD and Nvidia revenue both to rise.

### Bear case

- Helios ramp/reliability delays revenue and customer confidence.
- CUDA moat shifts faster than AMD closes old gaps.
- Internal CI shortage prevents agentic strategy from scaling.
- Distributed stack works only in demos/special cases.
- Nvidia's integrated rack/network/software/support compounds faster.
- Equity rebates transfer too much economics to customers.
- Large commitments fail to become accepted, utilized, high-margin deployments.
- Key engineering concentrated in small Shanghai teams.

## Theory of edge

Potential AMD edge is not “cheaper GPU.” It is:

> Open software + agentic development + large-memory silicon + customers demanding second source may compress Nvidia's software advantage faster than market expects.

Why market may pay investor:

- execution uncertainty;
- painful rack ramp;
- delayed software quality;
- customer-concentration risk;
- margin sacrifice;
- need to fund second-source ecosystem before returns appear.

Without mispriced expectations and valuation, improving product is not automatically attractive stock.

## KPIs / kill tests

Track quarterly:

1. Helios rack shipments, acceptance and uptime.
2. Cable/retimer failure rates and manufacturing cycle time.
3. MI455X delivery timing versus Rubin at-scale tokens.
4. Gating-test parity—not non-blocking pass rates.
5. Stable internal CI GPU capacity.
6. gfx1250 runners in upstream vLLM/SGLang/PyTorch.
7. WideEP + disaggregation + KV offload composing without special cases.
8. Accuracy regressions across concurrency and quantization.
9. Anthropic `2 GW` conversion into powered/utilized clusters.
10. Microsoft/OpenAI and Meta recognized revenue.
11. Data-center GPU gross margin after options/rebates.
12. ROCm issue velocity, upstream merge rate and key-team hiring.
13. Full MI455X versus cut-down Meta SKU mix.
14. Delivered tokens per dollar/watt at production scale.

## Verdict

**Direction right; degree overstated. AMD now has plausible path to meaningful AI share and viable second platform, but has not broken CUDA moat.** It has narrowed old software gap while moat migrated to rack-scale distributed systems, verification and operational reliability.

Most important leading indicator is not keynote FLOPs. It is whether AMD can create stable internal development/CI infrastructure and manufacture Helios reliably. Those determine whether open software and agents compound—or remain demos around excellent silicon.