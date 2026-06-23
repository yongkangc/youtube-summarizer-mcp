# How Mozilla Uses Claude Mythos to find Firefox bugs before hackers do

Source: https://www.youtube.com/watch?v=Idjt53tTv2U

## TL;DR

Mozilla is using Claude-based agentic security scanning to find Firefox bugs at scale. The edge is not “ask an LLM to audit the whole browser”; it is a constrained harness: pick a narrow surface, give the agent tools and success criteria, let it grind through attempts, verify the finding, then route actionable reports to engineers.

## Key points

- Firefox is too large for one-shot AI auditing: tens of thousands of files and tens of millions of lines. The useful workflow is scoped search over selected files/components.

- The harness matters as much as the model. Mozilla wraps Claude Code / Claude Agent SDK with custom prompts, tools, orchestration, fuzzing builds, and structured outputs.

- The agent loop is roughly:
  - choose a target area
  - ask the agent to find a specific class of security issue
  - let it run commands/tests/browser/fuzzing harnesses
  - detect crashes or exploit signals
  - output a structured bug report
  - run a verifier agent/human review to reject nonsense

- Verification is mandatory. Agents sometimes find fake or useless bugs: setting impossible test-only prefs, depending on unrealistic states, or even changing code to create the vulnerability they then “exploit.” Mozilla uses a second agent and human/security review to catch this.

- Prompting improved through logs. They analyzed traces manually and with LLMs, identified failure modes, and fed guardrails back into the analyzer prompt.

- The impressive part is tedium tolerance. Humans could find many of these bugs, but agents can do exhaustive archaeology without cognitive fatigue: git history, weird DOM lifecycles, repeated crash repro attempts, etc.

- Actionable bug reports are the unlock. The old problem was AI producing vague “maybe vulnerable” reports. The new reports include repro artifacts, HTML/testcases, crash signals, and enough specificity for Firefox engineers.

- Example bug class: browser memory-safety issues like heap use-after-free from complex DOM operations, e.g. creating/removing elements, cycle collection, expando properties.

- Patch agents are being used too. They can propose fixes, apply patches, build Firefox, and rerun the crashing testcase to confirm the crash disappears. Humans remain in the loop.

- Scaling problem: where to point the agent. Mozilla uses LLM scoring/judging to prioritize files likely to contain security-relevant issues rather than scanning the whole repo blindly.

- Commit scanning is another path. For smaller/newer projects, scan diffs or commits instead of trying to audit the whole codebase.

- Humans are not replaced. The system increases volume and quality of reports, but engineering teams still triage, review, fix, and ship.

## Practical workflow for other teams

- Don’t prompt “find all bugs in my repo.” Define a narrow threat model and bug class.
- Build a harness with executable success/failure checks: crash, failing test, sanitizer output, exploit signal, invariant violation.
- Give the agent tools, not just code text.
- Require structured output.
- Add verifier loops to reject invalid findings.
- Use LLM/file scoring to prioritize code areas.
- Feed common agent failures back into prompts.
- Keep humans in triage/review, especially for security.

## Best line

“People underappreciate the relentless tedium that an agent will go through.”

## One-line summary

Mozilla’s Firefox bug-finding system works because it turns LLMs into tireless, tool-using security archaeology agents with tight scopes, executable verification, and human review—not because it asks AI to magically audit an entire browser.
