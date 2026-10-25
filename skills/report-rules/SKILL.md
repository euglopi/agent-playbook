---
name: report-rules
description: Report-specific rules for a standalone report or PDF, on top of the presentation-rules skill. Use for research reports, data reports, revenue plans delivered as PDF, and report templates.
---

# Report rules

Load `presentation-rules` first; it holds the brand foundations, assets, structure, table
and copy rules. This file adds only what a standalone report needs.

- The full symbol-and-wordmark lockup is required on a standalone report, because it may be
  read outside its original context. Posts and graphics on the website use the approved symbol alone.
- Letter size, white page. The cover follows the presentation skill; the running header
  carries the part name and the footer the page number.
- Tables are sized for their actual longest headings and values with side padding. Every
  numeric value, 3-digit row numbers included, stays on 1 line without clipping or tiny type.
- Keep the report's factual scope, totals, source links, caveats and section hierarchy when
  changing its design.
- Render the finished report, inspect every page, and run an automated overflow and
  numeric-wrap check when tables are generated programmatically. Fix every unreadable line,
  broken link, awkward page break or clipped cell before delivery.

The request controls over this skill, including any express background, logo or layout
choice. Never reuse report-specific data or claims from an earlier report.
