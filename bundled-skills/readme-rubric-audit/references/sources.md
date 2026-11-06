> Last verified: 2026-07-20

# Sources

Annotated bibliography. Every KB file's trailing `Sources:` line keys into this
table. `last-verified` = date the source was actually re-fetched; `status` =
active / moved / dead (dead sources keep their row with an archive link where
possible — claims still cite them).

## Canonical standards & templates

| Key | Source | URL | Claims derived | Verified | Status |
|---|---|---|---|---|---|
| standard-readme | RichardLitt/standard-readme (spec) | https://github.com/RichardLitt/standard-readme/blob/main/spec.md | Formal section order, required/optional, TOC 100-line rule, License-last, title/one-liner rules | 2026-07-20 | active |
| best-readme-template | othneildrew/Best-README-Template | https://github.com/othneildrew/Best-README-Template | Hero conventions, Prerequisites subsection, back-to-top links, anti-rigidity stance | 2026-07-20 | active |
| art-of-readme | hackergrrl/art-of-readme | https://github.com/hackergrrl/art-of-readme | Cognitive funneling, tired-evaluator principle, brevity, image caution, badge skepticism, API section rules | 2026-07-20 | active |
| makeareadme | Make a README | https://www.makeareadme.com/ | Baseline sections, expected-output rule, project-status honesty, novice-level install detail | 2026-07-20 | active |
| readme-so | readme.so section taxonomy | https://github.com/octokatherine/readme.so | Section block inventory; only default block is Title+Description; no prescribed order | 2026-07-20 | active |
| jehna-practices | jehna/readme-best-practices | https://github.com/jehna/readme-best-practices | Copy-paste template order, runnable code-block rule, GIF demo placement | 2026-07-20 | active |
| banesullivan-readme | banesullivan/README | https://github.com/banesullivan/README | Highlights-first, bare-minimum set, usage-before-install variant, dev-setup segregation, four evaluator questions | 2026-07-20 | active |
| rdd-essay | Preston-Werner, README-Driven Development | https://tom.preston-werner.com/2010/08/23/readme-driven-development.html | README-first rationale | 2026-07-20 | active |
| awesome-readme | matiassingers/awesome-readme | https://github.com/matiassingers/awesome-readme | Exemplar corpus for the per-type sample (catalog descriptions can lag live files) | 2026-07-20 | active |
| observed-types-2026-07 | 20-README structural sample (this project's research) | see [research log](../../../research/log/2026-07-20-initial-research.md), cluster 2 | Per-type structures, TOC threshold, hero-style split, badge-as-type-signal, exemplar patterns | 2026-07-20 | active |

## Badges

| Key | Source | URL | Claims derived | Verified | Status |
|---|---|---|---|---|---|
| shields-io | Shields.io catalog | https://shields.io/badges | Badge categories, styles | 2026-07-20 | active |
| shields-static-badge | Shields.io static badge docs | https://shields.io/badges/static-badge | Static syntax, escaping, params | 2026-07-20 | active |
| gh-actions-badge | GitHub Docs: workflow status badge | https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge | Badge-to-workflow-file binding, branch pinning, private-repo limits | 2026-07-20 | active |
| observed-badges-2026-07 | 7-repo badge sample (this project's research) | see [research log](../../../research/log/2026-07-20-initial-research.md), cluster 3 | Count norms, ordering families, flat-style universality, placement | 2026-07-20 | active |
| cicirello-badges | Cicirello, "Badges – TL;DR" | https://dev.to/cicirello/badges-tldr-for-your-repositorys-readme-3oo3 | Metadata+link test, >5 → table rule, badge-wall criticism | 2026-07-20 | active |
| dailydev-badges | daily.dev badge best practices | https://daily.dev/blog/readme-badges-github-best-practices/ | 2–4 badge stance, staleness warnings, single-sourcing | 2026-07-20 | active |
| usethis-badge-a11y | usethis badge accessibility | https://usethis.r-lib.org/articles/badge-accessibility.html | Alt-text purpose-label rule, WCAG contrast caveats | 2026-07-20 | active |

## AI-era

| Key | Source | URL | Claims derived | Verified | Status |
|---|---|---|---|---|---|
| agents-md | AGENTS.md spec | https://agents.md/ | README-humans/AGENTS.md-agents split, recommended sections, monorepo nesting, adoption (60k+ repos), AAIF governance | 2026-07-20 | active |
| llmstxt | llms.txt proposal | https://llmstxt.org/ | Format, purpose, complement-not-replace | 2026-07-20 | active |
| claude-memory-docs | Claude Code memory docs | https://code.claude.com/docs/en/memory | CLAUDE.md bridging (@AGENTS.md), <200-line target, specific-imperative rule | 2026-07-20 | active |
| eth-agentsmd-study | Gloaguen et al., "Evaluating AGENTS.md" (ETH Zurich/LogicStar) | https://arxiv.org/abs/2602.11988 | Generated context files −3% success +20% cost; human-written ~+4%; non-standard practices are what helps | 2026-07-20 | active |
| lulla-agentsmd-study | Lulla et al., "Impact of AGENTS.md on Efficiency" | https://arxiv.org/abs/2601.20404 | ~29% lower median runtime, ~17% fewer output tokens with AGENTS.md | 2026-07-20 | active |
| daplab-hcc | DAPLab, "Your AI Agent Doesn't Care About Your README" | https://daplab.cs.columbia.edu/general/2026/03/31/your-ai-agent-doesnt-care-about-your-readme.html | Non-obvious-info principle, size caps. **Tool write-up, not a study** — quantitative claims belong to the arXiv papers | 2026-07-20 | active |
| augment-agentsmd | Augment Code AGENTS.md guide | https://www.augmentcode.com/guides/how-to-build-agents-md | No-duplication rule, non-obvious-patterns section, permission tiers, snippet-over-prose | 2026-07-20 | active |
| morphllm-agentsmd | MorphLLM AGENTS.md guide | https://www.morphllm.com/agents-md-guide | Never-duplicate-README, 20–30-line start. **Fetched via search excerpts only (HTTP 429); spot-check on next refresh** | 2026-07-20 | active |
| ericmjl-agentsmd | Eric Ma, teaching agents with AGENTS.md | https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/ | Curated-memory framing, update-on-error workflow | 2026-07-20 | active |
| upsun-readme | Moigneu, "Why your README matters more than AI configuration files" | https://developer.upsun.com/posts/insights/why-your-readme-matters-more-than-ai-configuration-files | Counter-position: README as single source of truth | 2026-07-20 | active |
| ben3d-ai-readme | Houston, "Crafting READMEs for AI" | https://ben3d.ca/blog/crafting-readmes-for-ai | README as AI efficiency cache | 2026-07-20 | active |

## GitHub platform

| Key | Source | URL | Claims derived | Verified | Status |
|---|---|---|---|---|---|
| gh-about-readmes | GitHub Docs: About READMEs | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes | Placement precedence (.github > root > docs), auto-TOC, relative links, 500 KiB truncation | 2026-07-20 | active |
| gh-writing | GitHub Docs: writing & formatting | https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | Alerts, anchors, kbd/sub/sup, footnotes, task lists, color-chip README exclusion, picture element | 2026-07-20 | active |
| gh-markup-sanitizer | github/markup pipeline + GFM tagfilter | https://github.com/github/markup · https://github.github.com/gfm/#disallowed-raw-html-extension- | No CSS/JS/iframe/class/id; surviving tags; align/width survive | 2026-07-20 | active |
| npm-readme-docs | npm: About package README files | https://docs.npmjs.com/about-package-readme-files | GFM-via-GitHub-API rendering, publish-time refresh, no alerts/mermaid/math | 2026-07-20 | active |
| pypi-readme-guide | PyPI-friendly README guide + readme_renderer | https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/ · https://github.com/pypa/readme_renderer/blob/main/CHANGES.rst | content-type requirement, allowlist history (details 19.0, picture 43.0, no video/source), absolute-URL need | 2026-07-20 | active |
