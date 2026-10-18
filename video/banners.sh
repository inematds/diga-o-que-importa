#!/usr/bin/env bash
while ! grep -q FIM ~/projetos/output/explica-diga-o-que-importa/logs/cenas2.log 2>/dev/null; do sleep 15; done
R=~/projetos/diga-o-que-importa; G=~/.claude/skills/projetos-landing-guia/assets/gerar-banner.sh
SIDES="um gestor de uns 40 anos de camisa azul-clara e uma técnica de TI de óculos, lado a lado, orientando um robô humanoide branco fosco estilo Tesla Optimus, liso, sem rosto de tela"
true # capa já existe: node ~/.claude/skills/capa-inema/assets/gerar-capa.cjs --repo $R --title "Diga o que importa" --cat "IA na prática" --save-raw $R/guia/assets/hero.png --gerador auto &
pt(){ bash $G --repo $R --title "DIGA O QUE IMPORTA" --destaque "IMPORTA" --sub "O gestor já sabe o mais difícil. Falta falar com o agente." --line "Regra 5-4-3 e o novo papel da TI" --tiles "O gestor,5 perguntas,4 níveis,3 casos,O técnico,4 papéis" --sides "$SIDES" "$@"; }
en(){ bash $G --repo $R --lang en --title "SAY WHAT MATTERS" --destaque "MATTERS" --sub "The manager already knows the hardest part. Now talk to the agent." --line "The 5-4-3 rule and the new role of IT" --tiles "The manager,5 questions,4 levels,3 cases,The tech,4 roles" --sides "$SIDES" "$@"; }
es(){ bash $G --repo $R --lang es --title "DI LO QUE IMPORTA" --destaque "IMPORTA" --sub "El gestor ya sabe lo más difícil. Falta hablar con el agente." --line "La regla 5-4-3 y el nuevo papel de TI" --tiles "El gestor,5 preguntas,4 niveles,3 casos,El técnico,4 roles" --sides "$SIDES" "$@"; }
pt & en --saida banner-en & es --saida banner-es & wait
pt --estilo grade --saida banner-grade & en --estilo grade --saida banner-grade-en & es --estilo grade --saida banner-grade-es & wait
echo FIM
