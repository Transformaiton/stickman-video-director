# Use Stickman Video Director

Read this after [installation](INSTALL.md). The homepage is [Stickman Video Director by Transformaiton.com](../README.md).

You talk to the installed skill in your AI assistant. You do not run a website, and you do not edit animation code yourself. The assistant should show a short plan, wait at the approval points below, and name any paid call before it makes one.

## Choose a mode

**Model Engine (A)** writes a director's proposal and one prompt per clip. You can generate those clips in a video tool such as [Google Flow](https://flow.google.com/), then add captions in your editor. An assistant that can control a browser and edit files can also run that path and hand you a local preview. Writing the proposal does not need an API key.

**Code Engine (B)** builds a finished MP4 on your computer: still art, narration, captions, small motion, and sound effects. It needs Node.js 20+, FFmpeg, and a way to create pictures and speech. Local rendering does not use video-model credits.

Use B1 for a faceless explainer or a training video. Use A when you want a video model to perform the motion and you already have credits on that platform.

Both modes accept `16:9` landscape and `9:16` portrait. Say which one you want. If you leave the length out, Model Engine defaults to about 60 seconds.

## Pick a style

Reply with a code. You do not download a style pack.

| Code | Name | Start here when you want |
| --- | --- | --- |
| A1 | Classic black and white | A clean analogy on a white or black field |
| A2 | Modern pop | A recurring character in a product story |
| A3 | Prehistoric cave | A short fable |
| A4 | Cozy storytelling | A calm everyday scene |
| A5 | Historical cartoon | A period setting. Consistency is better if you attach character reference images |
| A6 | Amber noir | A warm, shadowed what-if |
| A7 | Rubber hose | Vintage elastic comedy |
| B1 | Minimal line art | A faceless explainer or training video |
| B2 | Colorful hand-drawn | A habit or attention lesson |
| B3 | Retro TV | A curious fact with a television look |
| B4 | Survival thriller | Suspense. The default narrator name is Brian, and you can choose another voice |
| B5 | Character explainer | A presenter plus stick figures acting out the idea. Do not use a famous character unless you have permission |
| B6 | Dynamic meme | A short cartoon story. Portrait is the stronger frame |

Samples for each code are linked from the [homepage style table](../README.md#styles). Those files are the original project's published renders.

## Code Engine: training or explainer video

Paste this and replace the bracketed outline.

```text
Use Code Engine / mode B to turn the following outline into a training video:
[Paste your outline, article, or script]

Requirements: about 3 minutes, landscape 16:9,
B1 "Minimal Line Art", English narration, captions, and sound effects.

Check image generation, voice, and video compositing setup.
Give me the script and a 20-second sample with sound first.
After I approve them, make the full video and deliver the file.
```

What happens:

1. The assistant checks image generation, voice, and FFmpeg. If something is missing, it names that item and how to set it. It should not ask you to paste an API key.
2. You receive a script, caption treatment, and voice choice. Change anything that is wrong before you approve.
3. You receive about 20 seconds with picture, voice, captions, and sound. Watch that file. Say what to fix, or approve that sample.
4. After approval, the assistant renders the rest to the narration. You get a video file and caption sidecars in the project folder. You do not assemble each scene by hand.
5. If a later scene is wrong, ask for that scene to be redone. Do not throw away an approved opening unless you want it changed.

A faceless social explainer uses the same prompt. Change the length, the ratio, and the style code. For a vertical clip, say `portrait 9:16`. For a presenter, say `B5 "Character Explainer"` and describe the presenter. Supply a picture you have rights to if the presenter is a real person or a complex character. The skill should not invent a code-drawn substitute for that face.

## Model Engine: prompts, then optional production

Prompts only:

```text
Use Model Engine / mode A to turn the following topic into a stickman video:
[Your topic, copy, or brief]

Requirements: landscape 16:9, A4 "Cozy Storytelling", 30 seconds.
Give me a director's proposal first. After I approve it,
deliver standalone prompts for each clip.
```

The proposal includes the story, narration by segment, visual action, camera, and sound. After you approve it, copy each prompt into your video tool. If the tool accepts reference images and you made a character sheet, attach the same sheet to every clip.

Finished file, only if the assistant can browse, save files, and edit:

```text
Use the agent production route. By default, open Google Flow
in the built-in browser for video generation.
Check browser access, Flow login and credits, file access,
and editing tools first. Explain the production plan,
tools, costs, and execution scope together.
After I confirm, continue within the authorized scope through
generation, targeted revisions, editing, and a local preview.
Add captions and sound to match my needs and selected style.
Do not wait for a reminder for every clip. Explain any missing
tools or changes to the plan or cost before proceeding.
```

Log into the video platform and confirm credits before you approve that second prompt. The assistant should stop if the login or the balance is missing.

## Approval rules

- Approving the topic is not approving the script.
- Approving the script is not approving a paid generation.
- Approving a 20-second Code Engine sample covers that sample. The assistant should still tell you the remaining cost before the full render if more paid image or voice calls are required.
- Changing the aspect ratio, style, length, or narration sends the plan back for a new approval.
- Installation is not permission to spend money.

## Covers and upload text

After you accept the finished video, you can ask:

```text
Generate the Thumbnail & Publishing Kit for this video:
- 1 landscape 16:9 thumbnail image matching the approved art style
- 5 YouTube title options
- A description, relevant tags, and verified timestamps if available
- 1 engagement question for the pinned comment
- A pre-publish checklist with any pending checks clearly marked
```

Image generation needs a tool and your cost approval. If no image tool is available, you still get the text. Nothing is uploaded. Example covers from the original project are on the [homepage](../README.md#styles).

## What you should receive

| Mode | Files |
| --- | --- |
| Model Engine, chat | A proposal, then one standalone prompt per clip, plus edit notes for captions. |
| Model Engine, agent production | Those prompts, the generated clips, and a local preview after editing. |
| Code Engine | An MP4, caption files, and a preview report in the project `output/` directory. |

Play the file with sound before you send it to a client or post it. The technical checks do not replace watching it.

## If something looks wrong

| Problem | What to say or check |
| --- | --- |
| The voice or pictures would cost money and you have not agreed | Tell the assistant to stop. Ask for the provider, model, and expected calls. |
| The character changes between Model Engine clips | Generate one reference image and attach it to every clip that supports references. |
| Code Engine `doctor` fails | Follow [INSTALL.md](INSTALL.md). Node 20+, FFmpeg, and FFprobe have to be visible in that terminal. |
| The 20-second sample is the wrong style | Name the style code again, for example `B1`, and ask for a new sample before the full video. |
| Captions do not match the words | Point at the line. The assistant should regroup captions to the real speech, not squeeze the type. |
| You need a different language | Say the narration language and the caption language. The skill can do that. The commands and style codes stay in English. |

Questions about this Transformaiton.com copy: [info@transformaiton.com](mailto:info@transformaiton.com). The original project is [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director). Transformaiton.com is not affiliated with or endorsed by the original author.

**Modifications by Transformaiton.com.** This guide is new English documentation. It does not change the skill.
