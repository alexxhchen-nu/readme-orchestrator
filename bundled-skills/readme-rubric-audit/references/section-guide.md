> Last verified: 2026-07-20

# Section guide

Per-section authoring rules, in canonical order. Each rule is sourced; where
canonical sources conflict, the recommendation picks a side and says why.

## Title

- Must match the repo, folder, and package-registry name; note any mismatch in
  the description (standard-readme spec).
- Self-explaining names win; if the name doesn't say what it does, the
  one-liner has to work twice as hard (art-of-readme, makeareadme).

## One-liner (short description)

- Directly under the title, no heading. Under ~120 characters. Identical to the
  GitHub repo description and the registry description (standard-readme spec).
- Says what the project does **and for whom / what problem it solves** in one
  sentence; define specialized terms inline (art-of-readme).
- This is the single highest-leverage line in the file: it's what search
  results, registry listings, and social cards show.
- The GitHub **About** description is this same sentence in another place. Keep
  them identical, and update both together (`gh repo edit --description`). The
  README file alone leaves the About stale.

### Tagline pattern

A repeatable shape for the one-liner and its matching About, so one owner's repos
read as a single voice:

`<Article> <plain-noun category> that <does the core thing>[, for <audience>].`

- One sentence, sentence case, present tense.
- Lead with the noun (what it *is*), not a verb or a hook.
- Drop the audience when the category already implies it; add `for <who>` only
  when it's genuinely distinctive.
- No marketing adjectives ("blazingly fast", "revolutionary"); let the noun and
  verb carry it.
- Keep it short (aim ~45-80 characters), and set the GitHub About to the same text.
- For a set of repos under one owner, keep them uniform in length and shape so
  they read as one voice, like copy on a single site.

Aligned examples (one owner, one voice):

- "A research agent that cites and checks its sources."
- "A Claude Code skill that writes and reviews your README to a standard."
- "An AI newsroom that writes and fact-checks a weekly journal."

## Badges

See `badges.md`. One block under the title, 3–6, one style, all dynamic where
possible, all linked, alt text always.

## Screenshot / demo (visual projects only)

- If the project has a UI or visible output, show it before asking the reader
  to read: screenshot for apps, animated GIF or terminal cast for CLIs
  (makeareadme, jehna, banesullivan).
- Never encode critical information only in an image — images rot and agents
  and screen readers can't read them (art-of-readme). Alt text always.
- Use the `<picture>` dark/light pattern for theme-sensitive images; the
  `<img>` child is the universal fallback (GitHub docs).

## Description / highlights

- 2–3 paragraphs max: what it does, why it exists, how it differs from the
  alternatives — named respectfully (makeareadme, banesullivan).
- A short bulleted **Highlights/Features** list before or after the prose lets
  skimmers bail early with the right impression (banesullivan, jehna).
- Long background/motivation moves to a Background section or linked doc
  (standard-readme spec).

## Table of contents

- GitHub auto-generates a TOC from headings in the file-header UI, so a manual
  TOC is **optional below ~100 lines** and useful mainly for long READMEs or
  READMEs read off-GitHub (GitHub docs; standard-readme requires one over 100
  lines).
- If present: starts at the section after itself, never lists the title or
  itself (standard-readme spec).

## Prerequisites

- Exact versions and OS requirements, stated for novices — name the ecosystem
  tools involved (makeareadme). A one-line "Requires Node 20+" beats a missing
  section; omit entirely only when truly zero-prerequisite.

## Installation

- A code block of copy-runnable steps — prose descriptions of installation are
  a defect (standard-readme spec, jehna).
- State the standard registry one-liner even when obvious (`npm install pkg`);
  link the registry page (art-of-readme).
- Development setup is a different audience: segregate it at the bottom or in
  CONTRIBUTING, don't interleave it with user install (banesullivan).

## Usage / quick start

- Minimal working example first, with **expected output shown** (makeareadme).
- Ordering note: canonical sources split on Install-first (standard-readme,
  makeareadme, Best-README-Template) vs Usage-first (art-of-readme,
  banesullivan — show value before setup cost). Recommendation: Install first
  when install is one line; Usage first when installation is heavy and the
  value needs proving.
- Keep the example honest: ship it as a runnable file in the repo where
  practical; code samples must pass the project's linter (art-of-readme,
  standard-readme spec).
- CLIs: show the invocation *and* its output (art-of-readme).

## Configuration / API

- README carries the entry point, not the reference: link out to `API.md`,
  docs site, or generated reference (standard-readme spec, art-of-readme).
- If API examples get long, that's a signal the API may be too complex, not
  that the README needs more sections (art-of-readme).

## Status / roadmap

- Say if the project is actively developed, maintenance-only, or archived;
  flagging slowed development honestly invites maintainers instead of losing
  users silently (makeareadme).
- Task lists (`- [x]`) render nicely on GitHub for roadmaps.

## Contributing

- Link-only: point to CONTRIBUTING.md, the issue tracker, and where questions
  get asked. State the PR acceptance policy in one line if it's unusual
  (standard-readme spec, makeareadme). Do not inline contribution guides.

## License

- Full license name or SPDX id + link to the local LICENSE file. Conventionally
  the last section (standard-readme spec requires it last; art-of-readme's
  near-the-top variant is worth considering only for license-sensitive
  audiences).

## Acknowledgments / citation

- Credit past maintainers and significant influences (standard-readme spec);
  research projects add a citation block (see `templates/research-data.md`).

## Pointer to agent files

- If the repo has AGENTS.md / CLAUDE.md / llms.txt, end with a one-line pointer.
  Never inline agent instructions in the README (see `ai-readers.md`).

## Formatting rules (platform-derived)

- Root-level `README.md`; `.github/README.md` silently overrides it — avoid
  surprises (GitHub docs).
- Portable-by-default markup: GFM core renders everywhere; alerts
  (`> [!NOTE]`), `<details>`, `<picture>` degrade gracefully; mermaid, LaTeX
  math, `:emoji:` shortcodes, and uploaded videos are GitHub-only — avoid them
  in READMEs that ship to npm/PyPI, or commit an exported SVG instead
  (GitHub docs, npm docs, readme_renderer changelog).
- Relative links for in-repo navigation on GitHub; absolute
  `raw.githubusercontent.com` image URLs for any README published to a
  registry (PyPI packaging guide).
- No inline CSS/JS/iframes — the sanitizer strips them; `align` and `width`
  attributes on `<img>` survive (github/markup, GFM tagfilter).
- No broken links, ever (standard-readme spec). Keep well under GitHub's
  500 KiB display truncation limit.

Sources: standard-readme, best-readme-template, art-of-readme, makeareadme, readme-so, jehna-practices, banesullivan-readme, rdd-essay, gh-about-readmes, gh-writing, gh-markup-sanitizer, npm-readme-docs, pypi-readme-guide
