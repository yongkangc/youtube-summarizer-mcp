# Dylan Patel (SemiAnalysis): The Datacenter in 2026: CPUs, RL Environments & Agent-Driven Workloads

Source: https://www.youtube.com/watch?v=c88l8daXiv4

## TL;DR

Dylan Patel’s core point: the AI bottleneck is moving beyond GPUs. As models become agentic and RL loops become environment-heavy, demand spills into CPUs, RAM, SSDs, sandboxes, orchestration, and warm pools. The new datacenter is not just GPU racks; it is a tightly coupled GPU + CPU + verifier/environment machine.

## Key insights

- **Neo-clouds had a real opening because hyperscalers moved slowly.** Google/Amazon/Microsoft had complex cloud software, reliability assumptions, and networks optimized for general cloud/storage traffic, not AI all-reduce workloads. Neo-clouds could skip legacy complexity, move faster on energy/GPU cluster buildout, and offer lower-overhead AI-focused infrastructure.

- **Neo-cloud quality now diverges.** Dylan says SemiAnalysis’ `ClusterMAX` ranks neo-clouds on observability, reliability, networking, security, orchestration, active/passive GPU health checks, fan/power/node/network monitoring, and whether the platform actually performs under AI workloads.

- **Bare-metal GPU rental is becoming commoditized.** Some clouds just rent GPUs over SSH. Better clouds add Slurm, Kubernetes, Slurm-on-Kubernetes, managed Ray, RL services, and higher-level software. The pattern reverts to old cloud economics: better software can charge more.

- **CPU was historically a laggard in AI.** Early AI workloads needed CPUs for storage, checkpointing, preprocessing, and light inference orchestration. Simple inference was “send string, get string back,” so CPU demand was modest.

- **Agentic models changed the CPU equation.** With o1-style reasoning and agentic workflows, models now do multi-step actions: call databases, scrape, run cron/server tasks, execute code, compile, run unit tests, use sandboxes, and interact with external environments. Each step creates CPU work.

- **RL moved from regex checks to heavy environments.** Earlier verification could be regex or simple classifiers. Now RL loops use code compilation, unit tests, databases, agentic flows, physics/biology simulations, world models, and other CPU-heavy environments.

- **The generator-verifier loop is tightening.** GPU model generates actions; CPU verifier/environment checks them; result feeds back into training. As agents get longer horizons and verify more often, CPU demand rises nonlinearly.

- **Code-agent revenue exploded.** Dylan says code-agent revenue went from a couple billion to **north of $10B** in a very short period, while agent horizons expanded dramatically — e.g. Codex-style agents working **6–7 hours**.

- **Cloud CPU scarcity is already visible.** He claims the entire cloud market has run out of CPUs over the last six months. Example symptom: GitHub instability, which he attributes to Microsoft selling/spending spare CPU capacity internally and externally for Anthropic/OpenAI-style deals.

- **GPU:CPU ratio is compressing.** Historically, something like **100 MW of GPUs** could be served by **~1 MW or less of CPUs**. Now RL and agentic inference require much more CPU per GPU.

- **OpenAI/Amazon deal partly about CPUs.** Dylan says OpenAI needed money and compute, but also effectively went to Amazon for CPUs. OpenAI’s stack was mainly x86, but Amazon had lots of ARM/Graviton CPUs, so OpenAI was willing to port code to get capacity.

- **CPU market is becoming capacity-constrained.** Intel and AMD are sold out and sending price-increase notices. They are less competing on price and more asking: how many can we make and sell?

- **ARM/x86 heterogeneity rises because capacity matters.** In a gold rush, even “broken pickaxes” can sell. Amazon Graviton, Nvidia Grace/Vera, Intel, AMD, and other CPUs all matter if workloads can be ported.

- **Long-running agent sandboxes are a new primitive.** The host talks about Windows sandboxes for finance/support/legacy software. Agents that interact with legacy GUIs or enterprise software need CPU boxes running for long periods, not just GPU inference.

- **Scale is already shocking.** One customer reportedly ran **1 million CPU workloads in six hours** on a small cloud. Dylan says large AI labs’ workload/contract scale is even more extreme.

- **Warm CPU pools become rational.** If GPUs are under long-term contract and expensive, users will keep CPU verifiers/environments hot so GPUs never idle waiting for CPU spin-up. Idle GPU time is more expensive than overpaying for ready CPUs.

- **Next-gen GPUs make CPU stress worse, not better.** Blackwell/Rubin-class GPUs get more powerful and expensive. Each GPU can drive more concurrent CPU work, simulations, verifications, and agent tasks. CPU count per GPU may rise even if CPU unit economics improve.

- **PC/laptop market feels the pressure.** Dylan says Mac minis are hard to get; people are buying them for Claude Code/dev workflows. Datacenters are inelastic buyers, so consumer PCs/laptops compete with AI demand for CPUs, DRAM, and SSDs.

- **Memory and storage prices are also squeezed.** Dylan says memory is up roughly **4x** over the last year and likely keeps rising; SSDs are up **3–4x** and could rise another **~60%**. CPU, RAM, SSD, and GPU scarcity are now linked.

- **Intel gets a short-term lift, not a full salvation.** Higher CPU demand helps Intel near-term, but Dylan is skeptical this alone “saves” Intel long-term. AMD, Amazon, and others can catch up on capacity.

- **TSMC leading-node capacity is crowding out everyone.** AI demand is consuming 3nm and future 2nm capacity. Apple and others get squeezed. Nvidia buying Groq is partly framed as wanting inference capacity on Samsung because TSMC 3nm is scarce.

## YK / investor read-through

- **Bottleneck rotation:** GPU scarcity created the first AI trade. Now scarcity is broadening to CPU, DRAM, SSD, sandboxes, orchestration, and verifier environments.

- **CPU is no longer “boring cloud plumbing.”** Agentic workloads make CPU an active part of the AI inference/training loop. Watch AMD/Intel/ARM/Graviton/Grace exposure, but distinguish short-term cyclical pricing from durable moat.

- **Neo-cloud edge is software + reliability, not just cheap GPUs.** Bare-metal rental compresses. Managed RL, sandboxing, observability, orchestration, and warm-pool economics are where differentiation can sit.

- **Agent infrastructure is a new stack.** The key primitive is not just model inference; it is long-running task execution with browser/OS sandboxes, verifiers, state, databases, code execution, and schedulers.

- **Structural edge claim:** market pays whoever correctly underwrites the next binding resource in the agent loop. GPUs remain important, but CPU/RAM/SSD/environment capacity can become the marginal constraint as agents and RL scale.

## One-line summary

Dylan’s 2026 datacenter thesis: AI agents turn CPUs, RAM, SSDs, sandboxes, and verifier environments into first-class bottlenecks — the next trade is not just “more GPUs,” but the whole agent-execution supply chain.
