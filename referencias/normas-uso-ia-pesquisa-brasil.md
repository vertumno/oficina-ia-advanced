# Normas sobre uso e declaração de IA na pesquisa (Brasil, 2026)

**Fontes principais:**
- CNPq. Portaria nº 2.664, de 06/03/2026. Institui a Política de Integridade na Atividade Científica, com diretrizes sobre IA generativa. Notícia oficial: https://www.gov.br/cnpq/pt-br/assuntos/noticias/cnpq-em-acao/cnpq-publica-portaria-que-institui-politica-de-integridade-na-atividade-cientifica
- Jornal da USP, "Portaria do CNPq detalha diretrizes de integridade na pesquisa com o uso de inteligência artificial": https://jornal.usp.br/atualidades/portaria-do-cnpq-detalha-diretrizes-de-integridade-na-pesquisa-com-o-uso-de-inteligencia-artificial/
- CAPES. Ofício-Circular nº 5/2026/DIRAV/CAPES (fevereiro de 2026). Comunicação interna aos programas; conhecida por fontes secundárias.
- UFRRJ. Memorandos Circulares nº 88/2026 e nº 93/2026 (PROPPG), modelo de declaração de uso de IA generativa: https://portal.ufrrj.br/ufrrj-orienta-declaracao-de-uso-de-ia-em-trabalhos-academicos/
- Limongi, Ricardo. "Voltando do GT da CAPES: o que aprendi sobre IA na pesquisa científica", 11/05/2026: https://ricardolimongi.substack.com/p/voltando-do-gt-da-capes-o-que-aprendi
- Feuerriegel, S. et al. "A reporting checklist for large language models in behavioural science" (GUIDE-LLM, 14 itens). *Nature Human Behaviour* 10, 1182–1186 (2026): https://www.nature.com/articles/s41562-026-02492-7
- Políticas de conferências citadas por Silvio Meira (ICML 2026 LLM Policy, ICLR 2026): ver `meira-2026-29000-papers.md`.
**Consultado em:** 02/09/2026.

## Em uma frase

Desde março de 2026 o Brasil tem uma norma nacional (CNPq) que exige declarar o uso de IA generativa em qualquer fase da pesquisa; a CAPES ainda não tem norma própria e recomenda aos programas adotar a do CNPq; várias universidades já publicaram modelos de declaração.

## O que diz cada fonte

### Portaria CNPq nº 2.664/2026

- Aplica-se a pesquisadores, bolsistas e docentes em atividades financiadas ou apoiadas pelo CNPq.
- **Obriga declarar** o uso de qualquer ferramenta de IA generativa em todas as fases do trabalho científico, da concepção à submissão, especificando **a ferramenta, a finalidade e a fase** em que foi usada (artigo 9, conforme o Jornal da USP).
- **Proíbe** apresentar conteúdo gerado por IA como se fosse de autoria humana.
- **Proíbe** o uso de IA na elaboração de pareceres científicos (revisão por pares), por risco à imparcialidade e ao sigilo.
- O pesquisador **responde integralmente** pelo conteúdo final, inclusive por plágio ou imprecisões decorrentes da ferramenta.
- Sanções graduadas, de advertência a suspensão no Lattes (segundo Limongi).
- O espírito é "uso consciente" por letramento, não proibição.

### CAPES (situação em maio de 2026)

- Não há portaria específica da CAPES sobre IA em dissertações e teses.
- O Ofício-Circular nº 5/2026/DIRAV/CAPES orientou os programas a adotar a Portaria CNPq 2.664/2026 como referência "no que couber", especialmente para bolsistas e projetos com recursos CAPES.
- A CAPES não exige declaração formal ainda, mas recomenda que orientadores incluam o uso de IA nos critérios de avaliação.
- Há um grupo de trabalho da CAPES; expectativa de norma complementar ainda em 2026.
- Cinco pilares de consenso (Limongi): letramento em IA obrigatório; transparência e declaração; autoria exclusivamente humana; responsabilidade humana integral; restrição ao uso em revisão por pares.
- Lacuna apontada: diretrizes para teses e dissertações. Modelo de Singapura ("statement of originality" explicando o uso de IA) citado como referência não punitiva.

### Modelo UFRRJ

- Memorando 88/2026: modelo de declaração para dissertações, teses, artigos e livros, indicando **qual tecnologia**, **com que finalidade**, **em qual etapa**, e reforçando a **responsabilidade do autor**.
- Memorando 93/2026: a declaração pode ficar na parte pré-textual, **após os agradecimentos**.
- Princípio: conteúdo gerado por IA não deve ser apresentado como inteiramente original; erros e imprecisões seguem sendo responsabilidade do pesquisador.

### GUIDE-LLM

- Checklist de 14 itens para relatar uso de LLMs em pesquisa nas ciências comportamentais e sociais, motivado pela constatação de que "pequenas mudanças em prompts, configurações ou versões do modelo levam a resultados substancialmente diferentes".
- Útil como referência de **o que registrar**: modelo e versão, prompts, parâmetros, data, procedimento de verificação.

### Conferências internacionais (via Meira)

- ICML 2026: pode usar IA para escrever e pesquisar; o autor responde por tudo; LLM não pode ser autor; prompt injection é desk reject.
- ICLR 2026: rejeição sumária de uso extensivo e não declarado de LLM.

## O que aproveitamos

- **O bloco "Declarar, não esconder" da oficina** se apoia em três fatos verificáveis: a Portaria CNPq existe e obriga; a CAPES recomenda seguir a Portaria; universidades já têm modelo. Isso responde exatamente à demanda da organizadora ("não sabe como declarar").
- **Os três elementos da declaração** (ferramenta, finalidade, fase) viram o esqueleto do modelo em `biblioteca/prompts/modelo-declaracao-uso-ia.md` e do arquivo `registro/LOG-IA.md` do kit. Se o registro guarda ferramenta, finalidade e fase a cada ação, a declaração sai quase pronta.
- **"Autoria exclusivamente humana, responsabilidade integral"** é a frase que separa assistir de substituir. Elton usou a mesma distinção na conversa.
- **A proibição de IA em pareceres** é útil para docentes na plateia e para quem faz avaliação de trabalhos de disciplina.
- **GUIDE-LLM** entra na página de referências para quem quer rigor de relato.

## Cuidados e limites

- O Ofício-Circular da CAPES é conhecido por fontes secundárias (artigo comercial e post de blog). Na oficina, dizer "a CAPES orientou os programas a usar a Portaria do CNPq como referência" e recomendar que cada um confirme com seu programa. Não citar número de ofício como se tivéssemos o documento.
- Programas e periódicos têm regras próprias, às vezes mais restritivas. A mensagem é: a norma nacional é o piso; o programa, a banca e o periódico podem pedir mais.
- Não sabemos a regra do programa de pós em Educação em Ciências e Matemática do Ifes. Perguntar à organizadora ou ao coordenador antes da oficina.

## A confirmar

- Texto integral da Portaria 2.664/2026 (buscar no DOU ou no site do CNPq) para citar o artigo correto na declaração modelo.
- Se o programa de pós do Ifes já tem orientação própria sobre IA.
- Se a CAPES publicou algo novo entre maio e setembro de 2026.
