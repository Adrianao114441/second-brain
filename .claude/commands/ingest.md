# Ingest

Read every file in `raw/`. For each piece of source material:

1. Identify the topic, type (concept, person, project, note), and key claims or facts.
2. Determine whether a matching wiki page already exists in `wiki/concepts/`, `wiki/people/`, or `wiki/projects/`.
   - If it exists, update it by merging new information without removing existing content.
   - If it does not exist, create a new page following the conventions in CLAUDE.md (YAML frontmatter, Title Case title, [[Wiki Links]], bullets ending with full stops).
3. Add `[[Wiki Links]]` between related pages wherever relevant.
4. After processing all files, append a single ingest run entry to `wiki/log.md` in this format:

```
## Ingest — YYYY-MM-DD

- Files processed: <list file names>.
- Pages created: <list new page titles or "none">.
- Pages updated: <list updated page titles or "none">.
- Notes: <any issues, ambiguities, or items needing Adrian's attention>.
```

Do not delete or move files from `raw/`. Do not modify files in `raw/`.
