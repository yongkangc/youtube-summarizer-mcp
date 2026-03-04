**Source**: https://www.youtube.com/watch?v=AAssk2N_oPk

## Summary

Computerphile explains why VPNs use UDP instead of TCP by examining the TCP meltdown problem — when reliable protocols are layered on top of each other, causing catastrophic performance degradation.

## Key Insights

### Protocol Fundamentals
- IP is inherently unreliable: Best-effort delivery with no guarantees about arrival, ordering, or integrity
- TCP builds reliability on unreliability: Sequence numbers, acknowledgments, retransmission over unreliable IP
- Retransmission timeout adaptation: TCP dynamically adjusts timers based on observed RTT and jitter
- Window-based flow control: Sliding windows send multiple packets before waiting for ACKs
- Congestion control prevents network collapse: TCP backs off when detecting congestion

### The Meltdown Problem
- Layered TCP causes algorithm conflict: TCP-over-TCP causes both layers to independently manage reliability
- Delayed packets trigger false retransmissions: Lower TCP reordering causes upper TCP to assume loss
- Exponential backoff amplification: Both layers exponentially back off, causing severe degradation under any packet loss
- UDP preserves single reliability layer: Using UDP for tunneling maintains TCP's assumptions about unreliable transport

### Design Implications
- Sequence number wraparound: TCP handles 32-bit overflow gracefully through modulo arithmetic
- Out-of-order delivery: TCP buffers and reorders packets before delivering to application

## Notable Quotes
- "IP doesn't guarantee that your data will get from A to B — it just says it'll do its best"
- "When you put TCP over TCP, you get two algorithms fighting each other"
- "The internet is designed to be unreliable, and that's actually a feature, not a bug"

## Actionable Takeaways
- Use UDP for VPN and tunneling protocols to avoid TCP-over-TCP problems
- Implement application-layer reliability on top of UDP when you need custom semantics
- Monitor TCP retransmission rates to detect network quality issues in production
- Design protocols to handle out-of-order delivery gracefully when using UDP
