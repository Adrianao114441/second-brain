# Debrief

Capture the end-of-day signal from Adrian, write a structured log entry, and surface any updates needed in the wiki or priorities.md.

---

## Step 1 · Read Priorities

Read `priorities.md` at the vault root. Note the active Projects, Areas, and Key People. Skip Archive. This is the baseline for detecting what shifted today.

---

## Step 2 · Gather Input

**If $ARGUMENTS is provided:** Skip the questions. Use $ARGUMENTS as the raw input and proceed to Step 3.

**If $ARGUMENTS is empty:** Ask Adrian the following questions **one at a time**. Wait for each answer before asking the next.

1. "What did you accomplish today?" *(Work done, decisions made, things shipped or progressed.)*
2. "What conversations mattered?" *(People you talked to, messages sent, anything discussed that has implications.)*
3. "Did your priorities shift?" *(Anything that jumped up the list, dropped off, or changed shape?)*
4. "Any ideas or things to capture before tomorrow?" *(Loose thoughts, observations, things you don't want to forget.)*

---

## Step 3 · Write the Log Entry

Synthesise all input into a structured entry for `wiki/log.md`. Apply strict signal filtering:

- Write **3 to 5 bullets only**.
- Each bullet captures: what shifted, what blocked, or what to carry forward.
- Do not transcribe raw answers. If Adrian said something that is context but not a signal (e.g. describing routine work with no implications), leave it out.
- If a bullet references a project, person, or concept that has a wiki page, link it using `[[Wiki Link]]`.

Append to `wiki/log.md` in this format:

```
## Debrief — YYYY-MM-DD HH:MM
type: debrief

- <signal bullet>.
- <signal bullet>.
- <signal bullet>.
[up to 5 bullets total]

*<One-line summary of the day.>*
```

---

## Step 4 · Update Wiki Pages

Review the answers for any new information about existing wiki pages in `wiki/projects/`, `wiki/people/`, or `wiki/concepts/`.

For each page that has new information:
- Summarise the proposed update in one sentence.
- Apply the update immediately without asking (updates to existing pages are low-risk).

If something entirely new surfaces (a project, person, or concept not yet in the wiki):
- Propose a new page by name and ask: "Should I create a wiki page for `[[Page Name]]`?"
- Wait for confirmation before writing the page.

---

## Step 5 · Update Priorities

If Adrian's answers indicate that priorities shifted (a project accelerated, stalled, or dropped; a new project appeared; a deadline moved):

- State the proposed change to `priorities.md` explicitly: "I'd suggest moving X to Archive / adding Y to Projects with target date Z / updating the Key People entry for N."
- Ask: "Should I update priorities.md?"
- Wait for confirmation before writing.

---

## Step 6 · Close

End with a single line:

```
Day summary: <one sentence capturing the most important thing that happened or shifted today>.
```
