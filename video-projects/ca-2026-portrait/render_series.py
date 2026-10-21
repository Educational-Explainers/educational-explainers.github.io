"""Render portrait projects, preserving the approved Prop 1 export."""
import pathlib,subprocess,os,concurrent.futures,time,json
root=pathlib.Path(__file__).resolve().parents[2];projects=list(sorted((root/'video-projects/ca-2026-portrait').glob('prop-*/project.json')));env=dict(os.environ,PYTHONPATH='/home/arvind/code/ampytech-video-gen-tools/src')
def one(p):
 if p.parent.name=='prop-01':return
 out=root/'.video-production/portrait'/p.parent.name;print('START',p.parent.name,flush=True)
 with (out/'render.log').open('w') as log:r=subprocess.run(['/tmp/ballot-video-env/bin/python','-m','ampy_video.sketchbook.portrait','--project',str(p),'--output',str(out),'--jobs','3'],env=env,stdout=log,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError(str(p)+': '+(out/'render.log').read_text()[-3000:])
 (p.parent/'validation.json').write_text((out/'validation.json').read_text());print('DONE',p.parent.name,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(one,projects))
print('ALL RENDERS COMPLETE',flush=True)
