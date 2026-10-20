# Handoff: finish the California proposition videos with human narration

Updated October 20, 2026. Start here after clearing conversation context.

## Current state and next objective

All 14 propositions already have full videos in the approved **Style C** sketchbook style, with existing AI narration. The remaining work is to record Arvind's wife, attach her approved takes to the scene graphs, align and retime each video, regenerate captions, review, and deliver the final collection. Do not rebuild the entire editorial structure or recreate all illustration assets from scratch.

Projects awaiting human narration: **01, 02, 03, 04, 05, 37, 38, 39, 40, 41, 42, 43, 44, 45**. No human take has been declared final or imported at this handoff. Browser test takes are not approvals for production. The real recording dashboard, followed by imported `project.json.recording`, tracks progress.

## Ownership and locations

- Content repo: `/home/arvind/educational-explainers.github.io`. Each `video-projects/ca-2026/prop-XX/project.json` owns the script, scene graph, sources, cues and asset references. Keep project sources and timed teleprompter files here in Git.
- Reusable tools repo: `/home/arvind/code/ampytech-video-gen-tools`; package `src/ampy_video/sketchbook`. Reuse it for future courses such as Bob-the-Robot; avoid ballot-specific logic in generic tools.
- Media store: `~/.local/share/ampy-video/assets/`, configurable with `AMPY_VIDEO_ASSET_ROOT`. Generated media and voice recordings stay outside Git. References use `asset://<sha256>.<extension>`.
- Existing review videos: `.video-production/sketchbook/prop-XX/explainer.mp4`; narration-only variant, scenes, captions, Resolve XML and validation sit beside them.
- Recording pack: `.video-production/recording-pack/`; portable `.video-production/ballot-recording-pack.zip`.
- Existing asset backup: `.video-production/sketchbook/assets-bundle.zip`. Rebuild it after attaching new recordings; the tools now include `recording.source` in asset bundles.
- Local review server: `http://localhost:8877/`. Recorder and tracker: **`http://localhost:8876/`**. These are local services, not public websites. Keep using the same browser, hostname and port: `127.0.0.1` and `localhost` have different browser storage.
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
