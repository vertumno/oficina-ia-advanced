# Hugo Cristo — Introdução à IA Generativa para Pesquisas em Psicologia (seminário PPGP/UFES)

**Fonte:** Sant'Anna, Hugo Cristo. Seminário da disciplina PPGP0104, PPGP/UFES, 4 encontros, 9 e 10/07/2026. Repositório: https://github.com/hugocristo/seminario-ia-2026
Compilado feito por nós (curadoria a partir dos slides, do README e dos dois projetos-exemplo): `fontes/2026-07-09-hugo-cristo-seminario-ia-compilado.pdf`.
**Consultado em:** 02/09/2026.

## Em uma frase

Um curso de dois dias para mestrandos de psicologia que organiza o uso de IA em pesquisa como uma progressão de autonomia (chatbots → copilotos → agentes) e um "funil responsável" de ferramentas por etapa, com ética e integridade atravessando tudo.

## O que diz

**Quatro blocos.**
1. *Fundamentos de Cibernética e IA.* Inteligência como propósito (James), "conceito mala de viagem" (Minsky), três paradigmas (simbólico, conexionista, enativo), linhagem histórica que entrelaça IA e psicologia, riscos concretos de chatbots.
2. *Chatbots e anatomia dos LLMs.* Transformer, tokens, embeddings, BERT versus GPT, pré-treino → refinamento → RLHF, temperatura. Engenharia de prompt com o modelo **P.A.R.T.E.**: Persona, Alvo, Recebedores, Tema, Estrutura. Zero/one/few-shot, chain-of-thought. Linha do tempo: chatbots (2022) → copilotos (2023–24) → agentes (2025+). Checklists: UNESCO, GUIDE-LLM, CNPq, ANPAD.
3. *Copilotos e integrações com R.* Modelos locais (Ollama, llama.cpp) versus nuvem; RStudio com Posit Assistant; laboratório Ollama + RStudio + Gemma3:1b rodando offline.
4. *Agentes como coautores.* Agent harnesses ("braços e pernas para os modelos"): LLM + ferramentas + planejamento + execução + contexto + laços. Claude Code, OpenCode. Markdown como "língua franca das IAGs". Ciclos fracos (turno a turno) versus fortes (autopesquisa). Caso real: replicar um estudo de mortalidade por suicídio no ES, em R, com saída Quarto.

**Funil responsável (5 etapas, 11 ferramentas).**

| Etapa | Ferramentas | Cuidado principal |
|---|---|---|
| Definir o problema | Elicit, Consensus, Scite.AI, Bohrium | Cobertura enviesada (inglês, biomédica); conferir cada célula extraída |
| Mapear a literatura | Research Rabbit, Connected Papers | Grafo herda o viés da semente; é descoberta, não protocolo |
| Estudar a literatura | NotebookLM | "Grounded" reduz mas não elimina erro; dados vão para o Google |
| Gerar textos, gráficos, imagens | Gemini | Generativo, não ancorado: inventa referências e DOIs; nunca usar para descobrir fatos |
| Elaborar relatórios | Gemini Deep Research | Idem; declarar uso |
| Infraestrutura local | Ollama, llama.cpp | Modelos pequenos erram estatística com confiança |

**Dois projetos-exemplo.**
- *ppgp-covid* (OpenCode, Python): análise descritiva de COVID-19 por município do ES; o documento âncora `pesquisa.md` funciona como protocolo de reprodutibilidade e memória; estatística frouxa (polinômio grau 3 com R² cosmético); manteve no repositório até o script que falhou, como rastro.
- *ppgp-suicidio* (Claude Code, R + Quarto): reproduz a metodologia de Caliman et al. (2023) com regressão de Prais-Winsten; o artigo-fonte fica em contexto como ground truth (`scratchpad_article.txt`); scripts de verificação cruzam a implementação com pacote independente; saída publicável em HTML e DOCX. O `.claude/` tem um único arquivo, `settings.local.json`, com uma allowlist de oito linhas. Nenhum CLAUDE.md, nenhuma skill.

**O padrão que Hugo ensina a não programadores.**
1. Você traz a pergunta e a fonte-âncora; o agente faz o encanamento.
2. Ancorar, não inventar: toda análise nasce colada a uma fonte de verdade.
3. O agente cobre o pipeline inteiro até um artefato publicável.
4. Humano no laço por verificação e permissão.
5. Ferramenta enxuta: o resultado vem de dado bom, fonte âncora e prompting, não de configuração sofisticada.

## O que aproveitamos

- **P.A.R.T.E.** como estrutura do "prompt bom" na demonstração web. É em português, tem cinco letras, cabe em um slide. Marquito lembrou dele na conversa como "o acrônimo do Hugo".
- **A progressão chatbot → copiloto → agente** como mapa mental de um slide: a pasta com instruções é um híbrido de assistente e agente. Elton propôs exatamente isso.
- **"Ancorar, não inventar"** vira regra número 1 do `AGENTS.md` do kit: não inventar referências; se não tiver certeza, dizer.
- **A lição do Claude Code vanilla** sustenta a decisão de manter o kit mínimo: três etapas, sem skills, sem automações. O poder vem das instruções e da fonte, não do andaime.
- **O funil responsável** entra na página de referências como "ferramentas por etapa da pesquisa", com os cuidados. Não cabe na oficina de 90 minutos; fica como material de continuidade.
- **Os riscos e a integridade** (Portaria CNPq, GUIDE-LLM, checklists) já estão no material dele; nossa ficha de normas complementa.
- **O evento dele é pastas e arquivos.** O repositório do seminário é a prova de que "as pessoas já estão preparando as coisas para serem lidas por IA". Bom exemplo para mostrar em 20 segundos.

## Cuidados e limites

- O seminário teve dois dias inteiros; o Secim tem 90 minutos. Só entram três coisas dele: P.A.R.T.E., a progressão, "ancorar, não inventar".
- Vários URLs do README original têm erros de digitação (elict.com, concensus.com); o compilado já traz os corrigidos.
- O laboratório Ollama + RStudio é interessante, mas fora do escopo do Secim (público de educação, não de estatística).
- O compilado é nosso e tem leituras nossas ("pontos de contato com o trabalho do Marquito"); ao citar Hugo, citar o repositório dele, não o compilado.

## A confirmar

- Se Hugo autoriza citar o seminário e os projetos-exemplo em uma oficina do Ifes. Os slides estavam protegidos por senha; o repositório é público.
- Se há interesse em uma colaboração (mini-módulo de agent harnesses no PPGP), como o compilado sugere.
