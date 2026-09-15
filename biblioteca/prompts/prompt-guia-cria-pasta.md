# Prompt que guia a criação da sua pasta

Prompt para a IA, no computador, **entrevistar a pessoa e montar com ela uma pasta-agente para uma tarefa da própria pesquisa**. É o que o participante leva para casa e o que usamos com voluntários na máquina do facilitador, no fim da demonstração.

Fica entre os dois extremos que já temos:

| | `prompt-cria-pasta.md` | Este prompt | Workspace-builder do ICM |
|---|---|---|---|
| Para quê | Mostrar que uma pasta nasce de um pedido | Criar a *sua* pasta, para a *sua* tarefa | Montar um espaço de trabalho completo |
| Como | Fechado: sempre a mesma estrutura | Sete perguntas curtas, etapas em P.A.R.T.E., aprovação antes de criar | Questionário longo, cinco etapas |
| Tempo | 2 minutos | 10 a 20 minutos | Uma sessão inteira |
| Nível | Demonstração | Pós-oficina, em casa | "Industrial"; para quem já domina |

Combina duas fontes: as perguntas de descoberta e mapeamento de etapas do workspace-builder do ICM (`referencias/icm-van-clief-mcdermott-2026.md`), bem reduzidas, e o P.A.R.T.E. de Hugo Cristo (`referencias/hugo-cristo-seminario-ia-2026.md`) aplicado a cada etapa.

## Antes de colar

1. Crie uma pasta vazia no computador, com o nome da tarefa (por exemplo `revisao-abnt` ou `fichamento-tese`).
2. Abra essa pasta na sua ferramenta de IA que trabalha em pastas (Antigravity, VS Code com Copilot em modo Agent, Claude Code, Codex, Gemini CLI ou outra).
3. Tenha em mente uma tarefa que você **repete** na pesquisa. Se é algo que você só vai fazer uma vez, talvez não valha montar a máquina: faça do jeito de sempre.
4. Cole o prompt abaixo e responda às perguntas com calma.

## O prompt

```
Você vai me ajudar a montar uma pasta de trabalho para uma tarefa que eu repito na minha pesquisa. Esta pasta será lida por uma IA (você ou outra) a cada etapa. Trabalhe em quatro fases e não pule nenhuma.

FASE 1 — ENTREVISTA. Faça as perguntas abaixo UMA DE CADA VEZ e espere a minha resposta antes da próxima. Se eu for vago, peça um exemplo concreto. Não crie nenhum arquivo nesta fase.
  1. Que tarefa você quer transformar em processo? (ex.: fichar artigos, revisar referências na ABNT, preparar uma submissão a periódico)
  2. O que você tem no começo? Que arquivos ou informações entram, e em que formato (PDF, Word, planilha, anotações)?
  3. O que precisa existir no fim, e quem vai ler (você, orientador, banca, periódico)?
  4. Como você faz essa tarefa hoje, passo a passo, mesmo sem IA?
  5. Em que momento você mais precisa conferir o que foi feito?
  6. Que referências fixas a IA deve seguir sempre? (seu tema e pergunta de pesquisa, normas, modelo do programa, seu jeito de escrever)
  7. Há dados sensíveis envolvidos (participantes, entrevistas, material sigiloso)?

FASE 2 — PROPOSTA. Com as respostas, proponha de 2 a 4 etapas, com um único trabalho cada. Para cada etapa, mostre em formato P.A.R.T.E.:
  - Persona: quem a IA deve ser nesta etapa.
  - Alvo: o que a etapa entrega, em uma frase.
  - Recebedores: quem usa essa saída (a etapa seguinte ou uma pessoa).
  - Tema: o assunto e o contexto da minha pesquisa que importam aqui.
  - Estrutura: entrada, processo, saída e o que eu devo verificar.
Diga também qual etapa usa um modelo mais capaz (as que dão direção) e qual pode usar um modelo simples (as que organizam ou formatam). Se houver conversão de formato (por exemplo, PDF para texto), trate-a como etapa separada ou como preparação fora da pasta, não misture com as outras. Espere a minha aprovação ou as minhas correções antes de seguir.

FASE 3 — CRIAÇÃO. Só depois que eu aprovar, crie exatamente esta estrutura, sem scripts, programas ou arquivos extras:
  README.md            o que a pasta faz e como usar, em até 15 linhas, para quem não programa
  CONTEXT.md           regras para a IA: ler este arquivo e o CONTEXT.md da etapa antes de agir; não inventar referências, citações, páginas ou números; registrar toda ação em registro/LOG-IA.md; escrever só nas pastas saida/; perguntar antes de apagar qualquer coisa ou de ler fora desta pasta; (se houver dados sensíveis) não enviar esses dados sem confirmação explícita
  _referencias/        um arquivo .md por referência fixa, com [colchetes] onde eu devo preencher
  00-entrada/          a única pasta que eu alimento diretamente
  01-<etapa>/          CONTEXT.md com as seções Entrada, Processo, Saída e Verificar, escritas a partir do P.A.R.T.E. aprovado; e uma subpasta saida/
  (uma pasta numerada por etapa aprovada)
  registro/LOG-IA.md   cabeçalho e formato de cada entrada: data; etapa; ferramenta e modelo; o que fez; arquivos lidos e escritos; o que o humano deve verificar
Todos os arquivos em Markdown e em português.

FASE 4 — CONFERÊNCIA. Mostre a árvore de pastas e explique cada arquivo em uma frase. Depois, liste o que eu devo conferir antes de usar a pasta: instruções que não refletem o que eu disse, etapas faltando ou sobrando, regras que ficaram vagas. Não execute nenhuma etapa.
```

## O que deve acontecer

1. A IA faz sete perguntas, uma por vez. Responder bem é o trabalho mais importante: é a "entrada" do padrão em U (capriche na entrada).
2. Ela propõe as etapas em P.A.R.T.E. Corrija aqui, antes de existir qualquer arquivo. É muito mais barato mudar a proposta do que a pasta.
3. Ela cria a pasta e mostra a árvore.
4. **Confira a máquina.** Abra cada `CONTEXT.md` e leia. Se a IA colocou um parafuso onde não era, vai sair metal junto com o sorvete: a ela não faz diferença, a você faz.
5. Coloque um material de teste em `00-entrada/` e rode só a etapa 01: "Leia 01-<etapa>/CONTEXT.md e execute a etapa."

## Com voluntários, na oficina

Chamar uma a três pessoas para sentar à máquina do facilitador. A pessoa explica a tarefa em voz alta; o facilitador digita as respostas; a plateia vê as perguntas e as pastas aparecendo. Ao final, abrir um `CONTEXT.md` e perguntar à pessoa: "é isso mesmo que você faz?". Ver `oficinas/2026-09-17-secim/05-roteiro-demonstracao.md`, Parte C.

## Se der errado

- A IA pulou a entrevista e já criou arquivos: "apague o que criou e volte à fase 1, uma pergunta de cada vez".
- Fez todas as perguntas de uma vez: responda "uma por vez, por favor" e comece pela primeira.
- Propôs etapas demais: "no máximo 3 etapas; junte as que fazem o mesmo trabalho".
- Criou scripts ou arquivos extras: "remova o que não estava na lista".
- As instruções ficaram genéricas: "reescreva o CONTEXT.md da etapa 01 usando exatamente as minhas respostas às perguntas 4 e 5".

## Histórico

- 14/09/2026: escrito a partir da conversa de revisão Marquito e Elton (`fontes/2026-09-14-transcricao-reuniao-marquito-elton-revisao-secim.txt`, trechos 00:57 a 00:58, 01:05 a 01:06 e 01:12 a 01:13): "eles precisam levar para casa um prompt, ou um passo a passo guiado por IA, para criar essa pasta"; "baseado no P.A.R.T.E. e no ICM, mais rápido que o questionário do ICM". **Não testado.** Testar em 15/09 com pelo menos duas ferramentas (Claude Code e Antigravity) e anotar aqui o resultado.
