# Plano da oficina: "IA na pós-graduação: usar bem, organizar e declarar"

Secim, Ifes campus Vitória, quinta-feira 17/09/2026, 16h às 17h30. Fonte canônica do roteiro. As razões estão em `02-analise-e-melhorias.md`; o que precisa acontecer antes, em `04-pre-oficina.md`; a demonstração, passo a passo, em `05-roteiro-demonstracao.md`.

## Visão em uma frase

O pós-graduando sai sabendo que declarar bem o uso de IA exige saber o que a IA fez, que saber o que a IA fez exige um processo visível, e que o jeito mais simples de ter um processo visível é uma pasta no computador com instruções em texto, e sai com essa pasta na mão.

## Objetivos

Ao final, quem participou:

1. Sabe **o que a norma pede** (ferramenta, finalidade, fase) e tem um modelo de declaração para adaptar.
2. Distingue **pedir um resultado de conduzir um processo**, e viu as duas coisas lado a lado na mesma IA.
3. Entende **por que a IA "fica burra"** numa conversa longa e o que fazer.
4. Viu uma **pasta virar um agente** no computador, abriu o arquivo de instruções e entendeu que pode mudá-lo.
5. Tem um **kit**, uma **página de referências** e um **canal de continuidade**, e sabe que em casa a própria pasta o guia.

O que a oficina **não** promete: que a pessoa saia operando o método sozinha. Dizer isso em voz alta (aprendizado do Concefor).

## Premissas de desenho

- 90 minutos nominais; planejar para 75 úteis a partir das 16h05, com ordem de corte definida.
- Sem laboratório; notebook próprio; instalação prévia não garantida. Logo, **três níveis de participação**, e ninguém sai sem entregável.
- O Bloco 0 (ambientação) acontece **fora do relógio**: mensagem prévia aos inscritos e clínica de instalação durante o credenciamento.
- O bloco conceitual (máquina de sorvete, erro nº 1) vem **antes** da primeira interação com a IA.
- Caminho gratuito explícito: VS Code + GitHub Copilot com conta do GitHub (testado no Concefor) ou Gemini CLI.
- Demonstração em uma ferramenta só (Claude Code na máquina do Marquito), com vídeo gravado como plano B.
- A oficina não fica mais longa se sobrar demanda: o "quero mais" é respondido com a próxima oficina, o Papo com IA.IÁ e o curso de extensão.

## Três níveis de participação (o entregável)

| Nível | Quem | O que faz durante a oficina | O que leva |
|---|---|---|---|
| **0: assiste** | Quem veio sem notebook ou sem vontade de mexer | Acompanha, preenche a folha de tema, lê a página no celular | Página de referências, modelo de declaração, kit para baixar depois |
| **1: faz na web** | Quem tem qualquer IA no navegador (Claude, ChatGPT, Gemini, gratuitos) | Cola o "prompt bom" com um artigo próprio ou um dos de exemplo; obtém ficha, resumo do processo e rascunho de declaração | O mesmo que o nível 0, mais o resultado da conversa e o prompt para reutilizar |
| **2: faz no computador** | Quem instalou VS Code e um agente antes ou na clínica | Descompacta o kit, conversa com a pasta, roda a etapa 01 com um artigo | O mesmo que o nível 1, mais a pasta funcionando no próprio computador, com registro |

Regra de facilitação (do Concefor): quem estiver travado, garanta o nível dele em vez de empurrar para o seguinte.

## Roteiro

| Hora | Min | Bloco | Conduz |
|---|---|---|---|
| 15h15 às 16h00 | 45 | **Bloco 0: clínica de instalação** (durante o credenciamento, na sala da oficina) | Ambos |
| 16h00 às 16h05 | 5 | Chegada e calibragem (três perguntas de mão levantada) | Elton |
| 16h05 às 16h10 | 5 | **1. Abertura:** 22.977 revisões em um dia | Elton |
| 16h10 às 16h22 | 12 | **2. Declarar, não esconder:** a norma, o modelo, a banca | Elton |
| 16h22 às 16h35 | 13 | **3. Pedido versus processo:** P.A.R.T.E., duas conversas, janela de contexto | Marquito |
| 16h35 às 16h40 | 5 | **4. Antes de ir ao computador:** máquina de sorvete, erro nº 1, o arquivo que a IA lê primeiro | Marquito |
| 16h40 às 17h05 | 25 | **5. A pasta vira agente:** demonstração ao vivo; níveis 1 e 2 em paralelo | Marquito conduz; Elton circula |
| 17h05 às 17h10 | 5 | **6. Recapitulação** (prevista, não socorro) | Elton |
| 17h10 às 17h20 | 10 | **7. Método e cuidados:** ICM em cinco princípios, etapas e rastro, três regras de segurança, caminhos gratuitos | Marquito |
| 17h20 às 17h30 | 10 | **8. Fecho:** níveis, QR duplo, coleta, "em casa a pasta te guia", próxima | Elton |
| 17h30 às 18h00 | 30 | **Plantão** no coffee break | Ambos |

Soma dos blocos 1 a 8: 85 minutos, dentro de 16h05 às 17h30.

**Ordem de corte se começar atrasado ou estourar:** (a) reduzir o bloco 3 tirando o slide chatbot → copiloto → agente (fica só citado); (b) reduzir o bloco 2 de 12 para 8 minutos, mostrando o modelo de declaração sem ler; (c) reduzir a demonstração de 25 para 18 minutos pulando a etapa 03 ao vivo (mostrar o resultado pronto do ensaio). **Nunca cortar o bloco 4** nem o momento de abrir o `CONTEXT.md` da etapa e ler em voz alta.

## Detalhamento dos blocos

### Bloco 0: clínica de instalação (15h15 às 16h00)

- **Objetivo:** reduzir o Bloco 0 a zero dentro do relógio. Quem quiser chega cedo e sai com VS Code e agente funcionando.
- **O que acontece:** os dois facilitadores na sala, projetor com o slide "Instale assim" (passo a passo de VS Code + conta GitHub + Copilot; alternativa Gemini CLI), o link do kit no quadro. Atender um a um. Quem chegou pronto testa o "primeiro pedido" do kit.
- **Material:** slide de instalação; folha de sobrevivência impressa; link curto e QR do kit; hotspot 4G de reserva.
- **Risco:** a sala não estar disponível às 15h15. Plano B: atender no corredor do credenciamento com o notebook do Elton, só para conta do GitHub e download.

### Chegada e calibragem (16h00 às 16h05)

Três perguntas de mão levantada, para calibrar falas, não para mudar o roteiro:

1. Quem usa IA toda semana na pesquisa?
2. Quem já declarou o uso de IA em algum trabalho?
3. Quem trouxe notebook e conseguiu instalar algo hoje?

Anotar os números no quadro (viram dado para a retrospectiva). Entregar a folha de tema e pedir que preencham a primeira metade enquanto a oficina começa.

### 1. Abertura: 22.977 revisões em um dia (5 min)

- **Objetivo:** choque calculado e a frase que organiza tudo.
- **Conteúdo:** AAAI-26 (Silvio Meira): 29.000 submissões, 22.977 revisões por IA em menos de um dia, e os autores preferiram. ICML 2026: "pode usar, você responde". A pergunta mudou: de "quem escreveu isso?" para "isso se sustenta?".
- **Fala-chave:** "Os orientadores de vocês estão usando. Os pareceristas estão usando. Esconder é a pior estratégia, porque a pergunta que vem não é 'você usou?', é 'isso se sustenta? o que a IA fez? o que você verificou?'."
- **Tela:** o número 22.977 grande; depois a frase "quem escreveu → isso se sustenta".
- **Fonte:** `referencias/meira-2026-29000-papers.md`.

### 2. Declarar, não esconder (12 min)

- **Objetivo:** responder ao "não sabe como declarar" com norma, modelo e lugar.
- **Conteúdo:**
  1. Portaria CNPq 2.664/2026: obriga declarar **ferramenta, finalidade e fase**; proíbe apresentar conteúdo de IA como humano; proíbe IA em parecer; autor responde integralmente. (2 min)
  2. CAPES: ainda sem norma própria; orientou os programas a usar a Portaria como referência; recomenda que orientadores incluam nos critérios. "O piso é a norma nacional; seu programa, sua banca e o periódico podem pedir mais. Perguntem." (2 min)
  3. Onde colocar: modelo da UFRRJ, parte pré-textual após os agradecimentos; em artigo, seção de declarações. (1 min)
  4. O modelo de declaração, projetado, lido em 40 segundos. "Reparem: para escrever isso, vocês precisam saber ferramenta, finalidade e fase. Quem usa na correria não sabe." (3 min)
  5. As quatro perguntas antes de usar IA na pesquisa (posso subir estes dados? consigo verificar cada referência? saberei dizer à banca o que a IA fez? a interpretação continua minha?). (2 min)
  6. Ponte: "A declaração não sai da cabeça. Sai do rastro. E rastro é o que vamos construir agora." (1 min)
- **Fala-chave:** "Assistir é diferente de substituir. A IA pode fichar, organizar, apontar. Interpretar e concluir é seu. É isso que a banca vai testar."
- **Material:** `biblioteca/prompts/modelo-declaracao-uso-ia.md`; `referencias/normas-uso-ia-pesquisa-brasil.md`; slides da Rutinelli (a pedir).
- **Risco:** perguntas sobre casos específicos ("e se eu usei só para traduzir?"). Responder com o modelo: declare a finalidade exata; e encaminhar o resto para o plantão.

### 3. Pedido versus processo (13 min)

- **Objetivo:** mostrar, na mesma IA e com os mesmos artigos, a diferença entre pedir e conduzir.
- **Conteúdo:**
  1. P.A.R.T.E. (Hugo Cristo): Persona, Alvo, Recebedores, Tema, Estrutura. Um slide. (2 min)
  2. As duas conversas, já prontas (rodadas no ensaio com os artigos de exemplo), projetadas lado a lado: o pedido solto e o processo com rastro. Apontar: citações com página, resumo do processo, rascunho de declaração no fim. "Se o orientador perguntar de onde saiu a terceira frase, na primeira você não sabe; na segunda, está apontado." (6 min)
  3. Janela de contexto, com o visual da barra que enche: "tem uma coisa acontecendo por baixo dos panos". Não demonstrar. Números do ICM: uma etapa bem delimitada usa 2 a 8 mil tokens; uma conversa que faz tudo chega a 30 a 50 mil, faixa em que a pesquisa documenta degradação. (3 min)
  4. Chatbot → copiloto → agente: a pasta é um híbrido. (2 min; primeiro corte)
- **Fala-chave:** "O prompt bom é longo demais para digitar toda vez. Então a gente escreve uma vez, num arquivo, e a pasta lê. É para isso que vamos ao computador."
- **Material:** `biblioteca/prompts/pedido-vs-processo.md`; `biblioteca/conceitos/janela-de-contexto.md`; `chatbot-copiloto-agente.md`.
- **Nível 1 começa aqui:** projetar o QR da página com o prompt; quem tem IA na web já pode colar com um artigo próprio.

### 4. Antes de ir ao computador (5 min)

- **Objetivo:** plantar a metáfora e o aviso antes do erro acontecer (aprendizado nº 3 e nº 4 do Concefor).
- **Conteúdo:**
  1. A máquina de sorvete: "a gente vai montar a máquina; vai dar vontade de pedir o sorvete. Não peça. Se o sorvete sair ruim, não conserte o sorvete; volte e conserte a máquina."
  2. O erro nº 1 aqui: "me dá logo o texto da revisão de literatura". Quem tem mais facilidade com computador é quem mais cai.
  3. O arquivo que a IA lê primeiro: "como seria se toda pasta do seu computador tivesse um leia-me?" (funcionou no Concefor).
- **Tela:** máquina de sorvete (uma imagem); "README: o arquivo que a IA lê primeiro".
- **Fonte:** `referencias/oficina-concefor-2026-08-20.md`, `biblioteca/conceitos/fabrica-vs-produto.md`.

### 5. A pasta vira agente (25 min)

Script completo em `05-roteiro-demonstracao.md`. Resumo:

- **Parte A (8 min):** pasta vazia no VS Code; colar o prompt que cria a pasta; ver a árvore nascer; **abrir `01-fichamento/CONTEXT.md` e ler em voz alta**; abrir `registro/LOG-IA.md` vazio. "A instrução está aqui, em texto. Vocês podem mudar."
- **Parte B (12 min):** trocar para a janela do kit pronto; "leia README, CONTEXT e AGENTS e me explique"; "execute a etapa 01 para o artigo em 00-entrada"; enquanto roda, ler em voz alta as permissões que a IA pede; abrir a ficha; abrir o registro preenchido; rodar a etapa 03 e mostrar o rascunho da declaração com ferramenta, finalidade e fase preenchidos a partir do registro.
- **Parte C (5 min):** níveis 1 e 2 trabalham; facilitadores circulam. Nível 2: descompactar o kit, "primeiro pedido", etapa 01 com um artigo baixado da SciELO. Nível 1: prompt bom na web.
- **Fala-chave:** "Vocês não estão mais conversando com a web. Estão conversando com uma pasta que vocês sabem o que tem."
- **Regra de facilitação:** quando alguém reclamar do resultado, não corrija o resultado; mande abrir o `CONTEXT.md` da etapa e mudar a instrução.
- **Risco:** rede lenta, IA lenta, permissão negada. Plano B: vídeo de 5 minutos gravado no ensaio; saídas prontas na pasta de ensaio.

### 6. Recapitulação (5 min)

Elton, de pé, sem slide: "o que aconteceu até agora". Norma pede três coisas; o processo entrega as três; a pasta é o processo escrito; o registro é a declaração quase pronta. Perguntar quem chegou ao nível 1 e ao nível 2. Foi o que ancorou quem estava perdido no Concefor; aqui está previsto.

### 7. Método e cuidados (10 min)

- **Conteúdo:**
  1. ICM em cinco princípios (um slide): uma etapa, um trabalho; texto simples como interface; contexto em camadas; toda saída é uma superfície de edição; configure a fábrica, não o produto. "Existe um artigo, está na página. Vocês são pesquisadores; leiam." (3 min)
  2. Etapas e rastro: a caixa-preta virou caixinhas; se a etapa 4 deu errado, volte à 3, não à zero. Padrão em U: capriche na entrada, confie no meio, verifique a saída. (2 min)
  3. Três regras de segurança: leia o que a IA pede permissão para fazer; não ative "bypass"; não suba dados sensíveis sem saber para onde vão. "Vocês vão dar acesso ao computador. Isso amplia o poder e amplia o perigo." (2 min)
  4. Caminhos e custos: VS Code + Copilot com conta GitHub (gratuito, ~50 interações por mês); Gemini CLI (gratuito, ~1.000 por dia); Claude Code e Codex (pagos). Copilot Student para quem tem GitHub Education. Está na folha. (2 min)
  5. A provocação: "vocês usam o computador de qualquer jeito e usam IA de qualquer jeito. Juntar as duas coisas potencializa a bagunça. A IA amplifica organização ou desorganização. Escolham." (1 min)
- **Material:** `referencias/icm-van-clief-mcdermott-2026.md`; `biblioteca/conceitos/etapas-e-rastro.md`; folha de sobrevivência.

### 8. Fecho (10 min)

Nesta ordem, com estas palavras ou parecidas:

1. **Níveis.** "Quem chegou ao nível 0, 1, 2? Todos os três são sucesso. Ninguém sai daqui operando sozinho; sai sabendo que existe e por onde começar."
2. **Em casa, a pasta te guia.** "O primeiro pedido é sempre 'leia o README e me explique'. A pasta responde. Não precisa de nós."
3. **Coleta.** "Quem gerou uma ficha, manda para a pasta compartilhada agora (QR). Quem preencheu a folha, deixa na mesa." (Aprendizado do Concefor: o que não se coleta na sala se perde.)
4. **QR duplo:** avaliação e página de referências, lado a lado. A página tem o kit, o modelo de declaração, os prompts, o artigo do ICM, os links do Cefor.
5. **Continuidade.** Papo com IA.IÁ: **online**, toda quinta, 15h às 15h45, link na página. Curso de extensão "Inteligência de Contexto Pedagógica com IA" em 2027. "Quem quiser ser multiplicador no programa, escreve o contato na folha."
6. **Fecho com Meira:** "O que sobra para nós, humanos, é julgamento: por que isso importa. Isso a IA não responde por vocês. O resto ela ajuda, desde que vocês saibam o que ela fez."
7. Certificado e material chegam juntos por e-mail.

### Plantão (17h30 às 18h00)

Ficar na sala ou perto do café com os notebooks abertos. É onde as perguntas específicas acontecem ("e no meu caso?"). Anotar os casos para a retrospectiva.

## Materiais necessários

### Sala (pedir à organização)

- Projetor com entrada HDMI e cabo; adaptador USB-C na mochila por garantia.
- Wi-Fi liberado para sites de IA, GitHub e download do VS Code; senha de visitante.
- Tomadas ou réguas para os notebooks.
- Mesa para os facilitadores perto do projetor.
- Quadro branco ou flipchart e canetão.

### Facilitadores (levar)

- Notebook do Marquito: VS Code, Claude Code logado com créditos, pasta `secim-demo` vazia na área de trabalho, pasta `kit-pesquisa` com um artigo em `00-entrada/`, pasta `kit-pesquisa-ensaio` com as saídas do ensaio, navegador com as duas conversas "pedido versus processo" abertas, fonte do terminal aumentada, notificações desligadas.
- Notebook do Elton: VS Code + Copilot com conta GitHub (para mostrar o caminho gratuito e atender na clínica), Gemini CLI instalado.
- Hotspot 4G de reserva.
- Vídeo da demonstração gravado no ensaio (plano B), em pendrive e no notebook.
- Slides em PDF (funciona sem internet).
- QR codes impressos e no último slide: avaliação, página de referências, pasta compartilhada.
- Pendrive com o kit zipado e o instalador do VS Code (Windows e Mac), para a clínica sem rede.

### Impressos

- Folha de tema (`folha-tema.md`): 40 cópias em A5.
- Folha de sobrevivência (frente e verso, A5): instalação em 6 passos; Shift+Enter; "trust this folder"; arquivo aberto vira contexto; onde ver créditos; três regras de segurança; links e QR. 40 cópias.
- Modelo de declaração (uma página): 40 cópias. Muita gente vai querer levar em papel.
- Lista de presença: da organização.

### Digitais (prontos antes do dia)

- Pasta compartilhada (Drive) com: `kit-pesquisa.zip`, PDF dos slides, modelo de declaração, links dos artigos de exemplo, o prompt "pedido versus processo" em `.txt`, e uma subpasta "envie aqui" para a coleta.
- Página de referências publicada (`referencias-secim.html`) e link curto.
- Formulário de avaliação (nota 0 a 10; "que pena que"; "que tal se"; "que nível você alcançou"; "quero ser multiplicador?").
- Formulário de calibragem prévia (três perguntas, na mensagem aos inscritos).

### Para os participantes (pedir na mensagem prévia)

- Notebook carregado e carregador.
- Conta no GitHub criada e e-mail confirmado (para o Copilot gratuito) ou conta Google (para o Gemini CLI).
- VS Code instalado; extensão GitHub Copilot instalada e logada com a conta do GitHub.
- Um artigo em PDF que a pessoa esteja lendo para a pesquisa.
- Ou, no mínimo, qualquer IA no navegador com login feito.

## Papéis

| | Elton | Marquito |
|---|---|---|
| Conduz | Calibragem, blocos 1, 2, 6, 8 | Blocos 3, 4, 5, 7 |
| Enquanto o outro conduz | Circula; ajuda níveis 1 e 2; anota perguntas | Prepara a demonstração; controla o relógio |
| Clínica (15h15) | Contas GitHub, Copilot | VS Code, kit, Gemini CLI |
| Plantão | Casos de declaração e programa | Casos de pasta e ferramenta |

Um dos dois controla o relógio e sinaliza os cortes. Sugestão: Marquito, que fica na máquina.

## Planos B

| Se... | Então... |
|---|---|
| A rede do campus bloqueia sites de IA | Hotspot 4G para a máquina da demonstração; nível 1 pelo celular dos participantes; nível 2 vira "instale em casa com a folha". |
| Ninguém instalou nada | A oficina não muda: nível 1 para todos com IA na web; a demonstração continua no computador do Marquito. |
| A IA está lenta ou responde diferente do ensaio | Mostrar as saídas prontas da pasta de ensaio; se muito lenta, o vídeo. Dizer: "é assim mesmo; a IA não é determinística; por isso o registro importa". |
| O projetor falha | Slides em PDF no notebook do Elton; demonstração vista em roda de cadeiras ao redor do Marquito; a página no celular de cada um. |
| Começou 16h20 | Aplicar a ordem de corte: bloco 3 sem o slide de progressão; bloco 2 em 8 min; demonstração em 18 min. Nunca cortar o bloco 4. |
| Perguntas sobre casos específicos consomem o tempo | "Anota na folha; no plantão a gente pega um a um." |
| Alguém pede "me dá logo o texto da revisão" | É o erro nº 1. Usar como exemplo, com gentileza: "é exatamente o sorvete". |

## Critérios de sucesso

| Nível | Critério |
|---|---|
| Mínimo (todos) | Sabe o que a norma pede; tem o modelo; viu pedido versus processo; tem a página e o kit |
| Bom | Rodou o prompt bom na web com um artigo próprio e obteve ficha e rascunho de declaração (nível 1) |
| Ótimo | Abriu o kit no computador, conversou com a pasta e rodou a etapa 01 com um artigo (nível 2) |

Medição no dia: pergunta "que nível você alcançou" no formulário. Medição em 30 dias: "voltou a abrir a pasta? produziu algo? o que travou?" (ver `06-pos-oficina.md`).

## O que fica com eles

1. Página de referências (`referencias-secim.html`).
2. Kit Pesquisa (`biblioteca/kits/kit-pesquisa/`, zipado).
3. Modelo de declaração de uso de IA (`biblioteca/prompts/modelo-declaracao-uso-ia.md`).
4. Os dois prompts (`pedido-vs-processo.md`, `prompt-cria-pasta.md`).
5. Folha de sobrevivência (impressa e em PDF).
6. Artigo do ICM e repositório, como leitura para pesquisadores.
7. Convite ao Papo com IA.IÁ e ao curso de extensão de 2027.
