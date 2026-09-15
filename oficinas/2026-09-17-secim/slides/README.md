# Slides da oficina do Secim

`apresentacao-secim.html` é a apresentação. Arquivo único, sem dependências: abre em qualquer navegador ou projetor, funciona **offline** (a fonte Open Sans vem embutida).

35 slides (31 na versão de 02/09; revisados em 14/09), Versão B (Degradê) da identidade oficial do Cefor. Gerado com a skill [`cefor-slides`](https://github.com/) a partir do [plano da oficina](../01-plano-da-oficina.md).

## No dia

| Tecla | O que faz |
|---|---|
| Setas, espaço | Avança e volta |
| Home / End | Primeiro e último slide |
| F | Tela cheia |
| E | Liga a edição de texto no próprio navegador; clique no texto e digite |
| Ctrl+S | No modo edição, salva uma cópia limpa |
| Esc | Sai do modo edição |
| Ctrl+P | Imprime ou gera PDF, um slide por página |

No celular, deslize para navegar.

## Como o deck mapeia o roteiro

Cada slide tem, no HTML, um comentário com o bloco do [`01-plano-da-oficina.md`](../01-plano-da-oficina.md) a que pertence. A ordem segue o roteiro:

| Slides | Bloco do plano | Tempo |
|---|---|---|
| 1–3 | Capa, link curto do material (projetado desde a clínica) e a tese da oficina | — |
| 4–6 | Bloco 1 · Abertura: 22.977 revisões em um dia | 5 min |
| 7–11 | Bloco 2 · Declarar, não esconder (9 cita o manual do Cefor) | 12 min |
| 12–15 | Bloco 3 · Pedir ou conduzir | 13 min |
| 16–17 | Bloco 4 · Antes de ir ao computador | 5 min |
| 18–23 | Bloco 5 · A pasta vira agente (21 e 22, Markdown e camadas, projetados enquanto a etapa 01 roda) | 25 min |
| 24 | Bloco 6 · Recapitulação | 5 min |
| 25–31 | Bloco 7 · Método e cuidados (27 conheça a máquina; 29 ferramenta pela conta; 30 modelo por etapa, primeiro corte) | 10 min |
| 32–35 | Bloco 8 · Fecho e encerramento | 10 min |

**Slide 16 (máquina de sorvete) não se corta**, em nenhuma hipótese. A ordem de corte está no plano.

## Como mudar o texto

Dois caminhos.

**Rápido, no navegador:** abra o HTML, tecle **E**, clique no texto, edite, **Ctrl+S**. Bom para ajustes de última hora. A alteração vale só para a cópia salva.

**Definitivo, na fonte:** edite a lista `DECK` no fim de [`build-slides.py`](build-slides.py) e rode:

```bash
python build-slides.py
```

O conteúdo está lá em português, sem HTML: cada slide é uma chamada de função com o título e os itens. O script regenera `corpos.html` e `apresentacao-secim.html`.

Precisa da skill instalada em `~/.claude/skills/cefor-slides`. Em outro caminho, aponte com a variável `CEFOR_SLIDES`. **Sem a skill**, o script avisa e troca só os slides dentro do `apresentacao-secim.html` já existente, preservando CSS e script: serve para mudar conteúdo, não para trocar de versão (A/B) nem o visual. Foi assim que a revisão de 14/09 foi gerada.

## Trocar para a Versão A (Cor Sólida)

O Cefor tem duas linguagens visuais. Escolhemos a **B (Degradê)** porque a tabela da skill indica a B para evento e palestra, e o Secim é isso. A **A (Cor Sólida)** é mais sóbria, com a seta CEFOR e painéis em lima.

Trocar não é só mudar um parâmetro: os modelos são diferentes (a seta CEFOR é exclusiva da A; a B usa os grafismos do degradê). É preciso reescrever os corpos nos modelos A1–A5. Se quiser a Versão A, peça.

## Exportar

O HTML é a entrega e a fonte da verdade. Sob demanda:

```bash
pip install odfpy                                              # LibreOffice Impress (recomendado)
python ~/.claude/skills/cefor-slides/scripts/generate-odp.py apresentacao-secim.html apresentacao-secim.odp

pip install python-pptx                                        # PowerPoint, se alguém exigir
python ~/.claude/skills/cefor-slides/scripts/generate-pptx.py apresentacao-secim.html apresentacao-secim.pptx
```

O `.odp` e o `.pptx` levam o texto editável, as tabelas e as cores; os grafismos do layout ficam no HTML. Quem abrir precisa ter a Open Sans instalada, senão a fonte é substituída.

## Verificação já feita

- O scaffold validou o deck: 31 slides, Versão B.
- Auditoria no Chrome, slide a slide: nada estoura o palco de 1920×1080 e nenhum texto fica cortado.
- Sem a seta CEFOR desenhada (correto para a Versão B), sem emoji, rodapé e logo IFES presentes.
- `h1` só na capa; títulos de conteúdo em `h2`; SVGs decorativos com `aria-hidden`.
- **14/09:** deck remontado sem o scaffold; o diff confirmou que só os slides revisados mudaram. No Edge headless a 1920×1080, nenhum dos 35 slides tem lista, tabela ou título passando do limite, e os slides 2, 22, 24, 27 e 29 foram conferidos por captura de tela.

## O que ainda falta

- Trocar "[link curto a definir]" nos slides 2 e 33 pelo link real (no `DECK` de `build-slides.py`) e regenerar.
- Conferir o slide 29 (ferramentas) depois do teste do Antigravity de 15/09.
- Conferir a projeção na sala: o palco escala sozinho, mas vale testar com o projetor do campus.
- Gerar o PDF (Ctrl+P) para a pasta do Drive e para o notebook do Elton.
- Não haverá ensaio cronometrado (decisão de 14/09).
