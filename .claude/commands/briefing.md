# Briefing

Generate a daily briefing for Adrian by reading his current priorities, calendar, recent log, and active project wiki pages. Append a timestamped entry to wiki/log.md when done.

---

## Step 1 · Read Priorities

Read `priorities.md` at the vault root.

Extract:
- All items listed under **Projects** (deliverable and target date if present).
- All items listed under **Areas**.
- All items listed under **Key People**.
- Skip anything listed under **Archive**.
- Note **Resources** for background context only; do not surface them as action items.

---

## Step 2 · Check Today's Calendar

Attempt to fetch today's events via the connected calendar MCP connector (Google Calendar or equivalent).

**Include:** All events for today (current local date).
**Exclude:** All-day notification events (e.g. birthdays, public holidays) and events titled "Free" or marked as free/transparent.

If the calendar connector is not configured or returns an error, print:
`[briefing] Calendar skipped: no calendar connector available.`
and continue to Step 3.

---

## Step 3 · Scan the Log

Read `wiki/log.md`. Extract the **last 3 entries** (the 3 most recent `##` headings and their content). Note any open items, flagged questions, or follow-ups mentioned in those entries.

---

## Step 4 · Read Active Project Pages

For each project listed under **Projects** in `priorities.md`, find and read its corresponding wiki page in `wiki/projects/`. If no matching page exists, note the gap.

Also read the wiki pages for the Key People listed under **Key People** in `priorities.md`, if pages exist in `wiki/people/`.

---

## Step 5 · Generate the Briefing

Output the briefing in this format:

---

### Briefing — YYYY-MM-DD

#### Today's Schedule
List today's calendar events in chronological order: time, title, and any relevant context (e.g. who else is involved if they appear in Key People). If the calendar was skipped, write: *Calendar not available.*

#### Active Threads
One bullet per active project from priorities.md. For each:
- **Project name** — current known status (from the wiki page), most recent relevant log entry, and any open questions flagged in recent log entries.

#### Priority Reminders
Surface any target dates or deadlines from priorities.md that are within the next 14 days. If none are known, write: *No upcoming deadlines recorded. Consider adding target dates to priorities.md.*

#### Suggested Actions
3–5 concrete, specific actions Adrian could take today, derived from the active threads and log entries. Each action should reference a specific project or person. Do not suggest generic tasks.

---

## Step 6 · Append to Log

Append a single entry to `wiki/log.md`:

```
## Briefing — YYYY-MM-DD HH:MM

- Projects reviewed: <list project names>.
- Calendar: <N events found / skipped>.
- Log entries scanned: 3.
- Suggested actions: <count>.
```
