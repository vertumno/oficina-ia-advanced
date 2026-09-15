# Slides visuais da oficina do Secim

`apresentacao-secim-visual.html` é uma segunda versão da apresentação, feita do zero, sem a identidade visual do deck original (`../slides/`). O conteúdo e a **ordem dos 35 slides são os mesmos**, então as referências do plano ("slide 2", "slide 16", "slides 21 e 22"...) continuam valendo.

Arquivo único: abre em qualquer navegador e funciona **offline** (as fontes Archivo e JetBrains Mono, licença SIL OFL, vêm embutidas).

## A linguagem visual

Cada slide tem uma afirmação no título e um desenho que mostra o mecanismo. As cores têm papel fixo:

| Cor | Significa |
|---|---|
| Laranja | O que a IA faz (etapas, ações no registro, a máquina) |
| Azul | O que você faz, decide e confere (revisão humana, perguntas, o prompt) |
| Amarelo | O que precisa ser visto, verificado ou declarado (a declaração, os grifos) |
| Pontilhado | O rastro: liga o chat à pasta, as etapas ao registro, o registro à declaração |

Onde há números, o desenho está em escala: os 29.000 pontos do slide 5 (um por submissão), a régua de 0 a 50 mil tokens do slide 15 e o padrão em U do slide 27.

## No dia

| Tecla | O que faz |
|---|---|
| Setas, espaço, PageUp/PageDown | Avança e volta (inclui os cliques dentro do slide; funciona com passador) |
| Número + Enter | Vai direto ao slide (ex.: 21 Enter durante a etapa 01) |
| Home / End | Primeiro e último slide |
| F | Tela cheia |
| O | Visão geral de todos os slides; clique em um para abrir |
| N | Notas do apresentador na parte de baixo da tela |
| P | Janela do apresentador: notas, próximo slide, relógio e cronômetro |
| B | Tela preta (de novo para voltar) |
| E | Edição rápida do texto; Ctrl+S salva uma cópia; Esc sai |
| ? | Mostra os atalhos |

Slides com cliques internos: 3 (quatro camadas), 7 (três vértices), 10 (quatro perguntas), 13 (cinco exemplos), 14 (processo e comparação), 15 (a escala), 16 (três cliques, **nunca cortar**), 17 (os cinquenta), 19 (o leia-me) e 24 (recapitulação). A janela do apresentador avisa quantos cliques faltam.

No celular, a apresentação vira uma lista rolável.

## Como mudar

**Rápido, no navegador:** tecle **E**, clique no texto, edite, **Ctrl+S**. Vale só para a cópia salva, e só para textos fora dos desenhos.

**Definitivo, na fonte:** edite os arquivos em `src/` e rode:

```bash
python build.py
```

| Arquivo | O que tem |
|---|---|
| `src/slides/*.html` | Os slides, em ordem alfabética do arquivo; cada slide traz suas notas em `<aside class="nota">` |
| `src/deck.css` | Paleta, tipografia, palco de 1920×1080, impressão |
| `src/deck.js` | Navegação, cliques, notas, janela do apresentador, animações |
| `src/sprite.svg` | Pictogramas reutilizados (pasta, arquivo, máquina de sorvete, casquinha...) |
| `src/fonts/` | As fontes embutidas |

## Exportar

Ctrl+P gera o PDF com um slide por página e todos os cliques já abertos. Para ver o estado final de um slide no navegador, abra o arquivo com `?static` no fim do endereço.

## O que ainda falta

- Trocar `[link curto a definir]` nos slides 2 e 33 (`src/slides/01-abertura.html` e `10-fecho.html`) e rodar `build.py`.
- Conferir o slide 29 depois do teste do Antigravity de 15/09.
- Não há logotipo do Ifes ou do Cefor (visual feito do zero, a pedido). Se o evento exigir a marca, acrescentar na capa e no encerramento.
- Decidir qual das duas apresentações vai para o projetor (decisão aberta no `CONTEXT.md` da oficina) e testar no projetor da sala.

## Verificação já feita

Os 35 slides foram renderizados no Chrome headless a 1920×1080, com todos os cliques abertos, e conferidos por captura de tela: textos dentro do palco, nada sobreposto, escalas conferidas contra as fontes.
