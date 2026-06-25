# Claude Code for Finance + The Global Memory Shortage: Doug O'Laughlin, SemiAnalysis

Source: https://www.youtube.com/watch?v=x9rWFiIubmc

## TL;DR

Doug O'Laughlin’s thesis: AI agents are already useful enough to transform finance/research workflows, but they still need expert supervision because they behave like high-throughput junior analysts, not fully autonomous PMs. The investing frame is bottleneck tracking: AI demand is real, memory/fab/power constraints are binding, and the software/hyperscaler stack is being repriced around agents.

## Key insights

- **Claude Code is a junior analyst, not a PM.** Doug repeatedly says these systems make mistakes “all the time.” They can gather, synthesize, chart, code, and automate painful work, but they do not yet develop true meta-level judgment or domain expertise from repetition the way a human junior analyst can.

- **The leverage is already real for experts.** His key caveat: AI massively amplifies people who already know the domain. Experts can spot slop, patch the final 5%, and use the agent to collapse hours/days of work into minutes. Non-experts risk compounding confident garbage.

- **Claude Code / agentic tools feel like the GPT-3.5/4 moment for information work.** Doug says once a tool becomes something he would not give up, he assumes other skilled knowledge workers will eventually adopt it too. He expects Claude Code / co-work style tools to become a baseline layer for information work within ~24 months.

- **Finance workflow change: less Excel/Bloomberg-shaped, more machine-shaped.** If agents can pull data, write code, create charts, and produce images/reports directly, the old human-readable Excel/PowerPoint workflow becomes less central. The machine can deposit the output in whatever form is useful.

- **SemiAnalysis is using agents for charting and research synthesis.** Example: ask the model to absorb SemiAnalysis style, visualization books, chart rules, and datasets, then produce charts in their format. Tokens are cheap enough that reading 70 books vs 3 books is almost the same operational cost.

- **The “find the 1–3 things that matter” problem remains human.** The analyst/PM game is still identifying which facts actually drive the investment decision. AI can gather everything; the edge is deciding what matters.

- **Sub-agents > naive agent teams.** Doug likes task-specific sub-agents because they can go away, solve a bounded problem, and return. He is more skeptical of “agent team” swarms if they are prompt-only and not trained/RL’d for coordination; they can degrade performance.

- **AGI definition is shifting.** Doug says if AGI means “can automate or materially change many common information jobs,” then current systems are making him AGI-pilled. He references GDPval-style benchmarks where models are approaching/exceeding expert parity on many white-collar tasks.

- **Entry-level data analysis is exposed.** He struggles to see how an average 22-year-old data analyst beats a well-designed agentic workflow at recurring tasks like finding interesting quarterly data points, building charts, and summarizing drivers.

- **But learning pipelines may break.** If AI replaces junior grunt work, the industry must solve how new people develop judgment. Historically, the junior analyst became expert by gathering data repeatedly; agents may remove that apprenticeship loop.

- **Memory market work: AI is useful for data assembly, not prophecy.** Doug does not ask the LLM to magically forecast memory prices. He uses it to gather memory prices, paid API data, covariates, macro variables, and structure the analytical dataset faster.

- **AI capex is larger than internet-scale; railroads are the better analogy.** He argues the AI buildout has already passed the internet in absolute size. Railroads are a better historical analog because they created a new layer of economic infrastructure and reshaped finance/banking around enormous capital needs.

- **Microsoft has the most to lose.** His view: Microsoft is the horizontal software company whose products humans use for information work, so agents paint a giant target on Office/Windows/workflow software. Azure helps, but the OpenAI relationship also risks “renting barbarians at the gate.”

- **Hyperscalers face a brutal choice.** Either become dumb-pipe infrastructure for AI workloads or copy/steal/rebuild agent features into their own products and defend the application layer. Doing both poorly is the worst outcome.

- **Oracle’s issue was expectations management.** Doug frames Oracle’s GPU/data-center story as an “own goal”: too much promised too quickly, too much fundraising/buildout all at once, then delays. Better path would have been staged deployment where early GPU revenue helps self-fund the next wave.

- **TPU vs Nvidia: TPU has huge theoretical value, but supply chain matters.** Doug says TPU could be worth enormous value inside Google if it gains meaningful share, but Nvidia still owns the supply chain better. Jensen personally working suppliers matters because HBM, packaging, TSMC, and Korean memory relationships decide who actually gets chips.

- **Memory shortage is structurally messy.** HBM/DRAM demand has been pulled forward hard. If data centers/power are delayed, buyers may eventually pause orders and cause memory price volatility, but aggregate AI demand still looks far larger than available supply.

- **Context windows have physical limits.** Very long context may improve, but full attention over massive token windows runs into physical/computational constraints. “100M token” claims often rely on architectures that do not apply full attention over everything.

- **CPU refresh cycle may re-emerge.** Cloud providers have squeezed non-AI capex to fund GPUs. But coding agents generate more software, and that software runs on CPUs. Old CPU fleets near end-of-life may need refresh, creating another infra demand pocket.

- **Writing advice: LLMs for outlining, not final voice.** Doug dislikes LLM-written prose but likes feeding messy thoughts into an outline, then writing himself. He uses *On Writing Well* as a style skill/reference.

## YK / investor read-through

- **Edge is workflow adoption + bottleneck sequencing.** The useful question is not “is AI good?” but: which workflows now cross the usefulness threshold, and which physical bottleneck captures economics next?

- **Finance AI wedge is real but supervised.** Best use is analyst amplification: data scraping, charting, variant datasets, transcript digestion, and first-pass synthesis. Do not outsource final thesis/judgment.

- **Software incumbents are exposed.** Microsoft/Salesforce/Bloomberg-style interfaces are valuable, but agent-native workflows can unbundle clunky human-facing software.

- **Semis remain bottleneck-rich.** Nvidia’s near-term strength is not just CUDA; it is supply-chain control. TPU/custom ASIC upside exists, but only if supply, HBM, packaging, and datacenter deployment scale.

- **Structural edge claim:** AI agents are productivity leverage for experts and bottleneck detectors for investors. The market pays whoever maps demand growth to the actual scarce layer: memory, packaging, fabs, power, CPUs, or application workflow ownership.

## One-line summary

Doug’s view: Claude Code is already good enough to change finance work, but the trade is not “AI replaces judgment” — it is expert + agent leverage, with memory/supply-chain bottlenecks deciding where the money accrues.
