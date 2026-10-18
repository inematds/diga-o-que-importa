#!/usr/bin/env bash
# gera as 9 ilustrações do vídeo v2 (3 por vez)
G=~/projetos/diga-o-que-importa/video/gerar_img.sh; O=~/projetos/output/explica-diga-o-que-importa
run(){ "$G" "$O" "$@"; }
run 01-capa "Escritório claro de empresa com janela grande. O GESTOR, confiante, em pé no centro, explica algo apontando para um quadro com um fluxo desenhado em ícones; ao lado dele a TÉCNICA de TI segura um tablet e sorri; o ROBÔ, atrás, executa uma tarefa numa bancada. Deixe o terço de cima da imagem com fundo limpo para o título." "O AGENTE TRABALHA DO SEU JEITO" &
run 02-gestor-sabe "O GESTOR no centro, de braços abertos, cercado por janelas translúcidas flutuantes com ícones simples (engrenagens de um processo, rostos de clientes, um caminhão de fornecedor, um grupo de pessoas da equipe), todos sem letras; ao lado, o ROBÔ aguarda parado, com a cabeça levemente inclinada, como quem espera instruções." &
run 03-funcionario-novo "Recepção de escritório claro: o GESTOR dá boas-vindas ao ROBÔ como a um funcionário novo, entregando um crachá e uma pasta de integração com cinco abas coloridas visíveis na lateral; aperto de mãos amistoso." &
wait
run 04-autonomia "O GESTOR ajusta com a mão um painel de controle na parede com quatro alavancas grandes lado a lado, cada uma com uma luz: vermelha, laranja, amarela e verde; o ROBÔ observa ao lado. Sem letras nem números." &
run 05-tres-casos "Bancada de testes clara: a TÉCNICA de TI, de prancheta na mão, observa o ROBÔ diante de três caixas sobre a mesa: uma caixa simples e arrumada, uma caixa complicada cheia de fios e nós, e uma caixa de formato estranho e torto. Clima de laboratório organizado." &
run 06-tecnico-muda "Imagem dividida em duas metades: à esquerda, a TÉCNICA de TI sozinha digitando código, cercada de três monitores, concentrada; à direita, a MESMA mulher de pé, sorrindo, orientando um pequeno grupo formado por duas pessoas e um ROBÔ diante de um quadro branco." &
wait
run 07-quatro-papeis "Grade de quatro quadros iguais (2 por 2) com a mesma TÉCNICA de TI em quatro papéis: no 1º sentada ao lado do GESTOR, ajudando-o num notebook (mentora); no 2º com uma lupa e uma prancheta inspecionando o ROBÔ (auditora); no 3º diante de uma pequena turma de pessoas e robôs numa sala de aula clara (treinadora); no 4º diante de um grande mapa de processos de ícones e setas numa parede (consultora). Sem letras." &
run 08-padaria "Padaria de bairro moderna e clara de dia: o DONO DA PADARIA conversa com a TÉCNICA de TI, que segura um notebook; ao lado do balcão de pães e bolos, o ROBÔ responde encomendas num celular grande, com balões de conversa verdes e brancos sem letras na tela." &
run 09-dupla "O GESTOR, a TÉCNICA de TI e o ROBÔ lado a lado diante de um quadro com três colunas de ícones grandes sem letras: um balão de fala com coração, uma engrenagem com escudo de verificação e uma mão robótica segurando uma caixa. Escritório claro, clima de time." &
wait
echo FIM
