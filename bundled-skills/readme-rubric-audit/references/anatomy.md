> Last verified: 2026-07-20

# Anatomy

The canonical section order, synthesized from the consensus of eight canonical
sources (standard-readme's formal spec, Best-README-Template, Art of README,
Make a README, readme.so, jehna, banesullivan, RDD) and verified against 20
top-tier real READMEs sampled 2026-07. Ordering principle: **cognitive
funneling** (art-of-readme) — broadest information first, so every reader can
bail out the moment they know it's not for them.

## Canonical order

1. **Title** (+ logo/hero for polished projects)
2. **Badges** — one block, 3–6 (research projects: bracket-link nav
   `[[Paper]] [[Demo]] [[BibTeX]]` instead — observed in all sampled research repos)
3. **One-liner** — what + for whom, no heading
4. **Visual proof** — type-dependent: terminal GIF (CLI), UI screenshot
   (web app), architecture diagram (research); libraries often need none
5. **Teaser snippet** — libraries/frameworks: a few lines of code showing the
   API's feel, placed *before* install (requests, express, zod, fastapi pattern)
6. **Highlights / features** — bulleted, skimmable
7. **Table of contents** — only if long (see threshold below)
8. **Prerequisites / requirements** — exact versions
9. **Installation** — copy-runnable code block
10. **Usage / quick start** — minimal working example with expected output
11. **Configuration / API** — entry point + link-out to real docs
12. **Status / roadmap** — honest maintenance state
13. **Contributing** — link-only
14. **License** — one line + link (research: full subsections when code/weights/
    data carry different terms — the alphafold pattern)
15. **Acknowledgments / citation** — BibTeX block for research
16. **Agent-file pointer** — one line to AGENTS.md/CLAUDE.md/llms.txt if present

## Required / recommended matrix by project type

R = required · ✓ = recommended · ○ = if applicable · — = usually omit

| Section | Library | CLI | Web app | API/service | Research | Minimal |
|---|---|---|---|---|---|---|
| Title | R | R | R | R | R | R |
| Badges | ✓ (version→CI→downloads) | ✓ (CI→release→license) | ✓ | ✓ (CI→coverage→version) | — (bracket-nav instead) | — |
| One-liner | R | R | R | R | R | R |
| Visual proof | — | R (GIF/screenshot) | R (UI screenshot) | ○ | ✓ (diagram) | — |
| Teaser snippet | ✓ | — | — | ✓ (hello-world early) | — | — |
| Highlights | ✓ | ✓ | R | ✓ | — | — |
| TOC | ○ | ○ | ○ | ○ | ○ | — |
| Prerequisites | ✓ | ○ | ✓ | R (version policy) | R (hardware/env) | ○ |
| Installation | R | R (per-OS/per-manager) | R (Docker-first) | R | R (setup + downloads) | R |
| Usage | R | R (invocation + output) | ✓ (post-install steps) | R (graduated example) | R (CLI + library) | R |
| Config / API | ○ (link-out) | ✓ (customization) | ✓ (env vars, link-out) | ✓ (link to docs site) | ○ | — |
| Live demo | — | — | ✓ (+ credentials) | ○ | ○ (Colab) | — |
| Status / roadmap | ○ | ○ | ✓ | ○ | ✓ (dated updates) | — |
| Contributing | ✓ | ✓ | ✓ | ✓ | ○ | ○ |
| License | R | R | R | R | R (per-artifact) | R |
| Citation | — | — | — | — | R (BibTeX) | — |
| Agent-file pointer | ○ | ○ | ○ | ○ | ○ | ○ |

## Thresholds and structural rules

- **TOC threshold:** hand-written TOC only above ~120 lines; below ~100,
  essentially never (observed across the 20-repo sample; GitHub's auto-TOC in
  the file header covers navigation for free — standard-readme's 100-line rule
  agrees). Long READMEs may still skip it and lean on the auto-TOC.
- **Hero style is a type signal:** centered HTML hero (logo, badges, nav pills)
  for user-facing tools and libraries; plain `# Title` for research and
  deliberately minimal repos. Both are valid; match project temperament.
- **Install vs Usage order:** Install first (majority convention), but put a
  teaser snippet above install for libraries/frameworks, and full description +
  paper links before install for research. When installation is heavy (Docker,
  model weights), show value first.
- **Self-contained vs gateway:** if the project has a docs site, keep the
  README a slim gateway (zod/fastapi pattern); if the README *is* the docs,
  it may grow into a full reference (axios pattern) — but that is a choice,
  not a default.
- **Every section must be honest or absent.** No "TBD" stubs, no aspirational
  features, no day-one-red badges.

Sources: standard-readme, best-readme-template, art-of-readme, makeareadme, readme-so, jehna-practices, banesullivan-readme, rdd-essay, observed-types-2026-07, gh-about-readmes
