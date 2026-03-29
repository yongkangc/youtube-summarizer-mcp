**Source**: https://www.youtube.com/watch?app=desktop&v=tND-wBBZ8RY

## Summary

This talk by Jon (surname not given) explores why mutexes appear slow in concurrent programs — and argues the real culprit is CPU cache coherence, not the locks themselves. Using benchmarks of a simple read-only counter shared across threads, Jon demonstrates that both mutexes and reader-writer locks degrade significantly under contention, with reader-writer locks actually performing *worse* than mutexes at high reader counts. He then introduces the **Left-Right** data structure as a case study in designing concurrency primitives that align with CPU memory architecture.

---

## Key Insights

**Benchmark Setup**
- Counter shared across N threads, read-only (no writes)
- Mutex: starts at ~250M ops/sec on 1 thread, drops to ~25M on 2 threads, then stays flat
- Reader-writer lock: starts similar to mutex, but *degrades further* as reader count increases — eventually worse than mutex
- Intuition says more threads reading = same or better throughput; reality is much worse

**CPU Cache Hierarchy**
- L1 cache: ~1ns, per-core, very small
- L2 cache: intermediate latency/size, varies by CPU
- L3 cache: ~30ns for cross-core, shared across all cores, larger
- RAM: ~100ns
- Cross-core cache line transfer: ~30ns — over halfway to RAM just to bounce a cache line

**MESI Protocol (Cache Coherence)**
- Cache operates on **64-byte cache lines**, not individual addresses
- Four states: **Modified** (dirty, only copy), **Exclusive** (clean, only copy), **Shared** (multiple readers, same value), **Invalid** (stale/evicted)
- Writing to shared data requires coordination: core must acquire exclusive ownership, invalidating all other copies
- This cross-core communication is the hidden cost

**Why Reader-Writer Locks Are Slow Under Many Readers**
- Taking a *read* lock requires an atomic increment to a shared reader counter — this is a **write** to shared state
- 100 reader threads → 100 sequential exclusive acquisitions of the same cache line
- Every reader must: get exclusive → modify → release → next reader gets exclusive → modify → ...
- Two cache line transfers per lock acquire+release cycle (~60ns minimum per reader, at 30ns/transfer)
- More readers = more cache line ping-pong = worse performance
- Mutex is actually *more stable* under contention because only one thread writes at a time, avoiding the escalating ping-pong

**Why Mutexes Plateau Instead of Continuing to Fall**
- Mutex only allows one thread to hold it, so they don't compete for the same cache line simultaneously
- They serialize naturally without bouncing the cache line as aggressively as many concurrent readers do

---

## The Left-Right Data Structure

**Motivation**: Jon's PhD workload had near-zero writes and very hot short read paths — reader-writer lock overhead dominated

**Design**
- Two copies of the data (left and right)
- Atomic pointer indicates which copy readers should use
- Writer always modifies the copy *not* pointed to
- After modifications, writer atomically flips the pointer
- Writer must then wait until all in-flight readers on the old copy have finished before modifying it

**Per-Reader Counters (the key insight)**
- Each reader has its **own cache line** with a counter
- Readers increment before and after each operation
- Writer scans all reader counters looking for: counter changed by ≥1 (reader saw new pointer) OR counter is even (reader is idle)
- Readers **never share state with each other** → no cache line contention between readers

**Performance Result**
- Throughput scales **linearly** with thread count — ~3 billion ops/sec at ~10 cores
- Readers are fully **wait-free** (no locks, no spin loops, no CAS)

**False Sharing Bug (Debugging Story)**
- During benchmarking, performance dropped 10x at 4 cores unexpectedly
- Root cause: multiple reader counters landed on the **same 64-byte cache line**
- Even though each counter was logically independent, MESI sees them as one unit
- Fix: add 64-byte alignment to the counter type → linear scaling restored
- **Key lesson**: lock-free ≠ contention-free

**Limitations of Left-Right**
- Doubles memory usage (two copies)
- Single-writer only (needs external mutex for multiple writers)
- Operations must be **deterministic** (need to replay the op-log on the other copy)
- Readers may see **stale data** (eventually consistent only)
- Writer must wait for readers to drain before modifying the old copy
- Not linearizable — inappropriate for financial transactions; suitable for caches/lookups

---

## Main Arguments / Thesis

1. **Mutexes are not slow — coordination is slow.** The lock is just an interface; the underlying cost is cache coherence traffic.
2. **Reader-writer locks can be *worse* than mutexes** when reads are short and readers are numerous, because they generate more cache line contention per operation than mutexes.
3. **The right algorithm depends on your workload's data transfer patterns.** No single primitive is universally best.
4. **Lock-free ≠ fast.** Even without locks, you can create heavy cache coherence pressure (as the false-sharing bug demonstrated).

---

## Notable Quotes / Highlights

> *"The real lesson is it's not about locks. It was never about locks. Coordination is expensive because of cache coherence... The locks are just the interface you happen to be using."*

> *"Lock-free does not mean contention-free. Just because there are no locks does not mean that the CPU isn't going to punish you because you made memory move around a bunch more."*

> *"The overhead of using a lock goes up the more you need that lock to be fast — sort of the inverse proportion of what you want."*

> *"Accessing something in L1 cache is 1ns. Cross-core communication is ~30ns. We're already over halfway to RAM just by acquiring the read lock alone."*

---

## Practical Takeaways

**Questions to ask before choosing a concurrency primitive:**
1. **Read/write ratio** — many reads + rare writes → Left-Right; balanced → mutex; read-heavy short ops → beware RWLock
2. **Critical section length** — long sections: mutex overhead amortized; short sections: synchronization cost dominates
3. **Thread count** — at low concurrency, none of this matters; at high concurrency, cache coherence dominates
4. **Consistency requirements** — need linearizability or read-your-writes? Left-Right is out; use mutex
5. **Eventual consistency acceptable?** — caches, config lookups → Left-Right is a fit

**Always measure before optimizing.** Profile first; cache effects won't show up as obvious hotspots in `perf`.

**Align cache-sensitive structures to 64 bytes** to avoid false sharing when multiple independent fields land on the same cache line.

---

## Additional Context

- **Scalable reader-writer locks** (mentioned as further reading): one counter *per core* instead of one global reader counter — writer walks all per-core counters, most ops stay core-local
- **AMD 3D V-Cache**: 3D stacking puts L3 cache physically above the CPU die, shortening distances and increasing L3 size — relevant to reducing cross-core coherence latency
- **Fetch-add optimization**: some CPUs batched commutative fetch-add operations (coalesce multiple adds, run on one core, return results) to reduce cache line bouncing — largely proprietary/undisclosed
- **Futexes** (Fast Userspace Mutexes): Linux primitive underlying most modern mutex implementations; minimal kernel involvement on the uncontended fast path
- **Memory barriers / fences**: compilers inject these around lock operations to prevent CPU out-of-order execution from hoisting reads/writes outside the critical section
- Left-Right crate available on crates.io (Rust); false-sharing fix was contributed upstream
