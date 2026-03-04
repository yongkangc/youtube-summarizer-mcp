**Source**: https://www.youtube.com/watch?v=qqRYkcta6IE

## Summary

Hussein Nasser compares TCP and UDP protocols through practical examples, covering their trade-offs, use cases, and demonstrating both through working Node.js server implementations.

## Key Insights

### TCP Characteristics
- Guarantees reliability, ordering, and flow control at the cost of latency and bandwidth overhead
- Connection state memory overhead: Per-connection state consuming server memory, limiting concurrent connections
- Acknowledgment overhead: Round-trip confirmation for every packet doubles network messages
- Congestion control: Automatically throttles transmission rate during congestion
- Connection establishment: 3-way handshake before data transmission
- Vulnerable to SYN flood attacks due to connection state

### UDP Characteristics
- Minimal headers (8 bytes vs TCP's ~20 bytes), significant for small messages
- Stateless: No connection state, enabling horizontal scaling
- Immediate transmission: No handshake overhead
- No ordering guarantees: Delivers packets as they arrive
- No congestion control: Application must handle its own

### Selection Criteria
- TCP for data integrity: databases, file transfers, secure communications
- UDP for real-time: gaming, video streaming, DNS, market data feeds
- Custom reliability on UDP: When you need specific semantics (e.g., partial reliability, custom retransmission)

## Notable Quotes
- "There's always trade-offs in software engineering — TCP vs UDP is a perfect example"
- "If you can destroy your server while clients are connected and they resume work normally, you're stateless"
- "TCP adds a lot of garbage to your messages, but that garbage keeps the internet working"

## Actionable Takeaways
- Choose TCP for applications requiring data integrity
- Use UDP for real-time applications where speed matters more than perfect delivery
- Implement custom reliability mechanisms on UDP when needed
- Consider server memory limits for TCP-based systems due to per-connection state
- Profile network protocols under realistic load conditions
