---
name: task-observer
description: >
  Capture patterns, corrections, and workflow insights worth preserving as
  reusable skills. Use when the user mentions skill observations, skill
  improvements, the observation log, or skill taxonomy, asks you to watch for
  skill opportunities, says "One Skill to Rule Them All", during post-task
  feedback, or for the weekly observation review. Not at session start —
  the shared personal rules capture observations inline; load this on request or for the review.
---

# Task Observer — skill discovery & improvement

**Methodology created by Eoghan Henn / [rebelytics.com](https://rebelytics.com)**, released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). *Also known as "One Skill to Rule Them All."*
This file is a portable adaptation for local coding agents; the upstream original
is available from the linked project. Local environment assumptions and private
examples were removed in this public edition. Methodology feedback belongs upstream at
[the skill's repo](https://github.com/rebelytics/one-skill-to-rule-them-all).

## How this fits the actual setup — read first

**Capture and review are separate.** [Operating principles](../../guides/operating-principles.md#observations)
defines the public entry format. Configure inline capture in the project's own
instructions if desired; installing this skill does not create a hook or schedule.
What this skill is for:

- the **weekly review** — cross-checking OPEN observations against the skills and applying them,
- **acting on a specific observation** when the user names one,
- deciding **where a new skill belongs** and what it must contain before it ships.

**Log:** `<project root>/skill-observations/log.md`. Establish whether it is versioned;
back it up before any bulk edit if recovery is not already assured. Principles: `skill-observations/cross-cutting-principles.md`.
Review timestamp: `skill-observations/last-review-date.txt`.

**Environment — this is a local coding agent, not Cowork.** The upstream original assumes a read-only skill
mount, a `[workspace folder]`, staged copies under `skill-updates/`, a `present_files` tool and an
upload button. **None of those exist here.** In this setup:

- Skill files are **writable and edited in place**. Each host's personal skills folder points to
  the actual user-owned skill source. Commit and publish changes only within the
  requested scope and repository policy. Repo skills follow the project review process.
- Applying an improvement needs **the user's existing authorization**. Within an
  authorized edit, use a recoverable in-place change rather than asking the user to
  perform steps the agent can do. A review-only request never permits an edit.
- Use the current host's `skill-creator` when it is available; otherwise write skills directly.
- Use the current host's task-list controls rather than assuming a specific tool name.

## What to watch for

**A NEW skill:** a multi-step workflow that will recur · a methodology the user explains that no skill
captures · a task type that keeps arriving with the same shape · "I always do it this way."

**IMPROVING an existing skill:** a documented rule that got ignored anyway (needs enforcement, not
louder wording) · a correction revealing a missing rule or uncovered edge case · a recommended
workflow that proved slower than what emerged naturally · a technique that worked well enough to
promote from incidental to explicit · a wrong assumption · a new tool making a step obsolete · a
correction that has now happened more than once.

**SIMPLIFYING an existing skill** — ask this as deliberately as "what should we add?":

- a section never relevant across multiple sessions where the skill was active
- a rule added from one observation and never validated by recurrence
- an elaborate workflow that gets shortcut every time
- content loaded but never acted on
- rules that contradict each other
- a rule the agent keeps failing to follow — usually remove it, or convert narrative guidance into
  structural enforcement (a checklist, a verification step, a tool call that can't be skipped)

**Do NOT log:** one-off corrections that don't generalise · preferences an existing skill already
covers · tool bugs unrelated to methodology.

## How to log

The entry format is defined in [Operating principles](../../guides/operating-principles.md#observations) (Status / Date / Session context / Skill / Type /
Issue / Suggested improvement / Principle) — that is canonical; don't restate a competing format here.
Append silently, in the same turn as the trigger. A mental note is not an observation.

**Numbering, with parallel sessions writing the same file.** Always `### Observation N:` and always
append to the END. Never trust a remembered count. Pre-check, then verify after the write, because
check-then-append is two operations and another session can land between them:

```bash
# POSIX / macOS — grep -P is unavailable on this platform
NEXT=$(( $(grep -o '^### Observation [0-9]*' log.md | grep -o '[0-9]*' | sort -n | tail -1) + 1 ))
grep -qE "^### Observation ${NEXT}:" log.md && echo "COLLISION on ${NEXT} — recompute past all"
# ...append using ${NEXT}, then confirm you still own it:
[ "$(grep -cE "^### Observation ${NEXT}:" log.md)" -gt 1 ] && echo "RACE — renumber my line to max+1"
```

If either check fires, renumber past **all** existing numbers rather than incrementing by one — and
log the collision itself as an observation.

## Log, or act?

Default is **log, don't act.** Observations are applied in exactly three situations: the weekly
review · the user naming one ("apply #12") · a skill actively producing wrong output right now, which
is surfaced immediately rather than held. Mid-task work produces observations only.

## References

| File | Load when |
|---|---|
| `references/weekly-review.md` | Running the review — the procedure, the escalation list, the archival rules |
| `references/publishing-a-skill.md` | A skill may go public: internal-vs-open-source, licence, attribution, confidentiality sweeps |
| [Upstream project](https://github.com/rebelytics/one-skill-to-rule-them-all) | Original methodology, licence, and comparison base for upstream updates |
