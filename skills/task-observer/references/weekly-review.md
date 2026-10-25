# The observation review — procedure

Loaded from `../SKILL.md`. Adapted from the upstream "Comprehensive Review"
([upstream project](https://github.com/rebelytics/one-skill-to-rule-them-all)) for
local coding agents. Apply edits only within the user's authorization.

## Trigger — ad hoc, never on a timer

This reference describes an on-demand review. It does not install a schedule.
Any recurring review needs the user's explicit authorization, including its cost
and cadence. Run an ad hoc review when requested or within authorized skill work;
retain review-only boundaries and apply only authorized changes.

In a review-only run, all edits, status/name corrections, timestamps and archive
moves below are proposals for the report. Do not write any files. The editing
steps apply only when the user has authorized those changes.

## Steps

**1 — Load.** Read `skill-observations/log.md`; take every entry with `Status: OPEN`. Read
`skill-observations/cross-cutting-principles.md` for active principles. No OPEN entries and no
unpropagated principles → say so in one line and stop. Update the timestamp only
when writing review records is authorized; a review-only request permits no writes.

**2 — Inventory the skills.** Discover the active host's personal, project and
plugin skill roots from its current catalog and configuration. These are separate
populations. Examples include `~/.claude/skills/`, `~/.codex/skills/`,
`~/.agents/skills/` and a repository's own skills folder; they are not an exhaustive
or universal load order. Resolve shared links before counting duplicate copies.
Vendor-managed plugin skills are not ours to edit. Route an observation to an
authorized local adaptation or the upstream feedback channel without changing
the installed vendor package. Sending feedback requires the user's permission.

**3 — Cross-check, don't trust the tag.** For each OPEN observation, judge relevance against *every*
skill, not just the one its `Skill:` field names — the `Principle` field often generalises past its
original context. Build skill → [observations].

**Skill names drift.** Resolve the current name before applying an older observation.
Correct the name in the log only during an authorized editing run; otherwise
include the proposed correction in the report.

**4 — Check principles.** For each active cross-cutting principle, find skills that don't yet comply.

**5 — For authorized edits, apply AND mark as one step, one observation at a time.** Edit the skill file **in place** —
using the active host's supported workflow and existing authorization. Integrate the
insight where it belongs structurally; don't append an observations list at the bottom. Preserve the
skill's voice and its author attribution. **Then, before you touch the next observation, write its
status back to `log.md`:** `ACTIONED — Applied to <skill> <date> (<PR or commit>)`. Change nothing
else in the entry. Ship through the owning repository's approved review and release process.

> **Apply and mark before moving on.** An implemented change left marked OPEN creates
> false work for the next review. Keep each application and its status update together.

**Escalate instead of applying** — report these, don't act:

1. **Creating a new skill.** Name, scope, and home are the user's call.
2. **Deleting or restructuring existing content**, where institutional memory is at risk. (Note the
   asymmetry with an overhead audit, which *is* chartered to restructure — this exemption is about
   unreviewed deletion, not about the audit's verdicts.)
3. **An observation that flags its own uncertainty** — "not sure if…", "worth discussing…" is the
   entry asking for input.
4. **Conflicting observations** where the reconciliation isn't obvious.

**6 — Identify what's already done or dead.** Before assuming an OPEN entry is work, **check whether it
was already implemented** — grep the skill it names for the change it asked for. Mark those `ACTIONED — Already implemented (verified <date>)`. Separately,
mark as `DECLINED` anything **superseded** — covered by a memory or rule since, obsoleted by new
tooling, or pointing at a skill that no longer exists — with the reason, so the next reader doesn't
re-litigate it. A one-off that never recurred is a legitimate DECLINE, not a failure.
Make these status changes only in an authorized editing run; otherwise report them.

**7 — Timestamp.** When writing review records is authorized, write today's date
to `skill-observations/last-review-date.txt`. Keep review-only runs read-only.

**8 — Report.** Per skill: what changed, which observation numbers, and the commit or PR. Then the
ACTIONED list, then anything escalated with the reason. **State the split** — how many were real work
versus already-done versus superseded — because that ratio is the health signal for the log itself.
Lead with a plain-language Net.

## Archival

During an authorized editing run, resolved entries move to `skill-observations/archive/log-<YYYY-MM-DD>.md` (the directory does not
exist yet — create it on first archive). Archival runs **on the next write, not the current one**: an
entry marked ACTIONED or DECLINED during *this* review stays in the active log for one full cycle, so
it gets a round of visibility before disappearing. Only archive entries resolved in a *previous*
session. The active log keeps its header and status key.

If `log.md` is not versioned, there is no `git revert` for it. Establish a recovery
copy before a bulk or scripted edit.

## Constraints

- Don't modify observation entries beyond their status (and a stale skill name, per step 3).
- Don't create new skills here — escalate the candidate.
- If an observation is relevant but you can't see how to integrate it, skip it and say so.
- `internal` entries get the same rigour as `open-source` ones.
