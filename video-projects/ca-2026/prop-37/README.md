# Prop 37 sketchbook pilot

A complete 202.867-second, 1280×720/30fps explainer in the approved C style: watercolor illustrations, selective pencil-hand drawing, exact animated charts, and uninterrupted narration. This was the first end-to-end pilot. The [full 14-video collection](../README.md) has now been rebuilt in this style.

## Scene graphs belong in Git; generated media does not

`project.json` is the source of truth. It contains 26 scenes, frame boundaries, narration anchors, illustration placements, ordered pencil paths, chart values, text, sources and the seven-part script. `assets.lock.json` records asset roles, hashes and byte sizes. Captions, word timestamps, prompts and editorial notes are also versioned here in the website repository. Reusable code lives in the separate `ampytech-video-gen-tools` repository.

Generated illustrations, the hand image and the approved narration are stored externally under `~/.local/share/ampy-video/assets/`, or `$AMPY_VIDEO_ASSET_ROOT`. References have the form `asset://<sha256>.<extension>`. Content hashes make references independent of the producing computer and detect accidental asset changes. The bundle is an ordinary zip of those hashed files; it can live on a separate drive or external storage. No hosted service or AI credits are needed to render existing assets.

From the tooling repository root, with Pillow, NumPy and FFmpeg installed:

```bash
export PYTHONPATH="$PWD/src"
PROJECT=/path/to/educational-explainers.github.io/video-projects/ca-2026/prop-37/project.json
python -m ampy_video.sketchbook check --project "$PROJECT"
python -m ampy_video.sketchbook build --project "$PROJECT" --output outputs/prop37-sketchbook --jobs 3
python -m ampy_video.sketchbook editor --project "$PROJECT" --port 8875
```

The actual pilot was rendered using `/tmp/ballot-video-env/bin/python` against this repository's code, not a separate production script. Its output is `/home/arvind/educational-explainers.github.io/.video-production/sketchbook/prop-37/`.

## Fast iteration

```bash
python -m ampy_video.sketchbook preview --project "$PROJECT" --scene 19 --time 5 --output outputs/stills
python -m ampy_video.sketchbook build --project "$PROJECT" --scene 19 --output outputs/prop37-sketchbook
```

A full build reuses scenes whose manifest, assets and renderer have not changed. A single-scene build updates that scene only; run the full build afterwards to assemble exports. `build.json` records cache hits. Do not hand-edit rendered output as a substitute for updating the manifest.

The local editor shows the real renderer, accepts edits to scene JSON, and can trace pencil paths by clicking points on the preview. Saving validates the complete scene graph and retains a `.json.bak` copy. It is a small authoring aid, not a full drag-and-drop timeline editor. Start it with filesystem permissions to write the project file.

## Transfer assets independently

```bash
python -m ampy_video.sketchbook.assets ingest /path/to/new-illustration.png
python -m ampy_video.sketchbook.assets pack --project "$PROJECT" --output /external/storage/prop37-assets.zip
# On another computer, after cloning the tools and scene graph:
python -m ampy_video.sketchbook.assets unpack /external/storage/prop37-assets.zip
```

Commit the reference returned by `ingest` in the asset registry, not the image. Bundles verify content hashes before installing and reject path traversal. New projects can reuse the same store. The current media bundle also includes the reused family and hand illustrations so it does not depend on the older prototype directory.

## Narration and future recordings

`teleprompter.txt` in the export contains clean paragraphs without headings. `recording-guide.txt` adds section headings. The pilot retains the previously approved narration exactly. Pencil sounds are added only while visible hand strokes are being drawn. The export validates the additive mix sample by sample; it does not apply fades, ducking or automatic leveling to the narration. The review page can switch pencil effects off.

For a replacement recording, produce an aligned word list (`text` or `word`, `start`, `end`, in seconds), then:

```bash
python -m ampy_video.sketchbook retime --project "$PROJECT" --words new-words.json --narration new-recording.wav --output /path/to/educational-explainers.github.io/video-projects/ca-2026/prop-37/retimed.json
```

The helper matches spoken anchor phrases, rejects ambiguous matches, and moves scene boundaries. Narration must end on a 30fps frame boundary. Element `cue` fields can follow individual words; elements without cues retain scene-relative timings. This is a starting point for review, not a claim that timing will automatically suit every delivery. Regenerate captions for the new recording, add their paths and clear `captions_need_regeneration` before export; builds deliberately refuse stale captions. Ingest the finished recording into the asset store before committing its final reference. The wife's replacement recording has not yet been made or tested.

## Resolve and validation

The export includes an FCP7 XML with 26 separate picture clips and continuous narration/pencil tracks. Import `resolve-timeline.xml` into Resolve. Source pictures are baked scene clips; revise their internal drawings through JSON and rebuild. Audio remains independently editable. The browser exports include SRT/VTT subtitles; the XML does not add a native Resolve subtitle track.

`validation.json` checks full-decode success, frame count, audio duration, asset integrity, scene coverage, text bounds and mix preservation. Regression tests also cover the small-bar failure found in the pilot, ambiguous cues, independent asset bundle transfer and XML audio continuity. Review the actual video as well: these checks cannot establish artistic quality or audibility on every speaker.

## Gaps found and fixed

- Text lists should not use arrows unless there is a causal or sequential relationship. Eligibility, monthly-cost and vote-choice screens were corrected.
- Economic sketches need labeled curves and an explicit illustration disclaimer.
- Animated bars can be less than one pixel wide on their first frame. The renderer now safely handles that case.
- Static previews cannot catch all animation failures. The entire video is rendered and decoded.
- Narration must not acquire scene fades. It stays on a single continuous track.
- Cache keys must include the pencil anchor metadata as well as image bytes.
- Generated files should not be tied to absolute project paths or committed with source. Content-addressed external storage and verified transfer bundles now support this.
- The website currently has no printable-checklist feature, so the CTA invites viewers to read the explanation and sources without promising a checklist.

Remaining limits: fixed 720p canvas, modest path-tracing editor, no automatic cloud asset synchronization, no photorealistic motion generation, and human review is still required for research and scene design. These are deliberate boundaries of this first tested workflow.

## Timed rehearsal prompter

The review page now links to `teleprompter.html`: centered phrases, word underlining, upcoming text, a three-second start/resume lead-in, WAIT countdowns, pace adjustment, mirror mode, fullscreen and optional reference narration. Silent mode is suitable for rehearsal. The page now also includes local microphone recording, saved takes, WAV export and timing notes; see the [collection recording instructions](../README.md). Timing is a guide, not a requirement for the new recording.

The canonical script is preserved. Existing transcription timestamps anchor matched words; 49 corrected or expanded words have interpolated timing, including spoken numbers. All 72 phrase cues retain the original script order. Browser checks exercised start, pause, wait countdown, word highlighting, pace, mirror and completion.

`teleprompter-timed.txt` gives suggested phrase start times. `teleprompter.lrc` contains line-level karaoke cues; compatibility depends on the receiving app. `teleprompter-timed.json` provides word timing and estimated-timing flags for a custom importer. These project files are versioned here. The generic browser view and exporter live in the tools repository.

Regenerate without rendering video:

```bash
# Run from ampytech-video-gen-tools, with PYTHONPATH set to its src directory.
python -m ampy_video.sketchbook.prompter --project /path/to/educational-explainers.github.io/video-projects/ca-2026/prop-37/project.json --output /path/to/rendered/prop-37
```

Full video builds also export the prompter whenever `prompter_words` is set. After recording a new voice, use newly aligned timestamps rather than the old reference timings. At 100% pace, suggested times match the existing video; slower rehearsal settings deliberately do not.
