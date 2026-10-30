---
title: "T3 Code broke me"
source: https://www.youtube.com/watch?v=uLGxb4F3SyI
channel: Theo - t3.gg
speaker: Theo Browne
date_uploaded: 2026-10-29
date_summarized: 2026-10-30
---

## TLDR

T3 Code is an open-source control plane for existing coding agents, subscriptions, repositories, and machines. Theo's central pitch is not a smarter model: it is easier parallel orchestration, remote execution, and an attention-driven inbox that shows work when human input is needed.

## Coverage and caveats

Reviewed all 1,264 captions in contiguous three-minute windows through approximately 41:51. Metadata runtime is 41:49. This is a founder/contributor's promotional product walkthrough, with an Apify sponsorship, not an independent comparison or benchmark. Feature availability and performance are described as demonstrated/claimed at recording time; exact model names in captions are unreliable.

## Three core ideas

- **03:30–10:00: one interface, many harnesses.** Connect existing Codex, Claude Code, Cursor, and other supported/ACP-compatible harnesses, using your own subscriptions or credentials. Orchestrator V2 can delegate to different models/harnesses, start threads in other repositories, and let threads communicate. Its MCP interface also permits external tools to control T3 Code. A demonstration starts several cross-provider review agents in a Git worktree. These are existing model capabilities coordinated by the app, not a new foundation model.
- **10:00–15:00: remote execution as default.** Select which laptop, Linux server, VPS, or Mac runs a thread. Theo describes load-aware routing using CPU/memory availability, remote terminals, device simulators, and browser previews. Connect through LAN, Tailscale, or T3 Connect tunneling. The walkthrough says T3 Connect supports three devices free; users supply their own machines and AI access. A hosted interface is not included cloud compute.
- **15:00–22:00: the sidebar is an inbox.** Settle completed threads, snooze deferred ones, and optionally hide actively working threads until they finish or need input. Linked PR merges can automatically settle a thread. Pins override hiding. This aims to restore project awareness while running many agents, not maximize the number of chats visible.

## Useful supporting features

- **18:00–26:00:** background prompt submission, steering versus queuing, scheduled tasks, interactive HTML artifacts, PR viewing, usage visibility, delayed prompts after rate-limit reset, drafts/stashing, and mobile controls.
- **26:00–31:00:** remote browsers and iOS simulators, handoff between harnesses, references between threads, annotations, project/environment-specific settings, configurable worktrees, and project creation on a selected machine. Theo recommends worktrees for parallel changes.
- **30:00–34:00:** integrated PR monitoring, multiple connection routes and granular remote permissions. Webhooks can trigger threads; optional buffering/replay lasts up to 24 hours, according to the demo. Fleet updates can update app and providers. Opening an editor can use SSH automatically when the code is remote and the client already has access.
- **33:00–37:00:** move/clone repositories to another machine, optionally copy ignored files, expose attachments as actual agent-readable files, capture context through accessibility snapshots, and launch model-assisted diagnostics through the triage command. These convenience features expand the trust surface: ignored files can include secrets, and snapshots can contain private information.

## Limitations admitted in the video

- Bring your own compute and subscriptions; no bundled AI access. T3 Chat is a separate closed-source chat product.
- More than three T3 Connect devices requires another connection method at recording time.
- Native computer-use tooling is not yet built in; compatible harness-provided computer use can still work.
- More concurrent tasks can consume subscription allowances faster and worsen attention/sleep habits.
- Stable and nightly builds differ; nightly prioritizes earlier features with potential breakage.

## Claims not independently verified

- Faster or better than competing apps, roughly 100-fold lower data transfer for switching threads, dramatically reduced GitHub API usage, and over 80% of issues fixed with triage are Theo's claims, without a controlled methodology here.
- Adoption figures are time-dependent and internally mixed: the description says over 700,000 users, the spoken opening says approaching 550,000 users and 140,000 weekly actives. Closing figures include about 27,000 GitHub stars and 516 contributors. Do not merge these into a single verified current metric.
- Open source improves inspectability and repairability; it does not establish security. No source-code/security audit was performed for this summary.

## Practical takeaways

1. Separate orchestration from intelligence: use the appropriate model/harness without rebuilding your whole workflow around one vendor.
2. Give parallel tasks isolated worktrees, explicit scopes, and acceptance checks. Cross-model agreement is not independent evidence of correctness.
3. Surface only finished work, failures, or decisions requiring attention. Background activity should not become notification noise.
4. Centralize remote management, but limit filesystem access, webhook authority, tunneling exposure, and which machines receive secrets.
5. Measure merged, tested changes and review time rather than thread or token counts. Tooling that makes launching work easier can merely move the bottleneck into review.

## One-line conclusion

The strongest idea is an attention-aware, provider-independent control plane for coding agents, not proof that running more agents automatically produces better software.
