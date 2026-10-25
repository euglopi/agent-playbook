---
name: systematic-debugging
description: >
  Find the root cause before proposing any fix. Use on any bug, test failure,
  crash, hang, unexpected output, performance problem, build or CI failure — and
  especially when a fix has already been tried and didn't work, when the cause
  "seems obvious", or when you're in a hurry. Hands off from design-intake for
  bug reports.
---

# Systematic debugging

*Adapted from the `systematic-debugging` skill in [obra/superpowers](https://github.com/obra/superpowers) (MIT). Trimmed to this setup: the upstream CI/codesigning example and the author's own eval fixtures are dropped, and the cross-references point at the public operating principles instead of the bundle's sibling skills. The upstream MIT notice is retained in `LICENSE`.*

## The Iron Law

**NO FIXES WITHOUT ROOT-CAUSE INVESTIGATION FIRST.**

A symptom fix is a failure, even when the symptom goes away. If Phase 1 isn't done, you don't get to propose a fix.

**Use this especially when it feels unnecessary:** under time pressure, when "just one quick change" looks obvious, when you've already tried something and it didn't work, or when you don't fully understand the issue. Simple bugs have root causes too, and the systematic path is *faster* than guess-and-check — measured against thrashing, it isn't close.

## Phase 1 — Root-cause investigation

1. **Read the error completely.** Full stack trace, line numbers, paths, codes. The answer is frequently in text that got skimmed.
2. **Reproduce it, and record how.** Name 1 command or safe observation that shows the user's exact symptom, and show its output with secrets and private data removed. Make it as fast and repeatable as practical. Intermittent: record how often it fails over a stated number of runs. Slow or live-only: keep the safe evidence (log lines, saved responses, timings) and say what it does not yet prove. Not reproducible: gather more data before forming a theory.
3. **Check what changed.** `git log`/`git diff`, recent merges, new deps, config, environment. With parallel sessions here, *someone else's* merge is a common cause — check `origin/main`, not just your own commits.
4. **Instrument the boundaries in a multi-component system.** Examples of layers include frontend → API → service → DB, and ingestion → parse → upsert → embed. Before proposing anything, log what enters and what leaves *each* boundary, run once, and let the evidence say which layer breaks. Verify the state at each layer rather than assuming it propagated.
5. **Trace the data backward.** Where did the bad value originate? What passed it in? Keep walking up until you reach the source, and fix there. Full technique: `references/root-cause-tracing.md`.
6. **Tag temporary logs** with 1 unique prefix (`[DEBUG-a4f2]`) and remove them by searching that prefix before finishing.

**Live systems get checked live.** A claim about what a deployed system contains or returns is not established by reading the code — the code says what it *would* do. Query the running system through authorized access and verify the *state*, not just presence. Never assume a production endpoint is public or needs no credentials. A hardcoded default proves intent, not outcome.

## Phase 2 — Pattern analysis

Find working examples of the same thing in this codebase. Read the reference implementation **completely** rather than skimming — partial understanding guarantees bugs. List every difference between working and broken, however small; "that can't matter" is where the bug hides. Note what the broken path depends on: config, env, assumptions.

Apply [Operating principles, Consider the whole system, keep execution scoped](../../guides/operating-principles.md#consider-the-whole-system-keep-execution-scoped): trace every actual caller and downstream use of the failing logic before selecting a correction. Record demonstrated failures, shared exposure, untested paths and intentional differences in the existing task plan or review. Include source, privacy, data and product requirements that a shared fix must preserve. A narrow build scope does not narrow this investigation or authorize changes outside it.

## Phase 3 — Hypothesis

When the evidence points to 1 cause, state it: "I think X is the root cause, because Y." When it does not, rank the plausible causes, each with the observation that would tell it apart. Test with the **smallest possible change**, 1 variable at a time. It worked → Phase 4. It didn't → form a *new* hypothesis; do not stack another fix on top. If you don't understand something, say so plainly instead of proceeding on a guess.

## Phase 4 — Implementation

1. **Write the failing test first.** Simplest reproduction that fails for the right reason — an automated test where a suite exists, a one-off script where it doesn't. This is [Operating principles, Building and shipping](../../guides/operating-principles.md#building-and-shipping): logic bugs need pre-fix failure.
2. **One fix, addressing the root cause.** No "while I'm here" improvements, no bundled refactor: the same Code discipline rule, trace each changed line to the request.
3. **Verify:** the new test passes, nothing else broke, the original symptom is actually gone. Rerun the recorded reproduction against the original full scenario, not only the narrowed test. Use the project's per-domain verification checklists when available.
   Reconcile the impact-and-prevention record with the result: check confirmed affected uses, preserve approved differences, and retain focused regression coverage for the shared cause. Ask the independent reviewer to look for missed uses and missing prevention. A reproduced shared defect does not prove an unobserved user failure has the same cause; record remaining uncertainty and required evidence before claiming it fixed.
4. **If the fix didn't work, count your attempts.** Under 3 → back to Phase 1 with what you just learned. **At 3+ → stop and question the architecture.**

**The 3-failure rule.** When each fix reveals a new problem somewhere else, or fixes keep requiring "massive refactoring," that is not a failed hypothesis — it's the wrong architecture. Stop fixing and raise it. Attempting fix #4 without that conversation is the mistake.

## Red flags — stop and return to Phase 1

"Quick fix now, investigate later" · "just try changing X and see" · "let me change several things and run the tests" · "skip the test, I'll check by hand" · "it's probably X" · "I don't fully understand this but it might work" · listing fixes before tracing the data · **"one more attempt" after two failures** · each fix surfacing a new problem elsewhere.

**Signals from the user that you're already off-track:** "is that not happening?" (you assumed instead of verifying) · "stop guessing" · "we're stuck?" · asking you to check something you claimed was fine.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "It's simple, skip the process" | Simple bugs have root causes. The process is quick on simple bugs. |
| "Emergency — no time" | Systematic is faster than thrashing. |
| "Try this first, investigate after" | The first fix sets the pattern. |
| "I'll add the test once the fix works" | Untested fixes don't stick. |
| "Several fixes at once saves time" | You can't tell which one worked, and you've added bugs. |
| "The reference is long, I'll adapt it" | Partial understanding guarantees bugs. Read it all. |
| "I can see the problem" | Seeing the symptom is not understanding the cause. |
| "One more attempt" (after 2+) | 3+ failures means architecture, not another patch. |

## When there really is no root cause

If investigation genuinely lands on environmental, timing-dependent, or third-party behaviour: say what you investigated, implement appropriate handling (retry, timeout, clear error), and add logging for next time. But assume incomplete investigation first — that's what it usually is.
