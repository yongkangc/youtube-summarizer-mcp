**Source**: https://www.youtube.com/watch?v=NH1Tta7purM

## Summary

Carl Cook from Akuna Capital dissects ultra-low latency trading systems where microseconds matter, covering hardware optimization, cache efficiency, branch prediction, and the critical engineering decisions that separate winning HFT systems from the also-rans.

## Key Insights

### Latency Hierarchy
- L1 cache hit ~1ns, L2 cache ~3ns, L3 cache ~12ns, RAM ~65ns, context switch ~3000ns — design around these realities
- Tail latency kills profitability: P99.9 latencies matter more than averages — one slow trade loses money

### Branch Prediction & Code Layout
- Modern CPUs predict branches with ~95% accuracy, but mispredictions cost 10-20 cycles — profile your hot paths
- Template metaprogramming eliminates runtime overhead: generate optimal code paths at compile time rather than branching

### Memory Architecture
- Memory prefetching beats reactive allocation: Use `__builtin_prefetch()` and design data structures for sequential access
- Cache line alignment prevents false sharing: Align critical data structures to 64-byte boundaries
- Static memory allocation in hot paths: Avoid malloc/free in latency-critical code — pre-allocate everything at startup

### Hardware & System Optimization
- NUMA topology awareness: Pin threads to specific CPU cores, ensure memory allocation matches CPU socket locality
- Network card bypassing: Kernel bypass with DPDK or Solarflare reduces latency from ~30μs to ~300ns
- Lock-free programming: Compare-and-swap operations enable multi-threaded performance without mutex contention
- Compiler optimization flags: `-O3 -march=native -mtune=native` can provide 2-3x performance improvements
- Hardware timestamping: NIC-level timestamps provide nanosecond accuracy versus software timestamps with microsecond drift
- Instruction-level parallelism: Modern CPUs can execute 4-6 instructions per cycle if dependencies are managed properly

## Notable Quotes
- "When you're trying to make money in microseconds, every nanosecond counts — and most of programming best practices go out the window"
- "The difference between a profitable trade and a losing trade is often measured in nanoseconds, not milliseconds"
- "If you're not thinking about which CPU cache your data lives in, you're probably losing money"
- "Template metaprogramming isn't just an academic exercise — it's how you eliminate the last microseconds of latency"

## Actionable Takeaways
- Profile with hardware performance counters (`perf`, Intel VTune) to identify cache misses and branch mispredictions
- Implement lock-free data structures using atomic operations for inter-thread communication
- Use memory pools and custom allocators to eliminate dynamic allocation in hot paths
- Benchmark different compiler optimization levels and CPU-specific flags
- Design data structures with cache efficiency in mind — prefer arrays of structs over struct of arrays
- Implement thread pinning and CPU affinity to reduce context switching overhead
