> Last verified: 2026-07-20

# Badges

Rules for choosing, ordering, and writing badges. Evidence base: shields.io
docs, GitHub Actions badge docs, and a 2026-07 sample of seven top-starred
READMEs (express, vuejs/core, axios, pandas, fastapi, ripgrep, fzf).

## Which badges earn a place

A badge earns its place only if it shows **live metadata a visitor acts on**
and links to the detail behind it. Recommended set by project type:

| Project type | Badge order |
|---|---|
| Registry library (npm/PyPI/crates) | version → CI → downloads (+ coverage after CI if strong) |
| CLI tool | CI → release tag → license or packaging spread |
| Framework | CI → coverage → version → supported platforms |
| Mature / foundation-backed | add OpenSSF Scorecard or DOI at the end |
| Research/data | DOI/citation → CI (if any) → license |

Observed norms across the sampled repos: median 5 badges; version-first for
registry libraries, CI-first for tools; downloads follows version; license,
community, and funding badges always last; coverage immediately after CI.

## Hard rules

1. **Count: 3–6.** Above ~5, restructure into a categorized markdown table
   (rows like Testing / Package / Meta — the pandas pattern) or cut.
2. **One contiguous block** directly under the title/logo, before the first
   prose paragraph. Never scatter badges through the document.
3. **One style.** Accept the shields default (`flat`) or force one `?style=`
   on every badge. No top repo mixes styles deliberately; `for-the-badge` and
   `plastic` appear in zero of the sampled top repos.
4. **Dynamic over static.** Anything that can be live data must be (CI,
   version, downloads). Static badges only for facts that don't drift (license).
5. **Every badge is a link** to the page with the detail (CI runs, registry
   page, coverage report).
6. **Alt text always**, and it names the badge's purpose ("Build status"),
   not the current value.
7. **No day-one red.** Skip any badge that would render failing/unknown/0
   at publish time; add it when it has something to show.

## Syntax quick reference

Static: `https://img.shields.io/badge/<label>-<message>-<color>`
(escaping: `_`/`%20` = space, `__` = underscore, `--` = dash; params
`?style=`, `?logo=<simple-icons slug>`, `?label=`, `?color=`).

Common dynamic badges:

```markdown
![npm version](https://img.shields.io/npm/v/PKG)
![PyPI version](https://img.shields.io/pypi/v/PKG)
![crates.io](https://img.shields.io/crates/v/PKG)
![downloads](https://img.shields.io/npm/dm/PKG)
![license](https://img.shields.io/github/license/OWNER/REPO)
![Python versions](https://img.shields.io/pypi/pyversions/PKG)
```

CI (GitHub-native — keyed to the workflow **file name**; pin the branch or the
badge silently shows the latest run on *any* branch):

```markdown
![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg?branch=main)
```

Shields CI proxy when the label needs overriding:
`https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&label=ci`

## Adoption badge

Projects that follow this standard may add the adoption badge — a static badge
(the one legitimate static case, alongside license: it states a fact that
doesn't drift) linking to the standard:

```markdown
[![README: readme-skill](https://img.shields.io/badge/README-readme--skill-brightgreen)](https://github.com/albertogrande/readme-skill)
```

It belongs in the badge block like any other. Only add it once the README
actually clears the [checklist](checklist.md) with no critical failures — an
unearned conformance badge is a vanity badge.

## Anti-patterns (named, for review mode)

- **Badge wall** — a haphazard row of everything remotely relevant; reads as
  noise and detracts from credibility.
- **Vanity badge** — unlinked or information-free (visitor counters,
  decorative "made-with" tags); fails the metadata-plus-link test.
- **Dead badge** — CI badge pointing at a renamed/removed workflow (404 or
  frozen), or unpinned branch showing the wrong run. Stale badges destroy the
  trust the badge exists to build.
- **Mixed styles** — off-geometry third-party badges breaking an otherwise
  uniform row; single-source from shields.io or quarantine the outliers.
- **Scattered badges** — badges outside the single top block.

Sources: shields-io, shields-static-badge, gh-actions-badge, observed-badges-2026-07, cicirello-badges, dailydev-badges, usethis-badge-a11y
