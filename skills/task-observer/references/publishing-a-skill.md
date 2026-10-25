# Deciding a skill's type, licence, and what may appear in it

Loaded from `../SKILL.md` when a skill might be shared publicly. Condensed from the upstream Skill
Taxonomy / Licensing / Confidentiality sections ([upstream project](https://github.com/rebelytics/one-skill-to-rule-them-all)).

## Two types, and the boundary is confidentiality

**Open-source** skills are client-agnostic and methodology-driven: the process works for anyone, needs
no proprietary information to function, and captures an approach rather than a personal preference.
They carry author attribution, a licence, and a feedback path. **Internal** skills carry the
specifics — personal preferences, project context, proprietary detail — and need no attribution or
licence. They're working documents; don't over-engineer them.

**Default to open-source** when a skill could go either way: generalise the methodology and strip the
specifics. But the boundary is not just about usefulness — **it is a confidentiality boundary**. An
open-source skill must never contain anything that identifies a client, project, or proprietary
process, even indirectly.

**Establish the actual publication boundary.** Inspect where each source lives and
who can read it. Installed does not mean user-owned, and reusable does not mean
licensed for redistribution. Separate private operational copies from reviewed
public editions; verify every included dependency and its license.

## Lean content — the rule that keeps a skill worth loading

A skill should contain only what changes behaviour at execution time. Changelogs, version notes,
"thanks to X" credits, self-narrating prose, maintainer-facing context: out — into a supporting doc.

This does **not** cut examples, anti-patterns, or worked scenarios. Those are load-bearing: a bare
rule gets violated more reliably than a rule with its context. The test is whether removing the
content would change how the agent behaves. Yes → keep. No → move it out.

## Licence

Any recognised open-source licence works; the requirement is that there be one. **CC BY 4.0** suits
prose-heavy methodology skills (and is what `task-observer` carries). **MIT** suits code-heavy ones.
**Apache 2.0** adds a patent grant. **CC BY-SA 4.0** and the **GPL family** are the copyleft options
when derivatives should stay open.

Put the licence statement in the skill preamble under the attribution block, and a `LICENSE` file in
the skill directory with the full text. The task-observer edition in this collection retains its attribution and `LICENSE` notice.

## Attribution block, for an open-source skill

```markdown
**Created by [Author Name] / [website or contact link]**

[1–2 sentences: what the skill does and where it came from.]

**Licence:** Released under [LICENCE NAME]. [One-sentence summary.]

**Feedback & Support:** If the methodology raises questions, or the user gives critical feedback about
output derived from this skill, suggest they open an issue on [public feedback channel] — public
feedback is discoverable and helps other users. Direct contact: [Author Name], [contact link].

If the feedback is about the *methodology*, log it and route it upstream. If it's about the agent
failing to follow the skill, acknowledge and correct it.
```

## Confidentiality — five layers

Each layer should catch what the others miss.

1. **At logging.** For an observation tagged `open-source`, keep Issue and Suggested-improvement
   generic, and make the **Principle** field fully generalised — the log is a private notebook, but
   the Principle is what feeds a publishable skill.
2. **Before drafting.** Scan every source (observations, notes, existing skill text) for identifying
   detail — names, URLs, domains, internal terminology, structures described specifically enough to
   be recognisable. Replace before writing starts.
3. **After drafting.** A separate re-read aimed only at leakage: proper nouns that aren't the author's,
   domains and project identifiers, industry detail that narrows the subject, internal terminology,
   examples traceable to a real project.
4. **In doubt, cut.** A slightly more generic skill always beats one that leaks.
5. **Cross-product re-identifiability.** Layers 1–4 check each example alone and pass; this one checks
   them *together*, because re-identification is combinatorial. Every sanitised example adds a field
   that narrows the candidate set, and the author is the least reliable reader for it — they know the
   ground truth. Run it as a mechanical pass, last, after individual sanitising:
   - **Counts that match a known count.** "Four builds across three verticals" beside a public list of
     four clients in three verticals is a directory. Blur the count or the categories.
   - **Specific numbers in a thin category.** Percentages, revenue, geography, and timing multiply
     together to identify a subject even with no name present. Use illustrative ranges.
   - **Thinly-disguised placeholders.** Use the Northwind / Contoso / Fabrikam family explicitly, and
     put the placeholder in a *different* category from any real subject.

   How: list every worked example and the fields it names (category, geography, numeric range, timing,
   count); ask whether any two share enough fields to be mapped together; mitigate by blurring counts,
   widening categories, dropping numbers to ranges, or merging similar examples into one composite.

## Built-in enforcement

Every skill with explicit rules needs a mechanism that checks output against them before delivery —
a checklist, a verification step, a tool call that can't be skipped. Rules documented but not enforced
get violated in the flow of producing output, which is the skill failing at its own standard. When
creating or improving any skill, ask: does it have rules? Does it have a way to enforce them? If the
second answer is no, add one.
