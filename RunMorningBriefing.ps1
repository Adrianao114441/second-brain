# Run-MorningBriefing.ps1
# Runs the full morning pipeline against the second-brain vault:
#   /pull-sources (fetches Claude chat sessions, Gmail, Notion, Drive, Canva, Desktop into raw/)
#   /ingest       (processes raw/ into wiki/ pages)
#   /briefing     (reads the freshly updated wiki/priorities/calendar and writes into wiki/log.md)
#
# EDIT THIS: set it to the folder that contains CLAUDE.md and priorities.md.
$VaultPath = "C:\Users\user\OneDrive\文件\second-brain"

# ----------------------------------------------------------------------
if (-not (Test-Path $VaultPath)) {
    Write-Error "Vault not found at $VaultPath. Edit `$VaultPath at the top of this script."
    exit 1
}

if (-not (Test-Path (Join-Path $VaultPath "CLAUDE.md"))) {
    Write-Error "$VaultPath exists but has no CLAUDE.md. Is that the right folder?"
    exit 1
}

Set-Location $VaultPath

# Keep a local record of each run so a silent failure is visible later.
$LogDir = Join-Path $VaultPath ".briefing-runs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Stamp = Get-Date -Format "yyyy-MM-dd"
$RunLog = Join-Path $LogDir "$Stamp.txt"

"=== morning run started $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ===" |
    Out-File -FilePath $RunLog -Encoding utf8 -Append

# --permission-mode acceptEdits lets each step write to the vault without prompting,
# which it must do to run unattended. Each step runs even if the previous one failed,
# so one bad connector doesn't block the rest of the pipeline; failures are visible
# in this run log afterward.
$Steps = @("/pull-sources", "/ingest", "/briefing")
$AnyFailed = $false

foreach ($Step in $Steps) {
    "--- $Step started $(Get-Date -Format 'HH:mm:ss') ---" |
        Out-File -FilePath $RunLog -Encoding utf8 -Append

    claude -p $Step --permission-mode acceptEdits 2>&1 |
        Out-File -FilePath $RunLog -Encoding utf8 -Append

    if ($LASTEXITCODE -eq 0) {
        "--- $Step finished OK $(Get-Date -Format 'HH:mm:ss') ---" |
            Out-File -FilePath $RunLog -Encoding utf8 -Append
    } else {
        $AnyFailed = $true
        "--- $Step FAILED, exit code $LASTEXITCODE ---" |
            Out-File -FilePath $RunLog -Encoding utf8 -Append
    }
}

if ($AnyFailed) {
    "=== morning run finished with at least one failed step $(Get-Date -Format 'HH:mm:ss') ===" |
        Out-File -FilePath $RunLog -Encoding utf8 -Append
} else {
    "=== morning run finished OK $(Get-Date -Format 'HH:mm:ss') ===" |
        Out-File -FilePath $RunLog -Encoding utf8 -Append
}
