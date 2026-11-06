> Last verified: 2026-07-20

# AI readers

READMEs are now consumed by coding agents as much as by humans. This file says
what that changes — and, just as importantly, what it doesn't.

## The file ecosystem

| File | Audience | Definition |
|---|---|---|
| `README.md` | Humans | "Quick starts, project descriptions, and contribution guidelines" (AGENTS.md spec's own framing) |
| `AGENTS.md` | Coding agents | "A README for agents": build steps, tests, conventions that would clutter the README. Open spec, 60k+ repos, governed by the Linux Foundation's Agentic AI Foundation since Dec 2025 |
| `llms.txt` | LLMs indexing docs sites | Root-path curated content map (H1 + summary + annotated links). Adoption contested — no major model provider commits to consuming it; its defensible niche is developer-docs entry points |
| `CLAUDE.md` | Claude Code | Session-persistent project instructions. Claude Code reads CLAUDE.md, not AGENTS.md; bridge with an `@AGENTS.md` import or symlink |

## Division of responsibility

- README stays **human-first**. The AGENTS.md spec's stated purpose is to "keep
  READMEs concise and focused on human contributors."
- Agent-only operational detail (exact test invocations, env vars, permission
  boundaries, code-style rules) goes in AGENTS.md.
- **Never duplicate the README into agent files.** The strongest evidence in
  this KB: an ETH Zurich study (arXiv:2602.11988, 138 real tasks) found
  LLM-generated context files *reduced* task success ~3% while adding >20%
  inference cost — mostly because they duplicated what the repo already showed.
  Human-written files helped only marginally (~4%), and what helped was
  **non-standard practices the agent couldn't infer**, not repo overviews.
- Bridge files instead: `CLAUDE.md` containing `@AGENTS.md`; AGENTS.md linking
  to the README rather than restating it.

## Rules to apply in every mode

1. **Copy-pasteable commands, exact flags.** Agents execute README commands
   verbatim. A prose description of installation is a bug.
2. **State non-obvious constraints explicitly.** "All routes must be registered
   in `src/routes/index.ts`" is valuable; "follow existing patterns" is noise.
   What code already shows, don't restate.
3. **No agent instructions inlined in the README.** If the project has an
   AGENTS.md (or CLAUDE.md), the README ends with a one-line pointer to it.
4. **Specific and imperative beats vibes.** "Use 2-space indentation", not
   "format code properly" — studies confirm explicit instructions are followed
   well; generic advice is dead weight.
5. **A good README is agent infrastructure in itself.** Accurate install/usage/
   structure sections are pre-computed knowledge that saves agent exploration
   tokens. The best thing a README can do for agents is be correct.
6. **Don't auto-generate agent context files as a README byproduct.** Evidence
   says generated files hurt. If the user asks for an AGENTS.md, write only
   verified non-obvious facts, keep it ~100–200 lines, and nest per-package in
   monorepos (closest file wins).

## Unsettled (do not state as fact; revisit each refresh)

- Whether context files help at all: ETH (arXiv:2602.11988) found no general
  gain; Lulla et al. (arXiv:2601.20404) found ~29% lower median runtime and
  ~17% fewer output tokens with AGENTS.md present. Both are 2026; the question
  is open.
- One-great-README vs. separate agent file: a counter-position (Upsun) argues
  "if information would help a human developer, it belongs in the README" and
  AGENTS.md should hold only genuinely agent-specific operations.
- llms.txt production value; optimal agent-file length (20–500 line
  recommendations coexist); whether AAIF stewardship consolidates the
  CLAUDE.md/.cursorrules/AGENTS.md fragmentation.

Sources: agents-md, llmstxt, claude-memory-docs, eth-agentsmd-study, lulla-agentsmd-study, daplab-hcc, augment-agentsmd, morphllm-agentsmd, ericmjl-agentsmd, upsun-readme, ben3d-ai-readme
