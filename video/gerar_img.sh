#!/usr/bin/env bash
# uso: gerar_img.sh <saida_dir> <nome> "<cena>" [texto]   -> <saida_dir>/media/<nome>.png (Codex image_gen pela assinatura)
set -u
cd "$1"; nome=$2; cena=$3; texto=${4:-}
mkdir -p media logs
rm -f "media/$nome.png"
ESTILO="Ilustração digital editorial sofisticada, estilo livro ilustrado moderno, traço limpo, cores sóbrias (azul-acinzentado, branco, \
cinza-grafite, toques de verde-água). Luz de dia NEUTRA e fria-clara (nada de tom amarelado, dourado, sépia ou pôr do sol). \
Personagens fixos (use só os que a cena pedir, sempre iguais): o GESTOR, um HOMEM de uns 40 anos, cabelo curto castanho, barba curta, camisa azul-clara de manga dobrada; \
a TÉCNICA de TI, uma MULHER de uns 35 anos, cabelo castanho preso, óculos de armação fina, camisa cinza-grafite; o DONO DA PADARIA, um HOMEM de uns 50 anos, cabelo grisalho curto, avental azul-marinho sobre camisa branca; \
e o ROBÔ, humanoide branco fosco estilo Tesla Optimus, liso, industrial, com cabeça preta lisa SEM rosto de tela, sem olhos desenhados, \
nada de robô fofo ou cartoon. Composição horizontal 16:9, assunto principal centralizado com respiro nas bordas."
if [ -n "$texto" ]; then
  REGRA="Escreva DENTRO da arte, grande, legível, em letras brancas com uma palavra em amarelo, com a grafia EXATA (português, com acentos), só este texto: $texto. Nenhum outro texto."
else
  REGRA="SEM NENHUM TEXTO: nada de letras, palavras, números, placas ou etiquetas escritas."
fi
pedido="Use sua ferramenta de geração de imagem (image_gen) para criar UMA imagem no maior formato HORIZONTAL (paisagem) disponível \
e salve o PNG em media/$nome.png dentro deste diretório. Não edite nenhum outro arquivo.

$ESTILO

Cena: $cena

$REGRA"
timeout 900 codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox - <<<"$pedido" > "logs/img-$nome.log" 2>&1
if [ -s "media/$nome.png" ]; then
  python3 ~/projetos/refazvideo/ferramentas/cor_neutra.py corrigir "media/$nome.png"
  echo "OK $nome"
else
  echo "FALHOU $nome (ver logs/img-$nome.log)"
fi
