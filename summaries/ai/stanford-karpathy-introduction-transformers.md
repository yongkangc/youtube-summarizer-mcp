---
title: "Stanford CS25: Introduction to Transformers with Andrej Karpathy"
source: "https://www.youtube.com/watch?v=XfpMkf4rD6E"
video_id: "XfpMkf4rD6E"
channel: "Stanford Online"
speaker: "Andrej Karpathy"
lecture_date: "2023-01-10"
published: "2023-05-19"
duration: "1:11:35"
date_summarized: "2026-07-27"
category: "ai"
---

# Introduction to Transformers with Andrej Karpathy

## TLDR

Karpathy explains Transformer as general-purpose message-passing computer. Each token stores vector; attention lets tokens exchange relevant information; MLP computes locally at each token. Repeating these blocks produces architecture expressive enough for language, images, audio, RL and biology, while remaining parallel and GPU-friendly.

Transformer won not only because attention models context. It simultaneously offers:

1. expressive forward pass;
2. stable gradient optimization;
3. efficient shallow-wide computation on GPUs;
4. runtime programmability through prompts/in-context learning.

## Historical arc `[10:39]`

Before 2012, AI fields used separate hand-engineered pipelines:

- computer vision: feature descriptors + SVM;
- NLP: parsing, tagging and field-specific machinery;
- speech/RL: different vocabularies and algorithms.

AlexNet showed large neural networks improve with data and compute. Fields converged onto common differentiable toolkit.

2017 Transformer pushed convergence further: largely same architecture can process any domain once inputs become token-like vectors.

Karpathy speculates this uniformity may resemble cortex's relatively homogeneous computation. Interesting analogy—not established neuroscience result.

## Why attention emerged `[14:00]`

Early neural language model predicted next word from fixed small window.

Sequence-to-sequence translation used:

`English sentence → encoder LSTM → one context vector → decoder LSTM → French sentence`

Problem: entire source sentence compressed into one fixed vector—**encoder bottleneck**.

Bahdanau attention let decoder softly search all encoder states for source information relevant to current output word. Transformer removed recurrence and made attention primary communication mechanism.

## Attention in plain English `[21:00]`

Karpathy models Transformer as directed graph:

- each token = node;
- each node holds vector/private state;
- attention = nodes communicating;
- MLP = each node thinking locally.

Each token generates:

- **Query:** what information am I looking for?
- **Key:** what information do I contain?
- **Value:** what information will I send if selected?

Mechanism:

1. Compare destination query against source keys using dot products.
2. Scale and softmax scores into weights.
3. Compute weighted sum of source values.
4. Add result back into destination representation.

Compact equation:

`Attention(Q,K,V) = softmax(QKᵀ / √d) V`

The `√d` scaling prevents dot-product variance from making softmax too peaky as dimension grows.

## Multi-head and multi-layer `[27:00]`

- **Heads:** independent attention operations in parallel. Each can seek different relationships.
- **Layers:** communication/computation blocks applied sequentially. Later layers reason over representations built earlier.

Transformer block:

1. LayerNorm.
2. Multi-head self-attention—communication.
3. Residual addition.
4. LayerNorm.
5. MLP/feed-forward network—computation at each token.
6. Residual addition.

Residual pathways and normalization help gradients flow through deep model. MLP commonly expands representation about `4×`, applies nonlinearity, then projects back.

## Decoder-only GPT `[30:00]`

Text converted into integer tokens. Model adds:

- token embedding—what token is;
- positional embedding—where token sits.

GPT receives context and predicts next token distribution. Training target is same sequence shifted one position.

Causal mask blocks future tokens. Positions may attend only to themselves and earlier positions. Forbidden scores set to negative infinity before softmax, yielding zero probability.

Generation loop:

1. Prompt model.
2. Sample next token.
3. Append token.
4. Run model again.
5. Repeat.

When sequence exceeds context window, oldest tokens must be cropped or handled through another memory mechanism.

## Three Transformer families `[42:00]`

### Encoder-only — BERT

All tokens communicate bidirectionally. Useful for classification, embeddings and understanding tasks.

### Decoder-only — GPT

Causal attention. Predicts next token and generates autoregressively.

### Encoder-decoder — T5/translation

Encoder tokens communicate fully. Decoder uses:

- causal self-attention over prior outputs;
- cross-attention where decoder supplies queries and encoder supplies keys/values.

## Why architecture generalizes `[51:00]`

Transformer naturally processes sets of vectors. Tokenization defines problem:

- text → word/subword tokens;
- images → patches;
- audio → spectrogram slices;
- RL → states/actions/rewards;
- proteins → amino-acid/residue representations;
- multimodal systems → mixed token types plus modality/position embeddings.

Instead of hand-designing every cross-modal interaction, place vectors in common context and let attention learn communication.

Low inductive bias helps at huge data scale. With small datasets, stronger priors—convolutions, local attention, known geometry—may improve sample efficiency.

## In-context learning `[55:00]`

GPT-3 accuracy improves when examples appear in prompt even without gradient updates.

Karpathy frames this as inner/outer learning:

- **Outer loop:** gradient descent changes model weights during training.
- **Inner loop:** prompt reconfigures behavior through activations at inference time.

Transformer becomes general-purpose text computer whose runtime program is prompt/document completion.

Some research suggests activations may implement learning-like algorithms such as regression. In lecture this remains hypothesis, not settled explanation.

## Why Transformer beat RNN `[58:00]`

RNN may theoretically compute general programs, but computation graph is long and serial:

`token1 → token2 → token3 → ...`

Problems:

- poor hardware parallelism;
- long gradient paths;
- harder optimization;
- lower scalable compute throughput.

Transformer is shallow and wide:

- tokens processed in parallel during training/prefill;
- residual paths shorten gradient travel;
- matrix multiplications map well to GPUs;
- scale can increase efficiently.

Karpathy's preferred name for architecture:

> **General-purpose efficient optimizable computer.**

## Limitations `[07:30, 42:00, 48:00]`

- attention cost/memory grows approximately `O(n²)` with context length;
- fixed context limits memory;
- autoregressive output commits token by token;
- long-term/external memory remains incomplete;
- outputs can be stochastic and hard to control;
- minimal inductive bias demands large data/compute.

Karpathy finds iterative/diffusion-like text generation conceptually appealing because humans draft and revise rather than irrevocably commit each token.

## Systems implications

Transformer's training/prefill parallelism drove accelerator demand. But decode remains sequential by generated token and repeatedly streams weights/KV cache.

Memory pressure comes from:

- model weights;
- optimizer states during training;
- activations;
- attention matrices;
- KV cache across context and concurrent users.

Longer context increases both compute and memory; attention's quadratic component explains pressure toward FlashAttention, sparse/local attention, efficient positional schemes and external memory.

Lecture predates many current long-context and agent systems, so its `1K–4K` context examples are historical, not current limits.

## Theory of edge

> Transformer won because architecture matched both problem and hardware: flexible global communication, stable optimization and parallel matrix computation.

Commercial implication: durable value accrues not only to model architecture—which is widely known—but to data, compute/memory/network efficiency, inference serving, distribution and product feedback loops.

## What to remember

1. Token = vector-bearing node.
2. Attention = data-dependent communication.
3. MLP = local computation.
4. Query asks; key advertises; value transmits.
5. Heads communicate in parallel; layers refine sequentially.
6. Causal mask prevents future leakage.
7. Prompt reprograms model at runtime.
8. Architecture scales because it is GPU-efficient and optimizable—not merely expressive.

## Bottom line

Transformer is less “language trick” than reusable computational substrate. Convert domain into tokens, define allowed connections, then alternate communication and computation. Its power comes from joint fit among representation, optimization and hardware scale.