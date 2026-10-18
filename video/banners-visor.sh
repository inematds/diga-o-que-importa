#!/usr/bin/env bash
R=~/projetos/diga-o-que-importa; G=~/.claude/skills/projetos-landing-guia/assets/gerar-banner.sh
SIDES="um gestor de uns 40 anos de camisa azul-clara e uma técnica de TI de óculos, lado a lado, orientando um robô humanoide branco fosco estilo Tesla Optimus, liso; a FRENTE da cabeça do robô é um VISOR PRETO brilhante (faixa escura onde ficam os olhos), bem visível, nunca a cabeça toda branca, sem rosto de tela nem olhos desenhados"
pt(){ bash $G --repo $R --title "DIGA O QUE IMPORTA" --destaque "IMPORTA" --sub "O gestor já sabe o mais difícil. Falta falar com o agente." --line "Regra 5-4-3 e o novo papel da TI" --tiles "O gestor,5 perguntas,4 níveis,3 casos,O técnico,4 papéis" --sides "$SIDES" "$@"; }
en(){ bash $G --repo $R --lang en --title "SAY WHAT MATTERS" --destaque "MATTERS" --sub "The manager already knows the hardest part. Now talk to the agent." --line "The 5-4-3 rule and the new role of IT" --tiles "The manager,5 questions,4 levels,3 cases,The tech,4 roles" --sides "$SIDES" "$@"; }
es(){ bash $G --repo $R --lang es --title "DI LO QUE IMPORTA" --destaque "IMPORTA" --sub "El gestor ya sabe lo más difícil. Falta hablar con el agente." --line "La regla 5-4-3 y el nuevo papel de TI" --tiles "El gestor,5 preguntas,4 niveles,3 casos,El técnico,4 roles" --sides "$SIDES" "$@"; }
pt & pt --estilo grade --saida banner-grade & es --saida banner-es & en --saida banner-en & wait
echo FIM
