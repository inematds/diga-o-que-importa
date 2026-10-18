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
</style>"""


def esc(s):
    return html.escape(s, quote=False)


def escada(passos):
    """Degraus em HTML que sobem da esquerda para a direita, um por vez."""
    return '<div class="steps">' + "".join(
        f'<div class="d" style="--i:{i};min-height:{110 + i * 45}px;animation-delay:{i * .3:.1f}s;background:rgba(250,204,21,{.06 + i * .06:.2f})"><b>{i + 1}</b><span>{esc(t)}</span></div>'
        for i, t in enumerate(passos)) + "</div>"


def construir(lang, videos):
    d = json.loads((SRC / f"{lang}.json").read_text())
    base = RAIZ / "guia" / ("" if lang == "pt" else lang)
    a0 = "assets/" if lang == "pt" else "../assets/"
    up = "" if lang == "pt" else "../"
    sfx = "" if lang == "pt" else f"-{lang}"
    nav = d["nav"]
    secoes = [("tese", nav["tese"]), ("ideias", nav["ideias"]), ("kit", nav["kit"])] + ([("video", nav["video"])] if videos else []) + [("cola", nav["cola"])]
    links = "".join(f'<a class="sec" href="#{a}">{esc(t)}</a>' for a, t in secoes)
    seletor = "".join(f'<a{" class=\"on\"" if l == lang else ""} href="{(up + ("" if l == "pt" else l + "/")) or "./"}">{l.upper()}</a>' for l in LANGS)
    alt = "".join(f'<link rel="alternate" hreflang="{"pt-BR" if l == "pt" else l}" href="{SITE}{"" if l == "pt" else l + "/"}">' for l in LANGS)
    h, t, k = d["hero"], d["tese"], d["kit"]
    cards = "".join(f'<div class="card"><h3>{e} {esc(a)}</h3><p>{esc(b)}</p></div>' for e, a, b in t["cards"])
    ideias = "".join(f"""<article class="ideia" id="{i['id']}">
  <figure><img src="{a0}{i['img']}" alt="{html.escape(i['img_alt'])}" loading="lazy"></figure>
  <div><span class="rot">{n + 1:02d} · {esc(i['nome']).upper()}</span><h3>{esc(i['titulo'])}</h3>
  {''.join(f'<p>{esc(p)}</p>' for p in i['texto'])}
  <p class="tip"><strong>{esc(d['faca'])}:</strong> {esc(i['faca'])}</p></div>
</article>""" for n, i in enumerate(d["ideias"]))
    b = d["bonus"]
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
    o, c = d["oport"], d["cola"]
    itens = "".join(f"<li>{esc(x)}</li>" for x in c["itens"])
    corpo = f"""
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{esc(h['chip'])}</span>
      <h1>{h['h1']}</h1>
      <p class="lead">{esc(h['lead'])}</p>
      <div class="cta"><a class="btn" href="#ideias">{esc(h['cta1'])}</a><a class="btn ghost" href="{REPO}" target="_blank" rel="noopener">{esc(h['cta2'])}</a></div>
    </div>
    <figure><img src="{a0}banner{sfx}.jpg" alt="{html.escape(h['alt'])}"></figure>
  </div>
</header>
<section id="resumo" class="resumo"><div class="wrap"><span class="chip">{esc(d['resumo_chip'])}</span><p>{esc(d['resumo'])}</p></div></section>
<section id="tese"><div class="wrap">
  <span class="chip">{esc(t['chip'])}</span><h2>{esc(t['h2'])}</h2><p class="sub">{esc(t['sub'])}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000"><img src="{a0}banner-grade{sfx}.jpg" alt="{html.escape(t['alt_grade'])}" loading="lazy" style="width:100%;display:block"></figure>
  <div class="grid g3">{cards}</div>
</div></section>
<section id="ideias"><div class="wrap">
  <span class="chip">{esc(d['ideias_chip'])}</span><h2>{esc(d['ideias_h2'])}</h2><p class="sub">{esc(d['ideias_sub'])}</p>
  {ideias}
  <div class="box" style="margin-top:20px"><div class="two" style="align-items:center">
    <figure class="ill"><img src="{a0}{b['img']}" alt="{html.escape(b['img_alt'])}" loading="lazy"></figure>
    <div><span class="chip">{esc(b['chip'])}</span><h3 style="font-size:1.25rem;margin:.3em 0">{esc(b['h3'])}</h3><p>{esc(b['texto'])}</p></div>
  </div></div>
</div></section>
<section id="kit"><div class="wrap">
  <span class="chip">{esc(k['chip'])}</span><h2>{esc(k['h2'])}</h2><p class="sub">{esc(k['sub'])}</p>
  <div class="two">
    <div class="box"><h3>{esc(k['entrevista_h3'])}</h3><p>{esc(k['entrevista_p'])}</p><pre id="p-entrevista">{esc(k['entrevista'])}</pre>
      <button class="btn copy" data-alvo="p-entrevista">{esc(k['copiar'])}</button></div>
    <div class="box"><h3>{esc(k['dic_h3'])}</h3><p>{esc(k['dic_p'])}</p><pre id="p-dic">{esc(k['dic'])}</pre>
      <button class="btn copy" data-alvo="p-dic">{esc(k['copiar'])}</button></div>
  </div>
  <div class="ladder"><h3 style="margin:0 0 10px">{esc(k['escada_h3'])}</h3>{escada(k['escada'])}</div>
</div></section>
{vid}
<section id="cola"><div class="wrap">
  <span class="chip">{esc(o['chip'])}</span><h2>{esc(o['h2'])}</h2>
  <div class="two" style="align-items:center;margin-bottom:40px">
    <figure class="ill"><img src="{a0}{o['img']}" alt="{html.escape(o['img_alt'])}" loading="lazy"></figure>
    <p style="color:var(--txt);font-size:1.05rem">{esc(o['texto'])}</p>
  </div>
  <span class="chip">{esc(c['chip'])}</span><h2>{esc(c['h2'])}</h2><p class="sub">{esc(c['sub'])}</p>
  <ul class="check">{itens}</ul>
  <p class="tip" style="margin-top:22px"><strong>{esc(c['frase'])}</strong></p>
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
