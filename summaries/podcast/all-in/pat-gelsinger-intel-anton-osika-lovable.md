---
title: "Former Intel CEO on What Went Wrong, What's Next + Lovable CEO on the Real Promise of Vibe Coding"
spotify: "https://open.spotify.com/episode/1iORv3MvIBf8Oh0lZS0kO9"
youtube: "https://www.youtube.com/watch?v=-ILKiOU5iAQ"
youtube_video_id: "-ILKiOU5iAQ"
show: "All-In Podcast"
guests:
  - "Pat Gelsinger"
  - "Anton Osika"
duration: "49:44"
category: podcast
---

# All-In: Pat Gelsinger on Intel + Anton Osika on Lovable

[Spotify episode](https://open.spotify.com/episode/1iORv3MvIBf8Oh0lZS0kO9) · [Official YouTube transcript source](https://www.youtube.com/watch?v=-ILKiOU5iAQ)

## TL;DR

Two interviews share one theme: technology winners compound deep technical capability and ecosystems; losers optimize current economics while missing architectural shifts.

Pat Gelsinger says Intel lost technical leadership through finance-led management, underinvestment in fabs/EUV, proprietary IDM thinking, and failure to compound software/platform bets like CUDA. Lovable CEO Anton Osika argues software creation is moving from coding toward product judgment and business operation, with Lovable building its moat above foundation models through orchestration, integrations, hosting, security, and feedback data.

## Pat Gelsinger: what went wrong at Intel

- Intel's early leaders were deeply technical. Gelsinger says roughly 15 of 20 executives in his first executive staff were PhDs.
- His central diagnosis: business leaders promoted more business leaders, weakening technical judgment needed for long-duration semiconductor bets.
- Intel returned roughly **$100B** through dividends and buybacks during the five or six years before his return, while allegedly going a decade without building a new fab and failing to buy enough EUV equipment.
- Apple built silicon competence incrementally because Intel could not satisfy its power/system needs indefinitely. Apple optimized silicon and system together rather than relying on Windows-oriented x86 designs.
- Intel dismissed GPUs as graphics devices while Nvidia compounded CUDA, SIMT, developer tooling, and community adoption until GPUs became general-purpose HPC and AI platforms.
- Intel's Larrabee effort pursued similar parallel-compute goals but was killed shortly after Gelsinger's first departure.
- TSMC standardized manufacturing around third-party customers, PDKs, and EDA tools. Intel kept process/design proprietary. Gelsinger says TSMC produced roughly **5× Intel's wafers** when he returned and later approached 7×.

**Intel edge lesson:** Hardware advantage compounds only when silicon, software, manufacturing scale, customer ecosystem, and sustained capex reinforce each other. Quarterly financial optimization can destroy long-cycle option value.

**Caveat:** This is Gelsinger's retrospective and partly self-serving. Capital allocation mattered, but Intel's process delays, execution failures, product roadmap, culture, customer economics, and his own foundry strategy also require separate underwriting.

## Taiwan and semiconductor resilience

- Gelsinger says US leading-edge manufacturing share rose from about **12% to 18%**, crediting CHIPS Act investment plus Intel and TSMC expansion.
- He claims Taiwan holds less than three weeks of energy reserves; blockade-induced brownouts could stop fabs, which might take roughly **90 days** to restart.
- His warning: a blockade need not destroy fabs physically to create a global depression-scale supply shock.
- Conclusion: geographic resilience is an economic necessity, not merely industrial-policy preference.

These are speaker claims and estimates, not independently verified in this summary.

## AI and quantum outlook

- Gelsinger sees possible valuation excess but expects AI infrastructure buildout to last **decades**, not years.
- Grid capacity acts as physical upper bound: data centers cannot outrun available power indefinitely.
- Goal: make AI roughly **10,000× better** and reduce token cost/energy by five orders of magnitude, enabling Jevons-style demand expansion.
- He predicts meaningful quantum-computing results before 2030, with cryptographic/Q-day implications perhaps around 2032–2033. Treat as forecast, not base-case fact.

## Anton Osika: Lovable's operating model

Founder claims after roughly 20 months:

- **1M new projects per week**;
- **50M+ apps** built cumulatively;
- **700M monthly visits** across customer applications;
- about **20% technical users / 80% nontechnical**;
- businesses generating $1M+ revenue on platform;
- annualized revenue reportedly reached **$500M in May**.

Lovable is expanding from app generation into:

- opinionated architecture and security scans;
- payments, email, search/discovery, and integrations;
- hosting built partly on infrastructure partners such as AWS;
- business operation and analytics;
- an “AI co-founder” that proposes optimizations and experiments.

Host gives anecdote of software once estimated at **$500K** being built in 4–8 hours for under roughly $2K. Another customer allegedly replaced 10+ internal tools and saves more than $1M annually. These are promotional anecdotes, not audited case studies.

## Lovable moat

- Routes work across multiple commercial frontier and open-weight models.
- Post-trains internal models where cheaper/specialized inference improves product economics.
- Uses large token volume and observed failures to improve agent harness, tool selection, integrations, and software-building skills.
- Owns workflow layer: architecture, deployment, hosting, data connections, payments, security, monitoring, and business context.
- Claims roughly **60% of lowest-tier customers** hit caps and buy top-ups, suggesting strong usage but also high inference intensity.

**Theory of edge:** Lovable gets paid to collapse software creation cost/time while making nontechnical users productive. Structural advantage exists if its workflow data, agent harness, integrations, deployment surface, and customer distribution improve faster than underlying models commoditize code generation.

## Lovable risks / kill tests

- Frontier labs absorb app-building/orchestration layer.
- Code generation becomes commodity faster than Lovable builds workflow lock-in.
- Security or data-loss incidents break trust among nontechnical users.
- Inference/overage economics prevent durable gross margins.
- Generated apps become hard to maintain, audit, or migrate.
- Enterprises reject tool proliferation and ungoverned bespoke software.
- Claimed ARR/usage growth fails to convert into retention and cash flow.

## Investor/operator read-through

- **Intel:** Never separate technical roadmap from capital allocation. Underinvesting through one architecture transition can erase decades of dominance.
- **Nvidia/TSMC:** Ecosystem and manufacturing scale compound slowly, then appear inevitable after crossing threshold.
- **Lovable:** Foundation model is supplier, not moat. Value accrues to layer owning customer workflow, proprietary feedback, deployment, security, and business outcome.
- **Operator action:** Cheap software increases number of experiments worth running. Build parallel prototypes, measure outcomes, then consolidate winners; avoid accumulating unmanaged “Franken-software.”

## One-line summary

Intel lost by underinvesting in technical compounding; Lovable wins only if it compounds workflow intelligence faster than foundation models commoditize coding.