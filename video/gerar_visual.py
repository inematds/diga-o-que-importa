#!/usr/bin/env python3
"""Roteiro visual v2 do vídeo diga-o-que-importa (1 bloco, 9 cenas) -> visual/pt-b01.json.
Confere se cada deixa (at / *_at) existe, em ordem, na fala da própria cena."""
import json, re, sys, unicodedata
from pathlib import Path

OUT = Path.home() / "projetos/output/explica-diga-o-que-importa"
M = str(OUT / "media") + "/"
rot = json.loads((OUT / "roteiro/pt.json").read_text())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s).split())


def img(nome, at, label, focus=(0.5, 0.5), zoom=(1.0, 1.06), prev=None, **kw):
    s = {"type": "media", "at": at, "src": M + nome, "focus": list(focus), "zoom": list(zoom), "label": label, "calm": True}
    if prev:
        s.update(cont=True, **{"from": {"focus": list(prev[0]), "zoom": prev[1]}})
    s.update(kw)
    return s


def node(i, label, col, row, at, icon=None):
    n = {"id": i, "label": label, "col": col, "row": row, "at": at}
    if icon:
        n["icon"] = icon
    return n


S = {}
S["1"] = {"header": False, "shots": [
    {"type": "hook", "at": "@start", "text": "Diga **o que importa**", "src": M + "01-capa-hook.png"},
    {"type": "statement", "at": "E quem sabe ensinar", "text": "Não é o **programador**", "then": {"text": "é **você, gestor**", "at": "É você, gestor"}},
    {"type": "fields", "at": "Você já conhece", "title": "O que você já sabe", "fields": [
        {"label": "Processos", "value": "como é feito", "at": "os processos"},
        {"label": "Clientes", "value": "o que pedem", "at": "os clientes"},
        {"label": "Fornecedores", "value": "quem entrega", "at": "os fornecedores"},
        {"label": "Equipe", "value": "quem resolve", "at": "a sua equipe"}]},
    {"type": "keyword", "at": "O que falta", "text": "O que falta", "sub": "**falar** com o agente", "sub_at": "falar com o agente"},
    {"type": "keyword", "at": "a regra cinco", "text": "Regra 5-4-3"},
]}
S["2"] = {"shots": [
    img("02-gestor-sabe.png", "Pense no que", "o que o **gestor** carrega"),
    img("02-gestor-sabe.png", "como cada processo", "**processos** e clientes", focus=(0.22, 0.35), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    img("02-gestor-sabe.png", "qual fornecedor atrasa", "**fornecedores** e equipe", focus=(0.8, 0.35), zoom=(1.18, 1.22), prev=((0.22, 0.35), 1.22)),
    {"type": "statement", "at": "Nenhum modelo", "text": "Nenhum modelo sabe **isso**", "then": {"text": "o conhecimento é **seu**", "at": "conhecimento é seu"}},
    {"type": "compare", "at": "O agente tem a capacidade",
     "left": {"title": "O agente", "at": "O agente tem", "tone": "neutral", "lines": [{"text": "tem a **capacidade**", "at": "a capacidade"}]},
     "right": {"title": "Você", "at": "mas não tem", "tone": "good", "lines": [{"text": "tem o **contexto**", "at": "Quem entrega o contexto"}]}},
]}
S["3"] = {"shots": [
    img("03-funcionario-novo.png", "E como entregar", "como um **funcionário novo**"),
    {"type": "steps", "at": "São cinco perguntas", "goal": "**5** perguntas", "steps": [
        {"title": "objetivo", "at": "objetivo da tarefa"}, {"title": "contexto", "at": "Que contexto"},
        {"title": "ferramentas", "at": "Que ferramentas"}, {"title": "sozinho ou com aprovação", "at": "pode ser feito sozinho"},
        {"title": "como saber se ficou bom", "at": "como você vai saber"}], "done_at": "se ficou bom"},
    {"type": "statement", "at": "Agora troque", "text": "Troque **pessoa** por **agente**", "then": {"text": "é a **mesma lista**", "at": "mesma lista"}},
    {"type": "keyword", "at": "Isso é gestão", "text": "Gestão de agentes"},
]}
S["4"] = {"shots": [
    img("04-autonomia.png", "O segundo número", "**4** níveis de autonomia"),
    {"type": "steps", "at": "Nível zero", "goal": "Quanto ele faz **sozinho**", "steps": [
        {"title": "0 · não toca", "at": "Nível zero"}, {"title": "1 · propõe", "at": "Nível um"},
        {"title": "2 · faz e avisa", "at": "Nível dois"}, {"title": "3 · faz sozinho", "at": "Nível três"}], "done_at": "registra"},
    {"type": "fields", "at": "Responder dúvida", "title": "Exemplos", "fields": [
        {"label": "Dúvida frequente", "value": "nível 3", "at": "Responder dúvida"},
        {"label": "Reembolso", "value": "nível 1", "at": "Reembolso"},
        {"label": "Cancelar contrato", "value": "nível 0", "at": "Cancelar contrato"}]},
    {"type": "statement", "at": "Quanto maior", "text": "Mais **impacto**", "then": {"text": "mais **você participa**", "at": "mais você participa"}},
]}
S["5"] = {"shots": [
    img("05-tres-casos.png", "O terceiro número", "**3** casos de teste"),
    img("05-tres-casos.png", "Um comum", "caso **comum**", focus=(0.32, 0.72), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    img("05-tres-casos.png", "Um difícil", "caso **difícil**", focus=(0.52, 0.72), zoom=(1.18, 1.22), prev=((0.32, 0.72), 1.22)),
    img("05-tres-casos.png", "E uma exceção", "a **exceção**", focus=(0.74, 0.72), zoom=(1.18, 1.22), prev=((0.52, 0.72), 1.22)),
    {"type": "compare", "at": "Se o agente acertar",
     "left": {"title": "Acertou os 3", "at": "acertar os três", "tone": "good", "lines": [{"text": "vai para o **trabalho**", "at": "vai para o trabalho"}]},
     "right": {"title": "Errou", "at": "Se errar", "tone": "bad", "lines": [{"text": "ajusta e **testa de novo**", "at": "testa de novo"}]}},
    {"type": "timeline", "at": "Cinco perguntas, quatro", "events": [
        {"label": "5", "sub": "perguntas", "at": "Cinco perguntas"},
        {"label": "4", "sub": "níveis", "at": "quatro níveis"},
        {"label": "3", "sub": "casos", "at": "níveis, três casos"}]},
]}
S["6"] = {"shots": [
    img("06-tecnico-muda.png", "Agora o outro lado", "o **técnico** de TI"),
    img("06-tecnico-muda.png", "passou anos", "anos **construindo**", focus=(0.25, 0.5), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "statement", "at": "Hoje o agente", "text": "O agente constrói **rápido**", "then": {"text": "o valor **muda de lugar**", "at": "muda de lugar"}},
    img("06-tecnico-muda.png", "Ele deixa de ser", "forma, confere e **orienta**", focus=(0.75, 0.5), zoom=(1.15, 1.2)),
]}
S["7"] = {"shots": [
    img("07-quatro-papeis.png", "São quatro papéis", "**4** papéis"),
    img("07-quatro-papeis.png", "O mentor", "**mentor**", focus=(0.25, 0.25), zoom=(1.2, 1.25), prev=((0.5, 0.5), 1.06)),
    img("07-quatro-papeis.png", "O auditor", "**auditor**", focus=(0.75, 0.25), zoom=(1.2, 1.25), prev=((0.25, 0.25), 1.25)),
    img("07-quatro-papeis.png", "O treinador", "**treinador**", focus=(0.25, 0.75), zoom=(1.2, 1.25), prev=((0.75, 0.25), 1.25)),
    img("07-quatro-papeis.png", "o consultor", "**consultor**", focus=(0.75, 0.75), zoom=(1.2, 1.25), prev=((0.25, 0.75), 1.25)),
    {"type": "keyword", "at": "São as quatro formações", "text": "Profissional 2030", "sub": "**4** formações", "sub_at": "dois mil e trinta"},
]}
S["8"] = {"shots": [
    img("08-padaria.png", "Veja os dois juntos", "gestor e técnico **numa padaria**"),
    img("08-padaria.png", "responda as encomendas", "encomendas no **WhatsApp**", focus=(0.8, 0.45), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "flow", "at": "Ele responde as cinco", "nodes": [
        node("d", "dono: 5 perguntas", 0, 1, "responde as cinco perguntas"),
        node("n", "desconto: nível 1", 1, 1, "desconto é nível um"),
        node("m", "mentor: instrução", 2, 1, "como mentor"),
        node("a", "auditor: 3 casos", 3, 1, "Como auditor")],
     "edges": [{"from": "d", "to": "n", "at": "desconto é nível um"}, {"from": "n", "to": "m", "at": "como mentor"},
               {"from": "m", "to": "a", "at": "Como auditor"}]},
    {"type": "keyword", "at": "inclusive o cliente", "text": "Bolo em 1 hora", "sub": "o caso **exceção**", "sub_at": "daqui a uma hora"},
    {"type": "statement", "at": "Passou nos três", "text": "Passou nos **três**", "then": {"text": "o agente **começa**", "at": "o agente começa"}},
]}
S["9"] = {"shots": [
    img("09-dupla.png", "Então fica assim", "cada um **no seu papel**"),
    {"type": "fields", "at": "O gestor diz", "title": "O time", "fields": [
        {"label": "Gestor", "value": "o que importa e por quê", "at": "O gestor diz"},
        {"label": "Técnico", "value": "o como e a prova", "at": "O técnico garante"},
        {"label": "Agente", "value": "executa", "at": "o agente executa"}]},
    img("10-guia.png", "O guia completo", "**inema.club** · guia grátis", zoom=(1.0, 1.05)),
]}

# conferência das deixas
erros = []
for k, sc in S.items():
    fala = norm(rot[int(k) - 1]["speech"])
    for sh in sc["shots"]:
        def ver(v):
            if v in ("@start",) or v is None:
                return
            c, _, n = v.partition("#")
            if norm(c) not in fala:
                erros.append(f"cena {k}: deixa '{v}' não está na fala")
        def anda(o):
            if isinstance(o, dict):
                for kk, vv in o.items():
                    if (kk == "at" or kk.endswith("_at")) and isinstance(vv, str):
                        ver(vv)
                    else:
                        anda(vv)
            elif isinstance(o, list):
                for x in o:
                    anda(x)
        anda(sh)
for k, sc in S.items():
    t = rot[int(k) - 1]
    sc.setdefault("takeaway", t["takeaway"])
(OUT / "visual/pt-b01.json").write_text(json.dumps({"block": "pt-b01", "scenes": S}, ensure_ascii=False, indent=1))
print("\n".join(erros) or "deixas OK", "| cenas", len(S), "| shots", sum(len(s["shots"]) for s in S.values()))
sys.exit(1 if erros else 0)
