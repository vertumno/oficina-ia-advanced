# oficina-ia-advanced

Base de trabalho da CGTE/Cefor (Ifes) para oficinas de Inteligência Artificial aplicada à pesquisa e à educação.

Nasceu para preparar a oficina do Secim (17/09/2026, 16h às 17h30, Ifes campus Vitória) e foi organizada para ser reaproveitada. O curso de extensão de 2027 e o MOOC são usos secundários e têm notas em `futuro/`.

Esta pasta é, ela mesma, um exemplo do que ensinamos: pastas com instruções claras em texto, que uma IA consegue ler e com as quais uma pessoa consegue conversar. Abra-a no VS Code (ou similar) com seu agente de IA e peça: *"Leia README.md e CONTEXT.md e me diga por onde começar."*

## Estrutura

| Pasta | O que é | Quando usar |
|---|---|---|
| `_inbox/` | Caixa de entrada. O que chega fica aqui até ser processado; a meta é estar vazia. | Ao receber algo novo. |
| `fontes/` | Originais já processados, renomeados com data e descrição. Não se edita. | Ao precisar do texto original de uma fonte. |
| `referencias/` | Fichas curadas de cada fonte: o que diz, o que aproveitamos, links verificados. | Ao montar qualquer oficina, curso ou página. |
| `biblioteca/` | Blocos reutilizáveis: conceitos, prompts, kits para participantes, modelos de página. | Ao construir o conteúdo de uma oficina. |
| `oficinas/` | Uma pasta por evento: briefing, plano, análise, divulgação, pré, demonstração, pós, página. | Ao preparar e registrar uma oficina. |
| `futuro/` | Notas para o curso de extensão de 2027 e o MOOC. Uso secundário. | Ao planejar formações longas. |

Cada pasta tem um `CONTEXT.md` que explica o que ela contém, de onde vem, para que serve e o que uma IA pode fazer ali.

A oficina anterior, "IA além do chat" (VIII Concefor, 20/08/2026), vive em outro repositório (`C:\dev\oficina-concefor-icm`) e é a principal referência prática. Ficha em [`referencias/oficina-concefor-2026-08-20.md`](referencias/oficina-concefor-2026-08-20.md).

## Oficina em preparação

**Secim, 17/09/2026.** Tudo em [`oficinas/2026-09-17-secim/`](oficinas/2026-09-17-secim/). Comece pelo [`CONTEXT.md`](oficinas/2026-09-17-secim/CONTEXT.md) da pasta, depois pelo [plano](oficinas/2026-09-17-secim/01-plano-da-oficina.md) e pela [análise](oficinas/2026-09-17-secim/02-analise-e-melhorias.md).

Pendência urgente: enviar à organizadora título, descrição, minibios e foto (Elton prometeu "até amanhã" em 01/09). Texto pronto em [`03-divulgacao-para-a-organizacao.md`](oficinas/2026-09-17-secim/03-divulgacao-para-a-organizacao.md).

## Como usar esta pasta

1. **Chegou material novo?** Coloque em `_inbox/`. Escreva (ou peça à IA para escrever) uma ficha em `referencias/`, no modelo das existentes. Mova o original para `fontes/` com nome `AAAA-MM-DD-descricao.ext` e registre na tabela de `fontes/CONTEXT.md`.
2. **Vai montar uma oficina?** Crie `oficinas/AAAA-MM-DD-nome/` com um `CONTEXT.md` e a estrutura descrita em `oficinas/CONTEXT.md`. Aponte para o que servir de `biblioteca/`; não copie. Se um bloco serve para duas oficinas, ele pertence à `biblioteca/`.
3. **Vai dar a oficina?** O plano é o roteiro; o `05-roteiro-demonstracao.md` é o script da demonstração.
4. **Deu a oficina?** Preencha "Lições aprendidas" em `06-pos-oficina.md`. O que valer para as próximas sobe para `biblioteca/` ou `referencias/`. A edição congela; a próxima nasce em `v2/`.

## Convenções

- Português, Markdown simples, nomes de arquivo em minúsculas com hífens.
- Arquivos numerados (`00-`, `01-`) indicam ordem de leitura ou de execução.
- `CONTEXT.md` em toda pasta.
- Dono único da informação: cada fato vive em um lugar; os outros apontam.
- Fontes com link e data de consulta. O que não foi verificado fica marcado como *a confirmar*.
- A metodologia de pastas segue, de forma livre, o ICM (Van Clief e McDermott, 2026). Ficha em [`referencias/icm-van-clief-mcdermott-2026.md`](referencias/icm-van-clief-mcdermott-2026.md).

## Estado atual (02/09/2026)

- Seis fontes recebidas, fichadas e arquivadas em `fontes/`. Inbox vazia.
- Fichas escritas: ICM, Silvio Meira, Hugo Cristo, normas brasileiras sobre IA na pesquisa, recursos do Cefor, sala Moodle dos NTEs, oficina do Concefor, ata do curso de extensão.
- Biblioteca: cinco conceitos, três prompts, um kit (Kit Pesquisa), um modelo de página.
- Secim: briefing, plano minuto a minuto, análise com insights e melhorias, divulgação, pré-oficina datada, roteiro da demonstração, pós-oficina, folha de tema, página de referências (HTML e Markdown).
- Futuro: mapa do curso de extensão de 2027 e nota sobre o MOOC.
- **Não testado:** o kit e os prompts. Testes previstos para 05/09 e 09/09.

## Próximos passos

Lista completa e datada em [`oficinas/2026-09-17-secim/04-pre-oficina.md`](oficinas/2026-09-17-secim/04-pre-oficina.md). Os três mais urgentes:

1. Enviar a divulgação à organizadora (02/09).
2. Testar o kit com Claude Code, Copilot gratuito e Gemini CLI (05/09) e com uma pessoa leiga (09/09).
3. Enviar a mensagem aos inscritos com as instruções de instalação (07/09).
