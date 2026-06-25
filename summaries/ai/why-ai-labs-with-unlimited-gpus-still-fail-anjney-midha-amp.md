# Why AI Labs With Unlimited GPUs Still Fail — Anjney Midha, AMP

Source: https://www.youtube.com/watch?v=h5dlIPM0X18

## TL;DR

Anjney Midha’s core point: AI is not compute-constrained in the naive sense; it is alignment/culture/infrastructure-constrained. Labs can have money and GPUs and still fail if incentives, scheduling, trust boundaries, and mission trade-offs are lossy.

## Key insights

- **GPU utilization is an organizational problem, not just an infra metric.** He says Google-style node utilization should be around **95–96%**, with 95% almost treated like an outage. Best-in-class MFU is roughly **60–70%**. Most single-tenant clusters are below this because capital, deployment, measurement, and model teams are too far apart.

- **AI scaling raises the cost of dumb infrastructure.** His framing: new model capability does not repeal common sense. “Move fast and break things” became “move fast with stable infrastructure”; for AI data centers, it should become “move fast with responsible infrastructure.” Wasted compute is now economically and politically expensive.

- **Data-center politics matter.** He claims up to roughly **20%** of US data centers this year may face community-support risk, though he admits that number may be overstated. His proposed fix: make the local benefit legible, e.g. charge slightly more per compute-hour and route the marginal amount back to the local community or electricity bills.

- **AMP wants to be a compute grid / ISO, not just another neo-cloud.** He describes AMP Grid as doing for compute what the electric grid did for power: pooling stranded capacity, coordinating demand/supply, and making “megaflops flow like megawatts.” Economically, he compares AMP to an **independent system operator** like PJM, not an asset-owning cloud.

- **Fungibility is the bottleneck.** Today compute pools are fragmented across clouds, silicon, scheduler stacks, and commercial relationships. AMP starts at scheduling and economics, but the bigger ambition is multi-cloud, multi-silicon coordination.

- **DeepMind/Google is framed as a market-failure case.** He argues a lot of frontier research inside DeepMind never ships or even gets published because internal business priorities embargo it. The published papers may be adversely selected: the best commercially useful work stays locked up. AMP/Foundry wants to unlock displaced frontier teams.

- **Scale of demand is huge.** He mentions **1.3 GW** of desired base-load compute demand, translating it to roughly **$40B of cloud spend**, and says spike capacity could need around **6 GW** over four years. He is careful that this is demand/target capacity, not fully secured supply.

- **“Output maxing” is the philosophy.** The broader discipline he wants is not just AI or infra; it is maximizing output from scarce resources. Examples span GPUs, Medicare/end-of-life care, research talent, and data-center power.

- **Alignment degrades at every abstraction boundary.** As systems scale, division of labor creates APIs, interfaces, and handoffs. Each adds “lossy transmission.” His engineering question: can we scale up/out without losing alignment?

- **Two ways to reduce loss: standards or new abundance.** Either standardize protocols/interfaces so communication becomes less lossy, or invent a new capability, like room-temperature superconductors, that creates so much capacity the old bottleneck matters less.

- **Chip startups need trust boundaries.** For accelerator companies, the issue is not just chip design. Co-design requires early visibility into future model architectures, but a founder outside Google/OpenAI/Anthropic no longer sits inside the trust boundary. This is why independent labs, chip teams, and investors need deeper coordination.

- **Nvidia’s ecosystem is a standard others can piggyback on.** He praises teams that use Nvidia’s reference architecture rather than trying to reinvent the whole data-center stack. His read: demand is so high that more chips are needed; the opportunity is to innovate at the right layer, not fight the whole ecosystem.

- **Culture beats “moat,” but culture is fragile.** He rejects static moats. Culture only works if replenished daily through actions that prove mission alignment. Quote: “Culture is not a set of beliefs. It’s a set of actions.”

- **Why rich AI labs still fail.** His diagnosis: some labs have cash and compute but do not ship because there is no hardship, no sharp P0, and no trade-off pressure. Without scarcity/crisis, culture stays fuzzy and brittle.

- **Anthropic is used as the positive example.** He says early hardship forced Anthropic to do more with less, build efficiency, and clarify its P0. In his telling, their focus on coding was the mechanism: if they cracked coding, they believed it could generalize toward AGI.

- **First-principles thinking is unusually valuable now.** He criticizes VCs for treating prior-cycle heuristics as axioms. In a regime shift, analogy is dangerous; the winners are people who can reason from the actual system and bottlenecks.

## YK/investor read-through

- **AI infra edge is shifting from “who owns GPUs?” to “who raises realized utilization?”** If AMP is right, the scarce asset is not only chips/power, but coordination across fragmented compute pools.

- **Neo-clouds are not all the same.** Asset-heavy clouds warehouse supply. AMP wants to be a neutral scheduling/economic layer. That is a different margin profile, trust requirement, and failure mode.

- **Community backlash is a real AI-capex constraint.** Data-center permitting, grid load, local power prices, and community benefit-sharing may become as important as chip procurement.

- **Culture is underwritten like a production system.** In frontier labs, excess funding may reduce discipline. Scarcity can be useful if it forces P0 clarity and fast feedback loops.

- **Structural edge claim:** AMP’s edge is not “more GPUs.” It is liquidity provision / market-structure design for compute: pooling fragmented supply and demand, reducing stranded capacity, and becoming a trusted coordination layer.

## Best lines

- “MegaFLOPs flow like megawatts.”
- “Culture is not a set of beliefs. It’s a set of actions.”
- “The number of people who use heuristics as axioms...”
- “There are so many AI labs today that have all the cash they need, all the compute they need, and they’re still not able to ship.”

## One-line summary

The episode is really about AI’s hidden bottleneck: not GPUs alone, but lossy coordination between compute, capital, talent, culture, and trust.
