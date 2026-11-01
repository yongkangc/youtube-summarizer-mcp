---
title: "Joseph Kim: Building ChatGPT for Finance"
source: https://www.youtube.com/watch?v=v-d1WTqIULs
channel: Latent Space
guest: Joseph Kim, OpenAI
hosts: swyx and Richard
date_uploaded: 2026-10-31
date_summarized: 2026-11-01
---

## TLDR

OpenAI's finance product is less about a separate finance model and more about reliable data, firm-specific workflows, and reviewable outputs built on a general model. Kim expects AI to move from junior-analyst execution toward judgment-heavy work, but acknowledges that evaluating investment ideas is much harder than checking spreadsheets.

## Source scope

Reviewed all 971 caption segments through approximately 27:36; metadata runtime is 27:34. This is an OpenAI executive's product/research interview, not independent verification of availability, accuracy, benchmark quality, security, or investment performance. Model and vendor names in captions are occasionally garbled; uncertain identifiers omitted. The linked keynote and announcement were not independently reviewed for this summary.

## Main points

### 00:56–04:27: general intelligence, specialized delivery

- Kim describes ChatGPT for Financial Services as an enterprise product combining general ChatGPT capabilities with financial data, firm templates, and enterprise requirements. He names Morgan Stanley and Evercore as design partners.
- Financial reasoning training is incorporated into the shared main model, rather than kept exclusively in a finance-specific first-party model. This is his stated approach, not an API/model-availability guarantee for every feature.
- He says internal nonengineering adoption of Codex jumped toward 90% after the desktop app launched. The adoption denominator and methodology are not provided: treat this as an anecdote that interface design can unlock existing capability, not proof of productivity improvement.

### 04:27–09:18: connectors alone do not make a product

- Kim says tests of some large-name financial-data MCP integrations showed error rates above 40%. He does not specify vendors, tasks, sample size, error definitions, or timing. This is not a general failure-rate estimate for MCP.
- OpenAI therefore bundled/controlled more of the data experience end to end, despite customers potentially already holding licenses or having connectors. The thesis is reliability and less integration friction, not that a protocol itself supplies trustworthy data.
- He estimates 95% of the product could have been built by another company using available plugin primitives, without privileged model changes. His 80%-generic/20%-specialized framing is a product heuristic, not an engineering measurement.
- The possible startup opportunity is proprietary or licensed data, UI, integrations, and domain-specific workflows on top of a strong horizontal agent. His prediction of a billion-dollar plugin business is speculation, not evidence of a moat or distribution economics.

### 09:18–15:46: current safety assumes human review

- The launched product is a productivity tool with humans responsible for reviewing its output, not an unattended investment decision-maker or trading system.
- Kim points to existing bank review chains: junior analyst → associate → VP → director/managing director. Future agents could inherit role-like permissions and checks familiar from human teams.
- He expects factual reliability to improve and argues existing review systems can catch errors. His claims that humans make comparable mistakes and severe propagated errors are unlikely are not supported by comparative data here.
- Important caveat: a human nominally in the loop is not a sufficient control. Review needs source traceability, independent recalculation, clear responsibility, permission boundaries, and safeguards against reviewers simply trusting polished output.

### 15:46–19:04: correctness and taste are separate

- Spreadsheet sums, reference validity, and other mechanical checks are verifiable. Presentation quality, financial-model structure, and sensible sensitivity behavior also require expert judgment.
- Kim describes collecting human pairwise preferences to train reward models, including judgments about slides. He argues humans can often recognize visual quality more efficiently than models can explain it.
- The coding analogy is useful: passing tests is not the same as producing maintainable code. Likewise, an error-free workbook is not necessarily an economically sensible model.
- Preference training can improve perceived quality but does not by itself establish truth, calibration, fiduciary suitability, or investment alpha.

### 19:04–25:25: moving up the analyst stack makes evaluation harder

- Initial products target concrete, tedious work: Excel models, slides, and specific instructions. Kim wants to move into associate- and MD-level tasks, including investment ideas, during 2027.
- These are research priorities and forecasts, not demonstrated capabilities. An investment idea may take years to assess; a convincing thesis or expert preference score is not realized risk-adjusted performance.
- Kim says existing financial evals are inadequate and some have saturated or contain incorrect answer keys and ambiguous prompts. He describes developing profession-specific evaluations that better predict real task automation.
- He explicitly notes an investigation bias: researchers investigate flat/bad scores more readily than good scores. This makes it important to audit both apparent improvements and alleged benchmark defects.
- His critique does not prove models have solved finance. Independent, out-of-sample task evaluation and robust grading remain necessary.

### 25:25–end: distribution and hiring

- At recording time, Kim describes an enterprise product and an effort to broaden access to Pro users, not a confirmed universal rollout or date.
- He says the team is hiring engineers, product managers, and finance subject-matter experts. Domain expertise matters because model researchers do not automatically know what good banking, research, or asset-management work looks like.

## Practical read-through for a one-man fund

- Use agents first for source extraction, reconciliation, repeatable calculations, sensitivity analysis, and memo preparation, with provenance attached.
- Build an acceptance checklist: correct entity, as-of date, units, filing version, source location, formula, and reconciliation. Assess whether model behavior under changed inputs makes economic sense.
- Preserve a separation between research assistance, investment judgment, portfolio-risk approval, and order execution. This interview does not justify autonomous trading permissions.
- Evaluate research quality on source fidelity, falsifiability, novelty, decision usefulness, and later outcomes, not fluent prose or analyst-like aesthetics.
- **Theory of edge required:** any proposed trade must identify a structural reason for compensation and why price fails to reflect it. Neither faster spreadsheets nor a plausible AI-generated narrative establishes alpha.

## One-line conclusion

The near-term product advantage is trusted data and reviewable workflow, not an AI that has proven it can independently pick winning investments.
