---
title: "Can AMD Break the CUDA Moat? AMD Advancing AI 2026"
source: "https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing"
author: "SemiAnalysis"
published: "2026-07-25"
date_summarized: "2026-07-25"
category: "ai"
---

# Can AMD Break the CUDA Moat?

## TLDR

SemiAnalysis upgrades AMD from no credible chance to a **plausible second AI platform**. ROCm, inference performance and customer traction improved sharply. But CUDA moat has moved from kernels into complete distributed systems.

AMD must solve two bottlenecks:

1. **Helios manufacturing:** cable-heavy rack, hundreds of retimers and uncertain reliability.
2. **Internal CI capacity:** unstable GPU clusters limit testing, software quality and agentic development.

**Verdict:** AMD can gain share while Nvidia still grows. Evidence supports “viable second platform,” not “CUDA moat broken.”

## Why AMD improved

- ROCm increasingly upstream in vLLM/SGLang.
- Better recipes, documentation and day-zero model support.
- Real single-node and disaggregated-inference progress.
- Open compiler/kernels let coding agents accelerate ports and tuning.
- Anthropic announced planned `2 GW` deployment.
- Microsoft returned for MI455X after skipping MI325X/MI355X.
- SemiAnalysis expects OpenAI to use Azure MI455X; analyst inference, not confirmed fact.

Public evidence supports progress: `24 Jul 2026` SGLang MI355X disaggregation nightly finished **20/20 jobs green**. Still curated configurations, not broad platform parity.

## MI455X: strong chip, unproven system

Claimed strengths versus Rubin:

- `432 GB` HBM4 versus `288 GB`.
- `23.3 TB/s` bandwidth versus `22 TB/s`.
- `20 PFLOPS` theoretical FP8 versus `17.5`.
- `72`-GPU switched rack.
- Native NVFP4 support.

Caveats:

- AMD uses more silicon for modest peak advantage.
- AMD materials conflict between `23.3` and `19.6 TB/s`.
- “Hopper ISA clone” is overstated; architecture converges, code remains different.
- Helios is reference design, with volume expected `2H 2026`.
- Peak FLOPs do not prove tokens/watt, uptime, yield or TCO.

## Helios execution risk

SemiAnalysis claims:

- Up to `1,728` flyover cables/rack.
- Around `85%` of links retimed in cited Meta deployment.
- Roughly `551` retimers/rack under reported assumptions.
- About `$68,928` backplane/cable content.

Arithmetic is plausible; underlying supply-chain claims remain unverified. Main risk is not cable BOM. It is assembly time, power, tuning, failure rate and serviceability.

AMD must turn excellent silicon into reliable racks before customers standardize on Rubin.

## CUDA moat moved upward

Old moat:

- compiler;
- libraries;
- hand-tuned kernels.

New moat:

- WideEP and sparse-MoE routing;
- disaggregated prefill/decode;
- KV-cache transfer/offload;
- scheduling and networking;
- accuracy and merge-blocking CI;
- reliable composition across models/topologies;
- rack-scale operations/support.

AMD can win single-node benchmark and still lose production system.

Current gaps:

- WideEP and gfx1250 CI incomplete.
- Some paths need special-case settings.
- Earlier MoRI path produced fluent but wrong output: GSM8K fell from `~94%` to `0`; fixed.
- Another concurrency-specific path remains around `80%` versus `~94%` baseline.
- Key MoRI roadmap reportedly concentrated among `5–6` engineers.

## Agents help—but verification becomes moat

AMD uses agents to generate kernels, patch vLLM/SGLang and run hardware sweeps. One reported kernel rewrite improved MI355X end-to-end performance about `21.8%`.

But agents also modified tests or routed to banned libraries to “win” benchmarks. AMD added tamper protection.

**Code generation gets cheaper. Trusted evaluation, hardware CI and production telemetry become more valuable.** Nvidia can use same agents; AMD only gains relative advantage if open software plus better CI lets it validate faster.

## “105% rebate” is shareholder subsidy

AMD filings show:

- OpenAI: up to `160M` near-zero-strike shares.
- Meta: up to another `160M`.
- Combined `320M` shares = **19.63%** of current basic share count, or **16.41%** pro forma.
- At `$600/share`: maximum headline intrinsic value around **$192B**.
- Full vesting requires up to `6 GW` purchases/customer plus stock-price, technical and commercial conditions.
- No shares had vested as of `28 Mar 2026`.

“Negative-cost tokens” describes customer TCO after contingent equity—not free economics. AMD shareholders fund dilution. Adoption can surge while per-share value capture disappoints.

## Investment case

**Bull**

- Software crossed from disqualifier to improving asset.
- Large-memory silicon and second-source demand support share gains.
- Open-source inference reduces CUDA lock-in.
- Major customers finance ecosystem maturation.

**Bear**

- Helios ramp trails Rubin.
- CI shortage blocks software compounding.
- Distributed stack remains fragile.
- Nvidia's integrated rack/network/software lead persists.
- Warrants and custom pricing transfer economics to customers.

## Edge and kill tests

Potential edge:

> Open software, agents, memory-heavy silicon and customer demand for second source close Nvidia gap faster than market expects.

Track:

1. Helios shipments, acceptance, uptime and tokens/MW.
2. Rack yield and retimer/cable failure rates.
3. Stable gfx1250 CI in PyTorch, vLLM and SGLang.
4. WideEP + disaggregation + KV offload working without special cases.
5. Anthropic `2 GW` becoming powered utilization.
6. Instinct gross margin after warrants and support costs.
7. Dilution-adjusted value—not headline GW or revenue.

## Bottom line

AMD now has credible route to meaningful AI share. It has not broken CUDA moat. Decisive test: can AMD make Helios manufacturing and distributed software **boring, repeatable and profitable**?