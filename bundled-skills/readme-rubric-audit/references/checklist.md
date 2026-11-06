> Last verified: 2026-07-20

# Review checklist

Scored rubric for review mode. Verify each item against the repo, not just the
README text — run commands where cheap, check links, compare claims to code.

**Scoring:** each item is pass/fail at its weight. Score = points earned /
points applicable × 100. Items marked ○ (not applicable to this project type
per `anatomy.md`'s matrix) are excluded from the denominator.
**Critical items (★): any ★ failure caps the total score at 49.** A README
that lies cannot score "good" no matter how pretty it is.

Bands: 90–100 exemplary · 75–89 solid · 50–74 needs work · <50 failing.

## Identity (15)

| W | Check |
|---|---|
| 5 | Title matches repo/folder/registry name |
| 7 | One-liner directly under title states what it does **and for whom**, ≤ ~120 chars |
| 3 | One-liner matches the GitHub repo **About** description (query it — a local clone won't show it; an empty About fails this) |

## Trust ★ (25)

| W | Check |
|---|---|
| 10 ★ | Install and usage commands actually work as written (verify against manifests, `--help`, CI config) |
| 5 ★ | No aspirational features presented as current capability |
| 5 | All links resolve (sample at minimum every install/docs/registry link) |
| 3 | Screenshots/demos reflect the current version |
| 2 | Maintenance status honest (active/maintenance/archived signaled when relevant) |

## Onboarding (25)

| W | Check |
|---|---|
| 8 | Installation is a copy-runnable code block, standard registry one-liner included |
| 8 | Usage shows a minimal working example **with expected output** |
| 4 | Prerequisites state exact versions/OS where they exist |
| 3 | Type-appropriate visual proof present (CLI: GIF/screenshot; web app: UI shot; research: diagram) |
| 2 | Dev setup segregated from user install |

## Structure (15)

| W | Check |
|---|---|
| 6 | Section order follows the canonical funnel (broad → narrow; no install-before-why) |
| 4 | README is an entry point: deep reference linked out, not inlined (unless deliberately a reference README) |
| 3 | TOC only if warranted (~120+ lines) and in sync with headings |
| 2 | License section present, correct, linked to LICENSE file |

## Craft (10)

| W | Check |
|---|---|
| 4 | Badges: 3–6, one block, one style, all linked, dynamic where possible, none red/stuck, alt text |
| 3 | Markup portable for the project's distribution (no GitHub-only features in registry-shipped READMEs) |
| 3 | Skimmable: no screen-height stretch without a heading, list, or code block; objective tone (facts and benchmarks, not adjectives) |

## Agent-readiness (10)

| W | Check |
|---|---|
| 4 | Every command copy-pasteable with exact flags (agents execute verbatim) |
| 3 | Non-obvious constraints stated explicitly rather than left for archaeology |
| 3 | No agent instructions inlined; pointer to AGENTS.md/CLAUDE.md if they exist |

## Report format

1. Score + band, with per-category subtotals.
2. Top 3–5 fixes ranked by reader impact (★ failures always first).
3. Each finding names its checklist item or the `anti-patterns.md` entry.
4. Concrete replacement text for the single worst offender.

Sources: synthesized from all KB files; see anatomy, section-guide, badges, anti-patterns, ai-readers
