---
title: "How to Understand the Next Wave of AI Before Everyone Else"
source: "https://www.youtube.com/watch?v=4qjEgPojjzM"
video_id: "4qjEgPojjzM"
channel: "Matthew Berman"
upload_date: "2026-08-24"
date_summarized: "2026-08-31"
guest: "Tibo, OpenAI"
---

# How to Understand the Next Wave of AI Before Everyone Else

## TLDR

OpenAI's Tibo expects AI to move from a chat box toward one adaptive, multimodal personal agent that knows the user, operates tools and performs coding or non-coding work through the same interface. Faster inference matters because it changes workflow design: serial interaction becomes real-time creation, while cloud agents escape the human-scale limits of a laptop.

## Structural edge claim

OpenAI's claimed edge is the combination of frontier models, preplanned compute, ChatGPT distribution, rapid product iteration and model-assisted optimization of its own inference stack. The market may pay OpenAI if these reinforce each other faster than model intelligence commoditizes. Claims in the interview are management/product claims, not independently benchmarked evidence.

## Product direction

- ChatGPT and Codex are converging into one underlying agent and harness rather than separate products for technical and nontechnical users.
- The interface should adapt to each person instead of forcing users to choose labels such as coder, designer or salesperson.
- Voice, vision, ambient context and tool access make the agent a natural extension of human communication. Tibo already uses voice dictation to issue morning tasks.
- Two paths coexist: a personal agent working closely with one person, and autonomous systems operating complex workflows such as production-log investigation and bug reproduction.
- Cloud agents become necessary because laptops and conventional applications were designed around human typing speed and attention, not hundreds of concurrent machine tasks.

## Speed changes the workflow

The interview says ultra-fast mode can deliver up to roughly **14×** raw generation speed, but tool-heavy workflows may realize only **3–4×** because network, tool-call and execution latency become bottlenecks.

Useful cases include:

- incident response, where every second matters;
- generating large amounts of code;
- interactive websites, games and prototypes;
- rapidly testing several designs before committing;
- keeping a user in one task rather than supervising many slow agents.

Tibo expects today's ultra-fast performance to become close to default within **1–2 years**, while a premium tier remains available through greater hardware allocation.

## Distribution and economics

- The interviewer says Codex reached **20 million users**; Tibo attributes growth partly to merging it into ChatGPT's broad distribution.
- OpenAI resets usage limits after outages or poor experiences, framing free usage as customer compensation and community goodwill rather than a formal marketing campaign.
- Tibo says OpenAI planned compute capacity years ahead and now divides it between research and products.
- He claims ordinary inference became roughly **60% faster in three months** through full-stack optimization.
- In the example discussed, a stronger model helped optimize a smaller model's serving stack, contributing to an **80% price reduction** while preserving the compute envelope despite higher throughput.

## Recursive improvement

The near-term version is not necessarily an uncontrolled model rewriting itself. Models improve the surrounding system:

- serving architecture;
- CUDA kernels;
- inference efficiency;
- agent harnesses;
- cloud-agent workflows;
- products used by researchers and engineers.

This creates an indirect feedback loop: better models improve infrastructure, which makes models cheaper and faster to use, which accelerates the humans and agents building the next system.

## Safety and culture

Tibo contrasts OpenAI's bottom-up shipping culture with Google's reluctance to disrupt established products. The operating rule is fast user feedback plus willingness to cannibalize existing products, balanced by simplicity and product quality.

He says frontier RL training was paused while teams strengthened alignment and safety systems, then restarted after the safety organization established principles for readiness. No technical thresholds or audit evidence were disclosed, so this remains a high-level company account.

## Investor/operator read

The important bottleneck rotates as tokens accelerate: model latency gives way to tool latency, network overhead, CPU execution and human attention. Winners must optimize the entire `model → harness → tools → compute → interface` path.

**Kill tests:** distribution does not convert into retained paid use; inference price falls faster than cost; tool reliability stalls; cloud-agent concurrency creates more review work than useful output; or open models replicate capability while application and distribution moats weaken.
