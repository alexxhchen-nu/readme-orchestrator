> Last verified: 2026-07-20

# Project types

How to classify a repo and pick a template. Classify by **who arrives at the
README and what they need first**, detected from repo structure.

## Detection heuristics

Inspect in this order; first strong match wins. When two types apply (a library
that ships a CLI), pick the one most users experience first and borrow sections
from the other.

| Type | Signals | Template |
|---|---|---|
| **Library / package** | Manifest with a registry name and exported entry points (`package.json` main/exports, `pyproject.toml`, `Cargo.toml [lib]`, `go.mod` without `main`); consumed via import | `templates/library.md` |
| **CLI tool** | Binary entry points (`bin` in package.json, `[[bin]]` in Cargo.toml, `cmd/` in Go, console_scripts); users type its name in a terminal | `templates/cli-tool.md` |
| **Web app / self-hosted** | `docker-compose.yml`/Dockerfile at root, frontend + backend dirs, migrations; users deploy and open a UI | `templates/web-app.md` |
| **API / service / framework** | Server framework deps, route definitions, OpenAPI specs, SDK config surface; users build on top of it | `templates/api-service.md` |
| **Research / data** | Paper links, `citation.cff`, notebooks, model checkpoints/dataset downloads, `requirements.txt` pinned for reproduction | `templates/research-data.md` |
| **Minimal / other** | Tiny scope, personal tool, config repo, or nothing above fits confidently | `templates/minimal.md` |

## What each type's readers need first (observed 2026-07)

- **Library:** the *feel of the API* — a teaser snippet before anything else
  (requests, zod pattern), then one-line install. Registry badges expected.
  Decide gateway-vs-reference based on whether a docs site exists.
- **CLI:** *visual proof it works* — terminal GIF or screenshot per headline
  feature (bat, httpie), then a large per-OS/per-package-manager install
  section; the best exemplars also say when *not* to use the tool (ripgrep).
- **Web app:** *a screenshot and a live demo* before any setup (immich's
  demo + login-credentials table is the gold standard), then Docker-first
  install; feature matrix if multi-platform.
- **API/service:** *a runnable hello-world early* (express's 6-line app above
  install), a prominent docs-site pointer, version-support policy, graduated
  tutorial if possible (fastapi's create → run → check → screenshot).
- **Research:** *paper identity first* — bracket-link nav, architecture
  diagram, then setup, model/dataset download tables with sizes, BibTeX
  citation, and per-artifact licensing (alphafold splits code/weights/data).
  No badges — all four sampled research repos use zero.
- **Minimal:** what it is, how to run it, license. Nothing else. A short
  honest README beats a padded template.

Sources: observed-types-2026-07, awesome-readme
