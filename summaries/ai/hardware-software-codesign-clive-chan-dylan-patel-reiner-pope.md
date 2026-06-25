# Hardware-software codesign, with Clive Chan, Dylan Patel and Reiner Pope

Source: https://www.youtube.com/watch?v=zrMYIhmuXEo

## TL;DR

This is a deep technical discussion on hardware/software co-design for AI chips. The core idea: real co-design means jointly changing model architecture and chip architecture, sometimes accepting worse model metrics in isolation if end-to-end energy, latency, utilization, or cost improves. The bottleneck framing shifts from “best model on today’s GPU” to “best intelligence per joule / dollar / latency on the future system.”

## Key insights

- **Co-design means optimizing both model and hardware together.** Reiner defines it as making software and hardware better jointly, instead of assuming a fixed workload or fixed chip. The point is to make sacrifices today that pay off when the future hardware and model are tuned together.

- **The keyword is sacrifice.** A normal ML paper says: “my architecture improves metrics.” A co-design result can say: “some metrics look worse on current GPUs, but the architecture has lower gate count, energy cost, or better intelligence per picojoule once hardware is built for it.”

- **Activation functions are a simple example.** Swish needs exponentials, lookup tables, polynomial approximations, and multipliers; ReLU is trivial hardware. ReLU may be lower-quality for the model, but could win if the energy/cost savings dominate.

- **Matrix/tensor-core width illustrates model-shape co-design.** A wider tensor core gives more arithmetic in one place, but models must be wide enough to use it. If researchers make models wider, the model may be less ML-efficient in isolation but more hardware-efficient overall.

- **DeepSeek-style optimization is adjacent, but narrower.** Dylan cites DeepSeek V3 attention matching Hopper arithmetic intensity and Chinese labs reducing layers to improve inference speed. The speakers distinguish this from full co-design: it adapts a model to existing hardware, whereas full co-design trades off model and chip together.

- **Nvidia-style design is hardware-for-models.** Nvidia listens to model labs and implements requested hardware features; OpenAI/Nvidia-style “co-designed with Blackwell” is a ping-pong relationship between model designers and hardware designers.

- **Researchers may hate well-co-designed chips.** A chip with a wide basin of workloads is flexible but may leave efficiency on the table. A narrow chip that forces the model into a specific efficient shape can be better economically but painful for researchers.

- **TPU V6E / Trillium example:** Dylan says researchers complain it has roughly **1 petaflop compute** and **32GB HBM**, a weird ratio versus Hopper. The point: a chip can make sense for certain production workloads while constraining research flexibility.

- **Dojo shows over-specialization risk.** Tesla’s Dojo-like designs were strong for certain data-local/locality-heavy workloads, but weak if model architectures move toward regimes needing much more memory bandwidth. If silicon bakes in the wrong future, it becomes stranded.

- **Chips are physically two-dimensional.** Layout matters. Systolic arrays map naturally to 2D chips; architectures needing many processors connected to a shared L1/L2 cache are harder to embed efficiently on silicon.

- **Racks add another topology layer.** At cluster/rack scale, networking topology matters: TPU torus/dragonfly-style designs, Nvidia switched/all-to-all fabrics, and other interconnect choices all shape feasible model parallelism.

- **Hardware designers must predict model trends.** Like ML researchers extrapolate scaling loss before launching a big run, chip designers must infer where model shapes will be by the time silicon arrives. Exact prediction is impossible; robust bets are around resources models are increasingly able to use.

- **Transformer specialization has limits.** You can specialize for large matrix multiplies and parts of attention, but fully burning a whole transformer architecture into silicon is dangerous because research directions can change.

- **Pretraining-to-sampling shift is the central cautionary tale.** In 2022 many people optimized for pretraining. Then reasoning/test-time scaling made sampling/decode much more important. Decode has low arithmetic intensity and high memory-bandwidth demand, changing the hardware target.

- **Labs need to hedge across hardware.** If a lab had built a chip only for pretraining, it may have been pointed the wrong way once reasoning/sampling dominated. This is why flexibility matters, especially for companies that cannot afford a failed chip generation.

- **Nvidia can hedge with multiple products.** The discussion mentions Nvidia branching into different bets: mainline GPUs, CPX/high-arithmetic-intensity products, and Groq-like/3D-DRAM-ish directions. Smaller chip companies often cannot fund multiple simultaneous bets.

- **Low-latency decode creates niches.** For thinking/reasoning models, latency matters. SRAM is the cleanest route for very low latency, while 3D-stacked DRAM may approximate some of the benefits for specific use cases.

- **Decode leaves compute idle.** Lab pricing implies prefill tokens can be around **5x cheaper** than decode tokens. The speakers infer decode has lots of idle compute, maybe **~80%** of FLOPs sitting unused in some regimes.

- **One research idea: use idle decode compute by growing MLPs.** If decode is memory/latency constrained with idle math units, make the MLP bigger — e.g. “crank up the MLP size by 5x” — to use spare FLOPs rather than leave them idle.

- **Disaggregation is a rising theme.** First: separate prefill and decode. Then: run them on different chips. Next possible step: disaggregate MLP and attention, with different memory systems — e.g. MLP weights in SRAM/3D RAM and attention leaning on HBM.

- **Quantization claims can be misleading.** The speakers dislike papers claiming “97% as accurate” if the real effect is closer to downgrading a 70B model into an 8B-quality model. MMLU/perplexity deltas can hide large economic/quality tradeoffs.

- **Better metric: same quality, lower energy.** Reiner says the fair comparison is: how much larger must the model be to recover the same quality after a compression/quantization approach? He mentions needing roughly **40% larger model** to hit same quality in their context; a better paper might get that to **35%**.

- **Dylan’s preferred framing: perplexity per picojoule.** Same quality, less energy per generated token is the right metric. “Perplexity per picojoule” is shorthand for model quality normalized by energy/system cost, not benchmark-chasing.

## YK / investor read-through

- **Structural edge claim:** the market pays chip winners that correctly co-optimize model shape, memory hierarchy, interconnect, and software stack around the next dominant workload. Wrong workload prediction strands silicon.

- **This is why Nvidia’s moat is hard.** Nvidia is not only selling fast chips; it sits in the feedback loop with model labs, software, compilers, memory systems, networking, and product hedges. That lets it adapt as workloads rotate.

- **Custom ASIC upside exists, but only for narrow, stable bottlenecks.** If the workload is stable — low-latency decode, MLP-heavy inference, specific attention patterns, high-volume production inference — specialization can win. If the model frontier shifts, specialization can die.

- **Watch for “benchmark-good, system-bad” claims.** Quantization/compression/startup chip claims need same-quality comparisons: energy/token, latency/token, capex per served token, and how much model size must increase to recover quality.

- **The next battleground is disaggregated inference.** Prefill vs decode, attention vs MLP, SRAM/3D DRAM vs HBM, and specialized verifier/sampling paths are all areas where new chip architectures can wedge in.

- **Best investor question:** what workload is stable enough to harden into silicon, and what part still needs GPU-like flexibility?

## One-line summary

Co-design is the art of sacrificing local model or chip metrics to win on full-system intelligence per joule — powerful when the workload is stable, dangerous when the AI paradigm shifts under the silicon roadmap.
