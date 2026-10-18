#!/usr/bin/env bash
# gera as 9 ilustrações do vídeo (3 por vez)
G=~/projetos/diga-o-que-importa/video/gerar_img.sh; O=~/projetos/output/explica-diga-o-que-importa
run(){ "$G" "$O" "$@"; }
run 01-capa "O homem sorri satisfeito diante de um monitor grande que mostra um projeto bonito e pronto; o robô ao lado entrega um tablet com o resultado. Escritório claro com janela grande. Deixe o terço de cima da imagem com fundo limpo para o título." "O AGENTE ENTREGA O QUE VOCÊ QUERIA" &
run 02-barreira "O homem e o robô frente a frente separados por uma parede de vidro fosco; acima do homem, um balão de pensamento com uma casa detalhada; acima do robô, um balão com uma casa torta e incompleta. Escritório claro." &
run 03-ambiente "Imagem dividida ao meio: à esquerda, o robô numa oficina bagunçada, com fios embolados, caixas caídas e papéis no chão, montando algo torto; à direita, o mesmo robô numa oficina organizada, ferramentas no painel, prateleiras etiquetadas sem letras, montando algo perfeito." &
wait
run 04-entrevista "Mesa de reunião num escritório claro: o robô, sentado, segura uma prancheta e faz perguntas; o homem responde gesticulando, pensativo; sobre a mesa, cartões com pontos de interrogação desenhados (só o símbolo, sem letras) sendo virados um a um." &
run 05-lingua "Cinco figuras em linha ligadas por uma fita azul contínua: uma cliente, o homem, o robô, um monitor com código abstrato e um celular; todos seguram ou mostram a MESMA caixa de pedido de papelão idêntica com o mesmo selo verde redondo. Fundo claro." &
run 06-base "À esquerda, uma pilha gigante e instável de documentos encadernados quase caindo sobre uma maquete quebrada; à direita, o robô encaixa com facilidade uma peça nova numa maquete modular bem organizada, feita de blocos que se encaixam. O homem observa aliviado." &
wait
run 07-escada "Uma escada larga de cinco degraus num espaço claro; o homem sobe ao lado do robô, de mãos dadas na subida como quem ensina a andar; no primeiro degrau, um pedal de freio de carro em destaque; nos degraus seguintes, objetos simbólicos: uma lupa, uma pilha de papéis, dois robôs pequenos, peças de quebra-cabeça, um envelope e um calendário." &
run 08-piso "O robô trabalha tranquilo sobre uma plataforma elevada e firme com uma rede de segurança verde-água por baixo, que segura peças que caem; o homem toma café ao lado, relaxado. Escritório claro." &
run 09-oportunidade "O homem apresenta para três empresários sentados numa sala de reunião clara um painel grande com um fluxo de trabalho desenhado em ícones (caixas e setas sem letras); o robô executa as etapas ao lado do painel. Clima de confiança." &
wait
echo FIM
