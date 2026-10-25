---
name: design-audit
description: Review a rendered web interface for accessibility, interaction and usability against a pinned snapshot of Vercel's Web Interface Guidelines. Use for a UI or accessibility review. Includes adaptations for React Native and Expo web output; does not design or restyle the interface.
---

# Web Interface Guidelines (pinned) with framework reconciliation

A UI review lens: read the rules, check the target, output terse `file:line` findings.
Use the project's approved interaction and accessibility requirements alongside this rubric.

## Rules source — pinned, do NOT live-fetch

Read the local snapshot: **`rules-snapshot-2026-07-13.md`** (in this skill folder).

The upstream skill fetches its rules from a live URL on every run. That is a supply-chain /
prompt-injection surface and needs network. This install deliberately pins a **dated, verbatim
snapshot** instead. To update: re-download `command.md` from the source repo (below), save it as
`rules-snapshot-<new-date>.md`, delete the old snapshot, and bump the date in this file. Refresh
deliberately, not automatically.

## How to run

1. Read `rules-snapshot-2026-07-13.md`.
2. Read the target the user names (a screen, a rendered page, or a specific file).
3. Apply the rules **through the framework reconciliation below** — not literally.
4. Output findings grouped by file, `file:line`, terse, per the snapshot's Output Format. This is the engineering artifact.
5. **Then explain the final recommendations in plain, non-technical layman's terms** — this is what the user actually reads. For each finding: name what it is by pointing to what they'd *see on screen* (e.g. "the grey hint text inside the address box"), say what the suggestion is, and why it matters *or* why it's minor, plus your take. Assume zero web/dev knowledge: never use `WCAG`, `AA`/`AAA`, `px`, `placeholder`, `aria`, `contrast ratio`, `token`, etc. without a plain-words gloss (say "the little tappable pills," not "the chips"; "how easy the text is to read against its background," not "contrast ratio"). If a finding can't be explained without jargon, you don't understand it well enough yet. The terse `file:line` list is for the engineer; the plain-language version is the deliverable.

## Framework reconciliation (read before every review)

First identify the actual frontend framework. For **React Native + Expo shipped to
web via `react-native-web`**, source uses RN primitives (`<View>`, `<Text>`,
`<Pressable>`, `<Image>`), not raw DOM/CSS/Tailwind. The snapshot is written for
the DOM. In that stack apply it like this:

- **Do NOT lint RN source files literally.** Rules naming raw HTML tags (`<button>`, `<img alt>`),
  ARIA attributes, CSS properties (`focus-visible:ring-*`, `transition: all`, `overscroll-behavior`),
  Tailwind classes, Next.js/hydration/`<meta>` specifics, and `env(safe-area-inset-*)` do **not** map
  to RN `.tsx` and will fire false positives. RN has its own equivalents (`accessibilityLabel`,
  `accessibilityRole`, `accessibilityState`, `hitSlop`, `SafeAreaView`, the `focus` shadow token).
- **Audit the RENDERED web output, not the source.** Run the app through its documented start command
  or open the intended preview. `react-native-web` emits real DOM there and maps RN a11y props to ARIA,
  so the DOM-level rules become checkable. **Fix findings by editing the RN props/tokens**, never by
  hand-editing DOM.
- **The platform-agnostic subset always applies, source or rendered.** This is the high-value core and
  it covers: visible focus, WCAG-AA contrast, ~44px touch targets, no
  affordance living only in hover, shareable state is represented in the URL where the product requires it, destructive
  actions confirm, honor reduced-motion, designed loading/empty/error states, `tabular-nums` for number
  columns, `…`/curly quotes, active-voice specific button labels.
- **Copy findings defer to approved copy.** Read the project's wording and punctuation
  rules. Do not overwrite deliberate product terminology or a documented exception
  merely to match a generic snapshot. Flag conflicts and explain the reader effect.
- **Check the actual accessible name.** A differing `accessibilityLabel` and
  `placeholder` can produce repetitive announcements in some RN-Web and screen-reader
  combinations. Inspect the rendered accessible name and listen to the target screen
  reader before changing either. Keep a clear name while the field is empty and after
  typing. Where label and placeholder repeat the same meaning, reconcile them using
  the project's approved field pattern; never remove the only persistent name based
  on a source-only rule. Icon-only controls still need an accessible name.

## Scope note

This reviews shipped UI. It does not generate or restyle designs. The user's
review scope controls whether fixes may be implemented.

If the project already has a specialist accessibility review, use this as the
broader interaction and polish pass on rendered web output. Do not assume an
installed plugin or a previous project's review results prove coverage here.


---

*Rules snapshot adapted from Vercel's [Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines)
(MIT License, © 2025 Vercel Labs — see `LICENSE`). Snapshot pinned 2026-07-13. This wrapper adds the
framework reconciliation; the rule text itself is unmodified.*
