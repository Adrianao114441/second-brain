# Second Brain

Adrian's personal knowledge base, hosted as an Obsidian vault and maintained with AI agents (Claude Code and compatible tools).

## What this is

A pipeline that turns raw source material into a cross-linked wiki and a running log:

```
raw/  →  /ingest  →  wiki/  →  /briefing, /debrief  →  wiki/log.md
```

- **`raw/`** — source material pulled from Canva, Gmail, Google Drive, Notion, and Claude Code sessions, plus manual drops in `raw/local/`. Read-only for agents.
- **`wiki/`** — the distilled, current understanding: `concepts/`, `people/`, `projects/`, with `index.md` for navigation and `log.md` as the historical record.
- **`priorities.md`** — the hand-maintained list of active Projects, Areas, Resources, Archive, and Key People. This is the source of truth for what is currently active. Review it weekly.

## Daily use

| When | Command | What it does |
| --- | --- | --- |
| Morning | `/briefing` | Briefing from priorities, calendar, recent log, and active projects. |
| Evening | `/debrief` | Capture the day; update the log; surface wiki/priority updates. |
| Anytime | `/query <question>` | Answer from the wiki (then raw), with citations. |
| Anytime | `/log <note>` | Append a timestamped note to the log. |

## Maintenance

| Cadence | Command | What it does |
| --- | --- | --- |
| When new material arrives | `/pull-sources` | Fetch fresh material from configured sources into `raw/`. |
| After pulling | `/ingest` | Process `raw/` into new or updated wiki pages. |
| Weekly | `/lint` | Wiki health report: broken links, missing frontmatter, orphans. |
| Weekly | — | Review `priorities.md` by hand; move finished items to Archive. |

## For AI agents

All agent instructions live in [CLAUDE.md](CLAUDE.md) — structure, operating rules, page conventions, and style guide. Other tools are routed there via [AGENTS.md](AGENTS.md) and [GEMINI.md](GEMINI.md). Command definitions live in `.claude/commands/`.
