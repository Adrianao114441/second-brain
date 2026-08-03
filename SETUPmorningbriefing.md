# Automatic morning briefing, on your own machine

This makes `/briefing` run every morning and write straight into `wiki/log.md`.
No GitHub permissions involved, because nothing has to push anywhere. Obsidian
picks the change up immediately, and OneDrive syncs it.

## Step 1. Save the script

Put `Run-MorningBriefing.ps1` somewhere permanent, for example:

    C:\Users\user\Scripts\Run-MorningBriefing.ps1

Open it and set `$VaultPath` on line 5 to the folder holding `CLAUDE.md` and
`priorities.md`. That is the only thing you need to edit.

## Step 2. Test it once by hand

Open PowerShell and run:

    powershell -ExecutionPolicy Bypass -File "C:\Users\user\Scripts\Run-MorningBriefing.ps1"

Then open `wiki/log.md` in Obsidian. A new `## Briefing` entry should be at the
top. If it is, the automation will work. If not, look in `.briefing-runs\` inside
the vault, where each run writes what happened.

Do not skip this step. It is much easier to fix a problem you can see now than
one that happens silently at 07:00.

## Step 3. Schedule it for 07:00 daily

In PowerShell:

    schtasks /create /tn "Morning Briefing" /tr "powershell -ExecutionPolicy Bypass -WindowStyle Hidden -File \"C:\Users\user\Scripts\Run-MorningBriefing.ps1\"" /sc daily /st 07:00

Change `07:00` to whatever time you want.

To check it exists:

    schtasks /query /tn "Morning Briefing"

To remove it later:

    schtasks /delete /tn "Morning Briefing" /f

## Notes

- Your computer has to be awake at that time. Task Scheduler can be told to run
  the job late if the machine was asleep: open Task Scheduler, find "Morning
  Briefing", and tick "Run task as soon as possible after a scheduled start is
  missed".
- `--permission-mode acceptEdits` in the script is what lets it write without
  asking you first. It is required for unattended running.
- If `claude` is not recognised as a command, use its full path in the script,
  or check that Claude Code is on your PATH.
- Verify the flags on your installed version with `claude --help` if the test
  run in step 2 complains about an unknown option.

## Adding the calendar back

Today's briefing had no schedule section, because no calendar is connected. If
you connect Google Calendar to Claude, the briefing will start including
"Today's Schedule" automatically. Nothing in this script needs to change.
