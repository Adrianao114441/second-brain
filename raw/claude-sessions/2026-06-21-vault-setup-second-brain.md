> claude-sessions: Adrian, second brain vault setup. Bootstrapped the Obsidian second-brain vault structure including raw/, wiki/, CLAUDE.md, and slash commands like /pull-sources and /ingest.

---
source: claude-code
captured: 2026-06-21
session_id: d1ede76a-b543-4a8c-9206-8a4ce818ca0c
---

## Session Summary

**Topic:** Initial setup of the AI second brain vault in Obsidian.

### What Was Built

- Created the full vault directory structure: `raw/` (with `.gitkeep`), `wiki/` with sub-folders `concepts/`, `people/`, `projects/`, and `wiki/log.md`.
- Wrote `wiki/index.md`: a one-paragraph introduction explaining that the wiki is maintained by Claude Code, raw notes live in `raw/`, and compiled pages live in `wiki/`.
- Wrote `CLAUDE.md` with four sections: Project Structure, Page Conventions, Style Guide, and Domain Context (covering Adrian's background, technical interests, active projects, key people, and what Claude helps with).
- Created `.claude/commands/pull-sources.md` defining the `/pull-sources` slash command to pull from Claude Code sessions, Gmail, Notion, and the local Desktop into `raw/`, and prompt Adrian to triage before running `/ingest`.

### Key Decisions

- `raw/` is read-only for Claude; Claude only writes to `wiki/`.
- Wiki pages use YAML frontmatter with `title`, `type`, `last-updated` fields.
- Internal links use `[[Wiki Links]]` Obsidian syntax.
- Style guide: second person for direct address, third person for factual entries, no em dashes, plain English.

### Open Questions

- The `/ingest` command was not yet created in this session; follow-up needed.
- No initial wiki content pages were written beyond the index and log skeleton.
