---
name: readme-rubric-audit
description: |
  Audit, score, or generate a repository README.md against a cited 100-point
  6-dimension rubric (Identity 15, Trust★ 25, Onboarding 25, Structure 15,
  Craft 10, Agent-Readiness 10) and 6 project-type templates. Invoke when
  auditing/reviewing an existing README, scoring README quality, checking
  badge/command honesty, syncing GitHub About descriptions, or generating a
  clean standard README for a library, CLI tool, web app, API service, or
  research dataset. Do not use for multi-page docs sites (MkDocs/Docusaurus).
  Triggers: audit readme/review readme/score readme/readme rubric/README体检/README打分/README审计/readme-rubric-audit.
argument-hint: "[review|generate] [path/to/README.md]"
---

# README Rubric Audit & Standard Generator (100-Point 6-Dimension Engine)

Generate or audit `README.md` files against a cited knowledge base located in
this skill directory (`<THIS_SKILL_DIR>/references/` and `<THIS_SKILL_DIR>/templates/`).
Resolve `<THIS_SKILL_DIR>` relative to this `SKILL.md` file across any Agent
Skills runtime (never hardcode single-runtime environment variables).

---

## Standard Execution Workflow (Step 0 → Step 4)

### Step 0 — Mode Gate & Write-Protection Lock
- **Input**: Target repository path and user request.
- **Action**:
  - **`review` (Audit-Only)**: Existing non-trivial `README.md` and the user asks to audit, score, critique, or check it.
  - **`generate` (Build/Fix)**: No `README.md` exists, or the user explicitly requests writing/rewriting/fixing `README.md`.
  - 🔴 **CHECKPOINT 1 (Audit Write-Lock)**: In `review` mode, **🛑 STOP — never modify `README.md` or run `gh repo edit`**. Output the scored diagnostic report and replacement snippets only.
- **Output**: Explicit mode declaration `[Mode: review | generate]`.

### Step 1 — Classify Project Gene & Style Profile
- **Input**: Repository manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`), directory layout, and entry points.
- **Action**:
  1. Read `references/project-types.md` (relative to this `SKILL.md`) and select **one** primary project type:

| Project Type | Skeleton Template (`templates/...`) | Required Proof Type |
|---|---|---|
| Library / SDK / Package | `templates/library.md` | Minimal runnable import + expected return/output |
| CLI Tool | `templates/cli-tool.md` | Terminal invocation block + sample stdout/GIF |
| Web App / Self-Hosted App | `templates/web-app.md` | UI screenshot / preview GIF + env table |
| API / Service / Framework | `templates/api-service.md` | Request/response `curl` example + endpoint table |
| Research / Data / ML | `templates/research-data.md` | Architecture/pipeline diagram + results table + BibTeX |
| Tiny Project / Minimal | `templates/minimal.md` | One-liner + install + 1 usage block |

  2. **Optional Style Profile**: Read `preferences/about.md`, then check in order: path named in prompt → target repo `.readme-preferences.md` → `~/.config/readme-preferences.md` → none (default neutral engineering voice). Style profiles shape tone only; objective rubric rules below always take precedence.
- **Output**: Selected `[Type]` + `[Template]` + `[Profile]`.

### Step 2a — Generate Mode (`generate`)
- **Input**: Selected template and verified repository facts.
- **Action**:
  1. Read in order: `references/anatomy.md` → `templates/<type>.md` → `references/section-guide.md` → `references/badges.md`.
  2. **Hard Integrity Rules**:
     - **Never invent facts**: Verify every command, flag, version, and badge against manifests, `--help` output, and `.github/workflows/`.
     - **No empty stubs**: Omit any section the project cannot fill honestly (never write `Roadmap: TBD`).
     - **Honest badges only**: 3–6 badges in a single block, unified style, zero red/unknown/unindexed badges.
     - **One-liner first**: State what the project does and **for whom** in `≤120` characters directly under `# H1`.
- **Output**: Drafted `README.md` matching the canonical funnel.

### Step 2b — Review Mode (`review` — 100-Point 6-Dimension Rubric)
- **Input**: Existing `README.md` and repository files.
- **Action**:
  1. Read `references/checklist.md` and `references/anti-patterns.md`.
  2. Score each applicable item pass/fail against the actual repository (`Score = points_earned / points_applicable × 100`; exclude `○` items not applicable to the project type per `references/anatomy.md`).
  3. 🔴 **CHECKPOINT 2 (Trust★ 49-Point Hard Cap)**: If **any** `★` item fails (`T1★` broken/unverified install or usage command; `T2★` fabricated feature or fake badge such as claiming `99% coverage` with no test suite), **the total score is hard-capped at `49/100` (`<50` Failing band)** regardless of visual polish!

| Category (Weight) | Item IDs & Weights | Core Verification Check |
|---|---|---|
| **1. Identity (15)** | `I1`(5) · `I2`(7) · `I3`(3) | `I1`: H1 matches repo/pkg name · `I2`: `≤120`-char one-liner states what + **for whom** · `I3`: Matches GitHub **About** description |
| **2. Trust ★ (25)** | **`T1★`(10) · `T2★`(5)** · `T3`(5) · `T4`(3) · `T5`(2) | **`T1★`: Install/usage commands verified runnable** · **`T2★`: Zero aspirational/fake features or badges** · `T3`: Links/images resolve · `T4`: Current visuals · `T5`: Honest status |
| **3. Onboarding (25)** | `O1`(8) · `O2`(8) · `O3`(4) · `O4`(3) · `O5`(2) | `O1`: Copy-runnable install one-liner · `O2`: Minimal example **with expected output** · `O3`: Exact OS/version prereqs · `O4`: Type-matched visual proof · `O5`: Dev setup separated |
| **4. Structure (15)** | `S1`(6) · `S2`(4) · `S3`(3) · `S4`(2) | `S1`: Broad→narrow funnel (no install-before-why) · `S2`: Deep docs linked out · `S3`: TOC only if `≥120` lines & synced · `S4`: License linked to `LICENSE` |
| **5. Craft (10)** | `C1`(4) · `C2`(3) · `C3`(3) | `C1`: 3–6 badges, 1 block, 1 style, alt text, none broken · `C2`: Portable markup · `C3`: Skimmable, objective facts over hype adjectives |
| **6. Agent-Readiness (10)** | `A1`(4) · `A2`(3) · `A3`(3) | `A1`: Non-interactive copy-pasteable commands with exact flags · `A2`: Non-obvious constraints explicit · `A3`: Link to `AGENTS.md`, no inline prompt dumps |

- **Output**:
  1. Overall score (`0–100`) + band (`90–100` exemplary · `75–89` solid · `50–74` needs work · `<50` failing) + 6-category subtotal table (explicitly noting if `Trust★` cap 49 was triggered).
  2. Top 3–5 highest-impact fixes ranked by reader impact (`★` failures always first), citing exact item IDs (`T2★`, `O2`, etc.) or `references/anti-patterns.md` names.
  3. Concrete copy-pasteable replacement Markdown for the single worst offender.

### Step 3 — Agent-Era Readiness Check
- Read `references/ai-readers.md` and ensure every command uses non-interactive flags, non-obvious runtime constraints are stated, and agent instructions are linked (`AGENTS.md`) rather than inlined.

### Step 4 — Sync GitHub "About" Description
- The README one-liner (`I2`) and GitHub **About** description (`I3`) must be identical.
- **In `review` mode**: Run `gh repo view <owner/repo> --json description` (if remote exists) to check `I3`, or provide the exact `gh repo edit <owner/repo> --description "<one-liner>"` command in the report.
- **In `generate` mode**: 🔴 **CHECKPOINT 3 (Remote Mutation Gate)** — **🛑 STOP and ask user confirmation before running `gh repo edit <owner/repo> --description "<one-liner>"` against a live remote repository.**

---

## 🛟 Failure Modes & 3-Stage Recovery Table

| # | Trigger Condition (If X Fails) | First-Line Fix (Action Y) | Final Fallback (Fallback Z) |
|---|---|---|---|
| **FM-1** | `references/*.md` or `templates/*.md` path not found | Resolve relative to this `SKILL.md` directory (`../readme-rubric-audit/references/...`) | Use the inline 100-point 6-dimension rubric table and hard rules in Step 2a/2b directly |
| **FM-2** | `gh` CLI unavailable, unauthenticated, or local repo has no remote | Skip live `gh repo view` query; inspect `.git/config` for remote URL | Mark `I3` as `[UNVERIFIED-LOCAL]` and output the exact `gh repo edit` command for the user |
| **FM-3** | Local image or link in `README.md` fails to resolve | Check relative path against repo tree (`assets/`, `docs/`); run `beautify-github-readme/scripts/audit_readme.py` if present | Deduct `T3` (5 pts) in `review` mode; replace broken image with verified path or table in `generate` mode |
| **FM-4** | Project has no test suite, CI workflow, or published package | Exclude inapplicable items (`○`) from denominator or omit CI/registry badges | Include only verified local badges (License, language version) and local git-clone install steps |
| **FM-5** | Existing `README.md` has custom user sections during rewrite | Back up original file to `README.old.md` before writing | Migrate all verified commands, links, and tables into the new canonical funnel structure |
| **FM-6** | Style profile conflicts with a required rubric item (e.g. drops License or output example) | Enforce Step 2a precedence: objective rubric correctness always overrides style profile taste | Keep the required section and apply the style profile's voice/formatting to it |

---

## 🚫 Counterexamples & Blacklist (What Never To Do)

| ID | Forbidden Action | Why It Fails | Mandatory Alternative |
|---|---|---|---|
| **BL-1** | **Never award `≥50` points to a README with broken install commands (`T1★`) or fake badges/features (`T2★`)** | Violates the `Trust★` critical gate; a lying README cannot pass regardless of aesthetics | Apply the **49-point hard cap** immediately and rank the `★` failure as Fix #1 |
| **BL-2** | **Never edit `README.md` when invoked in `review` / Audit-Only mode** | Destroys uncommitted user state when only an evaluation was requested | Output the scored report and concrete replacement code blocks in chat |
| **BL-3** | **Never use single-runtime skill-directory env vars or hardcoded user paths in instructions** | Breaks portability across Codex, Cursor, Magpie, OpenCode, and other Agent Skills runtimes | Resolve skill files relative to `SKILL.md` and keep README commands runtime-neutral |
| **BL-4** | **Never write placeholder sections (`## Roadmap\nTBD`, `TODO: add example`)** | Penalized under `T2★` / `S1` as vaporware padding | Omit sections that lack real repository backing |
| **BL-5** | **Never write usage code blocks without showing expected output (`O2`)** | Readers cannot verify whether their command succeeded or what the return shape looks like | Follow the usage snippet immediately with a short output block or comment |
| **BL-6** | **Never inline long system prompts or agent rules inside `README.md` (`A3`)** | Clutters human onboarding and duplicates `AGENTS.md` | Keep `README.md` focused on human + CLI onboarding and link to `AGENTS.md` |
