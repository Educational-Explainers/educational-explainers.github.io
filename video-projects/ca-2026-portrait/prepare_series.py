"""Curated portrait edits of the existing human-narrated landscape series.
Run from the content repository with the shared tools on PYTHONPATH.
The approved Prop 1 pilot is preserved. No synthetic speech or speed changes.
"""
import json, pathlib, subprocess, wave, math, copy, hashlib
import numpy as np
from ampy_video.sketchbook.assets import ingest
from ampy_video.sketchbook.engine import resolve_path
from ampy_video.sketchbook.portrait import Renderer
ROOT=pathlib.Path(__file__).resolve().parents[2]
BASE=ROOT/'video-projects/ca-2026-portrait'
OUT=ROOT/'.video-production/portrait'
INK='#263d50';TEAL='#357f78';GOLD='#a67728';CORAL='#a35a43'
def shot(a,b,title,detail='',asset='civic',label='WHAT CHANGES',mode='picture',**kw):
 return dict(words=[a,b],title=title,detail=detail,asset=asset,label=label,mode=mode,**kw)
def yes(a,b,title,detail='',asset='family'):return shot(a,b,title,detail,asset,'WHY VOTE YES?')
def no(a,b,title,detail='',asset='budget'):return shot(a,b,title,detail,asset,'WHY VOTE NO?')
def decision(a,b,y,n):return shot(a,b,'What your\nvote means',label='YOUR VOTE',mode='decision',yes=y,no=n)
def cta(a,b):return shot(a,b,'',label='GO DEEPER',mode='cta')
SPECS={
2:[shot(0,9,'Save more for\nhard times?','California’s rainy-day fund','budget','THE QUESTION'),
 shot(44,77,'A larger\nreserve threshold','Share of General Fund tax revenues',mode='bars',bars=[['Current rule',10,100,'10%'],['Proposed rule',20,100,'20%']],bar_words=[57,68]),
 shot(78,92,'Room to save','The balance does not instantly double','budget','THE DISTINCTION'),
 shot(181,202,'Extra debt\npayments','Extend the requirement',mode='dates',dates=['2030','2040']),
 yes(248,265,'A stronger buffer','Protect services in a downturn','civic'),no(292,299,'Spend on needs\ntoday','Services and infrastructure now','construction'),
 decision(360,370,'Change reserve and debt-payment rules','Keep current rules'),cta(371,383)],
3:[shot(0,10,'Should higher\nrates expire?','Existing income-tax rates','budget','THE QUESTION'),
 shot(33,44,'Who pays?','Roughly the highest-earning 2%','voter','THE CURRENT RULE'),
 shot(65,72,'Temporary →\npermanent','Keep current higher rates beyond their sunset',mode='dates',dates=['After 2030','Permanent']),
 shot(145,173,'$5–15B / year','Estimated revenue maintained; high earners’ incomes vary','budget','THE ESTIMATE'),
 yes(249,268,'Keep revenue\nfor services','Education and other programs','civic'),no(296,315,'Honor the\nsunset','A small, volatile tax base','budget'),
 decision(395,406,'Make current higher rates permanent','Keep scheduled expiration'),cta(407,419)],
4:[shot(0,15,'Public funding\nfor campaigns?','California Proposition 4','voter','THE QUESTION'),
 shot(58,78,'Allow future\nprograms','No automatic program or payment',mode='flow',steps=['Governments get an option','Later decisions set programs']),
 shot(175,188,'Rules for\ncandidates','Broad district support + spending limits','voter','THE REQUIREMENTS'),
 shot(214,225,'A public cost','Campaign funds have other possible uses','budget','THE TRADEOFF'),
 yes(255,272,'Help candidates\ncompete','Community support without wealthy backers','voter'),no(301,324,'Should taxpayers\npay?','Including candidates they oppose','budget'),
 shot(344,353,'A NO vote','Keep the general ban and existing exceptions','civic','YOUR VOTE'),cta(421,432)],
5:[shot(0,27,'After a recall,\nwhat comes next?','The power to recall remains','voter','THE QUESTION'),
 shot(59,85,'One recall\nquestion','Remove the replacement contest',mode='flow',steps=['Vote on removal','Use vacancy procedures']),
 shot(136,160,'Replacement\nroutes differ','Legislators: generally a special election',mode='flow',steps=['Most other state offices','Governor appoints a replacement']),
 yes(247,266,'Decide removal\non its own','Avoid a low-support replacement winner','voter'),no(298,310,'Less direct\nchoice','Appointments and automatic succession','civic'),
 decision(368,380,'Change the replacement process','Keep the replacement question'),cta(381,393)],
37:[shot(0,11,'Help buying a\nnew home?','Loans for qualifying homes','family','THE QUESTION'),
 shot(29,58,'Another loan,\nnot free money','Up to $25B in revenue bonds',mode='flow',steps=['Bonds finance homebuyer loans','Buyers repay investors + administration']),
 shot(116,136,'Less cash\nat closing','Both the assistance loan and main mortgage remain','family','THE TRADEOFF'),
 yes(274,287,'Bridge the\nsavings gap','For households with adequate income','family'),no(319,335,'Could prices\nrise?','More buyers, constrained construction','construction'),
 decision(420,436,'Create the new loan program','Keep existing assistance options'),cta(437,449)],
38:[shot(0,15,'$8.4B for\nmedical research','Immunology + immunotherapy','medical','THE QUESTION'),
 shot(29,36,'Research takes\nrisks','No guaranteed new treatment','medical','THE DISTINCTION'),
 shot(117,144,'Two funding\nstreams','About half in each stream',mode='bars',bars=[['One selected institute',50,100,'≈50%'],['Competitive grants',50,100,'≈50%']],bar_words=[118,133]),
 shot(193,212,'$500–600M','Annual General Fund repayments',mode='years',years=20),
 yes(230,244,'Invest in\nlong-term research','Returns remain uncertain','medical'),no(277,296,'Debt and\nconcentration','Funding one institute before knowing results','budget'),
 decision(352,365,'Authorize this research bond','Reject this bond; existing research continues'),cta(366,378)],
39:[shot(0,18,'New ID checks\nwhen voting?','Citizenship is already required','voter','THE QUESTION'),
 shot(119,137,'In-person ID','Government-issued identification',mode='flow',steps=['Present government ID','Free voter ID card on request']),
 shot(229,240,'Proposed rules,\nnot instructions','Use official election guidance today','civic','IMPORTANT DISTINCTION'),
 yes(254,271,'Another layer\nof verification','Consistency and voter confidence','voter'),no(306,330,'Access and\npaperwork','A free card does not remove every burden','voter'),
 decision(443,453,'Add the proposed requirements','Keep current identification framework'),cta(454,466)],
40:[shot(0,9,'A one-time tax\non large fortunes','California Proposition 40','budget','THE QUESTION'),
 shot(37,72,'Up to 5%','Covered net worth; certain billionaires tied to Jan. 1, 2026 residency','budget','THE TAX'),
 shot(160,176,'Where revenue\nwould go','A one-time levy',mode='bars',bars=[['Health care',90,100,'90%'],['Other designated uses',10,100,'10%']],bar_words=[160,169]),
 shot(268,284,'Other measures\ncould block it','If a conflicting measure passes with more YES votes',mode='flow',steps=['Propositions 41 and 42','Legal interpretation may be needed']),
 yes(303,323,'Fund health care\nand other needs','Without broadly raising taxes','medical'),no(373,381,'Prefer recurring\nfunding','Fewer collection uncertainties','budget'),
 decision(490,504,'Adopt the tax, subject to legal outcome','Reject this one-time levy'),cta(505,517)],
41:[shot(0,9,'Audits +\nspending limits','Two parts to Proposition 41','civic','THE QUESTION'),
 shot(27,35,'Which taxes?','New or increased state special taxes','budget','THE SCOPE'),
 shot(149,178,'Find 10%\nin cost options','Identified savings are not guaranteed savings',mode='flow',steps=['Audit identifies possible reductions','Decisions determine actual savings']),
 shot(254,275,'A potential\nconflict','Could block Prop 40 if both pass and 41 gets more YES votes','civic','BEYOND AUDITS'),
 yes(276,291,'Evidence before\nnew taxes','Efficiency and regular follow-up','civic'),no(326,346,'Costs and\nfunding flexibility','Reviews even when measures never qualify','budget'),
 decision(426,436,'Add audits and spending-limit provisions','Keep current framework'),cta(437,449)],
42:[shot(0,5,'Restrict future\ntax options?','Asset ownership and retroactive taxes','budget','THE QUESTION'),
 shot(121,153,'Two proposed\nlimits','New state taxes',mode='flow',steps=['Ownership of personal / financial assets','Certain taxes applied retroactively']),
 shot(224,244,'A potential\nconflict','Could block Prop 40 if both pass and 42 gets more YES votes','civic','THE INTERACTION'),
 yes(256,274,'More predictable\nrules','Savings, investments and business assets','budget'),no(305,320,'Keep future\nchoices open','Decide tax proposals individually','voter'),
 decision(408,424,'Impose new limits','Keep current options; no new tax created'),cta(425,437)],
43:[shot(0,9,'Raise the hurdle\nfor local taxes?','California Proposition 43','civic','THE QUESTION'),
 shot(47,68,'Voter-proposed\nspecial taxes','Approval threshold',mode='bars',bars=[['Current: simple majority',50,100,'>50%'],['Proposed: two-thirds',100*2/3,100,'⅔']],bar_words=[55,63]),
 shot(156,178,'A future\nvoting hurdle','No new tax rate or blanket cancellation of existing taxes','voter','THE DISTINCTION'),
 yes(222,245,'Require broader\nagreement','Same hurdle for council or citizen proposals','voter'),no(274,294,'A majority may\nnot be enough','Services can lose funding despite majority support','civic'),
 decision(376,390,'Raise threshold to two-thirds','Retain the current majority route'),cta(391,403)],
44:[shot(0,18,'A spending rule\nfor clinics','Private nonprofit safety-net clinics','medical','THE QUESTION'),
 shot(35,60,'How revenue\nis spent','Covered clinics’ annual revenue',mode='bars',bars=[['Health care services: at least',90,100,'90%'],['Other expenses: at most',10,100,'10%']],bar_words=[45,55]),
 shot(128,157,'Penalty for\nfalling short','Temporary waivers in some cases',mode='flow',steps=['Penalty equals the shortfall','Recover it by complying within 5 years']),
 yes(240,261,'More revenue\nfor patients','Reporting and consequences','medical'),no(294,313,'Necessary support\ncosts matter','Fees and financial fragility','budget'),
 decision(368,382,'Adopt the spending rule','Keep existing requirements'),cta(383,395)],
45:[shot(0,8,'Faster review\nfor construction?','Eligible projects','construction','THE QUESTION'),
 shot(37,71,'An optional\nfaster route','Housing, transport, water, health and clean energy',mode='flow',steps=['Change deadlines and scope','Change review and litigation']),
 shot(153,160,'Not automatic\napproval','Missing a deadline does not approve a project','construction','THE DISTINCTION'),
 yes(269,286,'More predictable\nschedules','Homes and infrastructure sooner','construction'),no(316,331,'Less scope\nfor scrutiny','Alternatives, participation, courts and tribes','civic'),
 decision(390,402,'Create optional new procedures','Keep existing review and challenges'),cta(403,415)]
}
# VAD-checked lead-ins: retain 150 ms before the first spoken syllable.
ONSETS={2:3.62,3:3.434,37:3.402,38:3.402,40:3.338,41:3.37,43:3.37}
def txt(s,x=90,y=220,size=86,width=850,color=INK,bold=False,serif=False,at=0):return dict(kind='text',text=s,x=x,y=y,size=size,width=width,color=color,bold=bold,serif=serif,at=at,duration=.25)
def card(y,h=260,color='#ebe6da',at=0):return dict(kind='card',box=[90,y,850,h],color=color,at=at,duration=.25)
def image(a,box=[110,570,810,520]):return dict(kind='image',asset=a,box=box,at=0,duration=1.4,animation='fade-rise')
def line(a=[95,505],b=[925,505],at=.25):return dict(kind='line',points=[a,b],color=GOLD,width=5,at=at,duration=.65,hand=True)
def elements(spec,words,start,seconds):
 mode=spec['mode'];title=spec['title'];detail=spec['detail']
 if mode=='cta':return copy.deepcopy(json.loads((BASE/'prop-01/project.json').read_text())['scenes'][-1]['elements'])
 if mode=='decision':
  return [txt(title,serif=True),card(550,310,'#e0e9e0'),txt('YES',125,580,84,760,TEAL,True),txt(spec['yes'],125,705,44,760),card(915,375,'#eee0d5',2),txt('NO',125,945,84,760,CORAL,True,at=2),txt(spec['no'],125,1070,44,760,at=2)]
 result=[txt(title,serif=True),line()]
 if mode=='picture':return result+[image(spec['asset']),card(1140,210),txt(detail,120,1180,43,790,TEAL,True)]
 if mode=='flow':
  return result+[card(565,240),txt(spec['steps'][0],125,610,48,760),line([515,825],[515,900],1.3),card(925,240,at=1.9),txt(spec['steps'][1],125,970,48,760,at=1.9),txt(detail,95,1230,35,850,TEAL)]
 if mode=='bars':
  for k,(label,value,maximum,big) in enumerate(spec['bars']):
   y=555+k*310;at=min(max(.35,words[spec['bar_words'][k]]['start']-start-.2),seconds-1.6)
   result += [card(y,280,at=max(0,at-.2)),txt(big,125,y+15,90,760,TEAL if k==0 else GOLD,True,at=max(0,at-.2)),txt(label,125,y+140,34,760,at=max(0,at-.2)),dict(kind='bar',box=[125,y+230,780,20],value=value,maximum=maximum,color=TEAL if k==0 else GOLD,at=at,duration=1.1)]
  return result+[txt(detail,95,1230,36)]
 if mode=='dates':return result+[card(555,620),txt(spec['dates'][0],125,595,78,760,TEAL,True),line([155,780],[865,780],1.2),txt(spec['dates'][1],125,900,78,760,TEAL,True,at=2),txt(detail,95,1230,38)]
 if mode=='years':return result+[txt(detail,95,555,48),txt('≈'+str(spec['years'])+' years',120,730,100,780,TEAL,True),dict(kind='timeline',box=[120,920,780,45],ticks=spec['years'],color=TEAL,at=max(.5,seconds-2.4),duration=1.5),image('medical',[220,1030,580,320])]
 raise ValueError(mode)
def stamp(t,sep):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}{sep}{ms%1000:03}'
def prepare():
 reports=[]
 for number,specs in SPECS.items():
  name=f'prop-{number:02}';base=ROOT/'video-projects/ca-2026'/name;dest=BASE/name;out=OUT/name;dest.mkdir(parents=True,exist_ok=True);out.mkdir(parents=True,exist_ok=True)
  long=json.loads((base/'project.json').read_text());words=json.loads((base/'words-human.json').read_text());source=resolve_path(base,long['narration']);pcm=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(source),'-ar','24000','-ac','1','-f','f32le','-']),dtype='<f4')
  locked=json.loads((BASE/'source-lock.json').read_text())[name]
  assert long['narration']==locked['narration'] and long['recording']['take_id']==locked['take_id'], 'Source take changed; review the edit recipe first'
  assert hashlib.sha256((base/'words-human.json').read_bytes()).hexdigest()==locked['words_sha256'], 'Source word indices changed; review the edit recipe first'
  corrections=json.loads((BASE/'opening-timing-corrections.json').read_text()).get(str(number),[])
  for i,c in enumerate(corrections):
   words[i]['start']=max(c['start'],ONSETS.get(number,0) if i==0 else 0);words[i]['end']=min(c['end'],words[i+1]['start']) if i==1 else c['end']
  scenes=[];audio=[];shortwords=[];offset=0;cues=[]
  for ix,spec in enumerate(specs):
   i,j=spec['words'];a=words[i]['start'];b=words[j]['end']
   if i==0:a=max(a,ONSETS.get(number,0))
   # Midpoints keep neighboring, unselected speech out of the short.
   a=max(0,a-.12,(words[i-1]['end']+a)/2 if i else 0);b=min(len(pcm)/24000,b+.14,(b+words[j+1]['start'])/2 if j+1<len(words) else len(pcm)/24000)
   start=max(0,math.floor(a*30));end=math.ceil(b*30)
   # Move energetic edit boundaries into the nearby pause, without entering
   # an adjacent sentence. Keep quiet boundaries and the approved speech intact.
   def energy(frame):
    center=frame*800;v=pcm[max(0,center-240):min(len(pcm),center+240)]
    return float(np.mean(v*v)) if len(v) else 0
   if energy(start)>10**(-38/10):
    lower=max(0,start-12,math.ceil((words[i-1]['end']+.04)*30) if i else 0)
    if lower<start:start=min(range(lower,start+1),key=energy)
   if energy(end)>10**(-38/10):
    upper=min(len(pcm)//800,end+12,math.floor((words[j+1]['start']-.04)*30) if j+1<len(words) else len(pcm)//800)
    if upper>end:end=min(range(end,upper+1),key=energy)
   frames=end-start;chunk=pcm[start*800:end*800].copy();assert len(chunk)==frames*800
   chunk[:72]*=np.linspace(0,1,72);chunk[-72:]*=np.linspace(1,0,72);audio.append(chunk);selected=[]
   for w in words[i:j+1]:
    t=dict(text=w['text'],start=max(0,w['start']-start/30)+offset/30,end=min(frames/30,max(0,w['end']-start/30))+offset/30);assert t['end']>=t['start'];selected.append(t);shortwords.append(t)
   scene=dict(id=f'{ix+1:02}-{spec["mode"]}',label=spec['label'],start_frame=offset,frames=frames,source_start_frame=start,source_end_frame=end,source_word_range=[i,j],narration=' '.join(w['text'] for w in words[i:j+1]),elements=elements(spec,words,start/30,frames/30));scenes.append(scene);offset+=frames
   # Caption groups never cross a speech edit or scene cut.
   group=[]
   for w in selected:
    if group and (w['start']-group[-1]['end']>.45 or len(' '.join(x['text'] for x in group))+len(w['text'])>58):
     cues.append(dict(start=group[0]['start'],end=group[-1]['end'],text=' '.join(x['text'] for x in group)));group=[]
    group.append(w)
    if len(group)>=8 or w['text'].endswith(('.', '?','!')):cues.append(dict(start=group[0]['start'],end=group[-1]['end'],text=' '.join(x['text'] for x in group)));group=[]
   if group:cues.append(dict(start=group[0]['start'],end=group[-1]['end'],text=' '.join(x['text'] for x in group)))
  print(name,round(offset/30,3),flush=True);assert offset<1800,(name,offset/30)
  with wave.open(str(out/'narration.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000);w.writeframes((np.clip(np.concatenate(audio),-1,1)*32767).astype('<i2').tobytes())
  p=dict(schema_version=1,format='portrait-short',number=number,title=long['title'],width=1080,height=1920,fps=30,frames=offset,checked=long['checked'],source_project=f'../../ca-2026/{name}/project.json',source_narration=long['narration'],source_take=long['recording']['take_id'],narration=ingest(out/'narration.wav'),assets=long['assets'],sources=long['sources'],scenes=scenes,caption_words='words.json',captions_srt='captions.srt',captions_vtt='captions.vtt',website='https://educational-explainers.github.io/ca-2026-ballot/',editorial_note='Short teaser cut from complete passages of the existing cleaned human recording at natural speed. Polling and additional detail remain in the full explainer. Original source-check date retained; no new factual review.',audio_edits={'boundary_taper_ms':3,'speed':1.0},safe_area={'left':90,'right':140,'top':120,'bottom':240})
  for s in scenes:
   Renderer(p,dest,s);assert max(e.get('at',0)+e.get('duration',.25) for e in s['elements'])<s['frames']/30
  for file,obj in [('project.json',p),('words.json',shortwords),('caption-cues.json',cues)]: (dest/file).write_text(json.dumps(obj,indent=2)+'\n')
  for ext,sep in [('srt',','),('vtt','.')]:
   entries=['WEBVTT\n'] if ext=='vtt' else []
   for ix,c in enumerate(cues):entries.append(f"{ix+1}\n{stamp(c['start'],sep)} --> {stamp(c['end'],sep)}\n{c['text']}\n")
   (dest/f'captions.{ext}').write_text('\n'.join(entries))
  reports.append(dict(project=name,seconds=offset/30,scenes=len(scenes),words=len(shortwords),source_take=p['source_take']))
 (BASE/'preparation-validation.json').write_text(json.dumps(reports,indent=2)+'\n')
if __name__=='__main__':prepare()
