---
title: "How Easy Is It to Steal $10,000 From a Locked Phone?"
source: "https://www.youtube.com/watch?v=PPJ6NJkmDAo"
video_id: "PPJ6NJkmDAo"
duration: "25:40"
category: technology
---

# How Easy Is It to Steal $10,000 From a Locked Phone?

[Video](https://www.youtube.com/watch?v=PPJ6NJkmDAo)

## TL;DR

Veritasium and University of Surrey researchers demonstrate a **$10,000 contactless payment from a locked iPhone** by relaying and modifying NFC messages between phone and retail terminal. Exploit requires a specific combination: iPhone Express Transit Mode, suitable Visa card, physical proximity or stolen phone, online payment terminal, and specialized man-in-the-middle equipment.

This is a real protocol-composition flaw disclosed in 2021, but not a universal remote iPhone drain. Apple and Visa argue scaled abuse is unlikely and Visa's zero-liability policy protects cardholders; video argues reimbursement after theft is weaker than preventing vulnerability.

## What happened

MKBHD's iPhone remained locked throughout. Researchers first charged $5, then $10,000, without Face ID, passcode, or explicit payment approval. Retail terminal printed a receipt saying transaction was verified on device.

Funds were later reversed. Demonstration was authorized and performed with researchers who developed attack.

## Attack architecture

Attack inserts relay between phone and legitimate payment terminal:

1. NFC device near victim's iPhone impersonates card reader.
2. It forwards phone messages to laptop running modification script.
3. Laptop relays altered messages through burner phone near real terminal.
4. Phone and terminal each believe they communicate directly.

This is classic man-in-the-middle attack. Practical version could use stolen iPhone, or one attacker/device near phone and another at merchant terminal.

## Three protocol lies

### 1. Pretend retail terminal is transit gate

Apple Express Transit lets designated card pay transport fares while phone is locked. Attack reproduces transit-terminal signalling, causing iPhone to authorize payment without unlock.

### 2. Label $10,000 as low-value

Phone reportedly relies on a high-/low-value indicator rather than numerical amount when deciding whether cardholder verification is required. Relay flips indicator so phone treats $10,000 request as low-value transaction and skips Face ID/passcode.

### 3. Tell terminal customer verified

Phone response says no customer verification occurred. Retail reader would normally reject high-value payment. Relay flips verification indicator before passing response to terminal, which then forwards apparently verified transaction to bank.

## Why cryptography did not stop it

Raw control fields between phone and reader must interoperate across legacy payment ecosystem and are not all encrypted/integrity-bound in way that prevents modification.

Payment still uses symmetric cryptography between card/phone and bank. But exploit changes different views presented to phone and terminal.

Mastercard reportedly requires additional asymmetric card-to-reader signature verification for this transaction path. Any changed transaction field would fail signature check.

Visa requires that check only in some cases. In demonstrated online-terminal path:

- iPhone signs what it believes is low-value transit transaction;
- retail terminal believes it has high-value verified transaction;
- terminal does not validate signature that would expose mismatch because it is online;
- bank-side cryptographic check still passes for message path presented.

Vulnerability therefore emerges from interaction between Apple's Express Transit behavior and Visa verification rules, not broken RSA or stolen cryptographic key.

## Conditions and limitations

Attack is not universal. Video says it requires:

- iPhone;
- Express Transit enabled;
- suitable Visa card in transit slot;
- online retail terminal;
- physical NFC proximity or possession of phone;
- relay/modification hardware and software;
- payment accepted by issuing bank/network controls.

Samsung transit mode reportedly checks numerical amount and accepts only zero-value transit tap before transport provider aggregates fare later, blocking this exact path. Mastercard's signature verification also blocks it.

Bank fraud detection, merchant controls, issuer limits, and transaction monitoring can still reject payment. Demo proves technical possibility, not high prevalence.

## Disclosure and industry response

Researchers privately notified Apple and Visa before publishing attack in 2021.

Apple's stated position:

- issue concerns Visa system;
- Visa considers real-world abuse unlikely;
- Visa zero-liability policy protects cardholders.

Visa's position:

- attack is mainly controlled-lab scenario and hard to scale;
- network-level fraud detection limits abuse;
- cardholder can dispute unauthorized charge;
- fraud cannot be entirely eradicated.

Visa cited approximately:

- $0.10 fraud per $100 total card spend;
- $0.02 fraud per $100 for in-person transactions.

Video's counterargument: low aggregate incidence does not remove severe temporary harm from $10,000 withdrawal, dispute delay, and burden on victim.

## Practical defenses

- Disable Express Transit/Express Mode if convenience not needed.
- Avoid assigning Visa card as iPhone Express Transit card; exact risk varies by issuer, region, and current implementation.
- Enable instant transaction alerts.
- Lock/freeze cards and put lost iPhone into Lost Mode immediately.
- Use lower-limit transit card rather than primary high-limit card.
- Review statements promptly; dispute unauthorized transactions quickly.

These reduce exposure but do not substitute for protocol fix.

## Security design lesson

Each component can behave “correctly” locally while combined system fails globally:

- Apple trusts terminal-supplied classification.
- Terminal trusts relayed verification status.
- Visa permits path without reader-side signature validation.
- Bank sees cryptographically valid authorization but lacks consistent end-to-end context.

Core failure: **security-critical transaction semantics were not end-to-end integrity-bound.** Convenience exception crossed trust boundaries and created compositional vulnerability.

## YK read

Main takeaway is not “anyone can remotely steal $10,000 from any locked phone.” Attack is constrained and operationally awkward.

But severity matters because downside is high and fix appears conceptually clear: bind amount, terminal type, and customer-verification state into signature checked end-to-end. Fraud reimbursement treats loss as network economics; user experiences liquidity shock and recovery burden.
