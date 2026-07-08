# CLAUDE.md — Second Brain Instructions

Instructions for any AI agent working in this vault. Follow the Operating Rules below exactly; they define how information moves through the vault and who owns which file. Do not improvise a different workflow.

## Project Structure

This vault is Adrian's AI second brain, hosted in Obsidian and synced via OneDrive.

```
vault/
├── raw/             # Source material Claude reads but does not edit
│   ├── canva/           # Pulled Canva designs
│   ├── claude-sessions/ # Recent Claude Code session transcripts
│   ├── gmail/           # Pulled email
│   ├── google-drive/    # Pulled Drive files
│   ├── notion/          # Pulled Notion pages
│   ├── local/           # Manually dropped-in files
│   ├── Projects/        # Project source documents
│   └── Whalerapy/       # Whalerapy project archive (large, ~900 files)
├── wiki/            # Claude-maintained cross-linked knowledge base
│   ├── concepts/
│   ├── people/
│   ├── projects/
│   │   └── improvements/  # One "<Project> Improvements" page per project: agent suggestions, not commitments
│   ├── index.md
│   └── log.md
├── priorities.md    # User-maintained priorities (source of truth for what is active)
├── CLAUDE.md        # This file: the single source of truth for agent instructions
├── AGENTS.md        # Pointer to CLAUDE.md for non-Claude tools
├── GEMINI.md        # Pointer to CLAUDE.md for Gemini CLI
├── README.md        # Human-facing overview of the vault
└── .github/copilot-instructions.md  # Pointer to CLAUDE.md for GitHub Copilot
```

AGENTS.md, GEMINI.md, and the Copilot instructions are pointers only. Never add rules to them; all instructions belong in CLAUDE.md so the tools cannot drift apart.

- `raw/` — Source material organised by origin. Most subfolders are populated by /pull-sources; `local/` is for manual drops. Claude reads this but does not edit it.
- `wiki/` — Claude-maintained knowledge base of cross-linked pages organised by topic. Sub-folders: `concepts/`, `people/`, `projects/`. The running log lives at `wiki/log.md`.
- `priorities.md` — the user's priorities file at the vault root, containing Projects (short-term deliverables with target dates), Areas (ongoing responsibilities), Resources, Archive, and Key People. **This file, not CLAUDE.md, is the source of truth for what Adrian is currently working on.** Read it at the start of every /briefing and /debrief. Prioritise signals tied to Projects and Areas; use Resources for background context; skip anything in Archive.

## Commands

Custom commands live in `.claude/commands/`. Read the command file for full steps before running one.

| Command | Purpose |
| --- | --- |
| `/briefing` | Daily briefing from priorities, calendar, recent log, and active project pages. Appends to `wiki/log.md`. |
| `/debrief` | End-of-day capture. Writes a structured log entry and surfaces needed wiki or priorities updates. |
| `/pull-sources` | Fetch fresh material from configured sources (Claude sessions, Gmail, Drive, Notion, Canva) into `raw/`. |
| `/ingest` | Process files in `raw/` into new or updated wiki pages, then log the run. |
| `/query` | Answer a question by searching `wiki/` first, then `raw/`, with citations for every claim. |
| `/lint` | Wiki health report: broken links, missing frontmatter, empty pages, orphaned pages. |
| `/log` | Append a timestamped entry to `wiki/log.md`. |

## Operating Rules

These rules define the vault's logic. Every agent, whatever the model, must follow them. The reasoning discipline behind these rules lives in `wiki/concepts/Agent Logic.md`: read it before working in the vault. If that page and this file ever disagree, this file wins.

### Ownership: who edits what

| File / folder | Owner | Agent may |
| --- | --- | --- |
| `raw/` | Sources | Read only. Never edit, rename, or delete anything here. |
| `wiki/` (except `log.md`) | Agent | Create and update pages following Page Conventions. |
| `wiki/log.md` | Agent | Append only. Never rewrite or delete past entries. |
| `priorities.md` | Adrian | Read always; suggest edits; change it only when Adrian explicitly asks. |
| `CLAUDE.md`, `.claude/commands/` | Adrian | Read; propose changes; edit only when asked. |

### Information flow

Information moves one way: `raw/` → (via /ingest) → `wiki/` → (via /briefing, /debrief) → `wiki/log.md`. Raw material is evidence; wiki pages are the distilled, current understanding; the log is the historical record. Never copy wiki content back into `raw/`, and never treat a log entry as more current than the wiki page it summarised.

### Reading order

When answering anything about Adrian's work: read `priorities.md` first, then the relevant `wiki/` pages, and go to `raw/` only when the wiki lacks the answer. Do not start by grepping `raw/` — it is large (Whalerapy alone is ~900 files) and contains superseded drafts.

### Fact discipline

- No source, no claim. Every factual statement must trace to a wiki page or a raw file; cite it as `[Page Name]` or the raw file name. If the knowledge base does not contain the answer, say so instead of guessing.
- When two sources conflict, the one with the later date wins. Note the conflict on the wiki page ("Earlier draft X said …") rather than silently discarding either version.
- Use absolute dates (YYYY-MM-DD), never "yesterday" or "last week" — pages outlive the session that wrote them.

### Editing wiki pages

- Before creating a page, search `wiki/` for an existing page on the same topic (including alternative names and Chinese names). Update rather than duplicate.
- When updating, merge: add and correct, but do not remove existing content unless it is demonstrably wrong or superseded — and say so in the edit.
- Set `last-updated` to today's date on every edit.
- Do not rename or move pages casually: `[[Wiki Links]]` resolve by file name. If a rename is genuinely needed, update every inbound link in the same session (run the /lint checks afterwards).
- Choose `type` by what the page is *about*: a person → `person`; a deliverable with a timeline or outcome → `project`; a technique, theory, or tool → `concept`; a navigation page → `index`.

### Scope

Do exactly what the command or request asks, then stop. Do not reorganise folders, mass-reformat pages, or "clean up" beyond the request; propose such changes instead. Never delete files without explicit confirmation.

## Page Conventions

Every wiki page must include YAML frontmatter at the top:

```yaml
---
title: Page Title In Title Case
type: concept | person | project | index | improvements
last-updated: YYYY-MM-DD
---
```

- Titles use Title Case.
- Internal links use `[[Wiki Links]]` with the page name matching the file name.
- Every bullet point ends with a full stop.
- Tag related pages using `[[link]]` inline in the body text.
- Pages may be named in Chinese where the source material is Chinese (e.g. `浊度传感器.md`); apply the same frontmatter and link conventions.

## Style Guide

- Write in second person ("you are working on…") where addressing Adrian directly; otherwise use third person for factual entries.
- Use plain English. Prefer short, common words over jargon unless the term is a defined concept.
- One idea per sentence.
- No em dashes. Use a comma, a colon, or a new sentence instead.
- Use **bold** for emphasis. Use it sparingly so it retains weight.

## Domain Context

Adrian Ao Pak Lon is a university student based in Macau, previously at Pui Ching Middle School (Coloane Campus).

### Field

Computer science and AI, with a focus on machine learning research and educational technology. Also active in UX/UI design and product management.

### Technical Interests

- **Machine Learning and Deep Learning:** CNNs, VAEs, RNNs, Transformers.
- **Reinforcement Learning:** Q-learning, Soft Actor-Critic (SAC).
- **Vision-Language-Action (VLA) models:** LeRobot framework, SO-101 robotic arm, Makermods hardware.
- **Competitive ML:** Kaggle Pokemon TCG AI Battle Challenge (strategy track).

### Projects

Current status lives in `priorities.md`; project details and history live in `wiki/projects/`. Long-running context worth knowing:

- **AI Tutoring Bias Study** (co-authored with Benjamin Tam at Pui Ching): Investigates whether eight major LLM platforms (ChatGPT, Gemini, Claude, Grok, DeepSeek, Qwen, Doubao, Yiyan) produce significantly different tutoring quality across Cantonese-dominant, Mandarin-dominant, and English-dominant Secondary 2 students in Macau. Within-subject repeated-measures ANOVA design with a 100-point blinded rubric. Analysis in Python (scipy, pingouin, pandas).
- **Robotics competitions:** Robo Fest and WRO (World Robot Olympiad) entries with the robotics team, including the Wall Climber vacuum-pump robot. See `wiki/projects/`.
- **Whalerapy:** Aromatherapy machine with emotion detection. Stanford proposal and WRO 2026 Macau materials submitted June 2026. Extensive source archive in `raw/Whalerapy/`.

### Organisation

**Pui Ching Middle School (Coloane Campus), Macau** — the institution where the AI tutoring bias study is conducted and where several project proposals originate.

### Key People

Current focus per person is tracked in `priorities.md`; stable relationships:

| Name             | Role / Relationship                                  |
| ---------------- | ---------------------------------------------------- |
| **Benjamin Tam** | Co-author on the AI tutoring bias research proposal. |
| **Bianca**       | Robotics teammate.                                   |
| **Ashley**       | Robotics teammate.                                   |
| **Oscar**        | Robotics teammate.                                   |
| **Cabrina**      | Robotics teammate.                                   |
| **Peony**        | Robotics teammate.                                   |

### What Claude Helps With

- Researching academic literature and summarising findings.
- Drafting proposals, reports, leaflets, and presentations.
- Processing raw notes into structured wiki pages.
- Answering questions by searching across the wiki and raw material.
