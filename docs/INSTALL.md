# Install Stickman Video Director

This is the install guide for [Stickman Video Director by Transformaiton.com](../README.md). It covers a computer you control. It does not change how the skill makes videos.

You need an AI assistant that can read files and run commands. Cursor, Claude Code, and Codex are the ones the project was exercised with. A chat-only assistant can still write Model Engine prompts after the skill is installed somewhere it can be read. It cannot render a Code Engine video.

## 1. Install the tools

Install these before the skill. Versions matter for Code Engine.

| Tool | Check | Notes |
| --- | --- | --- |
| Git | `git --version` | Used to clone this repository. |
| Node.js 20 or newer | `node -v` | The renderer declares `"node": ">=20"` in `skills/directing-stickman-videos/package.json`. npm comes with Node. |
| FFmpeg and FFprobe | `ffmpeg -version` and `ffprobe -version` | Both must be on your PATH. If they live somewhere else, set `FFMPEG` and `FFPROBE` to those files. |

On macOS, Homebrew is a typical way to install Git, Node, and FFmpeg. On Windows, install the official Git for Windows, Node.js, and a current FFmpeg build, then open a new PowerShell window so PATH updates. On Linux, use your distribution's packages.

Confirm the three checks above succeed before you continue.

## 2. Install the skill

The skill name is `directing-stickman-videos`. Install it from this repository, not from a zip of unrelated files.

### Option A: let the assistant install it

Paste this to Cursor, Claude Code, or Codex:

```text
Help me install this Skill:
https://github.com/Transformaiton/stickman-video-director

After installation, read the installed SKILL.md immediately.
Explain what each mode delivers, the tools it needs,
and its production workflow in plain language.
Give me examples I can copy, then tell me what is missing
for my request and exactly what to do next.
```

The assistant should finish by reading the installed `SKILL.md`. If it only says the install succeeded and does not summarize the two modes, ask it to read that file.

### Option B: install from the terminal

From any directory:

```sh
npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

`npx` downloads the skills installer. The first run can take a few minutes because the repository includes sample media.

When the command finishes, ask your assistant to read the installed `SKILL.md` on the next turn.

## 3. Check Code Engine

Skip this section if you only want Model Engine storyboards and prompts.

Open the installed skill directory. A local clone of this repository keeps it at `skills/directing-stickman-videos/`. An assistant install copies it into that assistant's skills folder. Run the commands in the copy that will actually render.

```bash
npm ci
node scripts/autopilot.mjs doctor
```

`npm ci` installs the renderer's locked dependencies (`@napi-rs/canvas` and `sharp`). `doctor` reports missing programs and whether `GEMINI_API_KEY` is set. It does not print the key, call Google, or spend credits.

A missing Gemini variable is a problem only if you chose the bundled Gemini adapter. Another image or voice tool does not need that variable.

## 4. Optional: Gemini image and speech adapter

Use this only when you want the bundled adapter at `scripts/gemini-media.mjs`.

1. Create a key in Google AI Studio or the Google Cloud project your team uses for the Gemini API.
2. Export it in the terminal that will run the adapter:

```sh
export GEMINI_API_KEY="your-key-here"
```

PowerShell:

```powershell
$env:GEMINI_API_KEY = "your-key-here"
```

3. Do not commit the key, do not put it in a prompt, and do not paste it into chat. This repository's `.gitignore` ignores `.env` files. Prefer your operating system's secret store or a local env file that is not committed.
4. Run `node scripts/autopilot.mjs doctor` again. It should report the variable as present. Presence is not proof of quota or billing.
5. The assistant must name the model and the expected charge, then wait for your approval, before it calls the API. Each adapter command makes one request and does not retry automatically.

Speech and image commands, once you have approved a call, look like this. Replace the model IDs with models your account can use:

```bash
node scripts/gemini-media.mjs speech --text narration.txt --output narration.wav \
  --model YOUR_AVAILABLE_TTS_MODEL --voice Bodi --allow-network
node scripts/gemini-media.mjs image --prompt scene-prompt.txt --output scene.png \
  --model YOUR_AVAILABLE_IMAGE_MODEL --allow-network
```

`Bodi` is an example voice from the published samples, not a requirement. There is no default image model.

## 5. Optional: caption timing

If narration already has word timestamps, you do not need Whisper. Otherwise the skill can call:

```bash
python3 scripts/align_captions.py narration.wav --output words.json --language en --device cpu
```

That uses a Whisper model already on the machine. Add `--allow-model-download` only when you accept the download. Do not let an install script pull a multi-gigabyte model in the background.

## Troubleshooting

### The clone times out

Retry with a 20-minute limit. macOS or Linux:

```sh
SKILLS_CLONE_TIMEOUT_MS=1200000 npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

Windows PowerShell:

```powershell
$env:SKILLS_CLONE_TIMEOUT_MS = "1200000"
npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

Use the same assistant and the same install scope you used the first time.

### Clone the repository yourself

If `npx` still times out, clone first and install from the folder. Run both commands in the same parent directory:

```sh
git clone --depth 1 https://github.com/Transformaiton/stickman-video-director.git stickman-video-director
npx skills add ./stickman-video-director --skill directing-stickman-videos
```

If `git clone` fails, fix the network or Git error it prints before you retry. A shallow clone is enough for installation. It still downloads the sample media that is stored in Git.

### `node` or `ffmpeg` is not found

Install it, then open a new terminal. `doctor` uses whatever is on PATH in that terminal. A version of Node older than 20 will not match the package engines field.

### The assistant says it cannot write files or run commands

Code Engine cannot finish in that session. Switch to Cursor, Claude Code, or Codex, or use Model Engine and generate the clips in your video tool.

### Nothing was billed, and nothing should have been

Installing the skill and running `doctor` does not call a paid API. A later image, speech, or video-model call does. Stop the assistant if it proposes a paid call you have not approved.

Next: [Use the skill](USAGE.md).

Transformaiton.com is not affiliated with or endorsed by the original author. Original project: <https://github.com/kaomei/stickman-video-director>. **Modifications by Transformaiton.com.** This install guide is English documentation. It does not change the skill.
