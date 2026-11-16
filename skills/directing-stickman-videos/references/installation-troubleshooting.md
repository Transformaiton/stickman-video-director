# Installation troubleshooting

If installation reports a repository clone timeout, retry with a 20-minute clone window. Run the commands in a terminal with Node.js/npm and Git available, then select the same agent and installation scope as before.

Install this public copy from Transformaiton.com. The original project remains [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director). Transformaiton.com is not affiliated with or endorsed by the original author.

## macOS / Linux

```sh
SKILLS_CLONE_TIMEOUT_MS=1200000 npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

## Windows PowerShell

```powershell
$env:SKILLS_CLONE_TIMEOUT_MS = "1200000"
npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

## Local clone fallback

If the installer still times out, clone to a new local directory first, then install from that path. Run both commands from the same parent directory; this also works in PowerShell.

```sh
git clone --depth 1 https://github.com/Transformaiton/stickman-video-director.git stickman-video-director
npx skills add ./stickman-video-director --skill directing-stickman-videos
```

If `git clone` itself fails, resolve the reported network or Git error before retrying. After installation succeeds, read the installed `SKILL.md` and continue with the [first-use guide](getting-started.md).
