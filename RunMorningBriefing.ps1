# Run-MorningBriefing.ps1
# Runs /briefing against the second-brain vault and writes straight into wiki/log.md.
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

"=== briefing run started $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ===" |
    Out-File -FilePath $RunLog -Encoding utf8 -Append

# --permission-mode acceptEdits lets it write wiki/log.md without prompting,
# which it must do to run unattended.
claude -p "/briefing" --permission-mode acceptEdits 2>&1 |
    Out-File -FilePath $RunLog -Encoding utf8 -Append

if ($LASTEXITCODE -eq 0) {
    "=== finished OK $(Get-Date -Format 'HH:mm:ss') ===" |
        Out-File -FilePath $RunLog -Encoding utf8 -Append
} else {
    "=== FAILED, exit code $LASTEXITCODE ===" |
        Out-File -FilePath $RunLog -Encoding utf8 -Append
}
