# Lint

Scan every `.md` file in `wiki/` and produce a health report covering the following checks:

1. **Broken links** — Find every `[[Wiki Link]]` and verify that a corresponding `.md` file exists in `wiki/`. List any links that resolve to no file.
2. **Missing frontmatter** — Flag any page that is missing the `title`, `type`, or `last-updated` field in its YAML frontmatter.
3. **Empty pages** — Flag any page whose body (below the frontmatter) contains fewer than two lines of real content.
4. **Orphaned pages** — List any page in `wiki/` that is not linked to from any other wiki page.

Output format:

```
## Wiki Health Report — YYYY-MM-DD

### Broken Links
- <file>: [[LinkName]] — no matching file found.

### Missing Frontmatter
- <file>: missing fields: <list>.

### Empty Pages
- <file>: body is empty or near-empty.

### Orphaned Pages
- <file>: not linked from any other page.

### Summary
- Total pages scanned: N
- Issues found: N
```

If no issues are found in a category, write "None."
