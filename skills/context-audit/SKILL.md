---
name: context-audit
description: Audit what loads into a coding session's context — enumerate every instruction layer (global rules, project rules, memory index, skills, hooks, MCP tools), find stray instruction files up the directory tree, measure each layer's size in tokens, and flag contradictions, duplicates, or obsolete references that degrade answers. Use when sessions feel misdirected, after adding a new tool or a new project, when context feels bloated, or on "audit my context", "what's loaded into context", "context hygiene check", "why is the session ignoring X". Works in Claude Code, Codex, and Cursor.
---

# Context audit

Every session's behaviour is shaped by instruction files it loads silently at start. A
stray, stale, or contradictory file degrades every answer without ever appearing on
screen. This audit walks the whole load surface, measures it, and flags what hurts.
Re-run it whenever a new tool or project joins the machine, when answers start
ignoring known rules, or roughly quarterly.

## 1. Enumerate the load surface

What actually loads, per layer (verify each with `ls -l` — a broken symlink means the
tool silently behaves as if it has no config):

| Layer | Path | Loads |
| --- | --- | --- |
| Personal rules | Inspect the active host's personal instructions, such as `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or Cursor rules; resolve any symlink and record its real source | as supported by the active host |
| Project instructions | Inspect repo `AGENTS.md`, `CLAUDE.md`, `.claude/rules/*` and any referenced instructions; establish which files the active host actually loads | according to host and project rules |
| Memory index | `~/.claude/projects/<project>/memory/MEMORY.md` | resident; the per-fact files load only on recall |
| Skills list | Inspect the active host's installed and project skills; record names, descriptions, real paths and duplicates | typically a resident list; bodies load when used; verify host behavior |
| Hooks | `settings.json` hooks (e.g. a SessionStart hook injecting a roadmap snapshot; per-prompt reply-style reminders) | as configured |
| MCP tool schemas | connected servers' tool definitions | verify which definitions are loaded and which use deferred discovery before measuring |

## 2. Hunt stray instruction files up the directory tree

Inspect the active host's rules for loading instructions from parent directories.
A forgotten `CLAUDE.md` in `~/Code/` or `~` may affect sessions below it, depending
on the host's loading rules. Inventory possible sources, then establish which load:

```bash
d=$(pwd); while [ "$d" != "/" ]; do
  ls -la "$d/CLAUDE.md" "$d/AGENTS.md" "$d/.cursorrules" "$d/.claude" "$d/.cursor" 2>/dev/null | grep -v '^total'
  d=$(dirname "$d")
done
```

Every hit must be accounted for in the layer table. A file nobody can explain is a
finding, whatever it says.

## 3. Measure

`wc -c` each resident artifact; tokens ≈ bytes ÷ 4. Report per-layer sizes and the
total a fresh session pays before any work happens. Tool-specific: in Claude Code the
user can run `/context` for the tool's own accounting — ask for it rather than
estimating when the exact number matters.

## 4. Flag what degrades answers

- **Contradictions between layers** — the same topic stated differently in personal
  rules, project rules, and memory. The fix is one authority and pointers.
- **Duplication** — a rule resident in two layers costs double and drifts; keep the
  authoritative copy, shrink the other to a pointer.
- **Obsolete references** — every file, flag, branch, command, or skill a resident
  rule names should still exist; spot-check with `ls`/`grep`. A rule pointing at a
  retired thing actively misdirects.
- **A prohibition with no clear alternative** — flag a "never X" whose useful
  alternative is unclear. Keep deliberate
  safety bans and bans on retired behaviour. This is a clarity check, not proof that
  negative wording causes disobedience.
- **Tool-specific content presented as universal** — split into a labeled
  tool-specific section instead (a bake-off between models needs identical, neutral
  shared context).

## 5. Route the fixes

Report findings first when the request is an audit. Apply authorized repo-layer fixes through
the project's normal review process; personal-layer fixes go to their actual owning file.
Memory fixes follow the lean strategy below. If a separate workflow-overhead review is
available and requested, use it for keep/trim/drop judgments about whether a rule earns
its cost; this skill maps and measures the load.

## The memory-layer lean strategy

The memory folder (`~/.claude/projects/<project>/memory/`) grows one file per fact and
never shrinks on its own. Keep it lean with these rules, re-run as part of this audit:

- **One fact per file stays the law**; `MEMORY.md` carries exactly one line per file.
- **Merge** when two or more files teach the same lesson; keep the strongest incident
  evidence in the merged body and delete the shells.
- **Delete** when the subject no longer exists AND the lesson generalizes to nothing.
  Establish a recoverable backup or versioned copy before deleting; do not assume
  memory files are committed automatically. Keep the deleted lesson in the change record.
- **"RESOLVED" alone is not a delete reason.** "This was fixed, don't re-fix it" is
  often the whole value of the memory; delete only when re-doing the work has become
  impossible or harmless.
- **Trigger:** re-run the memory section when `MEMORY.md` passes ~150 lines or the
  folder passes ~150 files.
