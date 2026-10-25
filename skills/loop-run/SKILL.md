---
name: loop-run
description: Run the post-task loop — after finishing a piece of work, deliberately hunt for AND act on the sensible adjacent follow-ups (bugs the work exposed, loose ends, stale docs/issues, lessons to capture) instead of stopping. This is the ACTING version — it executes the safe/reversible/in-lane items itself and reports after. Invoke as /loop-run, or when the user says "run the loop", "do the follow-up pass", "what else should we clean up after this — and do it", "keep going on adjacent work". For evaluate-only (report for approval, take no action) use /loop-audit instead. Runs on request within the user's authorization; shared boundaries are in guides/operating-principles.md.
---

# loop-run (act on adjacent follow-ups)

This is the manual "run the follow-up loop and do it" workflow: after finishing something, investigate sensible adjacent work, execute authorized safe/reversible pieces, and report after. Its read-only sibling is `loop-audit` (same evaluation, but reports for approval instead of acting). Shared boundaries live in [Operating principles](../../guides/operating-principles.md#authorization); this skill is the procedure to run on request. Part of the `loop-*` family of loop-engineering skills.

## loop-run vs loop-audit
- **`loop-run` (this skill):** evaluate **and act** — execute safe/reversible/in-lane items (edits, low-risk PRs, issue updates, lessons capture), report after. Reserved pauses still stop for approval.
- **`loop-audit`:** evaluate **only** — investigate read-only and produce a ranked triage list with recommended actions for approval; changes nothing. Use it when the field is risky, or when the user wants to review before anything happens.

## When this runs

Invoke this skill for an explicitly requested follow-up pass or as part of an
already authorized completion workflow. Installing it does not create an always-on
hook, expand the task's scope, or authorize recurring work.

## Procedure — one round at a time, until safe/valuable/unblocked work runs out
Each round, pick the next item in priority order and act within the existing request (report after; do not ask again for already authorized reversible work):

1. **Bugs / regressions the work exposed.** New defects the just-finished change surfaced. If already tracked *and owned by another session* → record precise measurements on that issue and route around; don't fix (that collides).
2. **Cleanup / loose ends it left behind.** Orphaned processes, temp state, half-done edits, dead references your own change created.
3. **Stale specs, docs, or issues the change invalidated.** Update or close them — including issues *you* filed that later verification proved wrong (correct them before anyone acts on the bad version).
4. **Lessons → durable homes.** Whatever the session taught you (a pitfall, a better approach, a gap) → write it into the relevant skill, `.claude/rule`, spec, or observation log **this session**, so the next similar/adjacent task is faster and more accurate.

Favor **highest-value + unblocked + reversible-first**. Batch a short what/why/outcome + plain-language **Net** per item so the user can course-correct.

## Guardrails
- **Scope = the authorized current work and directly related issues/specs.** Don't wander into unrelated areas or manufacture busywork.
- **Verify, don't infer.** Re-check live state before acting on an earlier finding — it may have been resolved by a teammate since you recorded it.
- **Don't collide with teammate sessions, and NAME the one you're routing around** (session id/name, not git author — several sessions may share a Git identity). Resolve ownership (PRs, commits, live processes, DB connections, assignees) before acting; never mutate shared state another session is using.
- **Reserved pauses:** a genuine toss-up (no basis to prefer), product, scope, policy, spending or access choices not already authorized, and never fire an unverified irreversible real-world side effect. When an item hits one of these, don't act — hand it to `loop-audit`-style triage (report it for approval).
- **When blocked on the user,** hand off with an actionable guide (exact steps, where to find what's needed, decisions-with-recommended-defaults, how you'll verify and continue) saved with the task and summarized in chat; update an external issue only when authorized — don't just say "blocked on X".
- **When sensible adjacent work runs out, say so and summarize.** Don't invent more.

## Related
- Skill `loop-audit` — the report-only sibling (evaluate, don't act).
- [Operating principles](../../guides/operating-principles.md) — authorization, completion and ownership boundaries.
- The project's own instructions control authorization, knowledge placement and release.
