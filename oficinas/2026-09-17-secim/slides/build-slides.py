#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gera os corpos de slide da apresentacao da oficina do Secim (17/09/2026)
e monta o deck com o scaffold da skill cefor-slides (Versao B, Degrade).

Como usar:
    python build-slides.py

O conteudo dos slides esta na lista DECK, no fim do arquivo, em portugues e
sem HTML: para mudar o texto da apresentacao, edite so essa lista.

Requer a skill instalada em ~/.claude/skills/cefor-slides (ou informe o caminho
em CEFOR_SLIDES). Sem a skill, o script troca so os slides dentro do
apresentacao-secim.html ja existente, preservando o CSS e o script do deck.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CEFOR_SLIDES = Path(
    os.environ.get("CEFOR_SLIDES", Path.home() / ".claude" / "skills" / "cefor-slides")
)
TITULO = "IA além do chat: usar bem, organizar e declarar na pós-graduação — Cefor/Ifes"
CORPOS = AQUI / "corpos.html"
SAIDA = AQUI / "apresentacao-secim.html"


# --------------------------------------------------------------------------
# Peças fixas da Versão B (Degradê). Sem seta CEFOR: na Versão B o acento
# gráfico são os grafismos do degradê.
# --------------------------------------------------------------------------

TRILHO_CONTEUDO = """    <div class="trilho" style="width:30%;background:var(--gray);border-top-right-radius:60px;border-bottom-right-radius:60px;">
      <div style="position:absolute;left:60px;top:130px;width:140px;height:140px;border:3px solid rgba(87,184,106,.4);border-radius:26px;"></div>
      <svg width="170" height="170" viewBox="0 0 100 100" style="position:absolute;left:230px;bottom:170px;" aria-hidden="true">
        <circle cx="50" cy="50" r="46" fill="none" stroke="rgba(54,180,166,.42)" stroke-width="1.6"/>
        <circle cx="50" cy="50" r="30" fill="none" stroke="rgba(54,180,166,.32)" stroke-width="1.6"/>
      </svg>
    </div>"""

TRILHO_DEGRADE = """    <div class="trilho" style="width:34%;background:var(--grad);border-top-right-radius:60px;border-bottom-right-radius:60px;">
      <div style="position:absolute;left:64px;top:110px;width:150px;height:150px;border:3px solid rgba(255,255,255,.32);border-radius:26px;"></div>
      <svg width="190" height="190" viewBox="0 0 100 100" style="position:absolute;left:210px;bottom:150px;" aria-hidden="true">
        <circle cx="50" cy="50" r="46" fill="none" stroke="rgba(255,255,255,.30)" stroke-width="1.6"/>
        <circle cx="50" cy="50" r="30" fill="none" stroke="rgba(255,255,255,.24)" stroke-width="1.6"/>
      </svg>
      <svg width="300" height="8" style="position:absolute;left:70px;bottom:90px;" aria-hidden="true">
        <line x1="0" y1="4" x2="300" y2="4" stroke="rgba(255,255,255,.5)" stroke-width="3" stroke-dasharray="2 14" stroke-linecap="round"/>
      </svg>
    </div>"""

RODAPE_CONTEUDO = """    <div style="position:absolute;right:0;bottom:84px;left:30%;height:4px;background:var(--olive);"></div>
    <div class="rodape" style="position:absolute;right:56px;bottom:48px;background:#fff;padding-left:28px;display:flex;justify-content:space-between;width:70%;align-items:center;">
      <span>cefor.ifes.edu.br</span>
      <span class="slide-counter">1 / 1</span>
    </div>"""

RODAPE_SECAO = """    <div style="position:absolute;right:0;bottom:96px;left:34%;height:4px;background:var(--olive);"></div>
    <div class="rodape" style="position:absolute;right:56px;bottom:48px;background:#fff;padding-left:28px;">cefor.ifes.edu.br</div>"""


def logo_ifes(cor: str = "#3A9E3A", ponto: str = "#CE1126", larg: int = 52,
              alt: int = 70, t1: int = 22, t2: int = 17, t3: int = 15) -> str:
    """Assinatura IFES/Cefor. cor='#fff' para a versão em negativo."""
    quadrados = "".join(
        f'<rect x="{x}" y="{y}" width="9" height="9" rx="1.4" fill="{cor}"/>'
        for x, y in [(0, 11), (0, 22), (0, 33), (11, 0), (11, 11),
                     (11, 22), (11, 33), (22, 0), (22, 22)]
    )
    return f"""      <div style="display:flex;align-items:center;gap:13px;">
        <svg width="{larg}" height="{alt}" viewBox="0 0 31 42" style="flex:none;display:block;" role="img" aria-label="Instituto Federal do Espírito Santo — Centro de Referência em Formação e em Educação a Distância">
          <circle cx="4.5" cy="4.5" r="4.5" fill="{ponto}"/>{quadrados}
        </svg>
        <div style="line-height:1.14;">
          <div style="font-weight:800;font-size:{t1}px;">INSTITUTO FEDERAL</div>
          <div style="font-weight:600;font-size:{t2}px;">Espírito Santo</div>
          <div style="font-weight:400;font-size:{t3}px;">Centro de Referência em Formação<br>e em Educação a Distância</div>
        </div>
      </div>"""


def cabecalho(titulo: str) -> str:
    """Barra de título em degradê + sublinhado com 'tique' (modelo B4)."""
    return f"""    <div style="position:absolute;left:660px;top:92px;right:108px;">
      <div class="barra-titulo b reveal"><h2 class="t-conteudo">{titulo}</h2></div>
      <div style="position:relative;height:10px;background:var(--ink);border-radius:5px;margin-top:18px;"><div style="position:absolute;left:62%;top:10px;width:10px;height:32px;background:var(--ink);"></div></div>
    </div>"""


def slide(nota: str, miolo: str, modelo: str = "B4", fundo: str = "#fff") -> str:
    trilho = TRILHO_DEGRADE if modelo == "B3" else TRILHO_CONTEUDO
    rodape = RODAPE_SECAO if modelo == "B3" else RODAPE_CONTEUDO
    return (f'  <!-- {modelo} · {nota} -->\n'
            f'  <section class="slide" style="background:{fundo};">\n'
            f'{trilho}\n{miolo}\n{rodape}\n  </section>')


# --------------------------------------------------------------------------
# Modelos de slide
# --------------------------------------------------------------------------

def capa(eyebrow: str, titulo: str, subtitulo: str) -> str:
    """Modelo B1: fundo degradê inteiro, grafismos brancos, logo em negativo."""
    return f"""  <!-- B1 · Capa -->
  <section class="slide active">
    <div style="position:absolute;right:150px;top:120px;width:220px;height:220px;border:4px solid rgba(255,255,255,.34);border-radius:34px;"></div>
    <div style="position:absolute;right:300px;top:270px;width:130px;height:130px;border:3px solid rgba(255,255,255,.26);border-radius:24px;"></div>
    <div style="position:absolute;right:110px;bottom:190px;width:88px;height:88px;border:3px solid rgba(255,255,255,.22);border-radius:18px;"></div>
    <svg width="260" height="260" viewBox="0 0 100 100" style="position:absolute;left:1310px;bottom:110px;" aria-hidden="true">
      <circle cx="50" cy="50" r="46" fill="none" stroke="rgba(255,255,255,.30)" stroke-width="1.6"/>
      <circle cx="50" cy="50" r="32" fill="none" stroke="rgba(255,255,255,.26)" stroke-width="1.6"/>
      <circle cx="50" cy="50" r="18" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="1.6"/>
    </svg>
    <svg width="420" height="8" style="position:absolute;left:190px;bottom:330px;" aria-hidden="true">
      <line x1="0" y1="4" x2="420" y2="4" stroke="rgba(255,255,255,.55)" stroke-width="3" stroke-dasharray="2 14" stroke-linecap="round"/>
    </svg>
    <div style="position:absolute;left:190px;top:296px;right:400px;color:#fff;">
      <div class="eyebrow reveal" style="color:rgba(255,255,255,.92);">{eyebrow}</div>
      <h1 class="t-capa reveal" style="color:#fff;margin-top:24px;text-shadow:0 2px 10px rgba(0,0,0,.22);">{titulo}</h1>
      <p class="corpo reveal" style="color:rgba(255,255,255,.94);font-size:30px;margin-top:30px;">{subtitulo}</p>
    </div>
    <div style="position:absolute;left:190px;bottom:88px;color:#fff;">
{logo_ifes(cor="#fff", ponto="#fff")}
    </div>
  </section>"""


def divisoria(numero: str, titulo: str, nota: str) -> str:
    """Modelo B3: divisória de seção."""
    miolo = f"""    <div style="position:absolute;left:800px;top:412px;right:160px;">
      <div class="num-secao reveal" style="color:var(--gray-dk);">{numero}</div>
      <h2 class="t-secao reveal" style="color:#1f3a52;margin-top:12px;">{titulo}</h2>
      <div class="reveal" style="display:flex;gap:14px;margin-top:36px;">
        <div style="width:120px;height:10px;background:#57B86A;border-radius:5px;"></div>
        <div style="width:60px;height:10px;background:var(--navy);border-radius:5px;"></div>
      </div>
    </div>"""
    return slide(nota, miolo, modelo="B3")


def lista(titulo: str, itens: list[str], nota: str, top: int = 380,
          gap: int = 36, rodape_extra: str = "") -> str:
    """Modelo B4: conteúdo com lista de bullets."""
    lis = "\n".join(
        f'      <li class="reveal" style="display:flex;gap:28px;align-items:flex-start;">'
        f'<span class="bullet b"></span><span class="corpo">{it}</span></li>'
        for it in itens
    )
    extra = (f'\n    <p class="corpo" style="position:absolute;left:668px;bottom:150px;right:128px;'
             f'color:var(--muted);font-size:24px;">{rodape_extra}</p>' if rodape_extra else "")
    miolo = (f"{cabecalho(titulo)}\n"
             f'    <ul style="position:absolute;left:668px;top:{top}px;right:128px;'
             f'display:flex;flex-direction:column;gap:{gap}px;list-style:none;">\n'
             f"{lis}\n    </ul>{extra}")
    return slide(nota, miolo)


def indicadores(titulo: str, cards: list[tuple[str, str]], nota: str,
                colunas: int = 2, top: int = 320, num_px: int = 64,
                rodape_extra: str = "") -> str:
    """Modelo B4 estendido: indicadores (KPI)."""
    cs = "\n".join(
        f'        <div class="kpi-card"><div class="kpi-num" style="font-size:{num_px}px;">{n}</div>'
        f'<div class="kpi-label">{r}</div></div>'
        for n, r in cards
    )
    extra = (f'\n    <p class="corpo" style="position:absolute;left:668px;bottom:150px;right:128px;'
             f'color:var(--muted);font-size:24px;">{rodape_extra}</p>' if rodape_extra else "")
    miolo = (f"{cabecalho(titulo)}\n"
             f'    <div style="position:absolute;left:668px;top:{top}px;right:128px;" class="reveal">\n'
             f'      <div class="kpi-grid" style="grid-template-columns:repeat({colunas},1fr);">\n'
             f"{cs}\n      </div>\n    </div>{extra}")
    return slide(nota, miolo)


def tabela(titulo: str, cabecalhos: list[str], linhas: list[list[str]],
           nota: str, top: int = 300) -> str:
    """Modelo B4 estendido: tabela com cabeçalho em degradê."""
    th = "".join(
        f'<th style="background:var(--grad);color:#fff;border-bottom-color:var(--ink);">{c}</th>'
        for c in cabecalhos
    )
    tr = "\n".join(
        "          <tr>" + "".join(f"<td>{c}</td>" for c in linha) + "</tr>"
        for linha in linhas
    )
    miolo = (f"{cabecalho(titulo)}\n"
             f'    <div style="position:absolute;left:668px;top:{top}px;right:128px;" class="reveal">\n'
             f'      <table class="admin-table">\n        <thead>\n          <tr>{th}</tr>\n        </thead>\n'
             f"        <tbody>\n{tr}\n        </tbody>\n      </table>\n    </div>")
    return slide(nota, miolo)


def destaque(titulo: str, frase: str, atribuicao: str, nota: str,
             aspas: bool = False, tamanho: int = 50) -> str:
    """Modelo B4 estendido: mensagem-chave ou citação."""
    marca = ('      <div class="reveal" style="font-size:128px;font-weight:800;color:#36B4A6;'
             'line-height:.6;" aria-hidden="true">&ldquo;</div>\n' if aspas else "")
    attr = (f'\n      <div class="reveal" style="font-size:28px;color:var(--muted);'
            f'margin-top:36px;">{atribuicao}</div>' if atribuicao else "")
    miolo = (f"{cabecalho(titulo)}\n"
             f'    <div style="position:absolute;left:668px;top:340px;right:128px;">\n'
             f"{marca}"
             f'      <div class="reveal" style="font-size:{tamanho}px;font-weight:700;color:#1f3a52;'
             f'line-height:1.32;">{frase}</div>{attr}\n    </div>')
    return slide(nota, miolo)


def etapas(titulo: str, passos: list[tuple[str, str, str]], nota: str) -> str:
    """Modelo B4 estendido: linha do tempo horizontal (3 etapas)."""
    its = "\n".join(
        f'        <div class="timeline-item"><div class="timeline-dot">{n}</div>'
        f'<div class="timeline-title">{t}</div><div class="timeline-desc">{d}</div></div>'
        for n, t, d in passos
    )
    miolo = (f"{cabecalho(titulo)}\n"
             f'    <div style="position:absolute;left:640px;top:330px;right:100px;" class="reveal">\n'
             f'      <div class="timeline">\n{its}\n      </div>\n    </div>')
    return slide(nota, miolo)


def encerramento(contatos: list[str]) -> str:
    """Modelo B5: encerramento."""
    linhas = "".join(
        f'<div class="corpo" style="font-size:26px;color:var(--muted);">{c}</div>'
        for c in contatos
    )
    return f"""  <!-- B5 · Encerramento -->
  <section class="slide" style="background:#fff;">
{TRILHO_DEGRADE}
    <div style="position:absolute;left:820px;top:250px;right:140px;">
      <div style="font-size:104px;font-weight:800;color:#1f3a52;line-height:1;" class="reveal">Obrigado!</div>
      <div style="width:440px;height:8px;background:var(--grad);margin-top:36px;" class="reveal"></div>
      <div class="reveal" style="margin-top:40px;display:flex;flex-direction:column;gap:10px;">{linhas}</div>
    </div>
    <div style="position:absolute;left:820px;bottom:150px;color:#1a1a1a;">
{logo_ifes(larg=56, alt=76, t1=22, t2=17, t3=15)}
    </div>
    <div class="rodape" style="position:absolute;right:56px;bottom:48px;background:#fff;padding-left:28px;">cefor.ifes.edu.br</div>
  </section>"""


# ==========================================================================
# CONTEÚDO DA APRESENTAÇÃO — edite daqui para baixo
# Cada item traz, no comentário "nota", o bloco do 01-plano-da-oficina.md a
# que pertence, para o deck e o roteiro andarem juntos.
# ==========================================================================

DECK = [
    capa(
        eyebrow="Secim 2026 · Ifes campus Vitória",
        titulo="IA além do chat:<br>usar bem, organizar e declarar<br>na pós-graduação",
        subtitulo="17 de setembro de 2026 · Elton Vinícius Silva e Marcos Accioly<br>Coordenadoria-Geral de Tecnologias Educacionais · Cefor/Ifes",
    ),

    destaque(
        "Antes de começar: abra o material",
        "[link curto a definir]",
        "Digite no navegador do notebook ou do celular. Lá estão a preparação, o kit, o modelo de declaração e os prompts.",
        nota="Chegada · projetar desde as 15h30 e durante a calibragem. Link curto é melhor que QR: notebook não lê QR. TROCAR pelo link real.",
        tamanho=72,
    ),

    lista(
        "A oficina inteira em quatro frases",
        [
            "<strong>Declarar bem</strong> exige saber o que a IA fez.",
            "<strong>Saber o que a IA fez</strong> exige um processo visível.",
            "<strong>Um processo visível</strong> exige organização.",
            "<strong>Organização, no computador,</strong> é pasta e arquivo com instrução em texto.",
        ],
        nota="Bloco 1 · a tese. Voltamos a ela na recapitulação.",
        top=360,
        gap=34,
    ),

    # ---------------------------------------------------------------- 01
    divisoria("01", "Declarar, não esconder", nota="Bloco 2 · 12 min · Elton"),

    indicadores(
        "A IA já está dos dois lados da mesa",
        [
            ("22.977", "Revisões escritas por IA na conferência AAAI-26, todas identificadas como tais"),
            ("1 dia", "Tempo que o sistema levou para revisar tudo. Menos de vinte e quatro horas"),
            ("29.000", "Submissões recebidas, quase o dobro do ano anterior"),
            ("43%", "Das revisões da ICLR 2026 teriam sido escritas inteiramente por humanos"),
        ],
        nota="Bloco 1 · abertura · 5 min. Fonte: Silvio Meira, 2026.",
        rodape_extra="Na pesquisa feita depois, os autores preferiram a revisão da máquina à humana em acurácia técnica.",
    ),

    destaque(
        "A pergunta mudou",
        "A pergunta deixa de ser <em>quem escreveu isso?</em><br>e passa a ser <em>isso se sustenta?</em>",
        "Silvio Meira · 29.000 papers: o fim da ciência SEM IA · 2026",
        nota="Bloco 1 · a ponte para o bloco de ética.",
        aspas=True,
    ),

    indicadores(
        "O que a norma pede que você declare",
        [
            ("Ferramenta", "Qual IA, qual modelo ou versão, e quando você usou"),
            ("Finalidade", "Para quê, concretamente: fichar, revisar, traduzir, analisar"),
            ("Fase", "Em que momento: concepção, levantamento, análise, redação, revisão"),
        ],
        nota="Bloco 2 · Portaria CNPq 2.664/2026. Os três dados que o registro do kit guarda sozinho.",
        colunas=3,
        top=340,
        num_px=36,
        rodape_extra="Portaria CNPq nº 2.664, de 6 de março de 2026 — Política de Integridade na Atividade Científica.",
    ),

    lista(
        "A Portaria, em quatro pontos",
        [
            "<strong>Declare em qualquer fase</strong> da pesquisa, da concepção à submissão.",
            "<strong>A IA não é autora.</strong> Apresentar conteúdo dela como humano é proibido.",
            "<strong>A IA não faz parecer.</strong> O uso em revisão por pares é vedado.",
            "<strong>Você responde por tudo,</strong> inclusive pelo erro que a ferramenta cometeu.",
        ],
        nota="Bloco 2 · o essencial da norma, sem juridiquês.",
        top=380,
    ),

    lista(
        "E na sua dissertação, onde isso entra?",
        [
            "A <strong>CAPES</strong> ainda não tem norma própria e orientou os programas a usar a Portaria do CNPq como referência.",
            "Universidades já têm modelo. Na UFRRJ, a declaração fica na <strong>parte pré-textual, após os agradecimentos</strong>.",
            "No Ifes, o <strong>Manual de Uso Ético de IA</strong> do Cefor também sugere como declarar.",
            "O piso é a norma nacional. <strong>Seu programa, sua banca e o periódico podem pedir mais.</strong> Pergunte.",
        ],
        nota="Bloco 2 · dizer 'a CAPES orientou', sem citar número de ofício. Manual: conferir antes se a sugestão cobre ferramenta, finalidade e fase.",
        top=370,
        gap=32,
    ),

    lista(
        "Antes de usar IA na pesquisa, quatro perguntas",
        [
            "Posso subir <strong>estes dados</strong> para uma ferramenta na nuvem?",
            "Consigo <strong>verificar</strong> cada referência, página e número que ela me der?",
            "Saberei dizer à banca <strong>o que a IA fez</strong> e o que eu fiz?",
            "A interpretação, as conclusões e a <strong>responsabilidade</strong> continuam minhas?",
        ],
        nota="Bloco 2 · também está na folha e na página de referências.",
        top=380,
    ),

    destaque(
        "Por que isso vira método, e não só cuidado",
        "A declaração não sai da sua cabeça.<br>Ela sai do rastro do que você fez.",
        "",
        nota="Bloco 2 · fecho. É a ponte para o bloco 3.",
        tamanho=54,
    ),

    # ---------------------------------------------------------------- 02
    divisoria("02", "Pedir ou conduzir", nota="Bloco 3 · 13 min · Marquito"),

    lista(
        "Um bom pedido tem cinco partes",
        [
            "<strong>Persona</strong> — quem a IA deve ser nesta tarefa.",
            "<strong>Alvo</strong> — o que você quer obter, em uma frase.",
            "<strong>Recebedores</strong> — quem vai ler o resultado depois.",
            "<strong>Tema</strong> — o assunto, com o seu contexto de pesquisa.",
            "<strong>Estrutura</strong> — em que formato, em que etapas, com o que verificar.",
        ],
        nota="Bloco 3 · modelo P.A.R.T.E., de Hugo Cristo (PPGP/UFES).",
        top=350,
        gap=28,
    ),

    tabela(
        "O mesmo artigo, dois resultados",
        ["", "Pedido solto", "Processo com rastro"],
        [
            ["O que sai", "Um texto corrido", "Fichas, tabela e lacunas"],
            ["Dá para verificar?", "Difícil", "Cada afirmação aponta ficha e página"],
            ["Dá para declarar?", "Só “usei IA”", "Ferramenta, finalidade e fase"],
            ["Serve na próxima vez?", "Não", "Vira arquivo; troque só os artigos"],
        ],
        nota="Bloco 3 · a diferença que importa é no PROCESSO, não no resultado: como você sabe o que a IA fez, de onde saiu cada frase, onde mexer.",
    ),

    indicadores(
        "Por que ela piora numa conversa longa",
        [
            ("2 a 8 mil", "Tokens que uma etapa bem delimitada consome para trabalhar"),
            ("30 a 50 mil", "Tokens de uma conversa que tenta fazer tudo de uma vez"),
        ],
        nota="Bloco 3 · janela de contexto. Falar, não demonstrar: encher a janela leva tempo demais.",
        top=360,
        rodape_extra="É nessa segunda faixa que os modelos começam a perder o fio, e você não vê acontecer. Quanto mais delimitada a etapa, menos ela gasta e melhor faz.",
    ),

    # ---------------------------------------------------------------- 03
    destaque(
        "Antes de irmos ao computador",
        "A gente vai montar a máquina de sorvete.<br>Vai dar vontade de pedir logo o sorvete.<br>Não peça.",
        "Se o sorvete sair ruim, não conserte o sorvete: volte e conserte a máquina.",
        nota="Bloco 4 · 5 min · a metáfora que funcionou no Concefor. NUNCA cortar este slide.",
        tamanho=50,
    ),

    lista(
        "O erro nº 1, e quem mais cai nele",
        [
            "“<strong>Me dá logo o texto da revisão de literatura.</strong>” Isso é pedir o sorvete.",
            "Quem tem <strong>mais</strong> facilidade com computador cai mais nessa, não menos.",
            "O que interessa não é o resultado de hoje. É a máquina que vai fazer os próximos cinquenta.",
        ],
        nota="Bloco 4 · avisar antes do erro acontecer, não depois.",
        top=400,
    ),

    # ---------------------------------------------------------------- 04
    divisoria("03", "A pasta vira agente", nota="Bloco 5 · 25 min · demonstração ao vivo"),

    lista(
        "O que faz uma pasta virar um agente",
        [
            "Um <strong>README</strong> que explica a pasta. É o primeiro arquivo que a IA lê.",
            "Um <strong>CONTEXT.md por etapa</strong>: o que entra, o que a IA faz, o que sai.",
            "Um <strong>registro</strong> que anota cada ação: ferramenta, o que fez, o que conferir.",
            "Nada de mágico: são <strong>arquivos de texto</strong> que você abre, lê e edita.",
        ],
        nota="Bloco 5 · mostrar na tela enquanto fala. Abrir o CONTEXT.md e ler em voz alta.",
        top=380,
        rodape_extra="Como seria se toda pasta do seu computador tivesse um leia-me?",
    ),

    etapas(
        "O kit que você leva tem três etapas",
        [
            ("01", "Fichamento", "Cada artigo vira uma ficha com referência, achados e citação com página."),
            ("02", "Correlação", "As fichas cruzam com o seu tema: convergências, divergências e lacunas."),
            ("03", "Relatório e declaração", "O registro do que a IA fez vira o rascunho da sua declaração."),
        ],
        nota="Bloco 5 · rodar a etapa 01 ao vivo; pular a 02; mostrar a 03 gerando a declaração. Dizer: não é sobre esta pasta, é uma máquina para entender como a máquina funciona; 00-entrada é a única pasta que você alimenta.",
    ),

    lista(
        "Markdown, a língua franca entre você e a IA",
        [
            "<strong>Língua franca</strong> é a que pessoas de línguas diferentes adotam para se entender.",
            "<strong>Markdown</strong> é texto com poucas marcações (# título, - lista). Não é código.",
            "Você lê bem, a IA lê bem, qualquer ferramenta abre. <strong>O PDF, não:</strong> cada um vem de um jeito e gasta muito mais.",
            "Converta uma vez e trabalhe em texto. <strong>A conversão é outra máquina</strong>, separada da sua.",
        ],
        nota="Bloco 5 · mostrar enquanto a etapa 01 roda. Termo de Hugo Cristo. Conceito: biblioteca/conceitos/markdown-lingua-franca.md.",
        top=380,
        gap=32,
    ),

    tabela(
        "Contexto em camadas: cada etapa leva só o que precisa",
        ["", "Na janela do chat", "Na pasta com etapas"],
        [
            ["O que a IA carrega", "Tudo o que foi colado e conversado", "O contrato da etapa e a saída da anterior"],
            ["Com o tempo", "A conversa cresce e a qualidade cai", "Cada etapa começa leve"],
            ["Os artigos", "Dentro da conversa, o tempo todo", "Nos arquivos; ela abre quando precisa"],
            ["Se ela se desviar", "Você nem percebe", "O registro mostra o que ela leu e fez"],
        ],
        nota="Bloco 5 · mostrar enquanto a etapa 01 roda. Ela às vezes sai da cerca e lê o que não foi indicado; ainda assim, é bem menos do que carregar tudo.",
    ),

    destaque(
        "A diferença que importa",
        "Não dá para ver o que há dentro do modelo.<br>Mas dá para ver o caminho que você<br>pediu para ele seguir, e por onde ele passou.",
        "",
        nota="Bloco 5 · fecho da demonstração. Na web também não se vê o treino do modelo; na pasta, o caminho fica visível.",
        tamanho=46,
    ),

    lista(
        "Onde chegamos",
        [
            "A norma pede três coisas: <strong>ferramenta, finalidade e fase</strong>.",
            "O processo entrega as três, <strong>sem você ter que lembrar</strong> de nada.",
            "A pasta é <strong>o processo escrito</strong>, em texto que você controla.",
            "O registro é <strong>a sua declaração quase pronta</strong>.",
            "<strong>Não é garantia:</strong> a IA ainda pode ignorar uma instrução. Mas direciona muito melhor, e você vê onde ela errou.",
        ],
        nota="Bloco 6 · 5 min · recapitulação prevista, de pé. Perguntar quem chegou a que nível.",
        top=350,
        gap=28,
    ),

    # ---------------------------------------------------------------- 05
    divisoria("04", "Método e cuidados", nota="Bloco 7 · 10 min · Marquito"),

    lista(
        "O método tem nome, artigo e cinco princípios",
        [
            "<strong>Uma etapa, um trabalho.</strong> Quem pesquisa não escreve; quem escreve não formata.",
            "<strong>Texto simples como interface.</strong> Markdown, que qualquer ferramenta lê.",
            "<strong>Contexto em camadas.</strong> Cada etapa carrega só o que precisa.",
            "<strong>Toda saída é editável</strong> por você antes da etapa seguinte.",
            "<strong>Configure a fábrica, não o produto.</strong>",
        ],
        nota="Bloco 7 · ICM (Van Clief e McDermott, 2026). O artigo está na página: vocês são pesquisadores, leiam.",
        top=350,
        gap=28,
    ),

    lista(
        "Conheça a máquina que você cria",
        [
            "<strong>Confira a máquina que a IA montou.</strong> Se entrou um parafuso errado, sai metal junto com o sorvete.",
            "Sorvete mole? <strong>Quem conhece a máquina sabe onde olhar.</strong> É tudo texto, e a IA explica o que você não entender.",
            "<strong>Uma máquina, um trabalho.</strong> A de casquinha fica fora da de sorvete: converter PDF é outra pasta.",
            "<strong>Nem tudo merece máquina.</strong> Com pressa, ou para algo que fará uma vez só, faça do jeito de sempre.",
        ],
        nota="Bloco 7 · substitui o slide dos percentuais (92%, 30%, 78%), que ficou só como rodapé com a fonte.",
        top=370,
        gap=30,
        rodape_extra="Capriche na entrada, confie no meio, verifique a saída: 30 de 33 praticantes ouvidos no estudo do ICM (Van Clief e McDermott, 2026) editam mais a primeira e a última etapa.",
    ),

    lista(
        "Três regras, porque agora a IA mexe no seu computador",
        [
            "<strong>Leia o que ela pede permissão para fazer.</strong> No começo, toda vez: é assim que você aprende como a máquina funciona.",
            "<strong>Só libere de vez</strong> um tipo de pedido quando souber o que ele faz e que não oferece risco.",
            "<strong>Não suba dados de participantes</strong> sem saber para onde eles vão.",
        ],
        nota="Bloco 7 · dois minutos, sem lista de horrores. Isto amplia o poder e amplia o perigo. Com o tempo, pedidos da mesma natureza podem ser liberados.",
        top=400,
    ),

    tabela(
        "Qual ferramenta? Comece pela conta que você já tem",
        ["Você tem", "Use", "Custo"],
        [
            ["Conta Google pessoal", "<strong>Google Antigravity</strong> (recomendado)", "Gratuito, com limite semanal"],
            ["Conta no GitHub", "VS Code + GitHub Copilot, modo Agent", "Gratuito, ~50 interações por mês"],
            ["Assinatura de IA", "Claude Code, Claude Cowork, Codex", "Incluído no plano pago"],
            ["Só o navegador", "Claude, ChatGPT ou Gemini, com o prompt do processo", "Gratuito"],
        ],
        nota="Bloco 7 · hoje demonstramos com Claude Code, mas a pasta não depende de nenhuma IA: dá para trocar de ferramenta sem perder o processo. Antigravity: plano individual gratuito, limite semanal sem número publicado (página oficial, 14/09/2026). Conferir no teste de 15/09.",
    ),

    lista(
        "Qual modelo? Depende da etapa",
        [
            "<strong>Modelos de fronteira</strong>, os mais capazes e caros: para pensar, planejar e dar direção.",
            "<strong>Modelos menores</strong>, rápidos e baratos: para organizar, converter e formatar.",
            "Organizar a bibliografia, o bolsista faz. <strong>Dar a direção é com quem orienta.</strong>",
            "Modelo fraco na etapa da direção <strong>leva você longe, rápido, para o lugar errado</strong>.",
        ],
        nota="Bloco 7 · 1 min; primeiro corte do bloco. A máquina é a pasta; o modelo é quem você chama para cada etapa. Não misturar as metáforas.",
        top=380,
        gap=32,
    ),

    destaque(
        "A provocação que fica",
        "A IA amplifica organização<br>ou amplifica desorganização.<br>Vocês escolhem qual.",
        "",
        nota="Bloco 7 · versão construtiva da provocação. Sem palavrão.",
        tamanho=50,
    ),

    # ---------------------------------------------------------------- fecho
    lista(
        "O que você leva daqui hoje",
        [
            "<strong>O que a norma pede</strong> e um modelo de declaração para adaptar.",
            "<strong>Uma pasta que vira agente</strong>, e a certeza de que é só pasta e arquivo.",
            "<strong>Um prompt que guia a criação da sua primeira pasta</strong>, e o kit para baixar.",
            "Travou em algum ponto? Normal. <strong>Ninguém sai daqui operando sozinho</strong>, e todo passo dado vale.",
        ],
        nota="Bloco 8 · 10 min · Elton. Assistir, fazer no navegador, fazer no computador ou sentar à máquina: tudo vale. Tem gente que vai travar, e isso é normal.",
        top=370,
        gap=32,
    ),

    lista(
        "Onde continuar depois de hoje",
        [
            "<strong>Papo com IA.IÁ</strong> — online, toda quinta, das 15h às 15h45. Leve o que travou.",
            "<strong>Curso de extensão</strong> “Inteligência de Contexto Pedagógica com IA” — previsto para 2027, 90 h, a distância.",
            "<strong>A página com tudo</strong> — norma, modelo, prompts e kit: [link curto a definir].",
            "Em casa, o <strong>primeiro pedido</strong> é sempre: “leia o README e me explique o que esta pasta faz”.",
        ],
        nota="Bloco 8 · QR da avaliação: o link do material aparece no fim do formulário. Coletar fichas ANTES de todo mundo levantar. O e-mail de contato fica no último slide.",
        top=370,
        gap=32,
    ),

    destaque(
        "O que sobra para nós",
        "O gargalo virou atenção, confiança e julgamento sobre o que importa. E nenhuma dessas três escala.",
        "Silvio Meira, 2026 · “E daí? Por que isso importa?” é a pergunta que máquina nenhuma responde por você.",
        nota="Bloco 8 · fecho.",
        aspas=True,
        tamanho=46,
    ),

    encerramento([
        "Elton Vinícius Silva · Marcos Vinícius Forecchi Accioly",
        "Coordenadoria-Geral de Tecnologias Educacionais · Cefor/Ifes",
        "cgte.cefor@ifes.edu.br",
    ]),
]


def remontar_deck_existente() -> int:
    """Sem a skill: troca só os slides do deck já gerado, preservando CSS e script.

    Serve para ajustes de conteúdo. Trocar de versão (A/B) ou de CSS exige o scaffold.
    """
    html = SAIDA.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in html else "\n"
    abre = html.find('<main class="deck-stage" id="deckStage">')
    fecha = html.find("</main>", abre)
    if abre < 0 or fecha < 0:
        print(f"[ERRO] palco dos slides não encontrado em {SAIDA.name}.", file=sys.stderr)
        return 1
    inicio = html.find(nl, abre) + len(nl)
    fim = html.rfind(nl, 0, fecha) + len(nl)
    corpos = ("\n\n".join(DECK) + "\n").replace("\n", nl)
    SAIDA.write_bytes((html[:inicio] + corpos + html[fim:]).encode("utf-8"))
    print(f"[OK] deck em {SAIDA} ({len(DECK)} slides, sem o scaffold)")
    return 0


def main() -> int:
    scaffold = CEFOR_SLIDES / "scripts" / "new-deck.py"
    CORPOS.write_text("\n\n".join(DECK) + "\n", encoding="utf-8")
    print(f"[OK] {len(DECK)} corpos de slide em {CORPOS.name}")

    if not scaffold.exists():
        if SAIDA.exists():
            print(f"[AVISO] scaffold não encontrado em {scaffold}.")
            return remontar_deck_existente()
        print(f"[ERRO] scaffold não encontrado em {scaffold}.\n"
              f"       Instale a skill ou defina CEFOR_SLIDES.", file=sys.stderr)
        return 1

    r = subprocess.run(
        [sys.executable, str(scaffold), "--version", "B", "--title", TITULO,
         "--slides", str(CORPOS), "--out", str(SAIDA)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    # O console do Windows costuma ser cp1252: imprime sem quebrar em acento.
    saida = ((r.stdout or "").strip() or (r.stderr or "").strip())
    enc = sys.stdout.encoding or "utf-8"
    print(saida.encode(enc, errors="replace").decode(enc, errors="replace"))
    if r.returncode == 0:
        print(f"[OK] deck em {SAIDA}")
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
