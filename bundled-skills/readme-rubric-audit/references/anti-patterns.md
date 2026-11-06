> Last verified: 2026-07-20

# Anti-patterns

Named failure modes for review mode. Each has a detection cue and a fix.

## Structure

- **Install-before-why** — installation instructions appear before the reader
  knows what the project does or for whom. Violates cognitive funneling
  (art-of-readme): broadest information first, so each reader can bail as soon
  as they know it's not for them. Fix: title → one-liner → (demo) → then install.
- **The wall of text** — no headings, or prose where a code block belongs.
  Detection: any screen-height stretch without a heading, list, or code block.
- **Everything-README** — API reference, contribution guide, and changelog
  inlined. The README is an entry point; deep docs live elsewhere and get
  linked (art-of-readme, standard-readme, banesullivan).
- **Orphan TOC** — a manual TOC that lists sections that no longer exist or
  misses ones that do. GitHub auto-generates a TOC; a manual one is a
  maintenance liability that must earn its place (GitHub docs).

## Honesty

- **The lying README** — commands that error, flags that changed, features
  described but never shipped. Worse than no README: it burns trust and, in
  the agent era, agents execute those commands verbatim (ai-readers.md).
  Review mode must run/verify claims, not just read them.
- **Stale screenshot** — UI images from several versions ago. Detection cue:
  screenshot content contradicts the current feature list; image files years
  older than recent releases.
- **Aspirational tense** — "will support", "coming soon" presented as current
  capability. Fix: move to a Status/Roadmap section, honestly labeled
  (makeareadme's project-status guidance).
- **Zombie status** — no commits in years, README silent about it. Honestly
  flagging maintenance status invites maintainers instead of silently losing
  users (makeareadme).

## Badges (see badges.md for detail)

- **Badge wall** — haphazard row of everything remotely relevant; reads as
  noise (Cicirello).
- **Vanity badge** — unlinked or information-free (visitor counters,
  decorative made-with tags).
- **Dead badge** — CI badge pointing at a renamed/removed workflow; unpinned
  branch showing the wrong run.
- **Mixed styles / scattered badges** — inconsistent geometry, badges outside
  the single top block.

## Writing

- **Assumed context** — jargon and ecosystem knowledge unexplained, prior-art
  unlinked. "No module is an island": link concepts on first use
  (art-of-readme).
- **Marketing-first** — superlatives ("blazingly fast") in place of evaluable
  facts. The README's job is to help readers "evaluate what your creation does
  as objectively as possible," not to sell (art-of-readme). Benchmarks may
  brag; adjectives may not.
- **Example without output** — usage code shown but not what it produces.
  "Show the expected output if you can" (makeareadme).
- **Prose installation** — install steps described in sentences instead of a
  copy-runnable code block (standard-readme spec).

## Platform

- **Registry-broken markup** — mermaid blocks, LaTeX math, `:emoji:`
  shortcodes, alerts, or relative image links in a README that ships to
  npm/PyPI, where they render as raw text or 404 (npm docs, readme_renderer,
  PyPI packaging guide).
- **Critical info only in an image** — hosting rots; agents and screen readers
  can't read it (art-of-readme).
- **Sanitizer casualties** — layouts depending on inline `style=`, `<iframe>`,
  or custom classes; GitHub strips them all (github/markup).

## Agent-era

- **Inlined agent instructions** — agent-only rules cluttering the README
  instead of living in AGENTS.md (agents-md spec).
- **README/agent-file duplication** — AGENTS.md restating the README; evidence
  says duplication adds cost and can reduce agent success (eth-agentsmd-study).
- **Generic agent advice** — "follow existing patterns", "write clean code":
  instructions an agent can't act on. Non-obvious specifics only (daplab-hcc,
  augment-agentsmd).

Sources: art-of-readme, standard-readme, makeareadme, banesullivan-readme, gh-about-readmes, cicirello-badges, dailydev-badges, npm-readme-docs, pypi-readme-guide, gh-markup-sanitizer, agents-md, eth-agentsmd-study, daplab-hcc, augment-agentsmd
