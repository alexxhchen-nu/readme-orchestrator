# Style profiles

The knowledge base is the objective, cited layer: what sections belong, honesty,
working commands, structure. It stays deliberately silent on **taste** — how long
a tagline runs, how crisp the voice is, whether you lean on bullets.

A **style profile** is that personal layer. It shapes voice and formatting on top
of the standard. Anyone writes their own; nobody has to use one.

## Precedence — the standard always wins on correctness

1. The standard's Trust and correctness rules are absolute. A profile never
   justifies a false claim, a broken command, a missing required section, or an
   unearned badge.
2. Within that, the profile governs the subjective space: tagline, voice,
   paragraph and bullet shape, tone, emoji, casing.
3. If a profile rule would force dropping required content, keep the content and
   restructure to honor the profile's spirit — more bullets instead of one long
   paragraph, a sub-heading instead of a run-on.

## Discovery — the skill uses the first profile it finds

1. A path named in the invocation (`/readme generate --prefs path/to/profile.md`).
2. `.claude/readme-preferences.md` in the target project — commit it to share one voice across a team.
3. `~/.claude/readme-preferences.md` — your personal default across every project.
4. None found → the standard's neutral voice.

## How each mode applies it

- **Generate:** write to the standard, then shape the prose to the active
  profile. Correctness first, taste second.
- **Review:** score against the sourced checklist as always, then add a separate,
  clearly-labeled **Style profile adherence** list (met / not met). Never fold
  subjective taste into the objective score.

## Format

Markdown, one `##` heading per category, short imperative bullets. Fill in only
what you care about; delete the rest. Copy [TEMPLATE.md](TEMPLATE.md) to start,
or adapt [example-crisp.md](example-crisp.md). Recommended categories: Tagline,
About (the GitHub description, Step 4), Voice, Punctuation, Paragraphs, Bullets,
Headings, Formatting, Avoid. If no About rule is given, it defaults to the
Tagline rule.
