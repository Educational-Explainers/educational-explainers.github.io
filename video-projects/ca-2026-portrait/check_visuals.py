"""Verify animation holds, caption bounds, source edits, and produce review sheets."""
import json,pathlib,math,hashlib
from PIL import Image,ImageDraw
from ampy_video.sketchbook.portrait import Renderer
ROOT=pathlib.Path(__file__).resolve().parents[2];BASE=ROOT/'video-projects/ca-2026-portrait';OUT=ROOT/'.video-production/portrait';reports=[];sheets=[]
for path in sorted(BASE.glob('prop-*/project.json')):
 p=json.loads(path.read_text());tiles=[]
 for s in p['scenes']:
  r=Renderer(p,path.parent,s);settle=math.ceil(max(e.get('at',0)+e.get('duration',.25) for e in s['elements'])*30);assert settle<s['frames'];frame=r.frame(settle)[0];assert frame==r.frame(s['frames']-1)[0],(path,s['id'],'hold');assert s['frames']==s['source_end_frame']-s['source_start_frame']
  for e in s['elements']:
   if e['kind'] in ['bar','timeline']:
    middle=round((e['at']+e['duration']/2)*30);assert r.frame(middle)[0]!=frame
  im=Image.frombytes('RGB',(1080,1920),frame);im.thumbnail((216,384));tile=Image.new('RGB',(216,415),'white');tile.paste(im);ImageDraw.Draw(tile).text((5,390),f"{s['label']} {s['frames']/30:.1f}s",fill='black');tiles.append(tile)
 sheet=Image.new('RGB',(216*8,415),'white')
 for ix,im in enumerate(tiles):sheet.paste(im,(216*ix,0))
 sheet.save(OUT/path.parent.name/'review-sheet.jpg');sheets.append(sheet)
 cues=json.loads((path.parent/'caption-cues.json').read_text());assert all(0<=c['start']<c['end']<=p['frames']/30 for c in cues);assert all(a['end']<=b['start']+.001 for a,b in zip(cues,cues[1:]));assert 'educational-explainers.github.io' in str(p['scenes'][-1]['elements'])
 reports.append(dict(project=path.parent.name,frames=p['frames'],seconds=p['frames']/30,animations_hold=True,animated_graphs_checked=True,caption_bounds=True,source_frame_lengths_match=True,website_on_closing_card=True))
for group in range(0,len(sheets),4):
 im=Image.new('RGB',(216*8,415*min(4,len(sheets)-group)),'white')
 for i,s in enumerate(sheets[group:group+4]):im.paste(s,(0,415*i))
 im.save(OUT/f'review-group-{group//4+1}.jpg')
(BASE/'visual-validation.json').write_text(json.dumps(reports,indent=2)+'\n');print('Verified',len(reports),'projects')
