# California 2026 portrait shorts

All 14 propositions have a separate portrait teaser derived from the cleaned human-narrated landscape explainer. The user approved Proposition 1's format and requested the full series for Instagram Reels and YouTube Shorts; the long videos remain the YouTube versions.

Local collection: http://localhost:8877/portrait/

Outputs live in `.video-production/portrait/prop-XX/`. Each video is 1080 × 1920, 30 fps, under 60 seconds, with H.264 picture and AAC audio. `explainer.mp4` includes burned-in captions; `clean.mp4` omits captions. Separate SRT/VTT subtitles and a suggested posting description accompany each short. The collection's ZIP includes only finished captioned videos, subtitles and descriptions, not private raw recordings or editing assets.

## Editorial and visual decisions

Each `project.json` records its original take, cleaned source asset, exact source frame and word ranges, edited narration asset, portrait scene graph, and original source-check date. Complete passages retain the mechanism and both voting perspectives. Polling and further detail remain in the full explainers. No speech is generated or sped up. The long recordings and landscape projects are preserved.

Proposition 1 remains the approved pilot. The other 13 use the same watercolor entrances, once-only drawing animations, color palette, phone-safe text, captions and website ending. Measures with quantitative comparisons use proportional animated bars or timelines; procedural measures use drawing diagrams. Every animation ends in an exact static hold.

ASR-aligned opening words sometimes incorrectly included the recording countdown. `opening-timing-corrections.json` stores short-window recognition evidence; preparation uses conservative VAD-checked speech onsets. A three-millisecond taper suppresses edit clicks. Energetic cut boundaries move into adjacent pauses, constrained by neighboring words. Captions never cross scene edits.

`boundary-review.json` retains localized ASR checks. Recognition is imperfect with accented speech and is not a substitute for listening approval. The full-length source alignment reviews remain relevant; these edits do not perform a new factual review. Prop 5's previously flagged “millions per recall” passage is not used in its short.

## Rebuild

From the content repository, with the existing Python environments and shared media library:

```sh
export PYTHONPATH=/home/arvind/code/ampytech-video-gen-tools/src
/tmp/ballot-video-env/bin/python video-projects/ca-2026-portrait/prepare_series.py
python3 video-projects/ca-2026-portrait/render_series.py
/tmp/ballot-video-env/bin/python video-projects/ca-2026-portrait/check_visuals.py
python3 video-projects/ca-2026-portrait/build_collection.py
```

Preparation contains the curated editorial choices and regenerates Props 2–45; it preserves the approved Prop 1 graph. Rendering also preserves Prop 1; to rebuild it explicitly:

```sh
/tmp/ballot-video-env/bin/python -m ampy_video.sketchbook.portrait \
  --project video-projects/ca-2026-portrait/prop-01/project.json \
  --output .video-production/portrait/prop-01 --jobs 3
```

The reusable portrait renderer belongs to `/home/arvind/code/ampytech-video-gen-tools/src/ampy_video/sketchbook/portrait.py`. It exports per-scene silent video, a separate pencil stem, audio mix, captioned/clean exports, and Resolve FCP7 XML. Content-addressed assets live outside Git in `~/.local/share/ampy-video/assets/`.

## Resolve and validation

Resolve project: `California Ballot 2026 - Narrated Explainers v3`. Portrait timelines are `Prop N - Portrait Short - Human Voice`; Prop 1 retains the suffix `Pilot`. Voice is on A1 `Narration - Human Excerpts`; pencil effects are on A2 `SFX - Pencil`. These are editable audio tracks with rendered scene picture. Captions are burned into web exports, with sidecars provided for editing. A retained Prop 2 initial-cut timeline is superseded by its final timeline.

Per-project `validation.json` checks resolution, frames, duration, audio and complete decode. `visual-validation.json` checks settled frames, diagram motion, edit frame lengths, captions and the closing website. `resolve-series-validation.json` records final timeline structure and online media checks. `export-manifest.json` records exact durations and MP4 SHA-256 hashes. Contact sheets and ASR output stay with local render outputs.

The review server's `.video-production/sketchbook/portrait` symlink points at the portrait output directory. All 14 captioned Shorts were subsequently uploaded through the user’s signed-in Chrome session to @ArvindPereira and saved as private. The YouTube Studio Shorts list verified all 14, with titles, descriptions, and not-made-for-kids audience settings. Local links and upload evidence: `.video-production/portrait/youtube-upload-results.json` and `youtube-evidence/all-14-private.png`. Instagram uploads remain outstanding; none were requested in that upload turn.
