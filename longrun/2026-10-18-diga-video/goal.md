# Goal — diga-o-que-importa (18/10/2026)

Pedido do Nei: página num repo sobre a visão "quem comunica melhor tira mais dos agentes" (sem citar fontes),
explicavideo (explicavideos v2) + r7e; publicar no lives4, portal, Telegram INEMA.DEV e bot v3 (só arquivos).
O pedido já é o OK do HeyGen para esta produção (vídeo + reel), pelo estúdio.

Regra de conteúdo: nada de nomes, podcast, patrocinador, nomes de skills de terceiros, versões de modelo,
nem anedotas do entrevistado na boca do Nei — tudo vira princípio.

## Pronto quando (comando → saída esperada)
1. `gh repo view inematds/diga-o-que-importa --json visibility -q .visibility` → `PUBLIC`
2. `curl -s -o /dev/null -w '%{http_code}' https://inematds.github.io/diga-o-que-importa/guia/` (e /en/ /es/) → `200`
3. `grep -ciE "pocock|nate|hostinger|grill|herk|opus|sonnet" guia/index.html guia/en/index.html guia/es/index.html` → 0 em cada
4. `ffprobe` do 16:9 → 1920x1080, duração ≥ 120 s; do reel → 1080x1920
5. yt-pubx: 2 IDs no lives4 (16:9 com thumb; short sem thumb)
6. portal: commit com `diga-o-que-importa` em communityProjects + 2 vídeos; push no origin
7. Telegram INEMA.DEV: link do tópico + msg do MENU
8. bot v3: 2 arquivos enviados; inemaytbot: links + lives4
