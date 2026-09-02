# Slides da oficina do Secim

`apresentacao-secim.html` é a apresentação. Arquivo único, sem dependências: abre em qualquer navegador ou projetor, funciona **offline** (a fonte Open Sans vem embutida).

31 slides, Versão B (Degradê) da identidade oficial do Cefor. Gerado com a skill [`cefor-slides`](https://github.com/) a partir do [plano da oficina](../01-plano-da-oficina.md).

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
| 1–2 | Capa e a tese da oficina | — |
| 3–5 | Bloco 1 · Abertura: 22.977 revisões em um dia | 5 min |
| 6–10 | Bloco 2 · Declarar, não esconder | 12 min |
| 11–14 | Bloco 3 · Pedir ou conduzir | 13 min |
| 15–16 | Bloco 4 · Antes de ir ao computador | 5 min |
| 17–20 | Bloco 5 · A pasta vira agente (demonstração) | 25 min |
| 21 | Bloco 6 · Recapitulação | 5 min |
| 22–27 | Bloco 7 · Método e cuidados | 10 min |
| 28–31 | Bloco 8 · Fecho e encerramento | 10 min |

**Slide 15 (máquina de sorvete) não se corta**, em nenhuma hipótese. A ordem de corte está no plano.

## Como mudar o texto

Dois caminhos.

**Rápido, no navegador:** abra o HTML, tecle **E**, clique no texto, edite, **Ctrl+S**. Bom para ajustes de última hora. A alteração vale só para a cópia salva.

**Definitivo, na fonte:** edite a lista `DECK` no fim de [`build-slides.py`](build-slides.py) e rode:

```bash
python build-slides.py
```

O conteúdo está lá em português, sem HTML: cada slide é uma chamada de função com o título e os itens. O script regenera `corpos.html` e `apresentacao-secim.html`.

Precisa da skill instalada em `~/.claude/skills/cefor-slides`. Em outro caminho, aponte com a variável `CEFOR_SLIDES`.

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

## O que ainda falta

- Trocar os três QR codes por imagens reais no slide 29 (avaliação, página de referências, pasta compartilhada) quando os links existirem.
- Conferir a projeção na sala: o palco escala sozinho, mas vale testar com o projetor do campus.
- Rodar o ensaio cronometrado de 14/09 com o deck aberto, na ordem do plano.
