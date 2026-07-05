# Why NVIDIA Is Giving Away AI Models — Bryan Catanzaro

Source: Spotify episode: https://open.spotify.com/episode/1uLyO1G64kNfcJeO5h1V8E
Transcript source: YouTube mirror: https://www.youtube.com/watch?v=Oojrfdl42LI
Show: The MAD Podcast with Matt Turck
Guest: Bryan Catanzaro, VP Applied Deep Learning Research, NVIDIA
Date: 2026-07-02
Duration: 1:22:59

## TL;DR

NVIDIA builds and releases open models because models are how it learns what future accelerated-computing systems must do. Nemotron is not charity: it is R&D for hardware/software co-design, ecosystem support, and demand creation for Blackwell/Hopper-style AI factories.

Core investor read-through: NVIDIA's moat is shifting from GPU chips alone to full-stack systems knowledge — models, numeric formats, networking, compilers, libraries, inference economics, and research culture all co-designed around frontier workloads.

## Key points

- Open-source AI is catching up, but unevenly. Catanzaro says Chinese labs have led in openness and collaboration. US/open Western labs need more willingness to release models and share progress.

- Open models matter because every company is built around secrets: proprietary data, workflows, customer context, and operating know-how. AI gets more valuable when tightly connected to those secrets, which is easier with open/customizable models.

- NVIDIA's model strategy has two jobs:
  - Understand how AI workloads work deeply enough to design future systems.
  - Support ecosystem developers with strong open models, tools, and reference implementations.

- Structural NVIDIA claim: Moore's Law is effectively dead, so acceleration now comes from specialization. Specialization requires understanding workloads from first principles. Nemotron is NVIDIA's microscope into future AI workloads.

- Bryan's career arc matters: cuDNN, DLSS, Megatron, then Nemotron. Megatron began as a systems proof that huge Transformer training could run well on NVIDIA GPUs, countering claims that TPUs were required.

- Nemotron family: Nano / Super / Ultra target different latency, cost, and capability points. NVIDIA emphasizes agent workloads where speed and cost matter, not pure benchmark prestige.

- 4-bit pretraining is big. Post-training quantization is common; pretraining a large model directly in NVFP4 is harder because numeric instability can make the run diverge. NVIDIA wants this because 4-bit formats can deliver much higher throughput and much lower energy use on Blackwell Ultra.

- Hybrid Mamba-Transformer architecture: state-space/Mamba layers summarize long sequences efficiently and may help global/intuitive sequence understanding; attention remains useful for precise retrieval. Their sweep found mostly state-space plus some attention worked best.

- Mixture-of-experts is default frontier architecture. It gives more intelligence per inference dollar by routing each token to relevant expert subnetworks rather than activating full model. Tradeoff: more memory and more complex serving.

- NVL72 rationale: MoE requires fast expert routing across many GPUs. Blackwell NVL72 lets up to 72 GPUs read/write each other's memory with high bandwidth and low latency, matching token routing needs.

- 1M-token context matters for agentic work: codebases, instructions, documents, tool traces, and long-running task state can be packed into context. Longer context expands problem class, but cost/latency still matter.

- Multi-token prediction: inference often bottlenecked by reading weights from memory, not math. If same weight fetch can predict multiple tokens, throughput improves. Model predicts several tokens, validates/continues on next pass.

- Multi-teacher distillation: Nemotron 3 Ultra used ~10–15 specialist teacher models for domains like science, theorem proving, coding, and agent harnesses. Student model learns from dense token-level rewards across domains.

- RL next frontier: environments get more complex. Current RL environments are still simple relative to real-world agent work; next gains come from richer, diverse, realistic environments and evals.

- NVIDIA research org runs less like clean org chart, more like mission-driven swarm. Multiple teams contribute to Nemotron; “mission is the boss.” GPU allocation and priorities follow strategic importance plus researcher initiative.

- Culture point: NVIDIA feels entrepreneurial because value is system-level. If compiler, library, networking, or software fails, chip value is destroyed. This forces cross-functional execution.

- Bryan rejects simplistic singularity framing. Intelligence is multifaceted; math-contest intelligence is not CEO/product/social/world-model intelligence. AI progress huge, but “one scalar intelligence explosion” is too crude.

- Open AI safety stance: Bryan argues open technologies can be safer because sunlight, scrutiny, and diversity beat safety decisions by a small closed group. Diversity is safer than monoculture, even when values conflict.

## Investor / operator read-through

- NVIDIA's real edge: workload intimacy. Building frontier/open models lets NVIDIA see bottlenecks before customers can articulate them.

- Hardware thesis: Blackwell/NVL72 not generic compute. It is shaped around MoE, low precision, memory movement, routing, and inference throughput.

- Open-model strategy is demand creation. Better open models make more companies run custom AI on NVIDIA-optimized stacks.

- Agent era = speed/cost frontier. If agents call models repeatedly, inference economics compound. Fast, cheap, specialized inference becomes moat.

- Watch bottleneck rotation: GPU FLOPs → memory bandwidth → interconnect → numeric formats → serving schedulers → RL environments/evals. NVIDIA wants control/visibility across all layers.

## Caveats / kill tests

- Open models may commoditize some model-layer value, but strengthen NVIDIA if compute demand and stack dependence rise.

- MoE serving is strong at batch size 1 or huge datacenter scale, trickier in middle utilization regimes.

- Long context is useful but can become expensive/sloppy without retrieval, memory hierarchy, and good agent harness design.

- Open-safety argument is philosophically plausible, not settled. Misuse and proliferation risks remain.

## One-line summary

NVIDIA gives away AI models because open models are both ecosystem fuel and the R&D instrument that tells NVIDIA what the next AI factory must be built to accelerate.
