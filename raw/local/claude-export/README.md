Drop your claude.ai data export here.

How to get it:
1. In claude.ai (web or desktop app), go to Settings → Privacy → Export data.
2. Wait for the emailed download link, then download and unzip it.
3. Copy `conversations.json` from the unzipped folder into this folder, so the path is:
   `raw/local/claude-export/conversations.json`
4. Run `/pull-sources`. It will split every conversation into its own file under `raw/claude-web/` and tell you it's safe to delete `conversations.json` afterward.

This file is not tracked by any automatic pull — claude.ai has no export API, so this step is manual and repeatable whenever you want fresh chats captured.
