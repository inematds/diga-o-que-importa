#!/usr/bin/env python3
"""uso: ytbot-envia.py "texto"  -> manda ao inemaytbot (links de vídeo publicado)."""
import json, sys, urllib.request, pathlib
env = {}
for l in (pathlib.Path.home() / 'projetos/yt-pub-livesx-master/config/.env').read_text().splitlines():
    if '=' in l and not l.lstrip().startswith('#'):
        k, v = l.split('=', 1); env[k.strip()] = v.strip().strip('"\'')
chat = (pathlib.Path.home() / '.config/aventurasinemavideo/telegram_chat').read_text().strip()
req = urllib.request.Request(f"https://api.telegram.org/bot{env['TELEGRAM_NOTIFY_BOT_TOKEN']}/sendMessage",
      data=json.dumps({'chat_id': chat, 'text': sys.argv[1], 'link_preview_options': {'is_disabled': True}}).encode(),
      headers={'Content-Type': 'application/json'})
r = json.load(urllib.request.urlopen(req, timeout=30)); print('ok msg', r['result']['message_id'] if r.get('ok') else r)
