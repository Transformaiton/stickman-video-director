<div align="center">

# Stickman Video Director by Transformaiton.com

**Turn a script, article, or rough idea into a stickman video with pictures, voiceover, captions, and sound effects.**

An open-source production skill for small-business owners who need faceless explainers, social videos, or training videos, without a camera crew.

[Install](docs/INSTALL.md) · [Quick start](#quick-start) · [Requirements and costs](#requirements) · [FAQ](#faq) · [Contact](#contact)

</div>

The previews below are published samples from the original project. They are real renders already in this repository, not mockups.

<table width="100%">
<tr>
<td width="50%" align="center">
<strong>Faceless explainer</strong><br>
<a href="assets/readme/b1-minimal-handdrawn.mp4"><img src="assets/readme/previews/b1-minimal-handdrawn.gif" alt="Minimal line-art stickman explainer about making YouTube videos without showing your face" width="90%"></a>
</td>
<td width="50%" align="center">
<strong>Presenter-style explainer</strong><br>
<a href="assets/readme/b5-character-explainer.mp4"><img src="assets/readme/previews/b5-character-explainer.gif" alt="Character explainer about asking for help, with a presenter and expressive stick figures" width="90%"></a>
</td>
</tr>
<tr>
<td width="50%" align="center">
<strong>Classic stick figures</strong><br>
<a href="assets/readme/dark-theme-demo.mp4"><img src="assets/readme/previews/dark-theme-demo.gif" alt="White stick figures on a black background" width="90%"></a>
</td>
<td width="50%" align="center">
<strong>Everyday story</strong><br>
<a href="assets/readme/style-4-cozy-cafe.mp4"><img src="assets/readme/previews/style-4-cozy-cafe.gif" alt="Cozy storytelling scene at an outdoor cafe" width="90%"></a>
</td>
</tr>
</table>

## What it does

Stickman Video Director is a skill you install in an AI assistant that can read files and run commands, such as Cursor, Claude Code, or Codex. You give it a topic, a blog post, a training outline, or a finished script. It plans the story, then produces a stickman video in one of two ways:

| | Model Engine (A) | Code Engine (B) |
| --- | --- | --- |
| How the pictures are made | A video-generation service creates each shot from a storyboard and prompts. | The assistant draws still assets, then code animates them and renders the video on your computer. |
| What you receive | A storyboard and standalone prompts. An assistant with a browser and editing tools can also assemble a finished file. | A finished video with narration, captions, and sound effects, plus a local preview. |
| Best fit | Short, character-led social clips. | Explainers and training videos you want rendered locally. |
| What you pay for | The video platform's credits, plus your AI assistant. Writing the storyboard does not need a video API key. | Your AI assistant, plus any image or voice service you connect. Local rendering does not spend video-model credits. |

Both modes support landscape `16:9` and portrait `9:16`. You approve the plan, and a short sample when you use Code Engine, before the full video is made.

The step-by-step guide is in [docs/INSTALL.md](docs/INSTALL.md) and [docs/USAGE.md](docs/USAGE.md).

## Use cases

- **Faceless YouTube or social explainers.** Teach a concept, introduce a service, or narrate a post without putting anyone on camera. Minimal Line Art (B1) and Character Explainer (B5) are the closest matches to the samples above.
- **Training videos.** Turn an internal how-to, onboarding outline, or product walkthrough into a narrated lesson with on-screen captions.
- **Short social clips.** Use portrait `9:16` for a 30-second hook, or landscape `16:9` for a longer explainer.
- **A script you already have.** Paste the copy. The assistant keeps your meaning and builds the shots around it.
- **A rough idea.** A topic sentence, a link, or a few bullet points is enough to start. You approve the script before rendering.

This tool does not publish the video for you, and it does not promise views, ad revenue, or a particular platform's monetization review.

## Requirements and costs

<a id="requirements"></a>

The software in this repository is free to use under the MIT license. There is no Transformaiton.com subscription. You still pay the companies whose services you choose to call.

### On your computer

| Requirement | Why |
| --- | --- |
| Git | Clone this repository if the one-line installer times out. |
| Node.js 20 or newer, and npm | Code Engine checks its setup and renders locally. |
| FFmpeg and FFprobe on your PATH | Code Engine measures audio and encodes the video. Optional variables `FFMPEG` and `FFPROBE` can point at the binaries. |
| An AI assistant with file access and a terminal | Cursor, Claude Code, or Codex can install the skill and run the renderer. A chat-only assistant can still write Model Engine prompts; it cannot render Code Engine videos. |

From the installed skill directory, Code Engine setup is:

```bash
npm ci
node scripts/autopilot.mjs doctor
```

`doctor` checks that Node, FFmpeg, fonts, and optional API variables are present. It does not log into a provider, spend credits, or print secret values.

### API keys

You do not put API keys in this repository, and you should not paste them into the chat. When a provider needs a key, set it as an environment variable.

| Service | Required? | What it is for |
| --- | --- | --- |
| None, for a Model Engine storyboard | No key | Prompts and a shot plan. You generate the clips later in a video tool such as [Google Flow](https://flow.google.com/). |
| Your video platform account | Only if you generate Model Engine clips | The published Model Engine samples were made in Google Flow. Any compatible video tool can be used. Cost is that platform's credits or quota. |
| `GEMINI_API_KEY` | Only if you use the bundled Gemini adapter | Optional Code Engine path for speech and still images. The adapter calls Google's API once per command, with no automatic retry. You choose the model ID. `doctor` only checks that the variable is set, not your quota or price. |
| Another image or voice tool your assistant already has | Optional | Code Engine accepts local image and audio files. Browser or built-in tools can supply them. The showcase voices (including Bodi and Brian) describe the samples. They are not a bill from this project. Style B4's default narrator is the Brian voice; you can select a different voice. |
| ElevenLabs or a similar speech API | Optional | Only if you choose that provider. This repository does not include an ElevenLabs key. |
| OpenAI Whisper, local | Optional | `scripts/align_captions.py` can time captions from narration. It uses a model that is already downloaded unless you pass `--allow-model-download`. Skip it when you already have word timings. |

### What a typical job can cost

- **This repository:** no license fee.
- **Your AI assistant:** whatever plan you already use for Cursor, Claude, or Codex. Long videos use more of that plan because the assistant writes and checks the scenes.
- **Model Engine clips:** the video service's rate. Check that service before you approve a batch. The assistant should tell you the tool and the expected spend, then wait for approval.
- **Code Engine pictures and voice:** the rate of the image and speech service you connect. Local encoding on your machine does not add a video-model charge.
- **A short sample first:** Code Engine asks you to approve about 20 seconds with sound before it makes the full video. That sample is the right moment to judge quality and the remaining cost.

Prices change and depend on length, resolution, and provider. This page does not quote a per-minute rate, because this project does not bill one.

## Install

<a id="install"></a>

Full steps, Windows notes, and timeout recovery are in [docs/INSTALL.md](docs/INSTALL.md).

1. Install Git, Node.js 20 or newer, and FFmpeg.
2. In Cursor, Claude Code, or Codex, send:

```text
Help me install this Skill:
https://github.com/Transformaiton/stickman-video-director

After installation, read the installed SKILL.md immediately.
Explain what each mode delivers, the tools it needs,
and its production workflow in plain language.
Give me examples I can copy, then tell me what is missing
for my request and exactly what to do next.
```

3. If you prefer the terminal:

```sh
npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos
```

4. Ask the assistant to read the installed `SKILL.md` and run `node scripts/autopilot.mjs doctor` from that skill directory before you start a Code Engine video.

## Quick start

<a id="quick-start"></a>

More copy-paste briefs, style codes, and approval steps are in [docs/USAGE.md](docs/USAGE.md).

**Training or explainer video (Code Engine).** After the skill is installed:

```text
Use Code Engine / mode B to turn the following outline into a training video:
[Paste your outline, article, or script]

Requirements: about 3 minutes, landscape 16:9,
B1 "Minimal Line Art", English narration, captions, and sound effects.

Check image generation, voice, and video compositing setup.
Give me the script and a 20-second sample with sound first.
After I approve them, make the full video and deliver the file.
```

**Short social clip (Model Engine prompts only).** No video API key is required for this step:

```text
Use Model Engine / mode A to turn the following topic into a stickman video:
[Your topic]

Requirements: portrait 9:16, A1 classic black and white, 30 seconds.
Give me a director's proposal first. After I approve it,
deliver standalone prompts for each clip.
```

You then paste those prompts into your video tool, or ask an assistant that can use the browser to generate and edit the clips. Approve the plan, and any stated cost, before generation starts.

## Styles

<a id="styles"></a>
<a id="a-styles"></a>
<a id="b-styles"></a>

Thirteen styles are included. Pick by code, for example `B1` or `A3`. You do not install a separate style pack.

| Code | Name | Useful for | Sample in this repo |
| --- | --- | --- | --- |
| A1 | Classic black and white | Clear analogies and business breakdowns | [Dark theme](assets/readme/dark-theme-demo.mp4), [light theme](assets/readme/light-theme-demo.mp4) |
| A2 | Modern pop | Product and tool stories with a recurring character | [Minimal tech](assets/readme/style-2a-demo.mp4), [colorful story](assets/readme/style-2b-demo.mp4) |
| A3 | Prehistoric cave | Short fables and workplace jokes | [First job](assets/readme/style-3-demo.mp4) |
| A4 | Cozy storytelling | Everyday situations and soft training stories | [Cafe](assets/readme/style-4-cozy-cafe.mp4) |
| A5 | Historical cartoon | History and period explainers | [Edo Japan](assets/readme/style-5-japan.mp4) |
| A6 | Amber noir | What-if stories with warm light and deep shadow | [Flow sample](assets/readme/style-6-amber-noir-flow.mp4) |
| A7 | Rubber hose | Vintage comedy with elastic acting | [Chased by a cloud](assets/readme/style-7-rubber-hose.mp4) |
| B1 | Minimal line art | Faceless YouTube explainers and training | [Faceless YouTube](assets/readme/b1-minimal-handdrawn.mp4) |
| B2 | Colorful hand-drawn | Habits, attention, and everyday psychology | [Sleep](assets/readme/b2-colorful-sleep.mp4) |
| B3 | Retro TV | Curious facts with a late-night TV look | [Night signal](assets/readme/b3-tv-night-signal.mp4) |
| B4 | Survival thriller | Suspense stories. Default narrator name is Brian | [Dispatch](assets/readme/b4-dispatch.mp4) |
| B5 | Character explainer | A presenter plus visual metaphors. Known characters need permission | [Asking for help](assets/readme/b5-character-explainer.mp4) |
| B6 | Dynamic meme | Short story cartoons. Portrait usually looks best | [Eiffel Tower](assets/readme/b6-dynamic-meme-eiffel-16x9.mp4) |

Style 5's visual concept was contributed by [Lawal Ridwan](https://github.com/leksautomate).

After you accept a finished video, you can ask for a matching cover and upload copy. The skill can draft a 16:9 thumbnail, title options, a description, and a pinned-comment question. It does not upload anything. These covers are real examples already in the repository:

| | | |
| --- | --- | --- |
| <img src="assets/readme/thumbnails/no-camera.jpg" alt="Thumbnail reading NO CAMERA, with a stick figure and a crossed-out camera" width="240"> | <img src="assets/readme/thumbnails/first-job.jpg" alt="Thumbnail reading THE FIRST JOB, with a prehistoric stick figure" width="240"> | <img src="assets/readme/thumbnails/a2-busy-vs-better.jpg" alt="Thumbnail reading BUSY does not equal BETTER, with a character buried in task cards" width="240"> |

## FAQ

<a id="faq"></a>

### Do I need to know how to code?

No. The assistant writes and runs the animation code. You review the script, the sample, and the finished file.

### Can I start without a finished script?

Yes. Paste a topic, a link, or bullet points. Approve the script the assistant writes before it generates pictures or spends money.

### Which mode should a small business use?

Use Code Engine B1 for a narrated explainer or training video with captions. Use Model Engine when you want a video service to generate the motion and you are comfortable paying that service.

### Will the character look the same in every scene?

Code Engine draws the character once and reuses those assets, which is the steadier option. Model Engine follows the written prompt. For a complicated costume, generate a reference image and attach it to every clip if your video tool allows reference images. That improves consistency. It does not guarantee it.

### Can we use the videos commercially?

The MIT license lets you use the software commercially. You still need the rights to your script, music, voice, and any character you did not create. A famous mascot or a copyrighted voice is not cleared just because this tool can draw a stick figure. YouTube or TikTok monetization is a decision those platforms make about your channel. This project does not grant or guarantee it.

### Does a successful install start billing?

No. Installation does not call a paid API. The assistant should explain any image, voice, or video-model charge and wait for you to approve it.

### The installer timed out. What now?

See [Troubleshooting](#troubleshooting) and [docs/INSTALL.md](docs/INSTALL.md). The usual fix is a longer clone timeout, or a manual `git clone` followed by a local install.

## Troubleshooting

<a id="troubleshooting"></a>

| What you see | What to do |
| --- | --- |
| Clone or `npx skills add` times out | Retry with a 20-minute window. macOS or Linux: `SKILLS_CLONE_TIMEOUT_MS=1200000 npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos` |
| The installer still fails | `git clone --depth 1 https://github.com/Transformaiton/stickman-video-director.git` and then `npx skills add ./stickman-video-director --skill directing-stickman-videos` from the parent folder. On Windows PowerShell, set `$env:SKILLS_CLONE_TIMEOUT_MS = "1200000"` before the same `npx` command. |
| `doctor` says Node or FFmpeg is missing | Install Node.js 20+ and FFmpeg, open a new terminal, and run `node -v` and `ffmpeg -version`. |
| `doctor` says `GEMINI_API_KEY` is absent | Ignore it unless you chose the bundled Gemini adapter. For that adapter, export the variable in the terminal. Do not paste the key into chat. |
| The assistant cannot render a Code Engine video | It needs file access and a terminal. Use Model Engine prompts, or switch to Cursor, Claude Code, or Codex. |
| The sample looks wrong | Say which shot, line, or sound to change. Approved pieces stay. A new sample is required when the approved range itself changes. |
| A video platform login or credit check fails | Model Engine generation stops until that account is usable. The storyboard you already approved is still yours. |

The same recovery commands live in the skill at [skills/directing-stickman-videos/references/installation-troubleshooting.md](skills/directing-stickman-videos/references/installation-troubleshooting.md).

## Contact

<a id="contact"></a>

Transformaiton.com is an AI consultancy for small businesses.

- Website: [https://transformaiton.com/](https://transformaiton.com/)
- Email: [info@transformaiton.com](mailto:info@transformaiton.com)
- GitHub: [https://github.com/Transformaiton](https://github.com/Transformaiton)

Questions about installing or using this copy can go to that email. Include your operating system, the style code you chose (`A1`, `B1`, and so on), and the error text with any API keys removed.

## Credits and license

<a id="credits"></a>

This repository is Transformaiton.com's public copy of [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director).

**Transformaiton.com is not affiliated with or endorsed by the original author.**

**Modifications by Transformaiton.com.** The customer guide is rewritten in English for small-business owners, including this page, [docs/INSTALL.md](docs/INSTALL.md), and [docs/USAGE.md](docs/USAGE.md). Upstream sponsor placements and social-marketing sections are removed from the homepage. The skill, local renderer, and sample media are unchanged.

The original copyright remains in [LICENSE](LICENSE):

> Copyright (c) 2026 Stickman Video Director contributors

Released under the MIT License. You may use, modify, and distribute this project, including commercially, if you keep that copyright notice and the license text. The software is provided as is, without warranty.
