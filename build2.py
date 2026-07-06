import base64, pathlib, json, glob, re
UP = pathlib.Path("/home/claude/fonts")
fd_reg = base64.b64encode((UP/"FUTURADEMIC.OTF").read_bytes()).decode()
fd_ita = base64.b64encode((UP/"FUTURADEMIC-ITALIC.OTF").read_bytes()).decode()
hero_jpg = base64.b64encode(pathlib.Path("/home/claude/hero.jpg").read_bytes()).decode()
band_jpg = base64.b64encode(pathlib.Path("/home/claude/band.jpg").read_bytes()).decode()
_pp={}
for _f in sorted(glob.glob("/home/claude/pp/*.jpg")):
    _pid,_n=pathlib.Path(_f).stem.split("_")
    _pp.setdefault(_pid, []).append((int(_n), _f))
PHOTOS={pid:["data:image/jpeg;base64,"+base64.b64encode(pathlib.Path(fp).read_bytes()).decode() for _,fp in sorted(lst)] for pid,lst in _pp.items()}
PIMG = {k: "data:image/jpeg;base64,"+base64.b64encode(pathlib.Path(f"/home/claude/v_{k}.jpg").read_bytes()).decode() for k in ["tus","sok","act","eat","drink","cult"]}
AVA = {name: "data:image/jpeg;base64,"+base64.b64encode(pathlib.Path(f"/home/claude/hero_{key}.jpg").read_bytes()).decode() for name,key in {"Настя":"nastya","Женя":"zhenya","Лиза":"liza"}.items()}

HTML = r"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<title>Нишевая карта Петербурга — тайми</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
@font-face{font-family:'Futura Demic';font-style:normal;font-weight:400;font-display:swap;src:url(data:font/otf;base64,__FD_REG__) format('opentype');}
@font-face{font-family:'Futura Demic';font-style:italic;font-weight:400;font-display:swap;src:url(data:font/otf;base64,__FD_ITA__) format('opentype');}
:root{
  --paper:#FFF6F6; --card:#ffffff; --ink:#181513; --ink2:#736a65; --ink3:#a89f9a;
  --line:rgba(24,21,19,.13); --line2:rgba(24,21,19,.07);
  --pink:#FF2E84; --orange:#FF8B33; --tintp:#FFE7F0; --tinto:#FFEAD7;
  --disp:'Unbounded',system-ui,sans-serif;
  --body:'Futura Demic','Helvetica Neue',Helvetica,Arial,sans-serif;
  --mono:'Space Mono',ui-monospace,monospace;
  --sh:0 18px 50px -24px rgba(24,21,19,.28);
}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.45;overflow-x:hidden}
.wrap{max-width:1140px;margin:0 auto;padding:0 22px}
a{color:inherit;text-decoration:none}
.mono{font-family:var(--mono)}
img{display:block;max-width:100%}

/* nav — frosted iOS */
.nav{position:sticky;top:0;z-index:40;backdrop-filter:saturate(1.4) blur(18px);background:rgba(255,246,246,.72);border-bottom:1px solid var(--line2)}
.nav .wrap{display:flex;align-items:center;gap:14px;height:60px}
.logo{font-family:var(--disp);font-weight:800;font-size:22px;letter-spacing:-.01em}
.nav .sp{flex:1}
.nav .lab{font-family:var(--mono);font-size:12px;color:var(--ink2)}
.btn{font-family:var(--mono);font-weight:700;font-size:13px;cursor:pointer;border:none;padding:11px 18px;border-radius:999px;color:#fff;background:var(--pink);transition:transform .12s,filter .2s;box-shadow:0 10px 24px -12px rgba(255,46,132,.5)}
.btn:hover{transform:translateY(-1px);filter:brightness(1.05)}
.btn.sm{padding:9px 15px;font-size:12px}
.btn.ghost{background:#fff;color:var(--ink);border:1px solid var(--line);box-shadow:none}
.btn.ghost:hover{border-color:var(--ink)}
.navtag{position:relative;font-family:var(--body);font-weight:700;font-size:13px;letter-spacing:.01em;cursor:pointer;border:none;padding:6px 17px;border-radius:0;color:var(--pink);background:rgba(255,46,132,.20);transition:background .2s}
.navtag:hover{background:rgba(255,46,132,.32)}
.navtag .bar{position:absolute;top:3px;bottom:3px;width:2.5px;background:var(--pink);border-radius:2px}
.navtag .bar.l{left:-1px}.navtag .bar.r{right:-1px}
.navtag .bar::after{content:"";position:absolute;left:50%;transform:translateX(-50%);width:8px;height:8px;border-radius:50%;background:var(--pink)}
.navtag .bar.l::after{top:-5px}.navtag .bar.r::after{bottom:-5px}

/* ── HERO : poster ────────────────────────── */
.poster{position:relative;width:100%;min-height:min(94vh,860px);overflow:hidden;background:#c9c9c9;
  --poster:#FF2E84; --ac:#FF8B33}
.poster .bgimg{position:absolute;inset:0;background:url(data:image/jpeg;base64,__HERO__) center 38%/cover no-repeat}
.poster .pe{position:absolute;z-index:4;font-family:var(--mono);font-size:clamp(10px,1.25vw,13px);
  color:var(--poster);letter-spacing:.02em;text-transform:lowercase;line-height:1.5}
.pe-tl{top:74px;left:24px}
.pe-tr{top:74px;right:24px;text-align:right}
.pe-bl{right:24px;bottom:26px;color:#fff;text-align:right}
.poster .star{position:absolute;top:118px;right:26px;width:40px;height:40px;color:var(--poster);z-index:4}
.poster .plus{position:absolute;z-index:4;font-family:var(--disp);font-weight:700;line-height:1;
  font-size:clamp(18px,2.6vw,30px);color:var(--poster)}
.plus.a{top:30%;left:2.4%}.plus.b{bottom:30%;right:6%;color:var(--ac)}
.ptitle{position:absolute;inset:0;margin:0;z-index:5}
.ptitle .w{position:absolute;font-family:var(--disp);font-weight:900;color:var(--poster);
  letter-spacing:-.025em;line-height:.84;text-transform:uppercase;text-shadow:0 2px 24px rgba(20,18,17,.18)}
.w1{top:8%;left:3.5%;font-size:clamp(36px,11.4vw,178px)}
.w2{top:31%;right:5%;font-size:clamp(30px,7vw,90px)}
.w3{bottom:19%;left:2.6%;font-size:clamp(36px,11.4vw,178px)}
.w3 .ast{color:var(--ac);-webkit-text-stroke:0}
.psub{position:absolute;left:3.6%;bottom:8%;max-width:30ch;z-index:5;margin:0;
  font-family:var(--body);font-weight:400;font-size:clamp(18px,2.6vw,28px);color:#fff;line-height:1.3;
  text-shadow:0 2px 6px rgba(20,18,17,.7),0 1px 22px rgba(20,18,17,.55)}
.psub b{color:var(--poster);font-weight:700}
@media(max-width:720px){
  .poster{min-height:88vh}
  .poster .bgimg{background-position:center 32%}
  .w1{top:11%;left:5%}.w2{top:30%;right:auto;left:5%}
  .w3{bottom:28%;left:4%}
  .psub{left:5%;bottom:7%;max-width:90%}
  .plus.b{right:8%}
}

/* photo placeholder */
.ph{position:relative;border-radius:14px;overflow:hidden;background:#FCE3EC;border:1px solid var(--line2)}
.ph.v2{background:#FFE7D6}
.ph.v3{background:#FFEFF4}
.ph::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(24,21,19,.07) 1px,transparent 1.4px);background-size:8px 8px;opacity:.6}
.ph .sil{position:absolute;inset:0;display:grid;place-items:center;color:rgba(24,21,19,.16)}
.ph .cap{position:absolute;left:8px;right:8px;bottom:8px;width:auto;max-width:calc(100% - 16px);box-sizing:border-box;font-family:var(--mono);font-size:10.5px;color:var(--ink2);background:rgba(255,255,255,.82);padding:3px 7px;border-radius:6px;white-space:normal;line-height:1.35}
.ph .lens{position:absolute;right:8px;top:8px;width:14px;height:14px;border-radius:50%;border:1.5px solid rgba(24,21,19,.3)}


/* ── verbs block (typographic filter) ─────── */
.verbs{font-family:var(--body);font-weight:400;font-size:clamp(20px,3.2vw,40px);line-height:1.5;letter-spacing:0;margin-top:14px;color:var(--ink)}
.verb{position:relative;display:inline-block;cursor:pointer;margin:.06em .34em;vertical-align:baseline;white-space:nowrap;
  transition:color .3s ease}
.verb .hl{position:absolute;inset:0 -5px;border-radius:0;background:rgba(255,46,132,.22);opacity:0;transform:scale(.97);
  transition:opacity .4s cubic-bezier(.16,1,.3,1),transform .4s cubic-bezier(.16,1,.3,1);z-index:-1}
.verb .hl .bar{position:absolute;top:0;bottom:0;width:2.5px;background:var(--pink);border-radius:2px}
.verb .hl .bar.l{left:-5px}.verb .hl .bar.r{right:-5px}
.verb .hl .bar::after{content:"";position:absolute;left:50%;transform:translateX(-50%);width:9px;height:9px;border-radius:50%;background:var(--pink);box-shadow:0 1px 4px rgba(255,46,132,.5)}
.verb .hl .bar.l::after{top:-6px}.verb .hl .bar.r::after{bottom:-6px}
.verb:hover{color:var(--pink)}
.verb.active{font-style:italic;color:var(--pink)}
.verb.active .hl{opacity:1;transform:scale(1)}
.vtile{display:inline-block;vertical-align:middle;height:clamp(32px,4.2vw,50px);width:auto;aspect-ratio:16/10;
  object-fit:cover;border-radius:0;margin:0 .3em;cursor:pointer;box-shadow:0 9px 24px -12px rgba(24,21,19,.55)}
@media(prefers-reduced-motion:reduce){.verb{transition:none}}

/* ── MAP : ios app card ───────────────────── */
.maphead{padding:46px 0 0}
.h2{font-family:var(--disp);font-weight:900;font-size:clamp(26px,4vw,42px);letter-spacing:-.02em;line-height:1.08;margin:0}
.sub{color:var(--ink2);max-width:52ch;margin:12px 0 0;font-size:15.5px}
.seg{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 6px}
.chip{font-family:var(--mono);font-size:12.5px;cursor:pointer;border:1px solid var(--line);background:#fff;color:var(--ink2);padding:9px 14px;border-radius:999px;transition:.16s;user-select:none;display:flex;gap:6px;align-items:center}
.chip:hover{color:var(--ink);border-color:var(--line)}

.appcard{margin-top:16px;background:var(--card);border:1px solid var(--line);border-radius:26px;overflow:hidden;box-shadow:var(--sh)}
.iosbar{display:flex;align-items:center;justify-content:space-between;padding:10px 18px;font-family:var(--mono);font-size:13px;color:var(--ink);border-bottom:1px solid var(--line2)}
.iosbar--plain{justify-content:center;font-weight:700;letter-spacing:.02em}
.iosbar .r{display:flex;align-items:center;gap:7px;color:var(--ink2)}
.iosbar .bat{width:22px;height:11px;border:1.4px solid var(--ink2);border-radius:3px;position:relative;padding:1px}
.iosbar .bat::after{content:"";position:absolute;right:-3px;top:3px;width:2px;height:5px;background:var(--ink2);border-radius:0 1px 1px 0}
.iosbar .bat i{display:block;height:100%;width:78%;background:var(--orange);border-radius:1px}
.maptop{display:flex;align-items:center;justify-content:space-between;padding:10px 18px;font-family:var(--mono);font-size:12px;color:var(--ink2)}
.maptop b{color:var(--pink)}
.map{position:relative;width:100%;aspect-ratio:16/9;min-height:320px}
.map svg.bg{position:absolute;inset:0;width:100%;height:100%}
.scan{position:absolute;left:0;top:0;width:100%;height:2px;z-index:6;pointer-events:none;background:var(--orange);opacity:0;box-shadow:0 0 16px var(--orange)}
.scan.run{animation:scan 1.4s cubic-bezier(.4,0,.2,1)}
@keyframes scan{0%{top:0;opacity:0}12%{opacity:.85}88%{opacity:.85}100%{top:100%;opacity:0}}
.det{position:absolute;transform:translate(-50%,-50%);z-index:8;cursor:pointer}
.det .box{position:relative;width:50px;height:40px;border:1.5px solid var(--pink);border-radius:4px;transition:.25s;background:rgba(255,255,255,.35)}
.det .box::before,.det .box::after{content:"";position:absolute;width:8px;height:8px;border:2px solid var(--ink);opacity:.7}
.det .box::before{left:-2px;top:-2px;border-right:0;border-bottom:0}
.det .box::after{right:-2px;bottom:-2px;border-left:0;border-top:0}
.det .pin{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:16px}
.det .tag{position:absolute;left:50%;top:calc(100% + 6px);transform:translateX(-50%);white-space:nowrap;max-width:min(46vw,220px);overflow:hidden;text-overflow:ellipsis;font-family:var(--mono);font-size:10.5px;color:var(--ink);background:#fff;border:1px solid var(--line);padding:3px 8px;border-radius:7px;box-shadow:0 8px 18px -10px rgba(24,21,19,.4);line-height:1.3}
.det .tag b{font-weight:700;color:var(--pink)}
.det:hover{z-index:12}
.det:hover .box{border-color:var(--ink);box-shadow:0 0 0 4px rgba(255,46,132,.18)}
.det.match .box{border-color:var(--orange);box-shadow:0 0 0 5px rgba(255,139,51,.16)}
.det.match .tag b{color:var(--orange)}
.det.dim{opacity:.32;filter:grayscale(.55)}
.det.dim .tag{display:none}
.det.pop{animation:pop .42s cubic-bezier(.2,1.3,.5,1) both}
@keyframes pop{from{opacity:0;transform:translate(-50%,-50%) scale(.6)}to{opacity:1;transform:translate(-50%,-50%) scale(1)}}

/* ── window (light app) ───────────────────── */
.scrim{position:fixed;inset:0;background:rgba(24,21,19,.34);backdrop-filter:blur(2px);z-index:55;display:none}
.scrim.open{display:block}
.win{position:fixed;z-index:60;width:min(430px,92vw);max-height:86vh;background:var(--card);border:1px solid var(--line);border-radius:22px;overflow:hidden;box-shadow:0 50px 100px -30px rgba(24,21,19,.5);display:none;flex-direction:column;left:50%;top:50%;transform:translate(-50%,-50%)}
.win.open{display:flex;animation:wi .26s cubic-bezier(.2,1,.4,1)}
@keyframes wi{from{opacity:0;transform:translate(-50%,-46%) scale(.97)}to{opacity:1;transform:translate(-50%,-50%) scale(1)}}
.win .head{display:flex;align-items:center;gap:9px;padding:11px 14px;cursor:grab;background:#fff;border-bottom:1px solid var(--line2);font-family:var(--mono);font-size:11px;color:var(--ink2);flex:none}
.win .head:active{cursor:grabbing}
.win .dots{display:flex;gap:6px}.win .dots i{width:11px;height:11px;border-radius:50%;display:block}
.win .dots i:nth-child(1){background:var(--orange)}.win .dots i:nth-child(2){background:var(--pink)}.win .dots i:nth-child(3){background:var(--line)}
.win .x{margin-left:auto;cursor:pointer;font-size:14px;color:var(--ink2);padding:4px 6px;position:relative;z-index:2}.win .x:hover{color:var(--ink)}
.win .body{padding:16px 18px 20px;overflow-y:auto;flex:1;min-height:0;-webkit-overflow-scrolling:touch}
.win .ttl{font-family:var(--disp);font-weight:700;font-size:24px;letter-spacing:-.01em}
.win .meta{font-family:var(--mono);font-size:11.5px;color:var(--pink);margin-top:3px}
.gal{display:grid;grid-template-columns:2fr 1fr;grid-template-rows:1fr 1fr;gap:7px;height:200px;margin:14px 0 4px}
.gal .ph:first-child{grid-row:1/3}
.gal .ph{height:100%}
.galcap{font-family:var(--mono);font-size:10.5px;color:var(--ink3);margin-bottom:12px}
.who{display:flex;align-items:center;gap:11px;margin:12px 0 4px}
.av{width:46px;height:46px;border-radius:50%;flex:none;overflow:hidden;border:2px solid #fff;box-shadow:0 6px 16px -8px rgba(24,21,19,.4),0 0 0 1px var(--line)}
.av img{width:100%;height:100%;object-fit:cover;display:block}
.who .nm{font-size:14.5px}.who .nm b{font-weight:400}.who .rl{font-size:12.5px;color:var(--ink2)}
.atags{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}
.atag{font-family:var(--mono);font-size:11px;color:var(--ink2);background:var(--tintp);border-radius:999px;padding:4px 10px}
.fit{border-top:1px solid var(--line2);padding-top:12px;font-size:13.5px;color:var(--ink2);display:flex;gap:9px}
.fit b{font-family:var(--mono);font-size:11px;color:var(--ink);background:var(--tinto);padding:3px 8px;border-radius:6px;height:fit-content;flex:none}

/* ── manifesto band ───────────────────────── */
.band{position:relative;margin:0;border-radius:26px;overflow:hidden;min-height:420px;display:flex;align-items:flex-end;box-shadow:var(--sh)}
.band .ph{position:absolute;inset:0;border-radius:0;border:0}
.band .ph::before{opacity:.45}
.band .txt{position:relative;z-index:2;padding:38px 34px}
.band h3{font-family:var(--disp);font-weight:800;letter-spacing:-.02em;line-height:.98;font-size:clamp(30px,6vw,68px);margin:0;color:var(--ink);max-width:16ch}
.band h3 em{font-style:italic;font-family:var(--body);font-weight:400;color:var(--orange)}
.band p{margin:14px 0 0;max-width:48ch;color:var(--ink);font-size:15px}
.bmeta{position:absolute;top:22px;left:26px;right:26px;z-index:2;display:flex;justify-content:space-between;font-family:var(--mono);font-size:11.5px;color:var(--ink2)}

/* ── places gallery ───────────────────────── */
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:30px}
.pc{background:var(--card);border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--sh);cursor:pointer;transition:.2s;display:flex;flex-direction:column}
.pc:hover{transform:translateY(-4px)}
.pc .gallery{display:grid;grid-template-columns:2fr 1fr;grid-template-rows:150px;gap:4px;height:150px;overflow:hidden}
.pc .gallery .ph{border-radius:0;border:0;height:100%;min-height:0}
.pc .gallery .col{display:grid;grid-template-rows:1fr 1fr;gap:4px;min-height:0}
.pc .info{padding:15px 16px 17px}
.pc .top{display:flex;align-items:center;gap:10px}
.pc .av{width:38px;height:38px}
.pc .pn{font-family:var(--disp);font-weight:600;font-size:17px;letter-spacing:-.01em;margin-top:11px}
.pc .pm{font-family:var(--mono);font-size:11px;color:var(--ink2);margin-top:2px}
.pc .pw{font-size:13px;color:var(--ink2);margin-top:9px}
.pc .pw b{color:var(--ink);font-weight:400}

/* ── CTA ──────────────────────────────────── */
.cta{position:relative;border-radius:26px;overflow:hidden;background:#FFE9F0;border:1px solid var(--line);box-shadow:var(--sh)}
.cta .inner{padding:46px 40px}
.cta h2{font-family:var(--disp);font-weight:900;text-transform:uppercase;font-size:clamp(30px,5.2vw,56px);letter-spacing:-.02em;margin:0;max-width:20ch;line-height:1.08}
.cta p{color:var(--ink2);max-width:46ch;margin:16px 0 0;font-size:15.5px}
.form{display:flex;gap:10px;margin:24px 0 0;max-width:440px;flex-wrap:wrap}
.form input{flex:1;min-width:0;font-family:var(--mono);font-size:14px;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:999px;padding:13px 18px}
.form input::placeholder{color:var(--ink3)}
.form input:focus{outline:none;border-color:var(--pink)}
.share{margin-top:16px;font-family:var(--mono);font-size:13px;color:var(--orange);cursor:pointer;display:inline-block}
.share:hover{text-decoration:underline}
.done{font-family:var(--mono);font-size:13px;color:var(--ink);margin-top:14px;display:none}
.done.show{display:block}
.ctlist{list-style:none;counter-reset:c;padding:0;margin:22px 0 0;max-width:54ch;display:grid;gap:15px}
.ctlist li{counter-increment:c;position:relative;padding-left:40px;color:var(--ink);font-size:16px;line-height:1.55}
.ctlist li::before{content:counter(c);position:absolute;left:0;top:-1px;width:27px;height:27px;border-radius:50%;background:var(--pink);color:#fff;font-family:var(--mono);font-weight:700;font-size:12px;display:grid;place-items:center}
.ctlist li span{color:var(--pink)}
.ctabtn{display:inline-block;margin-top:26px;font-family:var(--body);font-weight:400;font-size:16px;color:#fff;background:var(--pink);padding:14px 26px;border-radius:999px;text-decoration:none;box-shadow:0 12px 26px -12px rgba(255,46,132,.6);transition:transform .12s,filter .2s;border:none;outline:none;appearance:none;-webkit-appearance:none}
.ctabtn:hover{transform:translateY(-1px);filter:brightness(1.06)}

.vh{text-transform:uppercase;color:var(--pink);font-size:clamp(30px,5.4vw,60px)}
section{padding:60px 0}
#mapsec,#cta{scroll-margin-top:80px}
footer{border-top:1px solid var(--line);padding:28px 0 54px;color:var(--ink3);font-family:var(--mono);font-size:11.5px}
footer .wrap{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}

@media(max-width:860px){.grid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){
  .grid{grid-template-columns:1fr}
  .map{aspect-ratio:3/4}
  .det .tag{font-size:9px;padding:2px 6px}
  .det .tag .tsep{display:none}
  .det .box{width:42px;height:34px}
  .nav .lab{display:none}
  .cta .inner{padding:34px 22px}
  .band .txt{padding:26px 22px}
}
@media(prefers-reduced-motion:reduce){.scan,.det.pop{animation:none!important}}

/* ── places heading / add btn ─────────────── */
.hcaps{text-transform:uppercase;font-size:clamp(30px,5.4vw,60px)}
.addbtn{margin-top:8px}
/* ── manifesto band (photo poster) ────────── */
.mband{position:relative;margin:0;border-radius:0;overflow:hidden;min-height:clamp(400px,50vw,560px);box-shadow:var(--sh)}
.mband .bgimg2{position:absolute;inset:0;background:url(data:image/jpeg;base64,__BAND__) center 42%/cover}
.mband .bmeta{position:absolute;top:20px;left:24px;right:24px;z-index:3;display:flex;justify-content:space-between;font-family:var(--mono);font-size:11.5px;color:#fff;text-shadow:0 1px 8px rgba(0,0,0,.55)}
.mbtitle{position:absolute;inset:0;margin:0;z-index:3}
.mbtitle .mw{position:absolute;font-family:var(--disp);font-weight:900;color:var(--pink);text-transform:uppercase;letter-spacing:-.02em;line-height:.9;text-shadow:0 1px 3px rgba(0,0,0,.28)}
.m1{top:14%;left:3.5%;font-size:clamp(27px,5.6vw,64px)}
.m2{top:30%;left:13.5%;font-size:clamp(27px,5.6vw,64px)}
.m3{top:46%;left:23.5%;font-size:clamp(27px,5.6vw,64px)}
.morange{color:var(--orange)}
.mbtitle .mw.morange{color:var(--orange)}
.mbsub{position:absolute;left:3.5%;right:6%;bottom:7%;max-width:52ch;z-index:3;margin:0;font-family:var(--body);font-size:clamp(17px,2.3vw,25px);color:#fff;line-height:1.4;text-shadow:0 1px 10px rgba(0,0,0,.65)}
.mbsub em{font-style:italic;color:#fff;font-weight:400}
@media(max-width:720px){
  .mband{min-height:540px}
  .m1{top:11%;left:5%}.m2{top:25%;left:15%}.m3{top:39%;left:25%}
  .mbsub{left:5%;right:5%;bottom:6%}
}
/* ── add-place modal ──────────────────────── */
.scrim2{position:fixed;inset:0;background:rgba(24,21,19,.34);backdrop-filter:blur(2px);z-index:65;display:none}
.scrim2.open{display:block}
.addwin{position:fixed;z-index:70;width:min(400px,92vw);max-height:86vh;background:var(--card);border:1px solid var(--line);border-radius:22px;overflow:hidden;box-shadow:0 50px 100px -30px rgba(24,21,19,.5);display:none;flex-direction:column;left:50%;top:50%;transform:translate(-50%,-50%)}
.addwin.open{display:flex;animation:wi .26s cubic-bezier(.2,1,.4,1)}
.addwin .head{display:flex;align-items:center;padding:15px 18px;border-bottom:1px solid var(--line2);font-family:var(--disp);font-weight:900;font-size:16px;text-transform:uppercase;letter-spacing:.02em;flex:none}
.addwin .head .x{margin-left:auto;cursor:pointer;color:var(--ink2);font-size:15px}
.addwin .body{padding:16px 18px 20px;overflow-y:auto;flex:1;min-height:0;-webkit-overflow-scrolling:touch}
.addwin .ctabtn{margin-top:18px}

/* ── dense map (34 pins): tags on hover/match only ── */
.det .box{width:33px;height:25px}
.det .pin{font-size:13px}
.det .tag{opacity:0;transition:opacity .16s}
.det:hover .tag,.det.match .tag{opacity:1}
.wrev{margin-top:13px;padding-left:12px;border-left:3px solid var(--pink);font-style:italic;color:var(--ink2);font-size:13.5px;line-height:1.45}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.galreal{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin:14px 0 10px}
.galreal img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:9px;display:block}
</style>
</head>
<body>

<div class="nav"><div class="wrap">
  <div class="logo">тайми</div>
  <div class="sp"></div>
  <span class="lab">твои люди и куда они ходят</span>
  <button class="navtag" onclick="document.getElementById('mapsec').scrollIntoView({behavior:'smooth'})"><i class="bar l"></i><i class="bar r"></i>открыть карту</button>
</div></div>

<header class="poster">
  <div class="bgimg"></div>
  <span class="pe pe-tr">хочется, чтобы их<br>никто не нашёл</span>
  <span class="pe pe-bl">тайми ©</span>
  <svg class="star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0 C12.6 6.2 17.8 11.4 24 12 C17.8 12.6 12.6 17.8 12 24 C11.4 17.8 6.2 12.6 0 12 C6.2 11.4 11.4 6.2 12 0 Z"/></svg>
  <span class="plus a">+</span><span class="plus b">+</span>
  <h1 class="ptitle">
    <span class="w w1">Нишевая</span>
    <span class="w w2">Карта</span>
    <span class="w w3">Петербурга<span class="ast">*</span></span>
  </h1>
  <p class="psub"><b>*</b> покажем аутентичные места,<br>куда ходят твои люди</p>
</header>

<div class="wrap"><section class="maphead" id="mapsec" style="padding-top:30px">
  <h2 class="h2 vh">твои люди ходят сюда:</h2>
  <div class="verbs" id="verbs"></div>
  <p class="sub" style="margin-top:20px">нажимай действие → выбирай места по советам людей, кто туда ходит постоянно</p>
  <div class="appcard">
    <div class="iosbar iosbar--plain"><span>спб тайми</span></div>
    <div class="maptop"><span>сканирую: <b id="scanlbl">всё</b></span><span id="found">9 точек</span></div>
    <div class="map" id="map">
      <svg class="bg" viewBox="0 0 1000 562" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <linearGradient id="nv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF79A9" stop-opacity=".22"/><stop offset="1" stop-color="#FF8B33" stop-opacity=".18"/></linearGradient>
          <pattern id="g" width="46" height="46" patternUnits="userSpaceOnUse"><path d="M46 0H0V46" fill="none" stroke="rgba(24,21,19,.05)" stroke-width="1"/></pattern>
        </defs>
        <rect width="1000" height="562" fill="url(#g)"/>
        <path d="M-20 230 C 180 165, 320 280, 500 250 S 850 185, 1020 260 L 1020 330 C 820 295, 640 370, 470 330 S 150 275, -20 330 Z" fill="rgba(255,46,132,.09)"/>
        <path d="M-20 282 C 200 230, 330 322, 500 295 S 860 248, 1020 305" fill="none" stroke="rgba(24,21,19,.14)" stroke-width="1.4" stroke-dasharray="2 8"/>
      </svg>
      <div class="scan" id="scan"></div>
    </div>
  </div>
</section></div>

<div class="wrap"><section>
  <h2 class="h2 hcaps">каждую неделю добавляем новые</h2>
  <p class="sub">собираем нишевую карту с классными людьми</p>
  <button class="ctabtn addbtn" onclick="openAdd()">добавь своё место</button>
  <div class="grid" id="grid"></div>
</section></div>

<section style="padding-top:14px">
  <div class="mband">
    <div class="bgimg2"></div>
    <div class="bmeta"><span>спб / 2026</span><span>твои люди</span></div>
    <h3 class="mbtitle">
      <span class="mw m1">Классное</span>
      <span class="mw m2">место —</span>
      <span class="mw m3">это люди</span>
    </h3>
    <p class="mbsub">на нашей карте нет самых лучших и топ-10 — мы показываем живые места и тех, кто ходит туда постоянно</p>
  </div>
</section>

<div class="wrap"><section id="cta">
  <div class="cta"><div class="inner">
    <h2>обсуди место, предложи своё или найди +1</h2>
    <ol class="ctlist">
      <li>перейди в наш тг-чат</li>
      <li>напиши про место, которое хочешь видеть на карте, прикрепи пару фото и хэштег #тутклассно — а мы добавим локацию <span>(пс, всех ждёт подарок от нас)</span></li>
      <li>напиши, куда собираешься пойти, или откликайся на предложения других — знакомься и кайфуй</li>
      <li>будь в курсе анонсов мест с карты, обсуждай их нишевость и делись своим опытом посещения</li>
    </ol>
    <a class="ctabtn" href="https://t.me/timy_chat" target="_blank" rel="noopener">перейти в тг-чат →</a>
  </div></div>
</section></div>

<div class="scrim" id="scrim"></div>
<div class="win" id="win" role="dialog" aria-modal="true">
  <div class="head" id="winhead"><div class="dots"><i></i><i></i><i></i></div><span id="winpath">место</span><span class="x" id="winx">✕</span></div>
  <div class="body" id="winbody"></div>
</div>

<div class="scrim2" id="scrim2"></div>
<div class="addwin" id="addwin" role="dialog" aria-modal="true">
  <div class="head">добавь своё место<span class="x" id="addx">✕</span></div>
  <div class="body">
    <ol class="ctlist" style="margin-top:2px">
      <li>перейди в наш тг-чат</li>
      <li>напиши про место, которое хочешь видеть на карте, прикрепи пару фото и хэштег #тутклассно</li>
      <li>мы добавим локацию <span>(пс, всех ждёт подарок от нас)</span></li>
    </ol>
    <a class="ctabtn" href="https://t.me/timy_chat" target="_blank" rel="noopener">перейти в тг-чат →</a>
  </div>
</div>

<script>
const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ── cut-out face avatars (flat vector) ───── */
const SK={a:'#F4CBA0',b:'#E7AE7B',c:'#CC8A5A',d:'#9A6440',e:'#F7D7BC'};
const HR={a:'#241d19',b:'#6f4a2c',c:'#cf9d3b',d:'#a8402b',e:'#d9cfc7'};
function face(o){
  const sk=SK[o.skin], hc=HR[o.hair], top=o.top||'#FF79A9';
  let hair='';
  if(o.style==='short') hair=`<path d="M24 52 C24 26 76 26 76 52 C76 45 71 36 50 36 C29 36 24 45 24 52 Z" fill="${hc}"/>`;
  else if(o.style==='bob') hair=`<path d="M22 64 V46 C22 24 78 24 78 46 V64 C78 50 73 40 50 40 C27 40 22 50 22 64 Z" fill="${hc}"/>`;
  else if(o.style==='bun') hair=`<circle cx="50" cy="22" r="8" fill="${hc}"/><path d="M24 52 C24 26 76 26 76 52 C76 45 71 36 50 36 C29 36 24 45 24 52 Z" fill="${hc}"/>`;
  else if(o.style==='curly') hair=`<g fill="${hc}"><circle cx="34" cy="36" r="11"/><circle cx="50" cy="30" r="12"/><circle cx="66" cy="36" r="11"/><circle cx="26" cy="46" r="8"/><circle cx="74" cy="46" r="8"/></g>`;
  else if(o.style==='long') hair=`<path d="M22 78 V46 C22 24 78 24 78 46 V78 L70 78 V52 C70 40 62 36 50 36 C38 36 30 40 30 52 V78 Z" fill="${hc}"/>`;
  const glasses=o.glasses?`<g fill="none" stroke="#241d19" stroke-width="2"><circle cx="40" cy="53" r="7"/><circle cx="60" cy="53" r="7"/><path d="M47 53 H53 M67 51 H72 M33 51 H28"/></g>`:'';
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <rect width="100" height="100" fill="#fff"/>
    <path d="M16 100 C16 82 34 78 50 78 C66 78 84 82 84 100 Z" fill="${top}"/>
    <rect x="43" y="70" width="14" height="14" rx="6" fill="${sk}"/>
    <ellipse cx="50" cy="53" rx="25" ry="28" fill="${sk}"/>
    <ellipse cx="32" cy="55" rx="4" ry="6" fill="${sk}"/><ellipse cx="68" cy="55" rx="4" ry="6" fill="${sk}"/>
    ${hair}
    <ellipse cx="40" cy="58" rx="4.5" ry="3" fill="${o.pk||'#FF9FBE'}" opacity=".5"/>
    <ellipse cx="60" cy="58" rx="4.5" ry="3" fill="${o.pk||'#FF9FBE'}" opacity=".5"/>
    <circle cx="41" cy="53" r="2.3" fill="#241d19"/><circle cx="59" cy="53" r="2.3" fill="#241d19"/>
    <path d="M43 63 Q50 69 57 63" stroke="#241d19" stroke-width="2.3" fill="none" stroke-linecap="round"/>
    ${glasses}
  </svg>`;
}
const SIL=`<svg width="64" height="64" viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><circle cx="24" cy="22" r="9"/><circle cx="44" cy="25" r="7.5"/><path d="M8 56 C8 42 18 36 24 36 C30 36 40 42 40 56 Z"/><path d="M36 56 C36 46 42 40 47 40 C52 40 58 46 58 56 Z"/></svg>`;

/* ── data ─────────────────────────────────── */
const ACTIONS=[
  {k:'all',  t:'всё',           e:'✦'},
  {k:'tus',  t:'тусоваться',    e:'🪩'},
  {k:'sok',  t:'искать сокровища',e:'🔎'},
  {k:'act',  t:'активничать',   e:'🤸'},
  {k:'eat',  t:'перекусить',    e:'🥐'},
  {k:'drink',t:'пить',          e:'🍸'},
  {k:'cult', t:'окультуриваться',e:'🖼️'},
];
const AT=Object.fromEntries(ACTIONS.map(a=>[a.k,a.t]));
const PIMG=__PIMG__;
const AVA=__AVA__;
const PHOTOS=__PHOTOS__;

const PLACES=[{"id": "p1", "name": "Alto Cafe", "type": "кофейня", "dist": "Центральный", "addr": "Караванная ул., 5", "acts": ["drink", "eat"], "phrase": "сканди-модерн, фильтр и книги про искусство", "hero": "Настя", "herokey": "nastya", "reason": "за кофе-вылазкой и стики-тофи-пудингом", "forwhom": "тем, кто любит камерные кофейни, искусство на стенах и хороший фильтр", "review": "Зашла за капучино, а зависла у книг, картин и десертов", "x": 38.5, "y": 36.5, "pin": "☕"}, {"id": "p2", "name": "Asiatiq", "type": "рамен-бар", "dist": "Петроградка", "addr": "Большая Зеленина ул., 9", "acts": ["eat"], "phrase": "горячая лапша и азиатский обед без церемоний", "hero": "Женя", "herokey": "zhenya", "reason": "за раменом, когда нужен нормальный горячий обед", "forwhom": "тем, кто хочет суп, лапшу или боул без долгой посадки", "review": "Хорошо, когда хочется сытно, остро и без меню на десять страниц", "x": 28.5, "y": 21.8, "pin": "🍜"}, {"id": "p3", "name": "К-30", "type": "пространство / двор", "dist": "Васька", "addr": "ул. Красного Текстильщика, 10-12", "acts": ["tus", "drink", "act"], "phrase": "диджей-сеты, бары и длинный летний вечер", "hero": "Лиза", "herokey": "liza", "reason": "за музыкой во дворе и танцами до заката", "forwhom": "тем, кто любит вечеринки без ночного марафона", "review": "Идеальный выходной: музыка, барные зоны и двор, где не надо ждать полуночи", "x": 10.5, "y": 40.8, "pin": "🪩"}, {"id": "p4", "name": "Cécile", "type": "французский бар-бистро", "dist": "Васька", "addr": "Кожевенная линия, 34", "acts": ["drink", "eat"], "phrase": "французский шик, портовый гранж и море рядом", "hero": "Настя", "herokey": "nastya", "reason": "за коктейлем, мидиями и закатом у воды", "forwhom": "тем, кто хочет отпусковый бар без выезда из города", "review": "Крок-мадам, кальмар и коктейли легко делают вид, что ты на побережье", "x": 19.5, "y": 40.8, "pin": "🍸"}, {"id": "p5", "name": "Chang x Kuta", "type": "тайское кафе", "dist": "Центральный", "addr": "ул. Некрасова, 1/38", "acts": ["eat"], "phrase": "том-ям, карри и честная острота", "hero": "Женя", "herokey": "zhenya", "reason": "за том-ямом и тайским обедом с перцем", "forwhom": "тем, кто любит яркую еду и не боится острого", "review": "Если просишь остро, здесь правда становится остро, а не питерски нежно", "x": 47.5, "y": 36.5, "pin": "🍜"}, {"id": "p6", "name": "Core Hot Yoga", "type": "студия горячей йоги и пилатеса", "dist": "Восстания", "addr": "Невский пр., 118", "acts": ["act"], "phrase": "жара, музыка и тренировка на максимум", "hero": "Лиза", "herokey": "liza", "reason": "за горячим пилатесом и чувством «я смогла»", "forwhom": "тем, кто любит интенсивные занятия", "review": "Выходишь мокрая, но довольная, как будто реально обновилась", "x": 61.0, "y": 37.8, "pin": "🧘"}, {"id": "p7", "name": "KGallery", "type": "галерея", "dist": "Центральный", "addr": "наб. реки Фонтанки, 24", "acts": ["cult", "drink", "sok"], "phrase": "выставки, кофе и книги с видом на Михайловский замок", "hero": "Настя", "herokey": "nastya", "reason": "за выставкой, кофе и книжкой после зала", "forwhom": "тем, кто хочет попасть в арт-среду без музейной тяжести", "review": "Смотришь выставку, берешь кофе у окна и внезапно покупаешь книгу", "x": 56.5, "y": 36.5, "pin": "🖼️"}, {"id": "p8", "name": "Kono", "type": "круглосуточная раменная", "dist": "Восстания", "addr": "ул. Восстания, 11", "acts": ["eat"], "phrase": "собери рамен сам и долей бесплатный лимонад", "hero": "Женя", "herokey": "zhenya", "reason": "за ночной лапшой и конструктором из топингов", "forwhom": "тем, кому нужен японский автомат-опыт, а не обычное кафе", "review": "Цены набегают по топингам, зато варить лапшу самому неожиданно весело", "x": 70.0, "y": 37.8, "pin": "🍜"}, {"id": "p9", "name": "Kiks", "type": "бильярдный клуб", "dist": "Владимирская", "addr": "ул. Марата, 56-58, лит. Б", "acts": ["act", "tus", "drink"], "phrase": "розовые столы, шары и барный свет", "hero": "Лиза", "herokey": "liza", "reason": "за партией на розовом столе и коктейлем рядом", "forwhom": "тем, кто хочет бильярд без подвального вайба", "review": "Даже если играешь средне, розовые столы спасают настроение", "x": 60.0, "y": 58.0, "pin": "🎱"}, {"id": "p10", "name": "LuCo", "type": "дог-френдли кофейня", "dist": "Центральный", "addr": "ул. Короленко, 3", "acts": ["drink", "eat"], "phrase": "дрипы с собачками и наклейки как в детстве", "hero": "Настя", "herokey": "nastya", "reason": "за кофе, дрипами с собаками и новым стикером", "forwhom": "тем, кто приходит с собакой или любит маленькие кофейные ритуалы", "review": "Здесь хочется собрать альбомчик, взять кофе и вернуться за новым стикером", "x": 65.5, "y": 36.5, "pin": "☕"}, {"id": "p11", "name": "ohaüs", "type": "кафе / комьюнити-пространство", "dist": "Черная речка", "addr": "ул. Академика Крылова, 4А, лит. А", "acts": ["eat", "drink", "tus"], "phrase": "завтраки, кино и камерные встречи", "hero": "Женя", "herokey": "zhenya", "reason": "за бранчем, кофе и событием после работы", "forwhom": "тем, кто любит кафе, где кроме еды есть жизнь", "review": "Можно прийти за завтраком, а попасть на показ или маленькую вечеринку", "x": 30.0, "y": 14.0, "pin": "☕"}, {"id": "p12", "name": "Orthodox", "type": "коктейльный бар", "dist": "Восстания", "addr": "ул. Восстания, 4", "acts": ["drink", "cult"], "phrase": "русская литература, северные ягоды и настойки", "hero": "Лиза", "herokey": "liza", "reason": "за коктейлем по Блоку или Ахматовой", "forwhom": "тем, кто хочет дегустацию русской барной культуры", "review": "Бармены легко собирают спешл под автора, и даже крепкое пьется мягко", "x": 79.0, "y": 37.8, "pin": "🍸"}, {"id": "p13", "name": "Ossu", "type": "лапшичная", "dist": "Центральный", "addr": "ул. Некрасова, 21", "acts": ["eat", "act"], "phrase": "лапша, пар и бильярдный стол в одном зале", "hero": "Настя", "herokey": "nastya", "reason": "за лапшой, а потом сыграть партию", "forwhom": "тем, кто любит еду с маленьким сюрпризом", "review": "Заходишь на лапшу, а задерживаешься из-за стола и шумной кухни", "x": 38.5, "y": 45.0, "pin": "🍜"}, {"id": "p14", "name": "Out Cinema", "type": "камерный кинотеатр", "dist": "Литейный", "addr": "Ковенский пер., 14", "acts": ["cult"], "phrase": "артхаус, драмы 80-х и тихий зал", "hero": "Женя", "herokey": "zhenya", "reason": "за фильмом, который потом надо переварить", "forwhom": "тем, кто выбирает кино не по постерам в ТЦ", "review": "То молча плачешь от любовной драмы, то выходишь после артхауса чуть другим", "x": 55.5, "y": 28.8, "pin": "🎬"}, {"id": "p15", "name": "Do Immigration", "type": "бар", "dist": "Восстания", "addr": "ул. Восстания, 24/27, лит. Г", "acts": ["drink", "tus"], "phrase": "барный вечер без ирландского пабного шума", "hero": "Лиза", "herokey": "liza", "reason": "за напитком и разговором, который не тонет в толпе", "forwhom": "тем, кто хочет бар, а не шумную пивную посадку", "review": "Сюда лучше идти за спокойным бокалом и компанией, с которой есть о чем говорить", "x": 61.0, "y": 46.2, "pin": "🍸"}, {"id": "p16", "name": "Sea Wolves", "type": "бильярдный бар", "dist": "Сенная", "addr": "Садовая ул., 62", "acts": ["act", "drink", "tus"], "phrase": "бильярд у Сенной без лакированного клуба", "hero": "Настя", "herokey": "nastya", "reason": "за партией и барным вечером после", "forwhom": "тем, кто хочет сыграть, а не просто сидеть за столом", "review": "Лучше приходить компанией: одна партия быстро превращается в еще одну", "x": 46.0, "y": 62.0, "pin": "🎱"}, {"id": "p17", "name": "Tsunami", "type": "азиатский ресторан", "dist": "Восстания", "addr": "ул. Восстания, 1Т", "acts": ["eat", "drink"], "phrase": "роллы, азиатская кухня и веранда у вокзала", "hero": "Женя", "herokey": "zhenya", "reason": "за роллами и столом на веранде", "forwhom": "тем, кому нужен понятный азиатский ужин до или после дороги", "review": "На веранде это не про шумный вечер, а про спокойно поесть и выдохнуть", "x": 70.0, "y": 46.2, "pin": "🍜"}, {"id": "p18", "name": "Pinkie Pie", "type": "секонд-хенд", "dist": "Лиговка", "addr": "Лиговский пр., 74, Лофт-проект «Этажи»", "acts": ["sok"], "phrase": "винтаж, трендовые рейлы и дизайнерские вещи", "hero": "Лиза", "herokey": "liza", "reason": "за обновками, которые не планировала", "forwhom": "тем, кто думает, что секонды не его формат", "review": "Заходишь «просто посмотреть», а выходишь с пакетом и новым образом", "x": 74.0, "y": 58.0, "pin": "🧥"}, {"id": "p19", "name": "Витя", "type": "бар", "dist": "Восстания", "addr": "ул. Восстания, 19", "acts": ["drink", "tus"], "phrase": "культовый бар, где вечер начинается сам", "hero": "Настя", "herokey": "nastya", "reason": "за настойками и местом у стойки", "forwhom": "тем, кто любит маленькие бары с постоянными людьми", "review": "Витя не объясняет себя с порога, но через полчаса уже кажется своим", "x": 79.0, "y": 46.2, "pin": "🍸"}, {"id": "p20", "name": "Дринкит у Казанского", "type": "кофейня", "dist": "Центральный", "addr": "наб. канала Грибоедова, 26А", "acts": ["eat"], "phrase": "кофейные спешлы, которые хочется тестить", "hero": "Женя", "herokey": "zhenya", "reason": "за сезонным спешлом между делами", "forwhom": "тем, кто любит кофе не только в формате капучино", "review": "Самое интересное здесь не базовый кофе, а спешлы, которые хочется сравнивать", "x": 47.5, "y": 45.0, "pin": "☕"}, {"id": "p21", "name": "Йога в Брусницыне", "type": "йога / практика", "dist": "Васька", "addr": "Кожевенная линия, 30", "acts": ["act"], "phrase": "утренняя йога у моря и воздух вместо зала", "hero": "Лиза", "herokey": "liza", "reason": "за ковриком, солнцем и зарядом у залива", "forwhom": "тем, кто обещал себе начать лето с движения", "review": "Круто тренироваться на свежем воздухе, когда после занятия сразу хочется гулять у воды", "x": 10.5, "y": 49.2, "pin": "🧘"}, {"id": "p22", "name": "Vivo", "type": "студия керамики", "dist": "Петроградка", "addr": "Газовая ул., 10, лит. Н", "acts": ["act", "cult"], "phrase": "лепка, чай и вечер без уведомлений", "hero": "Настя", "herokey": "nastya", "reason": "за кружкой, которую потом заберет домой", "forwhom": "тем, кому хочется руками и без оценки результата", "review": "На мастер-классе с кино легко выключиться: свечи, экран, глина и никакой спешки", "x": 37.5, "y": 21.8, "pin": "🏺"}, {"id": "p23", "name": "Аврора", "type": "исторический кинотеатр", "dist": "Центральный", "addr": "Невский пр., 60", "acts": ["cult"], "phrase": "исторический зал и старое кино на большом экране", "hero": "Женя", "herokey": "zhenya", "reason": "за ретро-сеансом в настоящем кинотеатре", "forwhom": "тем, кто любит не просто фильм, а место с историей", "review": "Сюда идешь не за попкорном, а за ощущением, что кино снова событие", "x": 56.5, "y": 45.0, "pin": "🎬"}, {"id": "p24", "name": "Желтый двор", "type": "книжный / культурное пространство", "dist": "Центральный", "addr": "ул. Маяковского, 15", "acts": ["sok", "cult"], "phrase": "Япония, Китай и Корея на полках и событиях", "hero": "Лиза", "herokey": "liza", "reason": "за редким изданием и лекцией про Восточную Азию", "forwhom": "тем, кто залипал на японском кино, китайской живописи или корейской прозе", "review": "Можно зайти за книгой, а попасть на разговор, концерт или теневой театр", "x": 65.5, "y": 45.0, "pin": "📚"}, {"id": "p25", "name": "Конец прекрасной эпохи + Полторы комнаты", "type": "музей-квартира Бродского / книжный", "dist": "Центральный", "addr": "ул. Короленко, 14", "acts": ["cult", "drink"], "phrase": "коммуналка Бродского, экскурсия и кофе после", "hero": "Настя", "herokey": "nastya", "reason": "за экскурсией по той самой коммуналке", "forwhom": "фанатам Бродского и тем, кто любит литературные места без пыли", "review": "После экскурсии хочется задержаться в книжном и спокойно выпить кофе", "x": 38.5, "y": 53.5, "pin": "📚"}, {"id": "p26", "name": "Парадная", "type": "кофейня", "dist": "Литейный", "addr": "Кирочная ул., 7", "acts": ["drink", "eat"], "phrase": "кофе, десерты и старый дом в центре", "hero": "Женя", "herokey": "zhenya", "reason": "за кофе и маленькой паузой в центре", "forwhom": "тем, кто любит камерные кофейни в старом фонде", "review": "Тут не нужен большой план: взял кофе, десерт и уже стало лучше", "x": 64.5, "y": 28.8, "pin": "☕"}, {"id": "p27", "name": "Маяковка на Кожевенной", "type": "библиотека / пространство", "dist": "Васька", "addr": "Кожевенная линия, 40", "acts": ["cult", "act"], "phrase": "бесплатные лекции, мастер-классы и выставки", "hero": "Лиза", "herokey": "liza", "reason": "за событием, которое не просит билет", "forwhom": "тем, кто любит городские культурные планы без бюджета", "review": "Это библиотека, куда приходят не только читать: здесь постоянно что-то происходит", "x": 19.5, "y": 49.2, "pin": "📚"}, {"id": "p28", "name": "Мечтатели", "type": "гастрономическое кафе", "dist": "Центральный", "addr": "наб. реки Фонтанки, 11", "acts": ["eat"], "phrase": "завтраки, ромовая баба и интерьер без перегруза", "hero": "Настя", "herokey": "nastya", "reason": "за завтраком и десертом, которого нет в меню", "forwhom": "тем, кто выбирает место для красивого завтрака без лишнего шума", "review": "Бери ромовую бабу, если есть: ее просят отдельно и не зря", "x": 47.5, "y": 53.5, "pin": "☕"}, {"id": "p29", "name": "Puri Guli", "type": "авторская пекарня", "dist": "Центральный", "addr": "Невский пр., 32-34", "acts": ["eat"], "phrase": "пури из печи в форме сердца", "hero": "Женя", "herokey": "zhenya", "reason": "за горячим пури прямо из зала", "forwhom": "тем, кто любит хлеб, который едят сразу", "review": "Лучше не ждать: горячий пури с хрустящей корочкой исчезает слишком быстро", "x": 56.5, "y": 53.5, "pin": "🥐"}, {"id": "p30", "name": "Сельский паб", "type": "паб / кафе", "dist": "Комарово", "addr": "2-я Дачная ул., 3", "acts": ["eat", "drink", "tus"], "phrase": "чебуреки, настойки и вечная посадка", "hero": "Лиза", "herokey": "liza", "reason": "за чебуреками и настойками после залива", "forwhom": "тем, кто любит культовые места, где тесно, шумно и честно", "review": "Тут почти не протолкнуться, но ради чебуреков это почему-то часть опыта", "x": 9.0, "y": 7.0, "pin": "🍸"}, {"id": "p31", "name": "Уделка", "type": "блошиный рынок", "dist": "Удельная", "addr": "Фермское шоссе, 41", "acts": ["sok"], "phrase": "деним, винил и торг за странные находки", "hero": "Настя", "herokey": "nastya", "reason": "за денимом, посудой и винилом с торгом", "forwhom": "тем, кто любит копаться и не боится хаоса", "review": "Лучшие покупки здесь находятся между «зачем мне это» и «беру»", "x": 23.0, "y": 9.0, "pin": "🧥"}, {"id": "p32", "name": "Утопист", "type": "винный бар", "dist": "Литейный", "addr": "Ковенский пер., 14", "acts": ["drink", "eat", "cult"], "phrase": "тихий двор, нестандартное кино и тартар с фри", "hero": "Женя", "herokey": "zhenya", "reason": "за вином, тихим двором и тартаром", "forwhom": "тем, кто хочет спрятаться от центра на один вечер", "review": "В Ковенском дворе легко зависнуть: лавочки, кино рядом и бар без суеты", "x": 55.5, "y": 37.2, "pin": "🍸"}, {"id": "p33", "name": "Юи", "type": "кафе", "dist": "Петроградка", "addr": "наб. реки Карповки, 5, к. 36", "acts": ["eat", "drink"], "phrase": "камерное азиатское кафе без лишнего шума", "hero": "Лиза", "herokey": "liza", "reason": "за спокойным обедом на Карповке", "forwhom": "тем, кто хочет красиво, тихо и поесть без суеты", "review": "Место небольшое, но теплое: сюда заходят не на бегу, а выдохнуть", "x": 28.5, "y": 30.2, "pin": "☕"}, {"id": "p34", "name": "Круч", "type": "бильярдный клуб и бистро", "dist": "Адмиралтейский", "addr": "ул. Блохина, 6/3", "acts": ["act", "drink", "tus"], "phrase": "бильярд с хорошей едой и взрослым вайбом", "hero": "Настя", "herokey": "nastya", "reason": "за партией, коктейлем и ужином у стола", "forwhom": "тем, кто хочет играть, есть и не переезжать между местами", "review": "Редкий случай, когда бильярд не выглядит компромиссом между баром и развлечением", "x": 41.0, "y": 66.0, "pin": "🎱"}];

/* ── verbs (typographic filter) ───────────── */
const verbsEl=document.getElementById('verbs');
ACTIONS.filter(a=>a.k!=='all').forEach(a=>{
  const v=document.createElement('span');
  v.className='verb';v.dataset.k=a.k;
  v.innerHTML='<span class="hl"><i class="bar l"></i><i class="bar r"></i></span>'+a.t;
  v.onclick=()=>toggleVerb(a.k);
  verbsEl.appendChild(v);
  const img=document.createElement('img');
  img.className='vtile';img.src=PIMG[a.k];img.alt='';img.loading='lazy';
  img.onclick=()=>toggleVerb(a.k);
  verbsEl.appendChild(img);
});
function toggleVerb(k){ setAct(cur===k?'all':k); }

/* ── detections ───────────────────────────── */
const map=document.getElementById('map');
PLACES.forEach(p=>{
  const d=document.createElement('div');d.className='det';d.dataset.id=p.id;
  d.style.left=p.x+'%';d.style.top=p.y+'%';
  d.innerHTML=`<div class="box"></div><div class="pin">${p.pin}</div><div class="tag">${p.name}<span class="tsep"> · <b class="cl"></b></span></div>`;
  d.onclick=()=>openWin(p);map.appendChild(d);
});

let cur='all';
function setAct(k){
  cur=k;const a=ACTIONS.find(x=>x.k===k);
  document.getElementById('scanlbl').textContent=a.t;
  document.querySelectorAll('.verb').forEach(v=>v.classList.toggle('active',v.dataset.k===k));
  const s=document.getElementById('scan');
  if(!RM){s.classList.remove('run');void s.offsetWidth;s.classList.add('run');}
  let m=0;
  PLACES.forEach(p=>{
    const hit = k==='all' || p.acts.includes(k);
    const det=map.querySelector(`.det[data-id="${p.id}"]`);
    det.classList.toggle('dim',!hit);
    det.classList.toggle('match',hit && k!=='all');
    det.querySelector('.cl').textContent = AT[ k==='all'?p.acts[0]:k ];
    if(!RM && hit){det.classList.remove('pop');void det.offsetWidth;det.classList.add('pop');}
    if(hit)m++;
  });
  document.getElementById('found').textContent=`${m} ${m===1?'точка':(m<5?'точки':'точек')}`;
}

/* ── places gallery ───────────────────────── */
const grid=document.getElementById('grid');
PLACES.forEach(p=>{
  const c=document.createElement('div');c.className='pc';c.onclick=()=>openWin(p);
  const ph=PHOTOS[p.id];
  const gal = ph
    ? `<div class="gallery"><div class="ph"><img src="${ph[0]}" alt=""></div><div class="col"><div class="ph"><img src="${ph[1]||ph[0]}" alt=""></div><div class="ph"><img src="${ph[2]||ph[0]}" alt=""></div></div></div>`
    : `<div class="gallery"><div class="ph"><div class="sil">${SIL}</div><span class="cap">${p.phrase}</span></div><div class="col"><div class="ph v2"></div><div class="ph v3"></div></div></div>`;
  c.innerHTML=`
    ${gal}
    <div class="info">
      <div class="top"><div class="av"><img src="${AVA[p.hero]}" alt=""></div>
        <div><div class="pn" style="margin-top:0">${p.name}</div><div class="pm">${p.type} · ${p.dist}</div></div></div>
      <div class="pw"><b>сюда ходит ${p.hero}</b> — ${p.reason}</div>
    </div>`;
  grid.appendChild(c);
});

/* ── window ───────────────────────────────── */
const win=document.getElementById('win'),scrim=document.getElementById('scrim');
function openWin(p){
  const cls = cur==='all'||!p.acts.includes(cur)?p.acts[0]:cur;
  document.getElementById('winpath').textContent=p.dist+' · спб';
  document.getElementById('winbody').innerHTML=`
    <div class="ttl">${p.name}</div>
    <div class="meta">${p.type} · ${p.dist} · ${AT[cls]}</div>
    ${(PHOTOS[p.id]
      ? `<div class="galreal">`+PHOTOS[p.id].slice(0,4).map(u=>`<img src="${u}" alt="">`).join('')+`</div>`
      : `<div class="gal"><div class="ph"><div class="sil">`+SIL+`</div><span class="cap">${p.phrase}</span><span class="lens"></span></div><div class="ph v2"></div><div class="ph v3"></div></div>`)}
    <div class="galcap">📍 ${p.addr}</div>
    <div class="who"><div class="av"><img src="${AVA[p.hero]}" alt=""></div>
      <div><div class="nm"><b>сюда ходит</b> ${p.hero}</div><div class="rl">${p.reason}</div></div></div>
    <div class="atags">${p.acts.map(a=>`<span class="atag">${AT[a]}</span>`).join('')}</div>
    <div class="fit"><b>кому зайдёт</b><span>${p.forwhom}</span></div>
    <div class="wrev">«${p.review}»</div>`;
  win.style.left='50%';win.style.top='50%';win.style.transform='translate(-50%,-50%)';
  win.classList.add('open');scrim.classList.add('open');
}
function closeWin(){win.classList.remove('open');scrim.classList.remove('open');}
document.getElementById('winx').onclick=closeWin;scrim.onclick=closeWin;
addEventListener('keydown',e=>{if(e.key==='Escape'){closeWin();closeAdd();}});
const addwin=document.getElementById('addwin'),scrim2=document.getElementById('scrim2');
function openAdd(){addwin.classList.add('open');scrim2.classList.add('open');}
function closeAdd(){addwin.classList.remove('open');scrim2.classList.remove('open');}
document.getElementById('addx').onclick=closeAdd;scrim2.onclick=closeAdd;
(function(){const h=document.getElementById('winhead');let dx,dy,drag=false;
  h.addEventListener('pointerdown',e=>{
    if(e.target.closest('.x'))return;
    drag=true;const r=win.getBoundingClientRect();
    win.style.transform='none';win.style.left=r.left+'px';win.style.top=r.top+'px';
    dx=e.clientX-r.left;dy=e.clientY-r.top;h.setPointerCapture(e.pointerId);});
  h.addEventListener('pointermove',e=>{if(drag){win.style.left=(e.clientX-dx)+'px';win.style.top=(e.clientY-dy)+'px';}});
  h.addEventListener('pointerup',()=>drag=false);})();

/* ── cta ──────────────────────────────────── */


setAct('all');
document.querySelectorAll('.band .sil').forEach(e=>e.innerHTML=SIL);
if(!RM)setTimeout(()=>document.getElementById('scan').classList.add('run'),300);
</script>
</body>
</html>
"""

HTML = HTML.replace("__FD_REG__", fd_reg).replace("__FD_ITA__", fd_ita).replace("__SIL__", "").replace("__HERO__", hero_jpg).replace("__PIMG__", json.dumps(PIMG)).replace("__AVA__", json.dumps(AVA)).replace("__BAND__", band_jpg).replace("__PHOTOS__", json.dumps(PHOTOS))
out = pathlib.Path("/mnt/user-data/outputs/taimi-landing.html")
out.write_text(HTML, encoding="utf-8")
print("written", len(HTML))
