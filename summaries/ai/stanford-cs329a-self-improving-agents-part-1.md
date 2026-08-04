---
title: "Stanford CS329A Self-Improving AI Agents — Part 1: Course Overview"
source: "https://www.youtube.com/watch?v=6YnLB0XbTnI"
video_id: "6YnLB0XbTnI"
channel: "Stanford Online"
instructors:
  - "Aakanksha Chowdhery"
  - "Azalia Mirhoseini"
upload_date: "2026-08-03"
date_summarized: "2026-08-04"
duration: "1:09:38"
tags:
  - ai-agents
  - self-improvement
  - inference-scaling
  - reinforcement-learning
  - verifiers
  - stanford
---

# Stanford CS329A Self-Improving AI Agents — Part 1

Source: [YouTube](https://www.youtube.com/watch?v=6YnLB0XbTnI)  
Course: [Stanford CS329A](https://cs329a.stanford.edu/)

## Source note

Summary uses complete 1:09:38 caption transcript. Main technical lecture ends around 60:30; remainder covers course logistics. Auto-captions occasionally garble model and product names; obvious cases such as Claude Code were normalized.

## Core thesis

AI progress has moved through three scaling regimes:

1. **Pre-training scaling:** more parameters, data, and compute lower prediction loss.
2. **Post-training scaling:** instruction tuning and preference optimization turn base models into useful assistants.
3. **Inference and reinforcement-learning scaling:** models spend more compute searching, verifying, correcting, and learning from generated solutions.

Self-improving agents close loop:

`generate → act → observe → verify → correct → retain useful experience`

Main constraint is no longer generating possibilities. It is obtaining trustworthy feedback that identifies which possibilities are correct.

## From base models to reasoning models

Pre-training teaches next-token prediction over broad data. Larger models gained:

- zero- and few-shot learning;
- chain-of-thought behavior;
- broad task generalization;
- some capabilities that appeared sharply with scale.

ChatGPT added major post-training layers:

- high-quality fine-tuning data;
- instruction tuning;
- chain-of-thought examples;
- RLHF using human preference labels and learned reward models.

Reasoning models extend this by training decomposition, analysis, backtracking, self-correction, alternative proposals, and tool use. Extra reasoning improves math, coding, and data analysis more reliably than subjective writing or editing.

## Test-time compute scaling

Mirhoseini's **Large Language Monkeys** work repeatedly samples fixed model, then selects a successful answer with verifier.

`problem → N stochastic solutions → verifier → accepted solution`

Examples of verifiers:

- code unit tests;
- known math answers;
- rule-based checks;
- reward models or LLM judges when deterministic checks are unavailable.

The study sampled up to `10,000` answers/problem. Smaller models that underperformed GPT-4o at one sample could exceed GPT-4o's **coverage** when given many attempts.

Important caveat: coverage is `pass@k`, not single-answer `pass@1`. For some hard problems, only `3–4` of `10,000` samples were correct. Capability exists in distribution, but system still needs reliable selector. Without verifier, sampling does not reveal which answer is right.

Parallel sampling reduces wall-clock latency when enough hardware exists, but not total compute cost. Temperature increases diversity only within useful range; lecturer says values above roughly `1.2` often degrade into poor output.

## Training and inference become feedback loop

Test-time search can generate verified synthetic training data:

1. sample many reasoning or code traces;
2. execute or verify them;
3. retain successful traces;
4. fine-tune or reinforce model on them;
5. improve future `pass@1`;
6. repeat.

This is self-improvement mechanism behind reasoning-model progress. DeepSeek and OpenAI o-series are cited as examples of bringing inference search, verifiable rewards, and RL together.

The lecturers explicitly say field does not fully understand how much improvement comes from pre-training capability versus RL elicitation and refinement. Both currently matter.

## From chatbot to agent

Chatbot answers prompt. Agent receives goal and operates over time:

- infer or clarify intent;
- plan and decompose task;
- take actions through tools;
- observe environment feedback;
- maintain state/memory;
- revise plan;
- decide when task is complete or impossible.

Current real systems remain largely constrained workflows rather than fully autonomous open-ended agents.

Common patterns:

- **Prompt chaining:** fixed sequence of subtasks.
- **Routing:** send task down simple or complex path.
- **Parallelization:** run independent subtasks concurrently, then aggregate.
- **Orchestrator-worker:** manager model plans and dispatches workers.
- **Evaluator/critic:** model grades another model's output.
- **Verifier loop:** deterministic execution feedback drives correction.

Coding and deep research show strongest current signs of end-to-end usefulness.

## Why coding agents improved

Basic architecture—read files, edit code, run commands, inspect failures, repeat—has not changed much.

Reliability improved through:

- stronger base models;
- better multi-step reasoning;
- reinforcement learning with verifiable rewards;
- test generation;
- execution feedback;
- self-correction.

High-value tasks mentioned:

- code migrations;
- dependency/version upgrades;
- repository restructuring;
- data engineering and warehouse migration;
- repetitive unit-test generation.

## Central bottleneck: verification

Generation cheap and abundant. Trustworthy judgment scarce.

### Easier domains

- math with known answer;
- code with tests;
- rule-based tasks;
- simulations with measurable outcome.

### Harder domains

- creative writing;
- open-ended research;
- ambiguous user goals;
- science where experiment is expensive;
- judgments without objective ground truth.

LLM judges can scale evaluation but may inherit bias, miss correlated errors, or reward plausible nonsense. Human feedback then becomes bottleneck.

This creates generator-verifier gap: model can propose much more than system can reliably validate.

## Applications

### Customer support

- transcription;
- knowledge assistance;
- suggested replies;
- call summaries;
- emerging end-to-end resolution.

### Deep research

- discover sources;
- create outline;
- summarize evidence;
- synthesize report.

Reliability still depends on source quality and factual verification.

### AI scientist

- brainstorm hypotheses;
- design/iterate experiments;
- help write papers.

Breadth can surface unusual ideas, but hallucination prevents unsupervised scientific trust.

## Operator lessons

1. **Optimize verified success, not generation volume.** More samples only help if selector works.
2. **Use deterministic feedback whenever possible.** Tests and execution beat LLM opinion.
3. **Allocate compute by difficulty.** Easy tasks should not receive same search budget as hard tasks.
4. **Clarify success criteria before running agent.** Ambiguous intent makes verification impossible.
5. **Keep workflows constrained until feedback is robust.** Static graphs often outperform open autonomy.
6. **Measure cost and latency with accuracy.** `10,000` samples can expose latent capability but may be economically useless.
7. **Separate coverage from reliability.** One correct answer somewhere is not production performance.

## Research directions from course

- adaptive test-time compute;
- robust or combined verifiers;
- learning from code/tool feedback;
- multi-step planning and reasoning;
- scaling RL;
- open-ended self-improvement;
- search and deep-research agents;
- memory;
- multimodal/robotics agents;
- AI scientists and automatic agent design.

## What would falsify self-improvement thesis

- verifier errors grow with generator capability;
- RL optimizes benchmark or reward-model loopholes rather than real outcomes;
- synthetic data collapses diversity or reinforces errors;
- compute costs rise faster than verified-task value;
- open-ended domains remain human-feedback bound;
- agents fail over long horizons despite strong short-task benchmarks.

## Bottom line

Durable agent edge is not more autonomous-looking prompts. It is a closed, economical, trustworthy feedback loop. Domains with executable ground truth—especially code and math—improve fastest. Open-ended work advances only as verification improves.
