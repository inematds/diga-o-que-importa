// uso: node v3-envia.mjs --texto "msg"  |  node v3-envia.mjs --video arq.mp4 --legenda "texto"
import { readFileSync } from 'node:fs';
import { basename } from 'node:path';
import { carregarEnv, lerConfig, validarTokenTelegram } from '/home/nmaldaner/projetos/openpcbotv3/dist/config/env.js';
const arg = (n) => { const i = process.argv.indexOf(`--${n}`); return i > 0 ? process.argv[i + 1] : undefined; };
carregarEnv(); const c = lerConfig();
if (!validarTokenTelegram(c.telegramToken).ok || !c.chatPermitido) throw new Error('config do bot v3 inválida');
const base = `https://api.telegram.org/bot${c.telegramToken}/`;
const me = await (await fetch(base + 'getMe')).json();
if (!me.ok || me.result.username !== 'inemav3bot') throw new Error('bot inesperado');
let r;
if (arg('video')) {
  const f = new FormData(); f.append('chat_id', String(c.chatPermitido)); f.append('supports_streaming', 'true');
  if (arg('legenda')) f.append('caption', arg('legenda'));
  f.append('video', new Blob([readFileSync(arg('video'))], { type: 'video/mp4' }), basename(arg('video')));
  r = await (await fetch(base + 'sendVideo', { method: 'POST', body: f })).json();
} else {
  r = await (await fetch(base + 'sendMessage', { method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: c.chatPermitido, text: arg('texto'), link_preview_options: { is_disabled: true } }) })).json();
}
console.log(r.ok ? `ok msg ${r.result.message_id}` : `ERRO ${JSON.stringify(r).slice(0, 300)}`);
