# Handoff: finish the California proposition videos with human narration

Updated October 20, 2026. Start here after clearing conversation context.

## Earlier session: Proposition 1 human narration trial (superseded)

The latest full Prop 1 browser take (`2026-10-20T20-16-40-238Z`) was recovered and used for a trial. Original audio and provenance are preserved under `.video-production/human-preview/prop-01/`. This legacy take has no script-version hash or production approval; the canonical recording was unset at that time; the full-series update below now supersedes this trial. Review captions and delivery near 0:17 and 1:20 before finalizing.

The user established DaVinci Resolve as the editable master for narration updates, with voice and sound effects on separate tracks. The existing project now contains **Prop 1 - Sketchbook C - Human Narration Trial**: 15 retimed scenes, 5495 frames at 30 fps, A1 **Narration - Human Take**, A2 **SFX - Pencil**. All 17 media items are online, with no gaps or overlaps. The prior timeline is retained. Project saved and backed up at `.video-production/resolve-backups/prop-01-human-trial-2026-10-20.drp` (media files remain separate). See `prop-01/resolve-human-trial-validation.json` for this trial's checks. Continue using separate Resolve tracks for future takes; do not flatten effects into the narration master.

Local preview: `http://localhost:8877/prop-01-human-preview/`. This preview was rendered by the sketchbook pipeline; the new Resolve timeline has been structurally verified, not separately rendered or given final listening approval.

## Current state and next objective

All 14 propositions now have full **Style C** videos using Arvind's wife's new recordings with the user-approved gentle noise reduction (`afftdn=nr=6:nf=-45`). All 18 original takes from **http://localhost:8877** were backed up and hash-verified in `.video-production/human-recordings/`. Thirteen selected takes were approved in the browser; Prop 1's sole new full take was selected under the user's conversation authorization, without fabricating a browser approval. All selected script hashes match the canonical scripts.

Canonical `project.json` files now contain the cleaned audio asset, original recording provenance, retimed scenes, `words-human.json`, regenerated captions and teleprompter timings. Every project is `aligned_cleaned_needs_review`: renders and Resolve structures are verified, but final listening/content review is still required. Per-project `alignment-review.json` preserves ASR differences. Short-window checks recovered ASR omissions in Props 2 and 42. In Prop 5, listen near 1:45 to confirm “millions per recall”; two ASR passes heard “billions,” which could be recognition error or a reading slip. Do not silently rewrite the recording.

All 14 cleaned timelines are saved in Resolve as **Prop N - Sketchbook C - Cleaned Human Narration**, with A1 **Narration - Cleaned Human Voice** and A2 **SFX - Pencil**. Readback verified complete scene coverage, matching durations, online media and no gaps/overlaps on either audio track. Backup: `.video-production/resolve-backups/cleaned-human-series-2026-10-20.drp`. See `resolve-human-series-validation.json` and `human-series-validation.json`. Web exports were made by the sketchbook pipeline, not re-rendered from Resolve.

The default collection at **http://localhost:8877/** now links to all 14 cleaned human-narrated videos via `/human/prop-XX/`. Previous AI videos remain at `/index-ai.html`. Original AI scene graphs are backed up in `.video-production/ai-project-backup/`. Do not overwrite the old AI scene media used by the retained Resolve timelines. For future human-series builds, use output `.video-production/human-series`, not `.video-production/sketchbook/prop-XX`.

## Ownership and locations

- Content repo: `/home/arvind/educational-explainers.github.io`. Each `video-projects/ca-2026/prop-XX/project.json` owns the script, scene graph, sources, cues and asset references. Keep project sources and timed teleprompter files here in Git.
- Reusable tools repo: `/home/arvind/code/ampytech-video-gen-tools`; package `src/ampy_video/sketchbook`. Reuse it for future courses such as Bob-the-Robot; avoid ballot-specific logic in generic tools.
- Media store: `~/.local/share/ampy-video/assets/`, configurable with `AMPY_VIDEO_ASSET_ROOT`. Generated media and voice recordings stay outside Git. References use `asset://<sha256>.<extension>`.
- Current review videos: `.video-production/human-series/prop-XX/explainer.mp4`; narration-only variant, scenes, captions, Resolve XML and validation sit beside them. `.video-production/sketchbook/human` links to this output. Earlier AI versions remain in `.video-production/sketchbook/prop-XX/`.
- Recording pack: `.video-production/recording-pack/`; portable `.video-production/ballot-recording-pack.zip`.
- Current asset backup: `.video-production/human-series/assets-bundle.zip` (35 assets including original and cleaned recordings). All 18 raw takes also remain backed up separately. Keep private recordings out of any public website upload.
- Local review server: `http://localhost:8877/`. The actual full-series recordings are in Chrome at **`http://localhost:8877/`** (including `/prop-45/teleprompter.html`); **port 8876 contains only earlier tests**. The newer takes were missed initially because only port 8876 was checked. These are local services, not public websites. Keep using the same browser, hostname and port: `127.0.0.1` and `localhost` have different browser storage.
- Existing Resolve project: **California Ballot 2026 - Narrated Explainers v3**. Timeline names: **Prop N - Sketchbook C - Timed Recording**; Prop 37: **Prop 37 - Sketchbook C - Full Pilot**. See `resolve-series-validation.json` for recorded checks, not a guarantee of current app state.

## Recording session for Arvind's wife

1. Open the recorder dashboard and select a script. There is also a script selector on each prompter.
2. Enable and select the intended microphone. Check that the meter moves. Record a short test and listen before a full take.
3. Record naturally. The prompter offers a three-second visual lead-in; pausing it keeps audio recording. Reference narration is muted while recording. Suggested cues guide pace; they do not recognize or follow speech.
4. Stop, listen, and **Approve this take** when satisfied. Only one take per script is approved; choosing another replaces the approval without deleting audio. The dashboard counts approved scripts and lets her return to the selected take.
5. Download the **original audio** and **scene-graph assignment JSON**. The dashboard can download all approved assignments as one JSON. Download audio files separately. WAV conversion is optional for editing; the assignment hashes the ORIGINAL, so retain that exact file and filename.
6. Downloaded files are the portable backup. Browser IndexedDB stores takes and approvals locally, but does not synchronize to another computer. There is no automatic upload or automatic Git write. Download clicks cannot verify that the browser finished saving a file.
7. On the Mac Mini, unzip the new pack and run `Start Recording.command`, or `python3 serve.py` in the extracted folder. Python 3 and a supported browser are needed, not GPUs or AI models. Actual Mac microphone/browser behavior still needs a short hardware test.

**Resolved audio issue:** the AKG C44 was both input and default playback output on the Linux computer. The recorded WAV contained audio, but playback went to the microphone's empty headphone jack. Arvind confirmed playback works after correcting output routing. This was not a WAV-conversion failure. Do not add fades or aggressive processing in response to this incident. Recorder diagnostics now include duration, captured bytes, a readable level meter, decoded signal checks and quiet-input warnings.

## Import approved takes into scene graphs

From the tools repo (use `/tmp/ballot-video-env/bin/python` on this machine):

```bash
export PYTHONPATH="$PWD/src"
python -m ampy_video.sketchbook.recording_import \
  --projects /home/arvind/educational-explainers.github.io/video-projects/ca-2026 \
  --assignments /path/to/approved-recordings.json \
  --recordings /path/to/downloaded-original-audio
```

A single `prop-XX-recording.json` assignment works too. The importer verifies the exact audio SHA-256 and canonical script version before copying into the asset store. It adds `recording.source`, take identity, approval date, script hash and timing metadata to `project.json`, with status `approved_needs_alignment`. Commit those source changes. It deliberately preserves `narration` and current video timings until alignment is finished; merely swapping audio can truncate speech or misalign illustrations.

Older takes made before script-version tracking cannot be approved through this workflow. Preserve them if needed, but do not invent approval or silently associate them with a changed script. A script edit after approval marks its dashboard status as needing a new recording.

## Finish one video first, then repeat

1. Start with an approved recording and listen through it. Trim lead-in/out and unwanted pauses while preserving natural delivery. Retain the original as `recording.source`; ingest any edited master separately.
2. Align the actual spoken words to the canonical script. Existing `words-global.json` belongs to the old voice and must not be reused as if it described the new recording. Timing event notes are guidance, not forced alignment. Review corrections and omissions manually.
3. Use the existing `sketchbook retime` command as a starting point; inspect its implementation first. It resolves scene anchor phrases against word timestamps and element cues. It expects narration ending on a video frame boundary, currently writes absolute paths, and removes old caption links. Normalize resulting references back to repo-relative word files and content-addressed audio before committing. Check every scene has positive duration and all drawing actions fit.
4. Regenerate SRT/VTT, canonical timed text, LRC and teleprompter JSON from the new word alignment. Retiming alone does not generate replacement captions. Advance `recording.status` only after alignment/review, retaining original take provenance.
5. Render one full video, check voice is continuous and intelligible, pencil effects are audible but subordinate, and visuals land with narration. Then batch the rest. Never use a long looping/stuttering image-to-video clip merely to fill time.
6. Reimport/update Resolve timelines with online media and no gaps, save the project, review exports, and rebuild the collection `index.html` after all videos are complete. Export and retain Resolve project backups externally.
7. Check factual claims and dated polling against primary sources before final publication. Existing source check dates are preserved, not refreshed by visual rendering. Explain uncertain estimates as estimates, distinguish illustrative stories from promises, and describe both voting positions fairly.
8. Publish only final reviewed outputs to the requested destination; no new YouTube upload has occurred in this workflow. Confirm the actual destination/channel if it is not established. Do not upload private raw recordings incidentally with the website.

## Established creative requirements

- Illustration motion preference (October 20): fade/rise/zoom in once over 1.4 seconds, then hold the image completely static. No repeated zoom, bounce, or slow resizing after the entrance. All 14 AI-narrated videos have now been rebuilt with this effect on all 152 illustrations across 223 scenes. Both export variants passed decode/duration checks, captions match source files, and all illustration layers were checked to settle to their original pixels and position. See `animation-rebuild-validation.json`. Collection: `http://localhost:8877/`. Narration, script, and timeline durations are unchanged. The shared renderer implements the opt-in `animation: fade-rise` image setting; preserve that tools-repo change with these project manifests. The new full human-narration series also uses this animation. The older isolated trial is superseded.
- Use approved Style C: artistic ink/watercolor illustrations revealed with a pencil/hand, drawing sounds, and animated diagrams/charts. Keep text slides visual, not walls of text.
- Structure: high-level background and what the proposition changes → concrete illustrative example → mechanism/details → reasons to vote yes → reasons to vote no → dated polling → CTA to visit the website and make a printable voting checklist.
- Brisk, comprehensible narration. Questions should sound like a viewer/voter asking, not an artificially inserted “neighbor.”
- Prefer short shots and cuts between relevant scenes over extended generated motion that bounces at clip joins. Use local generation; reserve Higgsfield credits for deliberate video uses. No new paid generation is needed to replace narration.
- Preserve continuous voice; avoid long fade-ins/fade-outs or ducking that obscures speech. Explain housing supply/demand limitations where relevant, not blanket promises of affordability.

## Commands and validation

```bash
# From tools repo, PYTHONPATH set as above:
python -m ampy_video.sketchbook check --project /path/to/prop-01/project.json
python -m ampy_video.sketchbook build --project /path/to/prop-01/project.json --output /path/to/review/prop-01 --jobs 3
python -m ampy_video.sketchbook.batch --projects /path/to/ca-2026 --output /path/to/review --concurrency 4 --jobs 3
python -m ampy_video.sketchbook.recording_pack --projects /path/to/ca-2026 --output /path/to/recording-pack --zip /path/to/ballot-recording-pack.zip
python -m ampy_video.sketchbook.assets pack-series --projects /path/to/ca-2026 --output /external/assets-bundle.zip
python -m unittest discover -s tests -p 'test_recording*.py' -v
```

Existing production has 223 scenes, about 44.9 minutes, 720p/30 fps. `series-validation.json` and per-export `validation.json` record the previous rendering checks. Do not imply they validate new human-voice exports. Check decode, durations, captions and complete scene coverage again after retiming. Synthetic Chrome tests cover sound/silence detection, persistence, approval replacement, assignment identity and dashboard navigation; real AKG playback was confirmed by the user.

Do not rerun `build_sketchbook_series.py` casually: it rewrites scene layouts from older storyboards. Preserve unrelated work in both repos. At handoff, the tools repo has unrelated Studio asset-library edits; the website has untracked `.gitignore`, `ca-2026-ballot/videos/` and `tools/ballot_video/`. These were not swept into this task's commits.

## Portrait shorts (October 20 follow-up)

The user approved the Prop 1 portrait pilot, including animated graphs and a closing website address, then authorized portrait teasers for all 14 propositions for Instagram Reels and YouTube Shorts. The landscape versions remain for YouTube. Portrait sources and rebuild instructions are in `../ca-2026-portrait/README.md`; local review is `http://localhost:8877/portrait/`. Each short is under 60 seconds, 1080 × 1920 at 30 fps, using excerpts from the same cleaned human recordings at natural speed. The separate portrait scene graphs preserve source-cut provenance and the approved pilot. Narration and pencil effects remain separate in Resolve. The local collection offers individual downloads and a finished-media-only ZIP; there has been no platform upload.
