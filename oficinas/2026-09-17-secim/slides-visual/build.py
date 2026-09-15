#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Monta a apresentação visual da oficina do Secim (17/09/2026) em um arquivo único.

    python build.py                       gera apresentacao-secim-visual.html
    python build.py --artifact SAIDA.html gera também a versão sem <html>/<head>/<body>

Fontes do deck (edite aqui, não no HTML gerado):
    src/deck.css        paleta, tipografia, palco, modos (lista, visão geral, impressão)
    src/deck.js         navegação, etapas, notas, janela do apresentador, animações
    src/sprite.svg      pictogramas reutilizados (<symbol>)
    src/slides/*.html   os slides, em ordem alfabética do nome do arquivo;
                        blocos <style> dentro deles sobem para o <head>
    src/fonts/*.woff2   Archivo e JetBrains Mono (SIL OFL), embutidas em base64
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SRC = AQUI / "src"
SAIDA = AQUI / "apresentacao-secim-visual.html"
TITULO = "IA além do chat"

FONTES = [
    # família, estilo, largura, peso, arquivo
    ("Archivo", "normal", "62% 125%", "100 900", "archivo-normal.woff2"),
    ("Archivo", "italic", "62% 125%", "100 900", "archivo-italic.woff2"),
    ("JetBrains Mono", "normal", "100%", "400 700", "jetbrains-normal.woff2"),
]

RE_STYLE = re.compile(r"<style>(.*?)</style>", re.S)


def fontes_css() -> str:
    regras = []
    for familia, estilo, largura, peso, arquivo in FONTES:
        dados = base64.b64encode((SRC / "fonts" / arquivo).read_bytes()).decode("ascii")
        regras.append(
            f"@font-face{{font-family:'{familia}';font-style:{estilo};font-weight:{peso};"
            f"font-stretch:{largura};font-display:block;"
            f"src:url(data:font/woff2;base64,{dados}) format('woff2');}}"
        )
    return "\n".join(regras)


def montar() -> tuple[str, str, str, int]:
    css = (SRC / "deck.css").read_text(encoding="utf-8")
    js = (SRC / "deck.js").read_text(encoding="utf-8")
    sprite = (SRC / "sprite.svg").read_text(encoding="utf-8")

    estilos, corpos = [], []
    for arq in sorted((SRC / "slides").glob("*.html")):
        texto = arq.read_text(encoding="utf-8")
        estilos.extend(RE_STYLE.findall(texto))
        corpos.append(f"<!-- {arq.name} -->\n" + RE_STYLE.sub("", texto).strip())

    slides = "\n\n".join(corpos)
    total = slides.count('<section class="slide')

    style = "\n".join([fontes_css(), css, *estilos])
    body = f"""<div class="viewport" id="viewport">
<main class="deck" id="deck">
{slides}
<div class="hud" id="hud" aria-hidden="true"></div>
</main>
</div>
{sprite}
<div class="notas" id="notas" role="region" aria-label="Notas do apresentador"></div>
<div class="aviso" id="aviso" role="status" aria-live="polite"></div>
<div class="breu" id="breu"></div>"""
    return style, body, js, total


def main() -> int:
    style, body, js, total = montar()

    completo = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITULO}</title>
<style>
{style}
</style>
</head>
<body>
{body}
<script>
{js}
</script>
</body>
</html>
"""
    SAIDA.write_text(completo, encoding="utf-8", newline="\n")
    print(f"[ok] {SAIDA.name}: {total} slides, {len(completo) // 1024} KB")

    if "--artifact" in sys.argv:
        destino = Path(sys.argv[sys.argv.index("--artifact") + 1])
        # Na página publicada o navegador não deixa baixar arquivos: troca o "salvar cópia" por um aviso.
        js_pub = re.sub(
            r"/\*SALVAR-INICIO\*/.*?/\*SALVAR-FIM\*/",
            "function salvaCopia() { mostraAviso('Nesta versão on-line não dá para salvar uma cópia. Use o arquivo local.', 4000); }",
            js, flags=re.S,
        )
        fragmento = f"<title>{TITULO}</title>\n<style>\n{style}\n</style>\n{body}\n<script>\n{js_pub}\n</script>\n"
        destino.write_text(fragmento, encoding="utf-8", newline="\n")
        print(f"[ok] versão para publicar: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
