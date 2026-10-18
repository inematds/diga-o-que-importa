#!/usr/bin/env python3
"""Gera o guia (página única) em PT/EN/ES a partir de src/<lang>.json.

  python3 src/build.py   -> guia/index.html, guia/en/index.html, guia/es/index.html
O texto mora só nos JSON; HTML, CSS e a escada animada saem daqui. Vídeos: src/videos.json (opcional).
"""
import html, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"
SLUG = "diga-o-que-importa"
REPO = f"https://github.com/inematds/{SLUG}"
SITE = f"https://inematds.github.io/{SLUG}/guia/"
LANGS = ["pt", "en", "es"]
CSS = (SRC / "base.css.html").read_text()
EXTRA_CSS = """<style>
  .ideia{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:center;padding:34px 0;border-top:1px solid var(--line)}
  .ideia:first-of-type{border-top:none}
  .ideia:nth-child(even) figure{order:2}
  @media(max-width:820px){.ideia{grid-template-columns:1fr}.ideia:nth-child(even) figure{order:0}}
  .ideia figure,.ill{margin:0;border-radius:14px;overflow:hidden;border:1px solid var(--line)}
  .ideia figure img,.ill img{width:100%;display:block;aspect-ratio:16/9;object-fit:cover}
  .ideia h3{font-size:1.35rem;margin:.3em 0 .5em} .ideia p{color:var(--mut);margin:.2em 0 .8em}
  .rot{font-family:Sora;font-weight:800;color:var(--amb);font-size:.95rem;letter-spacing:.08em}
  .tip{border-left:3px solid var(--amb);background:rgba(250,204,21,.08);padding:12px 16px;border-radius:0 10px 10px 0;margin:14px 0 0;color:var(--txt)}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:22px} @media(max-width:820px){.two{grid-template-columns:1fr}}
  .box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;min-width:0}
  .box h3{font-size:1.05rem;margin-bottom:.4em} .box p{color:var(--mut);margin:.2em 0 .8em}
  .box pre{white-space:pre-wrap;overflow-wrap:anywhere;margin:0}
  .copy{margin-top:12px;font-size:.85rem;padding:.45em .9em}
  .ladder{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin-top:22px}
  .steps{display:flex;align-items:flex-end;gap:10px}
  .steps .d{flex:1;min-width:0;border:2px solid var(--amb);border-radius:10px;padding:12px;opacity:0;animation:up .5s ease-out forwards}
  .steps .d b{display:block;font-family:Sora;font-weight:800;font-size:1.5rem;color:var(--amb)}
  .steps .d span{font-size:.92rem;line-height:1.3}
  @media(max-width:700px){.steps{flex-direction:column;align-items:stretch}.steps .d{min-height:0!important;margin-left:calc(var(--i)*14px)}}
  @keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
  @media(prefers-reduced-motion:reduce){.steps .d{animation:none;opacity:1}}
  .vids{display:grid;grid-template-columns:2fr 1fr;gap:20px;align-items:start} @media(max-width:820px){.vids{grid-template-columns:1fr}}
  .vids video{width:100%;border-radius:14px;border:1px solid var(--line);background:#000;display:block}
  .vids .v916 video{max-width:360px;margin:0 auto}
  .vids h3{font-size:1rem;margin:0 0 .6em} .vids p{margin:.6em 0 0;font-size:.88rem}
  ul.check{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
  @media(max-width:700px){ul.check{grid-template-columns:1fr}}
  ul.check li{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px 14px 46px;position:relative}
  ul.check li::before{content:"";position:absolute;left:16px;top:16px;width:18px;height:18px;border:2px solid var(--amb);border-radius:5px}
  .ill{margin:0;border-radius:14px;overflow:hidden;border:1px solid var(--line)}
  .big{font-family:Sora;font-weight:800;color:var(--amb);font-size:1.1rem;letter-spacing:.06em;text-transform:uppercase;display:flex;align-items:baseline;gap:10px}
  .big span{font-size:3.4rem;line-height:1}
  ul.lista{margin:.4em 0 0;padding-left:1.2em} ul.lista li{margin:.35em 0}
  .minis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px} @media(max-width:820px){.minis{grid-template-columns:1fr 1fr}}
  .mini{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:4px}
  .mini .ic{font-size:1.4rem} .mini span:last-child{color:var(--mut);font-size:.9rem}
  .papeis{display:grid;grid-template-columns:1fr 1fr;gap:12px} @media(max-width:600px){.papeis{grid-template-columns:1fr}}
  .papel h3{font-size:1.02rem} .papel p{font-size:.92rem} .papel .usa{color:var(--amb);font-size:.85rem;margin-top:.4em}
  ol.passos{list-style:none;counter-reset:p;padding:0;margin:0;display:grid;gap:12px}
  ol.passos li{counter-increment:p;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px 12px 54px;position:relative;display:flex;flex-direction:column;gap:3px}
  ol.passos li::before{content:counter(p);position:absolute;left:14px;top:12px;width:28px;height:28px;border-radius:50%;background:var(--amb);color:#1a1206;font:800 .95rem/28px Sora;text-align:center}
  ol.passos li span{color:var(--mut);font-size:.92rem}
  .modelos{display:grid;grid-template-columns:1fr 1fr;gap:18px} @media(max-width:820px){.modelos{grid-template-columns:1fr}}
  .grid.g4{grid-template-columns:repeat(4,1fr)} @media(max-width:900px){.grid.g4{grid-template-columns:1fr 1fr}} @media(max-width:540px){.grid.g4{grid-template-columns:1fr}}
  a.card.link{color:var(--txt)} a.card.link:hover{border-color:var(--amb)}
  table.cola{width:100%;border-collapse:collapse} table.cola td{padding:12px;border-bottom:1px solid var(--line)} table.cola td:first-child{font-family:Sora;font-weight:800;color:var(--amb);white-space:nowrap}
</style>"""


def esc(s):
    return html.escape(s, quote=False)


def construir(lang, videos):
    d = json.loads((SRC / f"{lang}.json").read_text())
    base = RAIZ / "guia" / ("" if lang == "pt" else lang)
    a0 = "assets/" if lang == "pt" else "../assets/"
    up = "" if lang == "pt" else "../"
    sfx = "" if lang == "pt" else f"-{lang}"
    nav = d["nav"]
    secoes = [("gestor", nav["gestor"]), ("regra", nav["regra"]), ("tecnico", nav["tecnico"]), ("kit", nav["kit"])] + ([("video", nav["video"])] if videos else [])
    links = "".join(f'<a class="sec" href="#{a}">{esc(t)}</a>' for a, t in secoes)
    seletor = "".join(f'<a{" class=\"on\"" if l == lang else ""} href="{(up + ("" if l == "pt" else l + "/")) or "./"}">{l.upper()}</a>' for l in LANGS)
    alt = "".join(f'<link rel="alternate" hreflang="{"pt-BR" if l == "pt" else l}" href="{SITE}{"" if l == "pt" else l + "/"}">' for l in LANGS)
    h, t, g, r, tc, ex, k, f = d["hero"], d["tese"], d["gestor"], d["regra"], d["tecnico"], d["exemplo"], d["kit"], d["fim"]
    fig = lambda src, altt, extra="": f'<figure class="ill"{extra}><img src="{a0}{src}" alt="{html.escape(altt)}" loading="lazy"></figure>'
    cards = "".join(f'<div class="card"><h3>{e} {esc(a)}</h3><p>{esc(b)}</p></div>' for e, a, b in t["cards"])
    sabe = "".join(f'<div class="mini"><span class="ic">{e}</span><b>{esc(a)}</b><span>{esc(b)}</span></div>' for e, a, b in g["sabe"])
    partes = "".join(f"""<article class="ideia" id="{p['id']}">
  {fig(p['img'], p['img_alt'])}
  <div><div class="big"><span>{p['num']}</span>{esc(p['nome'])}</div><h3>{esc(p['titulo'])}</h3><p>{esc(p['texto'])}</p>
  <ul class="lista">{''.join(f'<li>{esc(i)}</li>' for i in p['itens'])}</ul></div>
</article>""" for p in r["partes"])
    papeis = "".join(f'<div class="card papel"><h3>{e} {esc(a)}</h3><p>{esc(b)}</p><p class="usa">{esc(c)}</p></div>' for e, a, b, c in tc["papeis"])
    passos = "".join(f'<li><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in ex["passos"])
    modelos = "".join(f"""<div class="box"><span class="chip">{esc(m['quem'])}</span><h3>{esc(m['titulo'])}</h3><p>{esc(m['p'])}</p><pre id="m{n}">{esc(m['txt'])}</pre>
      <button class="btn copy" data-alvo="m{n}">{esc(k['copiar'])}</button></div>""" for n, m in enumerate(k["modelos"]))
    mais = "".join(f'<a class="card link" href="{u}" target="_blank" rel="noopener"><h3>{esc(a)} ↗</h3><p>{esc(b)}</p></a>' for a, b, u in k["mais"])
    linhas = "".join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for a, b in f["linhas"])
    vid = ""
    if videos:
        v = d["video"]
        yt = lambda key: f' · <a href="{videos[key]}">YouTube</a>' if videos.get(key) else ""
        vid = f"""<section id="video"><div class="wrap">
  <span class="chip">{esc(v['chip'])}</span><h2>{esc(v['h2'])}</h2><p class="sub">{esc(v['sub'])}</p>
  <div class="vids">
    <div><h3>{esc(v['longo'])}</h3><video controls preload="metadata" playsinline poster="{a0}{videos['poster']}"><source src="{videos['longo']}" type="video/mp4"></video>
      <p><a href="{videos['longo']}">{esc(v['baixar'])}</a>{yt('yt_longo')}</p></div>
    <div class="v916"><h3>{esc(v['reel'])}</h3><video controls preload="metadata" playsinline poster="{a0}{videos['poster_reel']}" style="aspect-ratio:9/16;object-fit:cover"><source src="{videos['reel']}" type="video/mp4"></video>
      <p><a href="{videos['reel']}">{esc(v['baixar'])}</a>{yt('yt_reel')}</p></div>
  </div>
</div></section>"""
    corpo = f"""
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{esc(h['chip'])}</span>
      <h1>{h['h1']}</h1>
      <p class="lead">{esc(h['lead'])}</p>
      <div class="cta"><a class="btn" href="#regra">{esc(h['cta1'])}</a><a class="btn ghost" href="{REPO}" target="_blank" rel="noopener">{esc(h['cta2'])}</a></div>
    </div>
    <figure><img src="{a0}banner{sfx}.jpg" alt="{html.escape(h['alt'])}"></figure>
  </div>
</header>
<section id="resumo" class="resumo"><div class="wrap"><span class="chip">{esc(d['resumo_chip'])}</span><p>{esc(d['resumo'])}</p></div></section>
<section id="time"><div class="wrap">
  <span class="chip">{esc(t['chip'])}</span><h2>{esc(t['h2'])}</h2><p class="sub">{esc(t['sub'])}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000"><img src="{a0}banner-grade{sfx}.jpg" alt="{html.escape(t['alt_grade'])}" loading="lazy" style="width:100%;display:block"></figure>
  <div class="grid g3">{cards}</div>
</div></section>
<section id="gestor"><div class="wrap">
  <span class="chip">{esc(g['chip'])}</span><h2>{esc(g['h2'])}</h2>
  <div class="two" style="align-items:center;margin-top:18px">{fig(g['img'], g['img_alt'])}<div>{''.join(f'<p>{esc(x)}</p>' for x in g['texto'])}</div></div>
  <h3 style="margin:28px 0 12px">{esc(g['sabe_h3'])}</h3><div class="minis">{sabe}</div>
</div></section>
<section id="regra"><div class="wrap">
  <span class="chip">{esc(r['chip'])}</span><h2>{esc(r['h2'])}</h2><p class="sub">{esc(r['sub'])}</p>
  {partes}
</div></section>
<section id="tecnico"><div class="wrap">
  <span class="chip">{esc(tc['chip'])}</span><h2>{esc(tc['h2'])}</h2>
  <div class="two" style="align-items:center;margin-top:18px">{fig(tc['img'], tc['img_alt'])}<p style="color:var(--txt);font-size:1.05rem">{esc(tc['texto'])}</p></div>
  <div class="two" style="margin-top:26px;align-items:start">{fig(tc['img2'], tc['img2_alt'])}<div class="papeis">{papeis}</div></div>
  <p class="tip" style="margin-top:22px">{esc(tc['prof'])} <a href="https://eventos.inema.pro/prof2030/" target="_blank" rel="noopener">{esc(tc['prof_link'])} ↗</a></p>
</div></section>
<section id="exemplo"><div class="wrap">
  <span class="chip">{esc(ex['chip'])}</span><h2>{esc(ex['h2'])}</h2><p class="sub">{esc(ex['sub'])}</p>
  <div class="two" style="align-items:start">{fig(ex['img'], ex['img_alt'])}<ol class="passos">{passos}</ol></div>
</div></section>
<section id="kit"><div class="wrap">
  <span class="chip">{esc(k['chip'])}</span><h2>{esc(k['h2'])}</h2><p class="sub">{esc(k['sub'])}</p>
  <div class="modelos">{modelos}</div>
  <h3 style="margin:34px 0 12px">{esc(k['mais_h3'])}</h3><div class="grid g4">{mais}</div>
</div></section>
{vid}
<section id="fim"><div class="wrap">
  <span class="chip">{esc(f['chip'])}</span><h2>{esc(f['h2'])}</h2>
  <div class="two" style="align-items:center;margin-top:18px">{fig(f['img'], f['img_alt'])}<div class="box"><table class="cola">{linhas}</table></div></div>
  <p class="tip" style="margin-top:22px"><strong>{esc(f['frase'])}</strong></p>
</div></section>
"""
    pagina = f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d['title'])} — {esc(d['tagline'])}</title>
<meta name="description" content="{html.escape(d['meta'])}">
{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
{CSS}
{EXTRA_CSS}
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="./"><span class="emoji">🗣️</span> {esc(d['title'])}</a>
  <span class="sep">|</span>
  <span class="clubpro">
    <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
    <span class="sep">-</span>
    <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a>
  </span>
  <div class="links">
    {links}
    <span class="lang">{seletor}</span>
    <button class="tgl" id="themeToggle" aria-label="{esc(nav['tema'])}" title="{esc(nav['tema'])}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">{esc(nav['github'])}</a>
  </div>
</div></nav>
{corpo}
<footer>
  <div class="wrap">
    {"".join(f'<div class="pill">{esc(s)}</div>' for s in d['footer']['stack'])}
    <p style="margin-top:18px">{esc(d['title'])} · {esc(d['footer']['nota'])} · <a href="{REPO}">inematds/{SLUG}</a> · <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>
<script>
  (function(){{
    var KEY='{SLUG}-theme', b=document.body, t=document.getElementById('themeToggle');
    try{{ if(localStorage.getItem(KEY)==='light'){{ b.classList.add('light'); t.textContent='☀️'; }} }}catch(e){{}}
    t.addEventListener('click',function(){{ var light=b.classList.toggle('light'); t.textContent=light?'☀️':'🌙'; try{{ localStorage.setItem(KEY, light?'light':'dark'); }}catch(e){{}} }});
    document.querySelectorAll('.copy').forEach(function(bt){{
      bt.addEventListener('click',function(){{
        var txt=document.getElementById(bt.dataset.alvo).innerText;
        (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(function(){{ var o=bt.textContent; bt.textContent='{esc(k['copiado'])} ✓'; setTimeout(function(){{bt.textContent=o;}},1600); }}).catch(function(){{}});
      }});
    }});
  }})();
</script>
</body>
</html>
"""
    base.mkdir(parents=True, exist_ok=True)
    (base / "index.html").write_text(pagina)


if __name__ == "__main__":
    vf = SRC / "videos.json"
    videos = json.loads(vf.read_text()) if vf.exists() else None
    for l in LANGS:
        if (SRC / f"{l}.json").exists():
            construir(l, videos); print("ok", l)
