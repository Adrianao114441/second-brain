# Log

Append a timestamped entry to `wiki/log.md`.

If $ARGUMENTS is provided, use it as the body of the entry.

If $ARGUMENTS is empty, ask Adrian what the entry should say before writing.

Entry format:

```
## Log — YYYY-MM-DD HH:MM

$ARGUMENTS
```

Use today's date and the current local time. Do not overwrite or reformat any existing content in `wiki/log.md`.
