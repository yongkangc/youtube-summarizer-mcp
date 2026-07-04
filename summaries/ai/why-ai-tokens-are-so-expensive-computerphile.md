# Why AI Tokens are so Expensive — Computerphile

Source: https://www.youtube.com/watch?v=-0HRzXk8vlk

## TLDR

Computerphile explains why AI tokens get expensive, especially for coding agents. A token is just a word or piece of a word, but LLMs generate output one token at a time, repeatedly re-reading the growing context. Coding agents multiply this cost because every tool call, file read, hidden reasoning step, patch, and follow-up gets added back into the context. Cheap flat-rate agent plans were always subsidized; token-based pricing exposes the real compute cost.

## What is a token?

- A token is usually a word, part of a word, punctuation mark, space-included fragment, code symbol, or character sequence.
- The exact split depends on the tokenizer.
- Common words like “the” may be one token.
- Code symbols, punctuation, spaces, Unicode characters, and non-English text all become tokens too.
- Modern models may have vocabularies around **100k tokens**, covering English, other languages, code, symbols, and rare Unicode.

## Why tokens cost compute

- LLMs are autoregressive: they take the input context, run the model, and predict **one next token**.
- To produce a long answer, they repeat this process token by token.
- Each new output token is appended back into the context, so the next prediction sees the original prompt plus everything generated so far.
- So a 10,000-token reasoning trace is not one cheap action; it means thousands of forward passes through the model.

## System prompts add hidden cost

- Every request includes hidden instructions:
  - system prompt
  - safety rules
  - product instructions
  - current time / OS / user context
- Example given: a user may ask a short 100-token question, but it is combined with a 1,000-token system prompt before the model even starts.
- Then hidden “thinking” and visible answer tokens add more cost.

## Caching helps, but does not eliminate the problem

- Providers can cache intermediate model state so repeated prefixes do not need to be recomputed from scratch.
- But caches have time-to-live limits and cannot stay in GPU memory forever.
- If the user pauses, the provider may need to “prefill” the context again later.
- Caching improves efficiency, but long conversations and large contexts still get expensive.

## Why normal chatbot use is cheaper

- Simple Q&A often has small context and short answers.
- Asking “what did the cat sit on?” does not cost much.
- The problem appears when context grows over multiple turns or when the model must inspect large documents/codebases.

## Why coding agents are expensive

Coding agents are expensive because they do not just answer. They act:

- read files
- inspect code
- make tool calls
- think between steps
- patch files
- verify results
- summarize what they did

Each step adds tokens.

Example bug-fix flow:

- system prompt: thousands of tokens
- user bug report: hundreds of tokens
- hidden thinking: thousands of output tokens
- tool call to read file: small output
- file contents returned: maybe **5,000 tokens**
- more thinking
- second file read: more file tokens
- patch diff: more output tokens
- success result and final response

Because each later model call includes the earlier prompt, thoughts, tool results, and file contents, the input size keeps ballooning.

## Concrete example from the video

A simple agentic bug-fix example that reads only two files can hit roughly:

- **55k–60k input tokens**
- plus several thousand output tokens

That is before retries or follow-up prompts.

Then he shows a real GitHub Copilot CLI toy project: a Windows 3.11-style starfield screensaver.

After only around **5–6 prompts**, using initially one file and later three files, the session consumed about:

- **2 million input tokens**
- **47,000 output tokens**

That is the core reason agentic coding plans are getting capped or repriced.

## Pricing numbers mentioned

He gives rough provider pricing:

- input tokens: around **$2–3 per million**
- output tokens: around **$15 per million**

Output is usually much more expensive because it requires sequential generation and active compute.

## Why GitHub Copilot / Anthropic caps changed

- Flat monthly pricing encouraged users to run very long agent sessions.
- If an agent can run for hours reading files and generating millions of tokens, the provider eats huge compute cost.
- Moving from request-based pricing to token-credit pricing was “inevitable” because the old model was subsidized.

## Bad metric: “tokens used”

He criticizes companies measuring AI adoption by token volume.

Analogy:

- measuring driver quality by how fast they wear through tires
- measuring broom productivity by how many times someone moves the broom back and forth

High token usage can mean waste, loops, bad prompts, oversized context, or inefficient agents.

## Practical implication

Agentic coding will be useful, but the expensive part is letting the agent freely read files, think for a long time, and keep growing context. Lightweight completion and local context tasks are much cheaper than full autonomous agents.

Over the next year, users will need to learn when to:

- use autocomplete/small context
- use cheaper models
- provide narrower file scope
- avoid long-running loops
- avoid making the model reread huge files repeatedly
- reserve expensive agentic runs for tasks where autonomy is worth the token burn

## My read

This is basically the unit economics behind why AI coding tools are moving from vibes/subsidy to metered usage. The product value is real, but the hidden bill is context replay + tool loops + output reasoning. For operator use, the edge is not “use more tokens”; it is **spend tokens where they replace expensive human search/debug time, and constrain agents hard when the task is simple**.

## One-line summary

Tokens are cheap individually, but coding agents burn millions because every file read, thought, tool call, and follow-up gets fed back into the model again and again.
