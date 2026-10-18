#!/usr/bin/env bash
R=~/projetos/diga-o-que-importa; G=~/.claude/skills/projetos-landing-guia/assets/gerar-banner.sh
SIDES="um homem de uns 40 anos conversando de frente com um robô humanoide branco fosco estilo Tesla Optimus, liso, sem rosto de tela"
node ~/.claude/skills/capa-inema/assets/gerar-capa.cjs --repo $R --title "Diga o que importa" --cat "IA na prática" --save-raw $R/guia/assets/hero.png --gerador auto &
pt(){ bash $G --repo $R --title "DIGA O QUE IMPORTA" --destaque "IMPORTA" --sub "Quem se comunica melhor tira mais dos agentes de IA" --line "6 ideias para o agente entregar o que você queria" --tiles "A barreira,O ambiente,A entrevista,Uma língua só,Base boa,A escada da confiança" --sides "$SIDES" "$@"; }
en(){ bash $G --repo $R --lang en --title "SAY WHAT MATTERS" --destaque "MATTERS" --sub "The best communicators get the most out of AI agents" --line "6 ideas so the agent delivers what you wanted" --tiles "The barrier,The environment,The interview,One language,Solid base,The trust ladder" --sides "$SIDES" "$@"; }
es(){ bash $G --repo $R --lang es --title "DI LO QUE IMPORTA" --destaque "IMPORTA" --sub "Quien mejor se comunica saca más de los agentes de IA" --line "6 ideas para que el agente entregue lo que querías" --tiles "La barrera,El entorno,La entrevista,Un solo idioma,Base sólida,La escalera de confianza" --sides "$SIDES" "$@"; }
pt & en --saida banner-en & es --saida banner-es & wait
pt --estilo grade --saida banner-grade & en --estilo grade --saida banner-grade-en & es --estilo grade --saida banner-grade-es & wait
echo FIM
