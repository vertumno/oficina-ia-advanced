# Curso de extensão "Inteligência de Contexto Pedagógica com IA" (2027): como o material daqui se encaixa

Fonte: `referencias/ata-curso-extensao-2027.md`. Estado: proposta aprovada pela CGTE em 14/05/2026 e submetida ao Edital 50/2026 (UnAC). Resultado a confirmar.

## A escada e o que já temos para cada degrau

| Degrau (ata) | O que já existe | Onde | Lacuna |
|---|---|---|---|
| 1. Inteligência de prompt | P.A.R.T.E.; pedido versus processo; as quatro perguntas antes de usar IA | `biblioteca/prompts/pedido-vs-processo.md`; `referencias/hugo-cristo-seminario-ia-2026.md` | Exemplos de docência (o Secim tem exemplos de pesquisa; o Concefor, de devolutivas e aulas) |
| 2. Markdown como linguagem operacional | Todo o kit é Markdown; "README: o arquivo que a IA lê primeiro"; Hugo: "língua franca das IAGs" | `biblioteca/kits/kit-pesquisa/`; `biblioteca/conceitos/pasta-como-agente.md` | Um módulo curto de Markdown em si (títulos, listas, tabelas, links), com exercício |
| 3. Segundo cérebro (PARA, Zettelkasten) | A organização desta pasta (`_inbox` → `fontes` → `referencias` → `biblioteca`) é um exemplo vivo; a provocação "Drive virou arquivo morto" | `CONTEXT.md` da raiz; `referencias/oficina-concefor-2026-08-20.md` | Conteúdo sobre PARA e Zettelkasten propriamente; ainda não temos ficha |
| 4. Inteligência de contexto em camadas | ICM completo: cinco camadas, contratos, janela de contexto, etapas e rastro | `referencias/icm-van-clief-mcdermott-2026.md`; `biblioteca/conceitos/` | Tradução dos exemplos para o cotidiano docente (plano de aula em etapas) |
| 5. Agentes pedagógicos especializados | Workspace-builder do Concefor (planejador, devolutivas, avaliador de salas); GPTs do Cefor como exemplo de "assistente especializado" | `C:\dev\oficina-concefor-icm\workspaces\workspace-builder`; `referencias/cefor-recursos-ia.md` | Kits prontos por caso (plano de aula, devolutivas, rubricas), no molde do kit-pesquisa |
| 6. Sistema Operacional Pedagógico pessoal | Visão de "dez caixas" e ecossistema de pastas; "configure a fábrica" | `biblioteca/conceitos/fabrica-vs-produto.md` | O desenho do entregável final e sua rubrica |

## O que as oficinas ensinaram sobre o público (para o desenho do curso)

- **A abstração pastas e arquivos é o obstáculo** (Concefor e Secim). O curso precisa de um módulo inteiro de ambientação, assíncrono, com vídeo curto e tarefa de "crie uma pasta, escreva um leia-me, abra com a IA". Não pode ser pré-requisito implícito.
- **Créditos gratuitos limitam o desenho.** Cinquenta interações por mês no Copilot gratuito. Cada módulo precisa dizer quantas mensagens gasta. Alternativa: Gemini CLI; ou negociar API institucional (pendência antiga da CGTE).
- **Erro nº 1: pedir logo o produto.** A máquina de sorvete vira o vídeo de abertura do módulo 4.
- **"Acabou cedo" é pedido de próximo módulo.** Um curso de 90 h responde exatamente a isso. Os participantes do Concefor são inscritos naturais.
- **A avaliação no fim mede entusiasmo.** O curso precisa medir transferência: a rubrica do entregável final e um formulário 30 dias após o término.
- **Em casa, quem entrevista é a IA.** O `setup` do workspace-builder e o "primeiro pedido" do kit são o mesmo gesto. Ensinar isso com nome.
- **Coletar tudo.** Workspaces e kits dos cursistas vão para o repositório público de materiais abertos (previsto na ata, com o bolsista).

## Estrutura possível em quatro meses (rascunho para discutir)

| Mês | Degraus | Entregável do cursista | Material daqui |
|---|---|---|---|
| 1 | Ambientação; 1 e 2 | Uma pasta com leia-me e um prompt em arquivo, aberta com a IA | Folha de sobrevivência; pedido versus processo; conceitos |
| 2 | 3 e 4 | Um "segundo cérebro" mínimo e uma pasta de três etapas para uma dor real | Kit adaptado (plano de aula ou devolutivas); ICM |
| 3 | 5 | Dois agentes especializados que se alimentam (saída de um é entrada do outro) | Workspace-builder corrigido; casos do Concefor |
| 4 | 6 | Sistema Operacional Pedagógico documentado; plano de aula AI-aumentado; declaração de uso de IA | Modelo de declaração; rastro; rubrica |

Encontros síncronos: um por mês, no formato do Papo com IA.IÁ (online, 45 min), mais uma socialização final.

## Pendências

- Resultado do edital.
- Cronograma de produção no Moodle.
- Fichas para PARA e Zettelkasten (degrau 3).
- Kits por caso docente (degrau 5): plano de aula, devolutivas, rubricas. Modelo: `biblioteca/kits/kit-pesquisa/`.
- Decidir a ferramenta oficial do curso (Copilot gratuito, Gemini CLI, ou API institucional).
- Conversar com a Rutinelli sobre onde o Protocolo de Atenção entra (provavelmente degraus 1 e 6).
