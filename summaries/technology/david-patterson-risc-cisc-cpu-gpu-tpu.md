---
title: "David Patterson: RISC vs CISC, CPU vs GPU vs TPU"
source: "https://www.youtube.com/watch?v=Pn4ZwlEh5nw"
video_id: "Pn4ZwlEh5nw"
guest: "David Patterson"
duration: "59:13"
date_summarized: "2026-07-11"
category: "technology"
---

# David Patterson: RISC vs CISC, CPU vs GPU vs TPU

## TL;DR

Computing progress shifted from universal transistor scaling toward specialization. RISC won most unit volume by simplifying instructions and reducing energy, while x86 survived through binary compatibility and internally translating complex instructions into RISC-like micro-operations. When Dennard scaling ended around 2005 and Moore's Law slowed in the 2010s, CPUs stopped gaining effortless single-thread performance. GPUs then exploited parallelism; TPUs specialized further for matrix-heavy machine learning. Current advantage comes from full-stack co-design: architecture, packaging, numerical formats, memory, compiler and libraries.

## RISC versus CISC

### Historical dispute

Early microprocessors copied mainframe/minicomputer instruction sets. CISC philosophy:

- richer, more complex instructions;
- fewer instructions per program;
- smaller semantic gap between high-level language and machine;
- microcode interprets complex instructions into lower-level control.

RISC alternative:

- simpler, regular instructions;
- compiler performs composition;
- more instructions execute, but each is faster and easier to pipeline;
- more registers reduce compiler-allocation pressure.

Patterson cites early measurements:

- RISC programs needed roughly **30–40% more instructions**;
- simple instructions could run roughly **4–5× faster**;
- potential net gain around **3–4×**.

Architectural debate persisted because 1970s/1980s design relied heavily on intuition rather than shared quantitative benchmarks.

### Why sophisticated instructions disappointed

Microprogramming originally made sense when fast read-only control memory could efficiently interpret richer instructions. As semiconductor technology changed, interpretation overhead became expensive.

Compiler teams often ignored elaborate instructions because separate simple instructions were faster or easier to optimize. CISC then paid microcode complexity without receiving expected software benefit.

RISC used around **32 registers**, versus common CISC designs with 8 or 16, reducing damage from imperfect register allocation.

### Who won?

“CISC won” only appears true if history stops at x86 PCs/servers:

- binary software distribution created enormous x86 lock-in;
- Intel preserved compatibility by decoding x86 into internal RISC-like micro-operations;
- commercial value of software compatibility justified decoder overhead.

But RISC dominates processor unit volume:

- ARM began as Acorn RISC Machine, then Advanced RISC Machine;
- energy/resource efficiency suited Apple's Newton, then Nokia/mobile devices;
- Patterson cites roughly **350 billion ARM-based processors** shipped;
- he estimates about **99% of processors** are RISC when embedded/mobile devices count;
- Apple moved PCs to ARM;
- Amazon, Microsoft and Google develop ARM server CPUs.

Conclusion: x86 retains important installed-base niches, but RISC keeps expanding because computing is energy-bound.

## Why specialization replaced free CPU scaling

Two historical engines:

1. **Moore's Law:** transistor count doubled every one to two years.
2. **Dennard scaling:** voltage fell as transistor density rose, keeping chip power around tens of watts.

Around 2005, Dennard scaling ended. More/faster transistors created unsustainable heat. Industry response:

- single complex core → 2, 4, 8+ cores;
- programmer/compiler had to expose parallelism.

Around the 2010s, Moore's Law itself slowed. General-purpose CPU gains became incremental. Patterson rejects claim that Moore's Law still holds merely because technology improves:

- original claim specifically concerns transistor-count doubling;
- logic still improves, but SRAM scales poorly;
- DRAM density once improved roughly **4× every three years**; he says now it may take about **10 years**;
- chiplets and advanced packaging aggregate multiple dies but do not restore monolithic transistor scaling.

If Moore plus Dennard scaling had continued, CPUs might theoretically run near **100THz** and GPUs would remain niche. Actual clock rates plateaued near a few GHz.

## CPU, GPU and TPU

### CPU

- Maximum generality.
- Runs operating systems, compilers and irregular workloads.
- Modern designs use many cores, but each remains recognizably conventional.
- Flexibility costs area and energy.

### GPU

Originally domain-specific graphics hardware:

- many hardware threads hide memory latency;
- high parallel throughput;
- graphics tolerated 16/32-bit floating point;
- strong floating-point performance per dollar.

Researchers repurposed GPUs by mapping non-graphics work onto graphics-like parallel operations. In 2006, NVIDIA invested in CUDA, giving programmers a C-like way to target GPU hardware. CUDA made parallel hardware accessible before AI demand arrived. GPU-trained **AlexNet's decisive 2012 ImageNet win** then helped establish neural networks and GPUs as default ML approach; cheap GPU compute let team test far more model configurations.

### TPU

Google feared internal machine-learning inference demand would require roughly doubling data-center fleet if served on CPUs. It developed first TPU as dedicated matrix/tensor accelerator.

Design choices:

- Center silicon on a very large matrix-multiply unit because neural networks are matrix-heavy.
- Remove expensive general-purpose mechanisms ML did not need.
- Replace three hardware-managed cache levels with software-scheduled transfers into explicitly managed memory.
- Introduce `bfloat16` (“brain floating point”): retain wide exponent/range while sacrificing mantissa precision.

Patterson cites first TPU result:

- roughly **30×** better inference than contemporary GPU;
- roughly **80×** better than CPU.

Google's 2016 disclosure became watershed:

- NVIDIA modified GPUs further for ML;
- Intel acquired accelerator companies;
- hyperscalers began building custom AI silicon.

TPU specializes more aggressively than GPU around matrix multiplication. Training TPU structure has remained broadly stable for roughly a decade:

- large matrix-multiply unit;
- vector unit;
- HBM;
- increasingly large/fast implementation.

## Why AI chips still improve rapidly

No single replacement for Moore's Law. Progress combines:

- advanced packaging and chiplets;
- closer dies/interconnect;
- lower precision: 16 → 8 → 4-bit formats;
- larger matrix engines;
- HBM and memory-system design;
- architecture tailored to ML operators;
- compiler/libraries optimized per workload.

Modern AI performance is system co-design, not transistor shrink alone.

## NVIDIA moat

“CUDA moat” means more than language:

- mature libraries;
- workload-specific kernels;
- compiler support;
- new libraries tuned for each architecture;
- large engineering organization able to optimize application stack.

Benchmarks evaluate hardware plus software. NVIDIA performs strongly partly because its libraries exploit chip fully. Startups often underestimate software investment and cannot match engineers/kernels.

Google competes with internal libraries and heavier compiler use, but historically TPU remained mostly internal/cloud-only.

MLPerf attempts shared, fair AI benchmarks like SPEC CPU. Yet participation remains imperfect because architecture cannot be separated from quality of libraries and implementation effort.

## Investor/operator implications

### Theory of edge

Semiconductor winner captures workload by co-designing whole stack more efficiently than general-purpose alternative: silicon, memory, packaging, interconnect, compiler, kernels and developer distribution.

### What matters

- Domain-specific acceleration replaces general scaling where workload large/stable enough.
- Energy per useful operation matters more than raw transistor count.
- Software can sustain hardware moat.
- Binary/developer compatibility can preserve inferior architecture for decades.
- Hyperscalers build ASICs when scale savings exceed design/software cost.
- HBM and packaging become central because distance/data movement dominate energy.
- Low precision offers performance gains but eventually faces accuracy limits.

### What can break NVIDIA moat

- workload consolidates around stable operators easily compiled to ASIC;
- hyperscalers amortize custom silicon over huge internal demand;
- open software layers reduce CUDA switching costs;
- memory/interconnect bottleneck overwhelms GPU generality;
- competitor reaches adequate—not necessarily superior—software quality at lower TCO.

### Why startups struggle

Chip benchmark alone insufficient. Need:

- compiler;
- libraries/kernels;
- framework integration;
- debugging/profiling;
- deployment reliability;
- developer support;
- enough capital and time to optimize workloads.

## Career and life lessons

- **Family first:** nobody on deathbed wishes for more office time.
- **Optimize happiness, not wealth:** they are separate goals.
- **Keep play/fun:** adulthood should not remove it.
- **Protect important, non-urgent work:** packed calendars eliminate thinking.
- **Finish:** achievement measured by completed important projects, not many starts.
- **One main thing at a time:** only five or six life contributions may be remembered.
- **People outlast projects:** teaching/helping people generates deeper satisfaction than ephemeral artifacts.
- **Courage:** bold bets create possibility; playing safe still permits failure.
- **Challenge weak arguments:** intellectual progress needs conflict around ideas.
- **But enemies accumulate:** confront selectively and for meaningful stakes.
- **Optimism helps persistence.**

Relationship mnemonic: **“I was wrong. You were right. I love you.”**

## Caveats

- Historical performance figures are Patterson's recollections, not independently verified benchmarks here.
- “99% RISC” depends on counting embedded/mobile unit volume, not revenue or compute capacity.
- TPU versus CPU/GPU numbers refer early-generation inference and should not compare current systems.
- Moore's Law definitions vary; Patterson uses original transistor-doubling definition.
- Hardware comparison without workload, precision, utilization, software and TCO is misleading.

## Bottom line

Architecture wins by matching abstraction to constraint. RISC removed unnecessary instruction complexity. GPUs exposed massive parallelism. TPUs removed generality for matrix throughput. Next gains come from full-stack specialization under energy, memory and software constraints—not automatic transistor scaling.