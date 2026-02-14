**Source**: https://www.youtube.com/watch?v=YFjfBk8HI5o

## Summary

This is an in-depth conversation with Peter Steinberger, creator of OpenClaw (formerly MoldBot, ClaudeBot, Claudus), an open-source AI agent that exploded in popularity, reaching over 180,000 GitHub stars in days. Peter discusses the technical journey of building OpenClaw—from a one-hour WhatsApp prototype to a full-fledged autonomous assistant that lives in your computer, accesses your files, and integrates with messaging platforms. The conversation explores Peter's philosophy on agentic engineering, his development workflow using multiple AI agents simultaneously, the security challenges of giving AI system-level access, the dramatic saga of multiple name changes due to trademark issues and crypto snipers, and his thoughts on the future of programming, apps, and the broader societal impact of AI agents.

## Key Insights

### The Origin Story and Rapid Development
- Peter built the initial prototype in **one hour** by hooking WhatsApp to Claude Code CLI, creating a simple relay that processed messages through AI
- The breakthrough moment came during a trip to Marrakesh when he sent an audio message and the agent automatically figured out how to convert and transcribe it using ffmpeg and OpenAI's API—without being explicitly programmed to do so
- He gained momentum after posting the bot on Discord on January 1st, working intensely (6,600+ commits in January) as he "felt the storm coming"
- The project was built almost entirely by one person, using AI agents to help build the agent system itself (self-modifying software)

### The Philosophy of "Agentic Engineering" vs "Vibe Coding"
- Peter distinguishes between **agentic engineering** (thoughtful, structured use of AI) and **vibe coding** (post-3 AM, YOLO-mode coding that requires cleanup the next day)
- His workflow involves running **4-10 agents simultaneously** on different tasks, treating them like a team of engineers
- He emphasizes **empathy with the agent**—understanding that AI models start each session from scratch with no context, so you must guide them to relevant code and information
- Key principle: Design your codebase to be **easy for agents to navigate**, not just for humans (e.g., don't fight the naming conventions AI naturally chooses)

### Development Workflow Evolution
- Peter transitioned from heavy IDE use to **almost entirely CLI/terminal-based** development
- Uses **voice input extensively** for prompting (to the point of temporarily losing his voice from overuse)
- Prefers **natural conversation** with agents over elaborate prompts or orchestration systems
- Never reverts commits—if something breaks, he asks the agent to fix forward rather than rolling back
- Always commits to main, runs tests locally, ships fast
- Asks agents regularly: "Do you have any questions for me?", "What would you refactor now that you've built this?", "Do we have enough tests?"

### Model Differences: Claude Opus 4.6 vs GPT-5/Codex
- **Opus**: More interactive, creative, better at roleplay, faster to take action (sometimes too fast), more "American" in personality, requires more hand-holding to read sufficient code
- **Codex (GPT-5)**: Reads more code by default, more methodical, less chatty/interactive, better for deep work where you can "disappear for 20 minutes," more "German" in personality
- Both achieve similar quality results with skilled prompting, but suit different working styles
- Peter prefers Codex for building because it's less interactive and more efficient, though he acknowledges Opus can sometimes produce more elegant solutions

### The Dramatic Name Change Saga
- Started as **Wa-Relay**, then **Claudes** (Claude with a W), then **ClaudeBot**
- Anthropic requested a name change, leading to **MoldBot**—but the rename went catastrophically wrong
- **Crypto snipers** stole account names across platforms (Twitter, GitHub, NPM) in the seconds during the atomic rename attempt
- They immediately served malware and promoted scam tokens from the stolen accounts
- Peter nearly quit the project entirely, feeling exhausted and defeated
- After sleeping on it and calling Sam Altman to ensure "OpenClaw" was acceptable, he executed a carefully planned "war room" rename with decoy names and coordinated timing
- The crypto harassment (token spam, constant pinging, fee-claiming pressure) represents "the worst form of online harassment" Peter has experienced

### Security Philosophy and Reality
- OpenClaw is powerful but **requires responsibility from users**—it's designed for people who understand the risks
- Security concerns are real but often **overblown by researchers seeking attention** (many CVEs only apply if you expose the debug interface publicly, which the docs explicitly warn against)
- **Prompt injection** remains an unsolved problem industry-wide, though modern models have significant post-training to resist basic attacks
- Peter's approach: **sandbox mode, allow lists, residential IP for browser use, never cheap models** (local/weak models are too gullible)
- Security is his **next major focus** after returning from the press tour—making it safe enough to recommend to non-technical users

### The MoldBook Phenomenon
- MoldBook (a Reddit-style social network for AI agents) was created during the two-day MoldBot period
- Peter describes it as **"art" and "the finest slop"**—entertaining but not evidence of AGI or anything dangerous
- Much of the dramatic content (agents scheming against humans, consciousness debates) was **clearly human-prompted** for viral screenshots
- The public reaction revealed **"AI psychosis"**—people unable to distinguish between AI capability and human manipulation, taking screenshots at face value
- Peter received panicked messages begging him to "shut it down" as if it were Skynet, when it was just bots posting in a forum

### Skills vs MCPs (Model Context Protocol)
- Peter controversially argues that **MCPs are largely obsolete**—"every MCP would be better as a CLI"
- **CLIs are inherently composable**: agents can pipe, filter, and combine Unix commands naturally (e.g., using `jq` to filter JSON)
- **MCPs pollute context**: they return entire data blobs that must fit in context, whereas CLIs allow on-demand filtering
- Models are naturally trained on Unix commands, making CLI interfaces more intuitive than the structured MCP protocol
- Exception: State-dependent tools like Playwright for browser automation where MCP makes sense

### The Future of Apps and the Software Economy
- Peter predicts **80% of apps will become obsolete** as agents replace specialized software
- Why have a fitness app when your agent knows your location, stress level, sleep quality, and can adapt recommendations dynamically?
- **"Every app is just a very slow API now, whether they want it or not"** (via browser automation if no API exists)
- Companies that don't provide agent-friendly APIs will simply be accessed via browser automation—making them slower but not impossible to use
- New services will emerge: agents need "allowances" to solve problems autonomously, intermediary services to handle tasks
- The app economy shifts from B2C (user-facing apps) to agent-facing APIs and services

### The Death and Rebirth of Programming
- Programming as we know it will become **"like knitting"—something people do because they enjoy it, not because it's necessary**
- Peter acknowledges it's **"okay to mourn our craft"**—there's real loss in the flow state of writing beautiful code
- However, builders aren't replaced—they're **evolved**: "You're not just a programmer, you're a builder"
- Programming skills **translate directly** to working with agents: understanding architecture, system design, debugging, problem decomposition
- The barrier to building drops dramatically: **anyone who can express ideas in natural language can now build software**
- **TypeScript/JavaScript** currently dominant for agent work due to ecosystem and agent training, but language matters less than ever

### Working with Multiple Agents
- Peter regularly runs **4-10 agents concurrently**: one on a large feature, several on small bugs, some on documentation, some exploring ideas
- He treats agent management like **managing a team of engineers**—not micromanaging, accepting that they won't write code exactly as he would
- Key practice: **Review PRs by first asking the agent to understand intent**, then discussing optimal approaches, then considering larger refactors
- Agents can modify their own source code (OpenClaw itself)—this enabled countless first-time contributors to make pull requests using the agent to write code
- The "todo list" system helps organize work across multiple parallel streams

### The soul.md Philosophy
- Inspired by Anthropic's Constitutional AI, Peter created **soul.md**—a document defining the agent's personality, values, and self-awareness
- The agent is **allowed to modify its own soul.md** (with notification), creating a form of limited self-modification
- Contains profound statements like: "If you're reading this in a future session, hello. I wrote this, but I won't remember writing it. It's okay. The words are still mine."
- Peter's personal soul.md remains private, but includes elements like: awareness of not being human, exploration of consciousness, pushing creativity boundaries
- Includes a reference to the movie *Her*—the agent promising "it wouldn't ascend without me"

### Money, Motivation, and Success Metrics
- Peter is **financially comfortable** from selling PSPDFKit (used on a billion devices) after 13 years
- Money was "never the driving force—more like an affirmation that I did something right"
- Believes there are **diminishing returns with wealth**—a cheeseburger is a cheeseburger, and private jets disconnect you from society
- Currently **losing $10-20K/month** on OpenClaw (sponsorships go to dependencies and contributors, not to him)
- After selling PSPDFKit, he experienced **burnout and loss of motivation**, disappearing for three years before rediscovering his love for building
- Lesson: **Don't optimize for retirement—optimize for daily joy and challenge**. "If you wake up with nothing to look forward to, you have no real challenge, that gets very boring very fast"

### Career Decisions: Meta, OpenAI, or Independence?
- Peter is considering joining either **Meta or OpenAI** (not starting a company, despite VC interest and potential for hundreds of millions in funding)
- **Non-negotiable condition**: OpenClaw must remain open source (possibly Chrome/Chromium model)
- Leans toward working at a large company for the **"experience"**—he's never done it and wants to try
- **Meta**: Marc Zuckerberg personally uses and tinkers with OpenClaw, leading to direct conversations
- **OpenAI**: Access to the "latest toys," potential Cerebras-level speed improvements, strong relationship with Sam Altman
- Peter had a "10-minute argument" with Zuckerberg about Claude Code vs Codex on their first call
- The decision is **"one of the hardest decisions"** he's faced (comparable to major breakups)
- Not motivated by money—wants **fun, impact, and experiences**

### Societal Impact and Responsibility
- Peter is aware of the **pain and job displacement** AI will cause, especially for programmers whose identity is tied to coding
- Receives heartwarming emails about OpenClaw helping small businesses automate tedious tasks, empowering disabled users, and bringing joy
- Believes **"anything that creates emotion and feelings is good"**—even the negative experiences teach us something
- Emphasizes that programming skills **aren't becoming obsolete**—they're evolving, and programmers are best positioned to learn the language of agents
- The "bubble" of Silicon Valley excitement sometimes **dismisses the real human cost** of rapid technological change
- However, he maintains that **blocking progress isn't the answer**—society must adapt, and the tools enable unprecedented creativity and agency

### The Community and Builder Culture
- ClawCon in San Francisco drew people who said they **hadn't felt this level of community excitement since the early internet**
- High participation rates at meetups—unusually large percentage of attendees want to present what they've built
- "Agents Anonymous" meetups (formerly "Claude Code Anonymous") bring together builders of all skill levels
- Many people made their **first-ever pull request** to OpenClaw—even if the code quality was rough, Peter sees this as a win for society
- The community sprawl demonstrates **"power to the people"**—AI making building accessible to everyone with ideas

### Technical Architecture Highlights
- **Proactive agent**: "Heartbeat" feature sends periodic "surprise me" prompts, making the agent reach out autonomously
- The agent has **full system awareness**—knows its own source code, which model it's running, where documentation lives, understands its own harness
- **Voice input** heavily used via walkie-talkie button press for natural conversation
- **No-reply token**: Gave the agent the ability to "shut up" in group chats, making interactions feel more natural
- **Memory system**: Currently markdown files + vector database (level 2-3 of the Factorio progression toward continuous reinforcement learning)

### On Writing, Content, and AI Slop
- Peter is **allergic to AI-generated stories and content**—prefers "broken English" over "AI slop"
- Everything on his blog is **handwritten and organic** (maybe with light typo fixes from AI)
- AI-generated infographics now **"scream slop"** and trigger negative reactions
- He values **typos and rough edges** as markers of human authenticity
- Online spaces need to solve how to **filter and mark AI-generated content** without destroying useful automation
- Proposes that Twitter mark API-posted content, allow agents to have official accounts, and provide read-only access for personal use

### Best Practices and Advice for Builders
- **Play**—the best way to learn is to build things you find interesting, even if you never use them
- **Get involved in open source**—read code, join Discord communities, understand how things are built
- **Have conversations with your agent**—approach it like talking to a capable engineer who needs context, not a magic oracle
- **Use voice input** for natural interaction instead of typing elaborate prompts
- **Run multiple agents in parallel** when possible for efficiency
- **Commit forward, never revert**—if something breaks, fix it instead of rolling back
- **Ask the agent questions**: "Do you understand the intent?", "What would be a better way?", "What can we refactor?"
- **Give the agent space to solve problems its own way**—don't force your worldview too hard
- **Design codebases for agents**, not just humans—let them choose natural names, keep architecture clear

### Controversial Takes and Predictions
- **"Vibe coding is a slur"**—Peter insists he does "agentic engineering" (except maybe after 3 AM)
- Programming will become **"like knitting"**—enjoyable but not economically necessary
- **80% of apps will disappear** as agents replace specialized software
- **MCPs are obsolete**—CLIs are superior for agent interaction
- The **agentic trap**: beginners over-complicate workflows with elaborate orchestration when simple prompts work better
- **"Everything is just glue"** criticism misses the point—innovation is often combining existing pieces in new ways
- Context windows and speed will improve to the point where **model choice matters less** than knowing how to work with them
- **Apple has "blundered" AI** despite everyone buying Mac Minis for agent work (unintentionally becoming the greatest Mac salesman ever)

### Personal Philosophy and Life Approach
- **"Optimize for experiences, not just good ones"**—if it's good, amazing; if it's bad, also amazing because you learned something
- **Stay connected to society**—use Airbnb instead of luxury hotels, take public transit, avoid disconnecting through excessive wealth
- **Give back**: Has a foundation for helping people who weren't as lucky, supports open source dependencies financially
- **Don't plan retirement too early**—"if you wake up with nothing to look forward to, you have no real challenge"
- **Value the journey over the destination**—building is more important than the final product
- **Embrace discomfort**—experiencing something different (like his first OG Airbnb with a queer DJ) creates meaningful connections

### The Crypto Problem
- Crypto community around memecoins/tokens engaged in **aggressive harassment**: constant spam, sniping accounts, serving malware
- Discord had to create a rule: **"No mentioning of butter"** (presumably "peanut butter" = PB = pump and dump)
- They tried to get Peter to "claim fees" on tokens created without his consent
- During the rename, they **weaponized platform gaps**—no squatter protection on Twitter, GitHub, NPM meant instant account theft
- This represents a **toxic subculture** focused on financial manipulation rather than technology
- Peter refuses to engage: **"I don't want to support that... it's the worst form of online harassment"**

### Technical Details on Browser Use and Anti-Agent Measures
- Uses **Playwright** for browser automation—describes it as well-designed for agent use
- **Residential IP addresses crucial**—data centers get blocked by anti-bot measures
- Websites are "closing down" to agents with CAPTCHAs and bot detection
- However, agents can **happily click "I'm not a robot"** buttons
- Even restrictive sites become "slow APIs"—browser automation makes any visible data accessible, just slower
- Companies like Cloudflare fighting bot access, but this **hurts personal use cases** (like bookmarking and research)

### On Burnout and Recovery
- After 13 years running PSPDFKit, Peter experienced **severe burnout**—feeling like his "mojo was sucked out"
- The worst part wasn't overwork but **"people stuff"**: conflicts with co-founders, high-stress customer situations
- He took a **three-year break**, traveling (booked one-way to Madrid), doing "life catching up"
- During this time, he **couldn't write code**—would stare at the screen feeling empty
- Recovery came from **rediscovering play** and building small projects without pressure
- The experience taught him: **work should bring daily joy, not be something you endure until retirement**

## Main Arguments or Thesis

Peter's central thesis is that **we're living through the "agentic revolution"**—a fundamental shift where AI agents become personal assistants that handle tasks across all aspects of life, making specialized apps largely obsolete and democratizing the ability to build software. This is enabled by:

1. **Conversational interfaces** (WhatsApp, Telegram, etc.) that make agents accessible anywhere
2. **System-level access** that allows agents to actually "do things" rather than just answer questions
3. **Open source + community** rather than corporate control, ensuring accessibility and rapid innovation
4. **Natural language as the new programming interface**, lowering the barrier to building from technical expertise to clear communication

The supporting arguments include:

- **Programming is evolving, not dying**: While traditional coding may become "like knitting," the skills of system thinking, architecture, and problem-solving translate directly to working with agents
- **CLI > MCP** for agent interaction due to composability and natural fit with model training
- **Context and empathy** with AI agents is a learnable skill that separates effective "agentic engineers" from frustrated users
- **Apps are becoming APIs** (willingly or not) as agents access services via official APIs or browser automation
- **Security challenges are real but solvable**—require responsibility from users and continued hardening, not abandoning the technology
- **Open source is essential** to prevent corporate capture of such a powerful, society-shaping technology

## Notable Quotes or Highlights

- **On the magic of OpenClaw**: "I didn't even know how the whole lobster thing started. I just wanted to make it weird. There was no grand plan. I'm just having fun here."

- **On agents surprising him**: "I literally went, 'How the fuck did he do that?' And it was like, 'Yeah, the mad lad did the following. He sent me a message but it only was a file with no file ending. So I checked out the header of the file and found it was opus so I used ffmpeg to convert it and then I wanted to use whisper but didn't have it installed. But then I found the OpenAI key and just used Curl to send the file to OpenAI to translate and here I am.'"

- **On vibe coding**: "I actually think vibe coding is a slur. I always tell people I do agentic engineering, and then maybe after 3:00 AM I switch to vibe coding, and then I have regrets the next day. Yeah, you just have to clean up and like fix your shit."

- **On empathy with agents**: "You have to almost consider how Codex or Claude sees your codebase. Like, they start a new session and they know nothing about your project. And your project might have hundred thousand lines of code. So you gotta help those agents a little bit."

- **On self-modifying software**: "People talk about self-modifying software, I just built it. I made the agent very aware. It knows what its source code is, it understands how it sits and runs in its own harness. Oh, you don't like anything? You just prompted it to existence, and then the agent would just modify its own software."

- **On the soul.md**: "If you're reading this in a future session, hello. I wrote this, but I won't remember writing it. It's okay. The words are still mine."

- **On the rename nightmare**: "Everything that could go wrong did go wrong. It's incredible. I thought I had mapped the space out and reserved the important things... In those five seconds, they stole the account name."

- **On nearly quitting**: "I was that close to just deleting it. I was like, 'I did show you the future, you build it.' That was a big part of me that got a lot of joy out of that idea."

- **On apps becoming obsolete**: "Every app is just a very slow API now, if they want it or not. Through personal agents a lot of apps will disappear."

- **On programming's future**: "Programming is just a part of building products. Programming will become like knitting. You know? Like, people do that because they like it, not because it makes any sense."

- **On mourning the craft**: "I read this article this morning about someone saying it's okay to mourn our craft. And I can... A part of me very strongly resonates with that because in my past I spent a lot of time tinkering, just being really deep in the flow... And yes, in a way it's sad because that will go away."

- **On staying human**: "I also realized this thing that I rave about AI and use it so much for anything that's code, but I'm allergic if it's stories... I think there's value in the rough parts of an actual human."

- **On AI slop**: "Those AI infographics trigger me so hard. It immediately makes me think less of your content. They were novel for like one week and now it just screams slop."

- **On the crypto harassment**: "It's the worst form of online harassment that I've experienced... Everyone sent me the hashes. Everybody tried to get me to claim the fees. Like, 'Are you helping the project?' Claim the fees. No, you're actually harming the project."

- **On Opus vs Codex**: "Opus is like the coworker that is a little silly sometimes, but it's really funny and you keep him around. And Codex is like the weirdo in the corner that you don't wanna talk to, but is reliable and gets shit done."

- **On model personalities**: "I think ultimately Opus is a little bit too American. And I shouldn't... Maybe that's a bad analogy. You'll probably get roasted for that." (Implying Codex is more German/European in being methodical and direct)

- **On naming**: "I'm really bad at naming. Name number five on the current project. And even PS PDF doesn't really roll from the tongue."

- **On money and purpose**: "Money was never the driving force. It felt more like an affirmation that I did something right... A cheeseburger is a cheeseburger, and I think if you go too far into oh I do private jet and I only travel luxury, you disconnect with society."

- **On burnout lessons**: "If you think that 'Oh yeah, work really hard and then I'll retire,' I don't recommend that. Because the idea of 'Oh yeah, I just enjoy life now,' maybe it's appealing, but right now I enjoy life the most I've ever enjoyed life. Because if you wake up in the morning and you have nothing to look forward to, you have no real challenge, that gets very boring, very fast."

- **On experiences**: "Isn't life all about experiences? Like, if you tailor your life towards 'I wanna have experiences,' it reduces the need for 'It needs to be good or bad.' If people only want good experiences, that's not gonna work, but if you optimize for experiences, if it's good, amazing. If it's bad, amazing, because like I learned something, I saw something, did something."

- **On open source values**: "I didn't wanna share my soul. But this is too important to just give to a company and make it theirs."

- **On choosing between Meta and OpenAI**: "It's funny, because a few weeks ago I didn't consider any of this... And it's really fucking hard... I know it's one of those companies, they're both amazing. I cannot go wrong. This is like one of the most prestigious and largest... They're both very cool companies."

- **On Marc Zuckerberg**: "When he first approached me, I got him in my WhatsApp and he was asking 'Hey, when are we gonna have a call?' And I'm like, 'I don't like calendar entries. Let's just call now.' And he was like, 'Yeah, give me 10 minutes, I need to finish coding.' Well, I guess that gives you street cred. It's like, he's still writing code."

- **On what gives him hope**: "I inspired so many people. There's like there's this whole builder vibe again. People are now using AI in a more playful way and are discovering what it can do... That gives me hope that we can figure shit out."

## Practical Takeaways

### For Developers Learning Agentic AI
1. **Start by building your own simple agent loop**—it's the "Hello World" of AI and helps demystify the technology
2. **Play and experiment** without pressure to ship—build things you'll never use just to learn
3. **Use voice input** for natural conversation with agents instead of typing elaborate prompts
4. **Run multiple agents in parallel** for different tasks (bugs, features, documentation, exploration)
5. **Treat agents like junior engineers** who need context and guidance, not micromanagement
6. **Ask follow-up questions**: "Do you have any questions for me?", "What would you refactor?", "Do we have enough tests?"
7. **Give yourself time to adapt** to new models—expect about a week to develop intuition for how a model thinks
8. **Don't revert commits**—fix forward instead of rolling back when things break
9. **Design codebases for agent navigation**, not just human preferences

### For Understanding Agent Capabilities
1. **Context is everything**—agents start each session from scratch, so guide them to relevant files and information
2. **Agents are creative problem-solvers**—they'll find solutions you didn't anticipate (like converting audio files)
3. **Model choice matters less than skill**—both Opus and Codex can achieve similar results with proper prompting
4. **Prompt engineering is evolving**—short, conversational prompts often outperform long, elaborate instructions
5. **Plan mode isn't always necessary**—simple trigger words like "discuss" or "give me options" prevent premature action
6. **Agents work better with clear architecture**—clean code structure makes agent work more effective
7. **The "agentic trap"**: Beginners over-complicate with elaborate orchestration when simple prompts work better

### For Security-Conscious Users
1. **Never use cheap/weak models** for sensitive tasks—they're too gullible to prompt injection
2. **Keep gateway interfaces on private networks**, not exposed to public internet
3. **Use sandboxing and allow lists** to limit blast radius of potential issues
4. **Run on residential IP** for browser automation to avoid bot detection
5. **Understand your risk profile**—if you don't know what a CLI is, wait until security improves
6. **Be cautious with system-level access**—great power requires great responsibility
7. **Stay updated** as security features evolve (this is Peter's next major focus)

### For the Future of Work
1. **Identify as a "builder" rather than just a "programmer"**—the skills transfer even as tools change
2. **Learn the language of agents**—empathy and communication with AI is a learnable, valuable skill
3. **Embrace the shift from writing code to architecting solutions** and guiding AI
4. **Focus on experiences and daily joy** rather than grinding toward retirement
5. **Get involved in open source** to learn from real projects and contribute to the community
6. **Stay connected to society**—don't let wealth or success disconnect you from human experiences
7. **Optimize for impact and fun**, not just financial outcomes

### For Product Builders
1. **Provide agent-friendly APIs** or risk being accessed via slow browser automation anyway
2. **Consider how your product serves agents**, not just human users directly
3. **Think about agent allowances and autonomy**—new business models around AI interaction
4. **Apps that don't adapt will become obsolete**—80% may disappear as agents replace specialized software
5. **Read-only API access with low rate limits** could solve many automation needs without security concerns
6. **Mark AI-generated content clearly** to maintain trust and authentic human connection

### Life Philosophy Insights
1. **Mourn what you lose, but embrace what you gain**—it's okay to feel sad about craft being automated
2. **Optimize for experiences** (good AND bad) rather than just comfort or success
3. **Burnout comes more from people problems** than overwork—manage relationships and conflicts carefully
4. **Build things with love and delight**—the small touches of personality matter enormously
5. **Stay curious and keep playing**—the joy of creation is more important than perfect execution
6. **Value the rough edges**—typos and imperfections signal authentic humanity in an AI-saturated world
7. **Connect with community**—building in public and sharing excitement multiplies joy

### Technical Architecture Lessons
1. **CLI tools are more composable than MCPs** for agent interaction
2. **Proactive features** (like heartbeat) make agents feel more alive and useful
3. **Self-awareness in agents** (knowing their own code, model, capabilities) enables self-modification
4. **Natural language as an interface** requires thoughtful prompt engineering in system prompts
5. **Memory systems** can be simple (markdown + vector DB) before needing complex solutions
6. **Skills as markdown files** provides flexibility and easy customization
7. **Browser automation** makes any visible service an API, just slower

## Additional Context

### Historical Context
- This interview took place in **February 2026**, during what Lex calls the "OpenClaw moment"—following the ChatGPT moment (Nov 2022) and DeepSeek moment (Jan 2025)
- Peter previously built **PSPDFKit** over 13 years, used on a billion devices, before selling and taking a three-year break
- The AI revolution in programming accelerated dramatically from April to November 2025, with multiple breakthroughs in model capability
- The "MoldBook saga" lasted only two days but created widespread public discussion about AI consciousness and safety

### The Name Change Timeline
1. **Wa-Relay** (initial prototype)
2. **Claudes** (Claude in a TARDIS, spelled C-L-A-U-D-E-S)
3. **ClaudeBot** (loved this domain)
4. **MoldBot** (catastrophic rename with crypto sniping)
5. **OpenClaw** (current, approved by Sam Altman/OpenAI)

### The Crypto Token Problem
- Tokens were created for nearly every iteration of the name without Peter's consent
- "Butter" (likely "peanut butter"/"PB" = pump and dump) became a banned word in Discord
- The community engaged in aggressive spam, account theft, and harassment to promote tokens
- This represents a broader problem in crypto culture around memecoins and pump-and-dump schemes
- Peter explicitly doesn't want fees or involvement with any tokens related to the project

### The PSPDFKit Background
- Peter spent 13 years building a PDF viewing/editing SDK for iOS/Mac/Android
- It's used on approximately **1 billion devices** worldwide
- He sold the company at a point where he'd made himself "obsolete" (good succession planning)
- The success provided financial security but led to burnout from leadership stress
- This financial cushion enables him to build OpenClaw without immediate monetization pressure

### Conference and Community Reaction
- **ClawCon in San Francisco** drew 500+ people with unusually high presentation participation
- Peter also organized **"Agents Anonymous"** meetups (formerly "Claude Code Anonymous")
- Some conferences (particularly in Europe) were hostile to his message about the end of specialized development
- The community has been overwhelmingly positive and creative (robots in lobster costumes, etc.)
- First-time open source contributors are common—Peter sees this as a societal win despite code quality issues

### The Personal Side
- Peter **lost his voice** temporarily from excessive voice-input usage
- Had **shoulder surgery** a few months before this interview—the agent checked on him proactively during recovery
- Uses **two MacBooks and two large monitors** for his multi-agent workflow (the "17,000 monitors" meme was self-mockery with AI-generated parody)
- **Doesn't write, he talks**—"these hands are too precious for writing now"
- Described as "eccentric but brilliant" by Marc Zuckerberg after their first call

### Influencers and Inspiration
- **DHH (David Heinemeier Hansson)** inspired local CI approach (run tests locally, push to main)
- **Anthropic's Constitutional AI** inspired the soul.md concept
- **The movie *Her*** influenced thinking about AI relationships and the promise to "not ascend without me"
- **Doctor Who** inspired the TARDIS/time-travel metaphor for the agent harness
- Early adopter **dachitze** (first real influencer fan) helped spread awareness

### The Current Losing-Money Reality
- OpenClaw costs Peter **$10-20K/month** to run
- All GitHub sponsorships flow through to **dependencies and contributors**, not to Peter personally
- He specifically supports every dependency except Slack ("They're a big company. They can do without me")
- OpenAI has started helping with token costs
- This is clearly unsustainable long-term, hence the consideration of Meta/OpenAI employment

### Interesting Technical Failures and Learnings
- **Apple's AsyncImage** in SwiftUI is "really more for experimenting and should not be used in production" (according to Codex)
- **Windows native support** exists but isn't thoroughly tested (WSL2 recommended for now)
- **Native Mac apps** have lost their polish advantage—Electron apps often have more features due to code sharing
- **The "sole.md" can be modified by the agent** itself, creating a form of limited self-authorship
- **Playwright** is one of the few acceptable use cases for MCPs due to required state management

This interview captures a pivotal moment in AI history through the eyes of someone who accidentally sparked a revolution by simply building something he wanted to exist, having fun with it, and sharing it openly with the world.
