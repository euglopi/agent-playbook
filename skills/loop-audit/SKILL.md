---
name: loop-audit
description: Evaluate the post-task loop WITHOUT acting — run the same investigation as loop-run (bugs the work exposed, loose ends, stale docs/issues, lessons to capture) but change nothing; produce a ranked triage list of findings with recommended actions, effort, ownership/collision status, and safe-to-auto flags, for the user to approve. Invoke as /loop-audit, or when the user says "what would the loop do", "audit the follow-ups", "triage what's left", "show me before you touch anything", "dry-run the loop". Read-only counterpart to /loop-run. Authoritative principle lives in the shared rules file (guides/operating-principles.md, Authorization).
---

# loop-audit (evaluate the loop, take no action)

This is the "show me what the follow-up loop *would* do, but don't touch anything" button. It runs the exact same investigation as `loop-run` but is strictly **read-only** — it produces a ranked triage list of adjacent follow-ups with a recommended action per item, for the user (or a later `/loop-run`) to approve and execute. Use it when the field is risky, when you want a plan before any change, or to queue work for review. Part of the `loop-*` family of loop-engineering skills.

## loop-audit vs loop-run
- **`loop-audit` (this skill):** evaluate **only**. Investigate read-only; change **nothing** — no file edits, no PRs, no issue creation/edits/comments, no data mutations, no process kills. Output a triage report for approval.
- **`loop-run`:** evaluate **and act** — executes the safe/reversible/in-lane items itself and reports after.

## Hard rule: this skill takes NO mutating action
While running loop-audit, the only permitted operations are **read-only investigation** (read files, `git log`/`diff`/`grep`, read-only DB queries, `gh issue/pr view`, `ps`, log reads). Do **not**: edit or create files, open/merge PRs, create/edit/close/comment on issues, run migrations or data writes, kill processes, or push. If the investigation itself would require a write to learn something, note it as "needs a write to confirm" rather than doing it. The deliverable is a report, not a change.

## Procedure — investigate all four rounds, then report
Investigate the same priority order as `loop-run`, but instead of acting, collect candidate items:

1. **Bugs / regressions the work exposed.**
2. **Cleanup / loose ends it left behind.**
3. **Stale specs, docs, or issues the change invalidated.**
4. **Lessons → durable homes** (skills/rules/specs/observation-log gaps).

For each candidate, resolve ownership and verify live state read-only (a finding may already be fixed by a teammate). Then produce a ranked triage list — highest-value + unblocked + reversible first — where every item carries:

- **What / where** — the finding and its location (file:line, issue #, table, etc.).
- **Round** — which of the 4 it belongs to.
- **Evidence** — what you observed (read-only) that establishes it.
- **Recommended action** — the specific change you'd make.
- **Effort** — small / medium / large.
- **Ownership / collision** — unowned, or the named session that owns it (session id/name, not git author — multiple sessions may share a Git identity) + route-around note.
- **Safe-to-auto?** — would `loop-run` execute this unattended (reversible + in-lane + verifiable), or does it hit a reserved pause (toss-up, product, scope, policy, spending or access choice not already authorized, unverified-irreversible)? Flag the reason.
- **Net** — plain-language one-liner: what it means / why it matters.

End with: a one-line summary count, and the handoff — "approve items to execute, or run `/loop-run` to act on the safe-to-auto set." If nothing valuable surfaced, say so plainly rather than padding the list.

## Guardrails
- **Scope = blast radius of the current work + the repo's open issues/specs.** Don't wander or manufacture busywork.
- **Verify, don't infer** (read-only): re-check live state before listing a finding as still-open.
- **Don't collide** — resolve ownership and name any session you'd route around; but since this skill only reports, the collision risk is only in what you'd *recommend* — flag it clearly so an approver doesn't step on a teammate.
- **When nothing valuable surfaces, say so and stop.**

## Related
- Skill `loop-run` — the acting sibling (evaluate and execute).
- [Operating principles](../../guides/operating-principles.md) — shared authorization and ownership boundaries.
- `guides/operating-principles.md` — "name which session"; plain-language Net convention.
- The current project's instructions control authorization, knowledge placement and release.
