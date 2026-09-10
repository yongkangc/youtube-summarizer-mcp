# Mati Staniszewski on ElevenLabs, Voice AI & Building the Communication Layer for AI

Source: https://open.spotify.com/episode/1PXS9dsGQuCcAgpNZcF1MB

Transcript note: Spotify supplied no text transcript. Summary uses the official Megaphone audio and local ASR; minor wording may be imperfect.

## TLDR

ElevenLabs wants to own the communication layer between humans, companies, and AI. Its strategy combines frontier audio research with products and forward-deployed engineers, then turns customer-specific deployment knowledge into reusable platform features. Mati Staniszewski believes voice becomes a primary AI interface because it is natural, fast, emotional, and requires less user adaptation than screens, keyboards, and forms.

## Origin and product evolution

- Mati and Piotr Dąbkowski, friends for roughly **15 years**, founded ElevenLabs in **2022**, before ChatGPT launched.
- Trigger: Polish films often used one narrator for every character, stripping away original emotion and identity.
- Full dubbing required three weak components: transcription, translation, and speech generation.
- Creator interviews revealed a nearer problem: narration, script preview, and post-production edits.
- ElevenLabs therefore solved text-to-speech first, then expanded into transcription, localization, dubbing, voice agents, and orchestration.

## Company strategy

Mati describes ElevenLabs as **research + product deployment**:

- Research builds frontier audio models.
- Product combines audio with knowledge, integrations, workflows, and creative tooling.
- Deployment embeds engineers with customers to make systems work in production.

Focus rule:

> Enter a product only when ElevenLabs' audio models create unique advantage or solve the core bottleneck.

They avoided building video/avatar models when visual quality, not audio, constrained the product. As open-source video improved, they could integrate it without building every model themselves.

## Moat thesis

Model quality alone may commoditize. Intended moat broadens into:

- audio-specialist researchers and architecture
- production integrations and workflow reliability
- customer trust and brand
- deployment knowledge
- voice marketplace and creator economics
- unified communication platform

The voice marketplace reportedly contains about **30,000 voices**. Creators can authenticate and share voices, then receive compensation when used.

## Deutsche Telekom example

Deutsche Telekom uses ElevenLabs across customer journey:

- podcasts and app content
- advertising/localization
- call-centre voice agents connected to company knowledge
- support and refund workflows
- in-network agent for bookings and real-time translation

Expansion pattern: prove value in one workload, build integrations, test with simulated and verified calls, deploy at small scale, monitor continuously, then broaden.

## Forward-deployed engineering

Mati imported Palantir's operating model:

- engineers work beside customers, not behind a sales handoff
- teams learn actual operational problem
- customer-specific integrations become reusable product capabilities
- domain knowledge compounds across customers

Critical distinction: if deployment knowledge never returns to core product, company becomes services business. ElevenLabs places forward-deployed engineers inside product, not go-to-market.

## Organizational design

- Small autonomous teams, usually **fewer than 10 people**.
- Flat hierarchy; roughly **five layers maximum**.
- Many managers have close to **10 direct reports**.
- Engineering talent sits inside legal, operations, talent, and revenue functions.
- Most internal documents and operational data are broadly accessible.
- AI summarizes granular work, allowing leadership to detect problems directly rather than receive layers of filtered reporting.

Mati expects AI-native firms to run with wider spans, fewer layers, and engineers embedded everywhere.

## Where demand is growing

- Largest growth areas: conversational agents and creative tools.
- Fastest vertical: fintech.
- Other major verticals: healthcare, telecom, retail, and e-commerce.
- Company has roughly six broad product lines, with many applications beneath them.

## Why voice matters

Voice contains emotion, identity, pacing, pauses, and imperfections absent from text. ElevenLabs found that making agents slightly imperfect, including natural hesitations and pauses, improved perceived humanness and user response.

Mati's thesis:

- model intelligence keeps improving
- bottleneck shifts toward accessing and communicating with intelligence
- voice lets technology adapt to humans rather than forcing humans to learn interface conventions
- AI should combine IQ with EQ: understand knowledge, emotion, timing, interruption, and when to pause

Analogy: telegraph required users to learn machine language; telephone used behaviour people already knew.

## Human amplification

ElevenLabs says it has helped more than **10,000 people** recreate lost voices and works with about **800 organizations** on accessibility, education, and cultural access.

Examples include people with ALS or throat cancer, musicians performing again, and public figures continuing to speak. This supports Mati's preferred AI frame: amplify human capability rather than replace humans.

## Founder stance

- Mati and Piotr turned down multiple acquisition offers.
- They view timing as unusually favourable and ElevenLabs as likely their best lifetime idea.
- Selling would provide financial ease but surrender independence during a rare platform shift.
- Conferences are treated as sales/partnership infrastructure: only **2–3 per quarter**, with meetings arranged before arrival. Attendance without clear commercial purpose is distraction.

## Investor read-through

**Theory of edge:** audio was under-researched while capital chased text and images; ElevenLabs used specialist model quality to enter, then converted that lead into distribution, workflows, customer feedback, and marketplace liquidity.

Bull case:

- voice becomes default interface for agents
- enterprise agents create recurring, high-volume usage
- deployment knowledge compounds into platform advantage
- marketplace improves language/accent coverage and creates switching costs

Risks:

- frontier labs commoditize speech models
- agent reliability/integration work remains labour-heavy
- deepfakes, consent, authentication, and regulation damage trust
- hyperscalers bundle acceptable voice cheaply
- broad product surface dilutes audio focus

Key KPIs:

- agent revenue and conversation volume
- enterprise retention and workload expansion
- gross margin after inference and deployment labour
- forward-deployed engineering per customer
- latency, interruption handling, and task-completion rate
- creator payouts and marketplace usage
- share of deployment work converted into reusable product

## One-line summary

ElevenLabs' durable bet is not merely better synthetic speech; it is turning an early audio-model lead into the default enterprise communication and agent interface.