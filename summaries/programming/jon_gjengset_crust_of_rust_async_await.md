**Source**: https://www.youtube.com/watch?v=ThjvMReOXYM

## Summary

Jon Gjengset provides a deep dive into Rust's async/await implementation, covering Future traits, state machines, pinning, and the mechanical details of how asynchronous code compiles to efficient state machines.

## Key Insights

### Core Mechanics
- Futures are state machines: `async fn` compiles to a state machine enum where each `.await` point becomes a different variant
- Poll-driven execution model: Futures only advance when explicitly polled, making them lazy and efficient
- Zero-cost abstractions: Async/await compiles to the same performance as hand-written state machines
- Executor independence: Futures work with any executor (Tokio, async-std, custom) due to standard trait design

### Pinning & Safety
- Pin prevents memory corruption: Pin<T> ensures futures can't be moved once polled, enabling self-referential structs safely
- Async blocks capture by reference: Variables are captured by reference, affecting lifetime management
- Cancellation via dropping: Dropping a future cancels its execution — enables timeout and cancellation patterns

### Scheduling & Composition
- Wakers enable cooperative scheduling: Waker trait allows futures to signal when they can make progress, avoiding busy polling
- Context threading eliminates overhead: Efficient waker passing without heap allocation
- Send bounds enable thread migration: Futures must be Send to be scheduled across threads
- Future chaining via combinators: `map`, `and_then` compose futures without additional allocations
- Stream vs Iterator: Streams are async iterators that yield values over time with backpressure

## Notable Quotes
- "Async/await is just sugar over state machines — but it's incredibly delicious sugar"
- "Pin is scary until you realize it's just preventing a specific class of memory bugs"
- "Futures are lazy by design — they do absolutely nothing until you poll them"

## Actionable Takeaways
- Design futures to be cancellation-safe by avoiding state that can't be recovered after dropping
- Use `Box::pin()` or `pin_mut!` when storing futures that reference local variables
- Implement custom futures using manual Poll when async/await syntax isn't sufficient
- Profile async code to ensure state machines aren't larger than expected due to captured variables
- Implement timeout and cancellation using `select!` macros or future combinators
