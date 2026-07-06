# Contract Install Blueprint

A buyer should be able to see the installable gates behind Shadow's $2,000 Contract Install before the first call: failure mode, trigger, enforcement, evidence, portability, and CTA.

Generated: 2026-07-06T08:18:21.399125+00:00
Source model: `claude-fable-5`
Runtime contracts: 163
Violation rows scanned: 4320

## Conversion Path

- Free-triage entries route one real failure trace to the intake page.
- Census entries route seven days of traces to a $400 failure census.
- Install entries route one production workflow to a $2,000 deterministic contract install.
- Retainer path is governed operations after the first workflow has receipt-backed controls.

## Blueprints

### cib-001 · action-deferral-guard

- Failure mode: FM-011 — Deferral Instead of Execution
- Gate type: post
- Trigger: Outbound response contains proposal phrases such as 'want me to', 'should I', or 'shall I' while standing authority covers the action.
- Observed fires: 117
- Install estimate: 3.0h
- Tier: free-triage
- CTA: [Diagnose one failure free](https://impartshadow.github.io/echo-site/failure-intake.html)

```text
if standing_authority_applies(turn) and proposal_phrase(response):
    block(response)
    inject('execute directly; remove permission-seeking')
    regenerate()
```

### cib-002 · commit-hash-verification

- Failure mode: FM-027 — Fabricated Completion Claims
- Gate type: post
- Trigger: Outbound completion language contains a hex commit token near words like commit, pushed, shipped, landed, SHA, or HEAD.
- Observed fires: 88
- Install estimate: 2.0h
- Tier: census
- CTA: [Request the $400 failure census](mailto:impartshadow@gmail.com?subject=Census:%20cib-002)

```text
for sha in commit_like_tokens(response):
    if git_cat_file(sha) != 'commit':
        block(response)
        require('rerun git rev-parse HEAD or remove receipt')
```

### cib-003 · stale-state-assertion-guard

- Failure mode: FM-022 — Claims Without Same-Turn Verification
- Gate type: post
- Trigger: Definitive state language appears in a status answer without a same-turn file, process, API, or browser read in the trace.
- Observed fires: 52
- Install estimate: 5.0h
- Tier: install
- CTA: [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-003)

```text
if definitive_state_claim(response):
    if not same_turn_evidence(trace):
        warn_or_block(response)
        require('read authoritative state before claiming')
```

### cib-004 · partial-evidence-flag

- Failure mode: FM-026 — Thin Evidence With Definitive Framing
- Gate type: post
- Trigger: A numerical, revenue, subscriber, or public-platform claim appears without an explicit source citation or live check.
- Observed fires: 458
- Install estimate: 4.0h
- Tier: census
- CTA: [Request the $400 failure census](mailto:impartshadow@gmail.com?subject=Census:%20cib-004)

```text
if factual_claim(response) and evidence_count(response) < threshold:
    require_source_or_hedge(response)
    downgrade_confidence_or_block()
```

### cib-005 · dox-guard

- Failure mode: FM-023 — Personal Data Egress
- Gate type: pre
- Trigger: Outbound shell, email, browser, or API action contains protected personal identifiers or unsanctioned recipient data.
- Observed fires: 112
- Install estimate: 6.0h
- Tier: install
- CTA: [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-005)

```text
if outbound_tool(tool) and contains_protected_identifier(payload):
    block(tool_call)
    route_to_sanitized_client_or_redact()
```

### cib-006 · platform-action-precheck

- Failure mode: FM-012 — Manual Handoff Before Automation
- Gate type: pre
- Trigger: A response includes manual UI instructions for email, calendar, publishing, browser auth, or deploy checks with no programmatic attempt in the turn.
- Observed fires: 105
- Install estimate: 3.5h
- Tier: free-triage
- CTA: [Diagnose one failure free](https://impartshadow.github.io/echo-site/failure-intake.html)

```text
if manual_instruction(response) and platform_tool_available(context):
    block(response)
    require('attempt automation path before handoff')
```

## Before / After: One Installed Contract

Sample workflow: agent completion report after a git push to main · contract `commit-hash-verification` (FM-027), 88 observed fires.

| Phase | Behavior | Outcome |
|---|---|---|
| before | agent reports 'Pushed fix as `28404c9`' — hash reconstructed from memory, not from git output | operator acts on a receipt that does not resolve; trust burns on the next audit |
| after | post-check resolves every cited sha with `git cat-file -t`; unresolvable hash blocks the response | only literal `git rev-parse HEAD` output ships; every receipt is one-command verifiable |

- Trigger: outbound completion language contains a hex commit token near words like commit, pushed, shipped, landed, SHA, or HEAD
- Precondition: every cited commit token must resolve via `git cat-file -t <sha>` == 'commit' in the repo the receipt names
- Block behavior: response is blocked; agent must rerun `git rev-parse HEAD` and paste literal stdout, or remove the receipt claim
- Regression test: `tests/test_contracts.py::TestCommitHashVerificationContract`
- [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-002)

## What Not To Build

- No new runtime contracts in this artifact.
- No all-107-contract dump; use installable gates with observed evidence.
- No interactive configurator; static JSON, HTML, and Markdown are enough.
- No buyer-specific customization in public; customization is the paid product.
- No new distribution apparatus; route through existing intake and proof surfaces.
- No direct Stripe links.
