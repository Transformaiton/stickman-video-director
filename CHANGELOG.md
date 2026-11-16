# Changelog

Customer-facing pages in this copy are maintained in English by Transformaiton.com. The entries below through 2026-11-15 are a translation of the original project's changelog. Sample media and the skill runtime were not changed for the 2026-11-16 documentation update.

## 2026-11-16 — English customer guide

- Rewrote the homepage as "Stickman Video Director by Transformaiton.com" for small-business owners.
- Added [docs/INSTALL.md](docs/INSTALL.md) and [docs/USAGE.md](docs/USAGE.md).
- Replaced the other language homepages with short English pointers to the main guide.
- Removed upstream sponsor placements and social-marketing sections from the homepage.
- Left the skill, renderer, license, and sample media unchanged.

**Modifications by Transformaiton.com.** Transformaiton.com is not affiliated with or endorsed by the original author. Original project: <https://github.com/kaomei/stickman-video-director>.

## 2026-11-15 — A7 Rubber Hose and separate A/B samples (v2026.11.15.1)

- Added A7 Rubber Hose Animation in Director mode: a locked thin-line stick figure, two curved hair tufts, vintage painted scenery, and fixed prompts, with reference stills plus production and acceptance notes.
- Kept two approved landscape samples. Sample 2 starts at the source file's 2-second mark. Lyrics belong to that sample only and are not an A7 default.
- Recorded the approved direct-to-video path that uses the kitchen reference material, and retests for a post office and a seaside scene. A material reference is not the same thing as a first frame. Generation cost and model choice still follow Director approval.
- Synced the A7 introduction across the nine language homepages of that release. The top grid listed A1–A7 on the left and B1–B6 on the right, with the last right cell empty. The published count was 13 styles.
- B7–B10 stayed local and unpublished.

## 2026-11-13 — B3 and B4 animation and review (v2026.11.13.3)

- B3 lines, arrows, and underlines must record their purpose and the object they attach to, including target, direction, follow relationship, and the time they are actually visible. Animation has to serve the current story. A CRT effect, decorative flicker, or unused path parameter does not count as action.
- B4 plans story-specific local animation per shot. Text motion and picture motion are reviewed separately, for Chinese and for other languages. A complete shot, and an unchanged principal picture that continues across shots, cannot stay still for more than 3 seconds. A crop, a caption swap, or a decoration does not reset that timer.
- Samples and finished films must be tied to the exported MP4, the current plan, and asset fingerprints. An independent reviewer records each item. Missing evidence stays pending. A technical check is not a visual pass.
- Added regression checks for semantic action, picture animation, and skipped review. The source tree passed 352 tests and the installed build passed 68 targeted tests. Those results check the rules and the implementation. They do not mean a new film was visually accepted.
- This release added no media, did not change the README gallery, and did not include B6–B8 development.

## 2026-11-13 — Native portrait samples for B1–B3

- Stored three user-approved 10-second portrait videos as internal references, with the original files and source fingerprints. The README gallery was left as it was.
- B1 kept thin hand-drawn lines, paper, and handwritten text, with elements appearing in semantic order and small local motion. B2 stayed colorful hand-drawn. B3 stayed white line on black with a television texture. Portrait did not replace those looks.
- Portrait projects check per-shot composition, readable captions, visible action, and safe areas. Reference review is bound to the portrait master, and the full film is reviewed again at phone size and original speed.
- Technical diagnosis, independent review, and user approval are recorded separately. Accepting the three samples does not accept future films. Real tool limits have to be stated.

## 2026-11-11 — B production rules and the B4 opening

- Locked B4's opening type, text grouping, and emphasis motion, and checked early narration plus real local animation. A still cut, a camera push, or a title entrance does not count as picture motion.
- Locked caption presets for B1, B2, and B3, and added local-action and continuity checks. The shared sound path supports quiet ambience, separate dialogue, file sound effects, and motivated silence.
- A new B5 story must record the actual assets, captions, action, and sound. A real person or a complex host uses an available image tool or an approved still, not a silent fallback to a code-drawn face.
- Voice services follow the user's choice. Case voices are source credits. B4's approved Brian default stayed. Eight languages were updated with model and motion notes, including the verified Gemini case voices.
- Local source and an isolated install each passed 163 runtime tests. That shows the checks run. It does not mean every model matches the same taste. No new paid generation. B6 and later were out of scope.

## 2026-11-04 — B4 Survival Thriller and multilingual notes

- Published the B4 Survival Thriller path in the same skill: five locked style references, full prompts, Brian as the default narration, sound and early narration on the first frame, grouped opening text, a visual escalation in the first three seconds, story cuts of at most three seconds, quiet continuous ambience, and story sound effects.
- Connected B4 to the installable production entry, including `init --style B4`, validation, a sample, approval, full export, and per-shot cache. Added separate checks for ambience, character dialogue, file effects, story silence, and the opening sound.
- Published the approved 911 and death-countdown samples, and synced ten style descriptions across eight languages, including titles, sources, narration credits, the Codex suggestion, and seven FAQ items. The default homepage matched the English one.
- Repaired the A6 installable reference images and reference-prompt path. Kept the existing A1–A5 and B1–B3 routes. B5 experiments were out of scope. No new paid generation.

## 2026-10-23 — B1 master and independent production rules

- Locked the approved 21-second Bodi sample with sound as the B1 Minimal Line Art standard, and synced the Chinese top and detail previews. The older sample stayed. The second case was still waiting on an update.
- Specified thin proportions, exaggerated and varied expressions, actions and props designed for the new script, a near-white faint grid, small local motion, and restrained effects. The picture follows the original-speed narration, and captions stay present.
- New B1 projects default to the Google Gemini Bodi voice, without an extra voice-style description. A user-selected setup wins. Each B style keeps its own voice, captions, and pacing.
- Corrected B-mode sample-range checks, approval fingerprints, and per-shot cache. A full film still needs a full check and sample approval. Verified A1–A5 rules stayed. Other language pages were not synced in that change.

## 2026-10-23 — Autopilot films and B1 Minimal Line Art

- Same repository and the same `directing-stickman-videos` skill. Director mode (A) produces a storyboard and video prompts. Autopilot mode (B) connects asset generation, voice, captions, local motion, sound effects, and local compositing.
- Added installable local scripts, configuration notes, an optional Gemini adapter, and an offline example. Picture timing follows the real narration. After sample approval the full film can resume from a shot cache.
- Published B1 Minimal Line Art and an approved original-speed Sadaltager sample with sound. A second showcase sample was not added then.
- Kept the Chinese homepage and the A/B style structure that had already been confirmed. Other languages were not synced. Series A prompts and reference rules stayed.

People who already had the skill update that same skill. Autopilot needs Node.js 20+, FFmpeg, and a usable image and voice tool. The first run checks the configuration. See [the runtime notes](skills/directing-stickman-videos/references/autopilot-runtime.md).

## 2026-10-20 — Style 5, Historical Cartoon

- Added Historical Cartoon: white round heads, black oval eyes, thin limbs, period costume, and colored painted scenery.
- Folded the era, character cards, prop state, and the full voice description into the Style 5 storyboard. Verified prompts for styles 1–4 stayed.
- Synced the language pages and showed an Edo Japan sample and an ancient Egypt sample. The Japan sample was also the header preview.
- Thanks to [Lawal Ridwan / @leksautomate](https://github.com/leksautomate) for the style, prompts, and Japan sample.

Using style 5 requires an updated skill. [Test record](tests/reports/style-5.md).

## 2026-10-15 — Chinese homepage and first-run experience

- The Chinese homepage showed four styles, six visual treatments, and eight samples, with each style note placed before its sample.
- The install entry kept one install request and the GitHub link, and dropped terminal steps and tool-specific commands from that page.
- The usage entry asked for a topic or source text. Ratio, style, and the director's proposal were confirmed by the skill. Users were not asked to prefill every parameter.
- Repeated notes were merged. Landscape and portrait advice sat under the tips.
- Lightweight GIF previews were made for the Chinese page. The original GIFs, MP4s, and other language pages stayed.
- Style requests and video submissions were combined into one section, with Star History and the MIT license noted.

That was a documentation update. Installed users did not need to reinstall. Skill rules did not change.

## 2026-10-14 — Style 4, Cozy Storytelling

- Added a cozy story style that combines minimal characters with colorful 2D locations.
- New segments change location on purpose, while characters and important props stay continuous.
- Published two selected samples: a subway commute and an outdoor cafe.

Using style 4 requires an updated skill. [Test record](tests/reports/style-4.md).

## 2026-10-13 — Style 1 character description

- Returned to a short stick-figure description and added a rule that the current pose replaces the previous one.
- Kept occasional simple expressions, as requested.

People who installed before this change can update the skill. [Test record](tests/reports/classic-character.md#2026-10-13--concise-current-pose-revision).

## 2026-10-12 — Shared voice and the prehistoric case

- All styles share a full voice description. Every segment of one video repeats the same voice. A different video may choose a different voice.
- Added the Style 3 prehistoric story and a community example.

Older installs that need these rules can update the skill. [Voice record](tests/reports/shared-voice.md) · [Style 3 record](tests/reports/style-3.md).
