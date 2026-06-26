# Cooking with OpenAI’s Research Chief: AGI, o1, Evals, and Scaling Laws — Mark Chen

Source: https://www.youtube.com/watch?v=fpAthTtha8c

## TL;DR

Latent Space interviews OpenAI Chief Research Officer Mark Chen while cooking Korean tofu stew. The core thread: OpenAI still believes scaling laws hold, reasoning/RL is one of the biggest recent unlocks, evals are now a bottleneck, and the next frontier is agents that can do long-horizon real-world work while learning from context across tasks.

## Key insights

- Mark Chen is strongly pro-scaling. He rejects takes like “pre-training is dead” or “language models cannot get to AGI,” arguing that every prior bottleneck has been broken by better research, data, engineering, or scaling.

- He says scaling laws have held across “almost 10 orders of magnitude,” and sees no fundamental reason they stop now. His view: each wall looks hard until a new technique or engineering path unlocks the next regime.

- Reasoning was a major contrarian bet inside OpenAI. The first public breakthrough was `o1`, but it initially competed against the dominant pre-training + post-training paradigm. Even inside OpenAI, people asked why chase reasoning when the existing machine looked so strong.

- RL works best where feedback is objective. Math, coding, and computer science are good domains because answers can be graded. Creative writing or consulting-like work is harder because quality is subjective and context is scattered.

- Coding is a key eval/work domain because it combines real-world context, long horizons, and clear-ish success signals. Chen says people are waking up to agents doing meaningful professional work, especially in coding.

- He frames “Move 37” moments as now appearing across fields: math, computer science, coding, and research. Models are producing surprising moves, theorem-level insights, and cross-domain connections.

- OpenAI’s high-level research stack: pre-training for world knowledge, RL for reasoning and chaining insights, and alignment/post-training. They try to scale the mainline in each area while also funding new bets that could change scaling properties.

- Compute allocation is a major management lever. Chen wants a stable high-level roadmap, but periodically reallocates compute toward the highest-priority bets. He describes giving big blocks of compute to major bets while leaving org leads flexible pools.

- Research management means choosing from hundreds of possible projects. He wants 3–5 major bets per org tied to the roadmap, with managers empowered on execution.

- Evals are in crisis. Many canonical benchmarks are saturated, and models can be “bench maxed” by overtraining on distributions similar to the benchmark. Strong benchmark numbers may not generalize to real usage.

- Deployment itself becomes an eval. Once models are used broadly, OpenAI can observe where they fail in real math/coding/software workflows, not just static tests.

- Codex-like tools speed up eval creation. Chen says one person can now build high-quality evals much faster, which helps address benchmark scarcity.

- Human advantage is still context and continual learning. Models have jagged capabilities: sometimes superhuman at narrow tasks, weak at things humans find natural. A big frontier is learning lessons from one task and applying them to future tasks.

- Continual learning is a “basic primitive” for AGI. Chen does not frame AGI as requiring exactly two or three paradigm breakthroughs, but says OpenAI has many shots on goal and is confident some will work.

- He prefers unified model/infrastructure stacks for modalities. Maintaining many separate stacks is expensive; one core model/research stack can transfer gains across audio, vision, text, and other modalities.

- On failed research bets: frontier labs need to kill ideas honestly when evidence says they are less important than expected. Failed experiments still matter because writeups prevent future teams from rediscovering the same dead end.

## Notable quotes

- “I firmly believe in exponent being on the exponential and in scaling laws.”

- “It’s these fields where things are hard to grade where RL has the least amount of ability to directly apply.”

- “We really are kind of in an evals crisis.”

- “Continual learning is a basic primitive that you have to unlock.”

## YK investor / operator read-through

- Structural implication: frontier AI progress is still being underwritten as a scaling + eval + RL problem, not a “LLMs are tapped out” story.

- Bottleneck watch: compute allocation, eval quality, real-world agent feedback loops, and continual-learning infrastructure matter as much as raw model size.

- For AI infra: Chen’s worldview supports continued demand for training + RL + agentic evaluation compute, not just one-off pre-training clusters.

- For product builders: domains with objective feedback loops should automate faster. Subjective, high-context, messy-context domains remain harder, but likely not safe forever.

## One-line summary

Mark Chen’s view: scaling is still alive, reasoning/RL was the key recent unlock, evals are the new bottleneck, and AGI progress depends on agents that can use context, learn continually, and do real long-horizon work.
