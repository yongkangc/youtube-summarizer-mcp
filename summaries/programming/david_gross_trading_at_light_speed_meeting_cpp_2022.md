**Source**: https://www.youtube.com/watch?v=8uAW5FQtcvE

## Summary

David Gross from IMC Trading explores the architecture and engineering challenges of building trading systems that operate at the physical limits of computation and network transmission, covering both hardware and software optimization strategies.

## Key Insights

### Physical Constraints
- Speed of light is the ultimate latency floor: Chicago to New York takes minimum 4.2ms — any system slower than 8-10ms roundtrip is losing money
- Microwave networks beat fiber: ~30% faster due to refractive index
- Clock synchronization precision: GPS/PTP synchronization to nanosecond precision required for accurate timestamping

### Hardware Architecture
- FPGA co-processors achieve nanosecond response: Custom logic processes market data and generates orders in 300-500ns
- Network topology determines winners: Direct market connections bypass internet routing — dedicated lines mandatory
- Hardware timestamping: NIC-level timestamping provides 10-100x better precision than software timestamps
- Memory bandwidth vs latency tradeoffs: DDR4 has higher bandwidth but SRAM has 10x lower latency

### Software Optimization
- Kernel bypass networking: DPDK, VMA, or custom drivers eliminate 20-30μs of kernel overhead per packet
- Interrupt coalescing hurts latency: Disable it and use dedicated CPU cores for network processing
- CPU core isolation: `isolcpus` isolates trading threads from OS scheduler
- Message parsing optimization: Binary protocols with fixed-width fields eliminate variable parsing overhead
- Order book reconstruction: Incremental updates with lazy evaluation reduce processing from microseconds to nanoseconds
- Speculative execution risks: CPU branch prediction failures add 10-20 cycle penalties in critical paths

## Notable Quotes
- "In HFT, the speed of light isn't just physics — it's your performance budget"
- "Every layer you add between your code and the hardware is latency you'll never get back"
- "The fastest trade is the one that happens before your competitor even sees the opportunity"

## Actionable Takeaways
- Measure end-to-end latency with hardware timestamps to identify bottlenecks
- Implement FPGA-based market data processing for ultra-low latency
- Use kernel bypass networking to eliminate OS overhead
- Design binary message formats with fixed-width fields for predictable parsing
- Set up dedicated network connections to exchanges to minimize routing hops
