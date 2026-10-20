"""Project-specific adaptation of the approved explainers to the shared sketchbook renderer."""
import json,math,shutil
from pathlib import Path
from ampy_video.sketchbook.engine import validate,text_layer,resolve_cue,asset_path,sha
root=Path(__file__).resolve().parents[2];projects=root/'video-projects/ca-2026';oldroot=root/'.video-production/explained-series'
shared=json.loads((projects/'shared-assets.json').read_text())['assets']
base37=json.loads((projects/'prop-37/project.json').read_text())

def txt(t,x,y,size=26,width=535,at=.2,**kw):return dict(kind='text',text=t,x=x,y=y,size=size,width=width,at=at,duration=.45,**kw)
def line(points,at=.5,duration=1,color='gold'):return dict(kind='stroke',paths=[points],at=at,duration=duration,hand=True,color=color,width=2.5)
def art(name,box=(55,200,565,405),at=0):return dict(kind='image',asset=name,box=list(box),at=at,duration=.85)
def icon(name,x,y,size=105,at=.3):return dict(kind='icon',icon=name,x=x,y=y,size=size,at=at,duration=1.2,color='teal',hand=True)
def choose_icon(label):
 t=label.lower()
 if any(x in t for x in ['home','hous','build','project']):return 'home'
 if any(x in t for x in ['voter','donor','candidate','support','patient','household']):return 'people'
 if any(x in t for x in ['year','203','204','deadline','timing','later','current','earlier']):return 'calendar'
 if any(x in t for x in ['money','fund','tax','revenu','repay','borrow','cost','debt','saving','income','$','budget']):return 'bank'
 if any(x in t for x in ['treatment','research','health','service']):return 'shield'
 return 'document'
def cards(items,asset,duration):
 out=[art(asset)]
 for i,item in enumerate(items):
  at=.35+i*max(.7,(duration-2)/max(1,len(items)));y=200+i*132
  e=txt(str(item),680,y,size=25 if len(str(item))>65 else 28,width=530,at=at);out.append(e);layer,_=text_layer(e)
  out.append(line([(680,y+layer.height+8),(1170,y+layer.height+8)],at=at+.5,duration=.75))
 return out

for folder in sorted(projects.glob('prop-*')):
 if folder.name=='prop-37':continue
 old=json.loads((folder/'storyboard-v3.json').read_text());record=json.loads((folder/'project.json').read_text());n=old['number'];words=json.loads((folder/'words-global.json').read_text())
 topic='construction' if n in [1,45] else 'medical' if n in [38,44] else 'civic' if n in [4,5,39,43] else 'budget'
 assets={k:v for k,v in base37['assets'].items() if k in ['hand','voter','construction','family']};assets.update(shared)
 if topic not in assets:continue
 scenes=[]
 for j,s in enumerate(old['shots']):
  kind=s['kind'];duration=s['frames']/30;items=s.get('items',[]);title=s['headline'];section=s['section'];els=[]
  source='Official voter guide / LAO · existing script checked '+old['checked']
  if kind=='art':
   a='voter' if title.lower().startswith('your question') else 'family' if n==1 and items==[0] else topic
   els=[art(a,(150,170,980,430))]
  elif kind=='flow':
   count=len(items);width=1080/count
   for i,item in enumerate(items):
    x=100+i*width;at=.3+i*(duration-2)/max(count,1)
    els.extend([icon(choose_icon(str(item)),x+width/2-55,240,110,at),txt(str(item),x,410,25,int(width-40),at+.5)])
   # A small topical vignette makes the conceptual diagram concrete.
   # Keep illustrated vignettes on their own shots, away from diagram labels.
  elif kind in ['cards']:
   a='voter' if 'case for' in title.lower() or 'your question' in title.lower() else topic
   els=cards(items,a,duration)
  elif kind in ['bars','split','poll']:
   vals=[float(v) for v in items];labels=s.get('labels') or [f'YES · {vals[0]:g}%',f'NO · {vals[1]:g}%',f'UNDECIDED · {vals[2]:g}%'];cols=['teal','coral','gold'] if kind=='poll' else ['teal','blue','gold']
   percent=kind in ['split','poll'] or any('%' in x or 'threshold' in title.lower() for x in labels);maximum=100 if percent else max(vals)
   if kind!='poll':els.append(art(topic,(55,215,380,360)))
   x=100 if kind=='poll' else 475;w=1080 if kind=='poll' else 710
   for i,(v,label) in enumerate(zip(vals,labels)):
    y=200+i*112;at=.5+i*max(1,(duration-3)/len(vals))
    els.extend([txt(label,x,y,25,w,at=at),dict(kind='bar',box=[x,y+66,w,25],value=v,maximum=maximum,color=cols[i%3],at=at+.4,duration=.9)])
   if kind=='poll':
    note=s.get('poll_note',old.get('polling_note','Dated survey snapshot'))
    if not isinstance(note,str):note='Dated survey snapshot'
    source=note[:160]
    els.append(txt('Dated survey snapshot, not votes cast. Rounded figures may not total 100%.',100,570,21,1080,at=min(duration-1,8)))
   elif kind=='split':els.append(txt('Shares of the stated total',475,570,21,700,color='muted'))
  elif kind=='formula':
   els=[art(topic,(50,200,430,390))]
   for i,item in enumerate(items):
    y=210+i*125;at=.4+i*(duration-2)/len(items);els.append(txt(str(item),520,y,31 if i<2 else 24,690,at=at,color='teal' if i==1 else 'ink',bold=i<2))
    if i==0:els.append(line([(520,290),(1180,290)],at=at+.8))
   source='Illustrative arithmetic, not a promised outcome · official analysis for policy details'
  elif kind=='match':
   els=[art('civic',(60,190,450,390)),txt('$20',560,215,48,650,color='gold'),txt('+ $40',560,305,48,650,at=3,color='blue'),line([(560,390),(1150,390)],at=5),txt('= $60',560,420,48,650,at=6,color='teal'),txt('Resident + public match = campaign funds',560,525,22,650,at=6.5)]
   source='Hypothetical matching example. Prop 4 does not set this matching rate.'
  elif kind=='threshold':
   els=[art('civic',(55,200,390,390)),txt('60 YES votes out of 100',490,190,32,720),dict(kind='bar',box=[490,270,690,45],value=60,maximum=100,color='teal',at=1,duration=1),line([(835,250),(835,335)],at=2,color='blue'),line([(950,250),(950,335)],at=3,color='coral'),txt('50%',795,345,22,130,at=2),txt('66⅔%',930,345,22,160,at=3),txt('Majority rule: passes',490,430,29,700,at=4,color='teal'),txt('Two-thirds rule: fails',490,500,29,700,at=6,color='coral')]
   source='Illustrative vote count: 60% is above 50% but below two-thirds'
  elif kind=='cta':
   els=[art(topic,(50,200,540,400)),txt('Read the explanation and sources',650,205,28,560),txt('Compare the trade-offs',650,315,28,560,at=2),line([(650,380),(1170,380)],at=3),txt('educational-explainers.github.io',600,455,25,650,at=1),txt('/ca-2026-ballot/',600,505,29,650,at=1,color='teal')]
   source='Visit the website and official voter guide before making your decision'
  else:raise ValueError(kind)
  # Words are authored script text; these anchors are descriptive, timing stays frame-exact.
  scene=dict(id=f'{j+1:02d}',title=title,chapter=section,start_frame=s['start_frame'],frames=s['frames'],source=source,elements=[txt(title,60,75,35,1160,at=0,serif=True)]+els)
  # Stable exact-ASR anchors support replacement narration retiming where possible.
  local=[w for w in words if w['start']>=s['start_frame']/30-.02 and w['start']<(s['start_frame']+s['frames'])/30]
  for length in [5,7,9]:
   phrase=' '.join(w['text'].strip() for w in local[:length])
   try:resolve_cue(words,phrase);scene['anchor']={'phrase':phrase};break
   except ValueError:pass
  if 'anchor' not in scene:raise ValueError('No unique cue '+folder.name+'/'+scene['id'])
  scenes.append(scene)
 project=dict(record,label=f'CALIFORNIA 2026 · PROP {n}',assets=assets,scenes=scenes,pencil_gain_db=16,captions_srt='captions.srt',captions_vtt='captions.vtt')
 project['title']=f'Prop {n} — '+old['title'];project.pop('basis',None)
 project['sources']=[{'name':x.get('name',x.get('use','Source')),'url':x['url']} for x in project['sources']]
 validate(project,folder)
 (folder/'project.json').write_text(json.dumps(project,indent=2)+'\n')
 (folder/'assets.lock.json').write_text(json.dumps([{'role':name,'path':a['path'],'sha256':sha(asset_path(project,folder,name))} for name,a in assets.items()],indent=2)+'\n')
 print(folder.name,len(scenes),'scenes',flush=True)
