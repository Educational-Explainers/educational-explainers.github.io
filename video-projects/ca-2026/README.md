# California 2026 sketchbook video series

All 14 propositions have illustrated sketchbook exports and timed rehearsal/recording pages. The current voice tracks preserve the previously approved narration. New recordings can replace them after alignment and review.

## Project ownership

Each `prop-XX/project.json` is the source of truth for script, scenes, charts, timing, captions and asset references. This website repository also owns the canonical teleprompter text, word alignment, timestamped text, LRC cues and timing JSON. `storyboard-v3.json` preserves the prior approved editorial plan for the 13 adapted videos. Sources and their original check dates are preserved; this visual remake is not a fresh polling update.

Reusable code lives in `ampytech-video-gen-tools/src/ampy_video/sketchbook/`, including the renderer, batch builder, browser prompter, microphone recorder, asset store and portable recording-pack builder.

Generated media stays outside Git in `~/.local/share/ampy-video/assets/` (override with `AMPY_VIDEO_ASSET_ROOT`). [Shared asset references](shared-assets.json) and the [exact illustration prompts](shared-art-prompts.json) are versioned here. Three new shared illustrations were generated with the built-in image tool; no Higgsfield credits were used. The tool did not report a dollar cost.

## Local outputs

- Video collection: `http://127.0.0.1:8877/`
- Recording collection: `http://127.0.0.1:8876/`
- Portable recording ZIP: `http://127.0.0.1:8877/ballot-recording-pack.zip`
- Video output directory: `.video-production/sketchbook/`
- Portable recording output: `.video-production/recording-pack/`
- Full external-media backup: `.video-production/sketchbook/assets-bundle.zip` (21 unique assets, including all original narration tracks).

These URLs refer to local servers on the production computer, not public hosting. To use the Mac Mini, transfer the recording ZIP to it, unzip it, and run `Start Recording.command`. It uses Python 3 to start `http://localhost:8876`; if the launcher is blocked, open Terminal in the extracted folder and run `python3 serve.py`. The ZIP's `READ-ME.txt` has the full instructions. The recording computer needs no rendering dependencies, GPU, AI models or API keys.

## Recording on the Mac Mini

Choose a proposition, enable the microphone, allow browser/macOS permission, and select the intended device. Speak to check the meter. Record take captures audio immediately, with a three-second visual lead-in before the script advances. Reference narration is muted during recording. Pausing the prompter keeps the microphone recording, preserving pauses for the edit. Keep the tab in front while reading.

Stop and save the take, play it back, then download **both the audio and its JSON timing notes**. Original audio format is selected according to browser support; WAV conversion is available for editing and does not improve the compressed original. The recorder requests echo cancellation, noise suppression and automatic gain control off; actual device settings are included in timing notes. Finished takes are retained in that browser's IndexedDB, but download a backup rather than relying on browser storage. Nothing uploads automatically.

Transfer the audio and timing notes back to the editing computer. Suggested timings are based on the current narration, with explicitly flagged interpolation for corrected words and numbers. The prompter does not listen and follow speech. Align the new recording, regenerate captions, retime the video and review it before replacing the existing exports.

Browser recording was tested with a synthetic microphone in Chrome on Linux, including persistence after page reload and WAV conversion. Actual Mac Mini microphone/Safari behavior still needs a short test on that machine before a full take.

## Reproduction

Run from the tools repository, with Pillow, NumPy and FFmpeg available:

```bash
export PYTHONPATH="$PWD/src"
PROJECTS=/path/to/educational-explainers.github.io/video-projects/ca-2026
python -m ampy_video.sketchbook.batch --projects "$PROJECTS" --output /path/to/sketchbook --concurrency 4 --jobs 3
python -m ampy_video.sketchbook.recording_pack --projects "$PROJECTS" --output /path/to/recording-pack --zip /path/to/ballot-recording-pack.zip
python -m ampy_video.sketchbook.assets pack-series --projects "$PROJECTS" --output /external/video-assets.zip
```

`build_sketchbook_series.py` records this collection's adaptation from the prior storyboard. Normally edit individual scene graphs directly; rerunning that adaptation script replaces their scene layouts. The Prop 37 pilot remains its manually reviewed scene graph.

[Series validation](series-validation.json) covers all 14 exports, canonical-script preservation and recording tests. [Resolve validation](resolve-series-validation.json) records saved timeline IDs, frame counts and gap/offline checks. Timelines are in **California Ballot 2026 - Narrated Explainers v3**, named **Prop N - Sketchbook C - Timed Recording**; Prop 37 retains **Prop 37 - Sketchbook C - Full Pilot**.
