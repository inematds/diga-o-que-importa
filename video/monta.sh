#!/usr/bin/env bash
# uso: monta.sh <cfg-v1.json> <cfg-v2.json> <dir-producao> <heygen-id> <titulo>
# espera o avatar baixado, renderiza v1 (transcrição + base) e depois o v2 (visual em <dir>/visual/pt-b01.json).
set -euo pipefail
C1=$1; C2=$2; D=$3; ID=$4; T=$5
EV=~/projetos/explicavideos; A=$D/v1/assets/nei-pt-b01.mp4
until [ -s "$A" ] && ! pgrep -f "estudio-baixar.mjs --id $ID" >/dev/null; do sleep 15; done
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A")
python3 - <<P
import json
json.dump({"pt-b01":{"id":"$ID","title":"$T","status":"completed","downloaded":True,"file":"$A","duration":round(float("$DUR"),1),"via":"estudio"}},open("$D/v1/verification/blocos-downloads.json","w"),indent=2)
P
cd $EV/engine
echo "== v1 $(date +%T)"; EXPLICAVIDEOS_CONFIG=$EV/examples/$C1 python3 produce_blocks.py
EXPLICAVIDEOS_CONFIG=$EV/examples/$C1 python3 wait_assembly.py || true
cd $EV; export EXPLICAVIDEOS_CONFIG=$EV/examples/$C2
echo "== v2 $(date +%T)"; python3 engine/v2/setup_output.py
cp $D/visual/pt-b01.json $D/v2/visual-v2/pt-b01.json
python3 engine/v2/build_block.py 1 --strict
engine/v2/run_lane.sh 1
python3 engine/assemble_languages.py
echo "== FIM $(date +%T)"; ls -la $D/v2/final/*.mp4
