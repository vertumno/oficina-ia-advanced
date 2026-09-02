# ICM — Interpretable Context Methodology: estrutura de pastas como arquitetura de agente

**Fonte:** Van Clief, Jake; McDermott, David (Eduba / University of Edinburgh). *Interpretable Context Methodology: Folder Structure as Agent Architecture.* arXiv 2603.16021v2, 18/03/2026. Licença MIT.
Artigo: https://arxiv.org/html/2603.16021v2
Repositório: https://github.com/RinDig/Interpretable-Context-Methodology
Skill derivada: https://github.com/RinDig/icm-architect
**Consultado em:** 02/09/2026.

## Em uma frase

Para fluxos sequenciais, revisáveis e repetíveis, a arquitetura mais simples para orquestrar uma IA já existe em todo computador: o sistema de arquivos. Um único agente lê o contexto certo, de pastas numeradas, no momento certo.

## O que diz

**Problema.** Frameworks multiagente (CrewAI, LangChain, AutoGen) resolvem coordenação por código. Muitos fluxos reais não precisam disso: são sequências de etapas em que uma pessoa revisa a saída antes de seguir.

**Proposta.** Pastas numeradas representam etapas; arquivos Markdown carregam instruções e estado; scripts locais fazem o trabalho mecânico; toda saída intermediária é um arquivo de texto que a pessoa pode ler e editar antes da próxima etapa.

**Cinco camadas de contexto.**

| Camada | Arquivo | Função |
|---|---|---|
| 0 | `CLAUDE.md` (ou equivalente) | Identidade do espaço de trabalho |
| 1 | `CONTEXT.md` da raiz | Roteamento: qual etapa faz o quê |
| 2 | `CONTEXT.md` de cada etapa | Contrato da etapa: entradas, processo, saídas |
| 3 | `references/`, `_config/` | Material de referência estável (voz, normas, estilo). Internalizado como restrição. |
| 4 | `output/` | Artefatos de trabalho de cada execução. Processados como entrada. |

**Contrato de etapa (exemplo do artigo).**

```
## Inputs
- Layer 4 (working): ../01_research/output/
- Layer 3 (reference): ../../_config/voice.md
## Process
Write a script based on the research output. Follow structure.md. Match voice.md.
## Outputs
- script_draft.md -> output/
```

**Cinco princípios.**
1. Uma etapa, um trabalho (herança do Unix: "faça uma coisa bem feita").
2. Texto simples como interface (Markdown e JSON; qualquer ferramenta participa).
3. Contexto em camadas: o agente recebe só o necessário para a etapa.
4. Toda saída é uma superfície de edição.
5. Configure a fábrica, não o produto: o espaço é configurado uma vez; cada execução produz um novo entregável com a mesma configuração.

**Estrutura de referência (repositório).**

```
workspace/
  CONTEXT.md
  stages/
    01-research/   CONTEXT.md  references/  output/
    02-script/     CONTEXT.md  references/  output/
  _config/   shared/   skills/
  setup/questionnaire.md
```

**Workspace-builder.** Um espaço de cinco etapas cuja saída é outro espaço: descoberta, mapeamento de etapas, scaffolding, desenho do questionário, validação. Para usar: entrar em `workspaces/workspace-builder`, abrir o Claude Code e digitar `setup`.

**Números reportados.**
- Contexto por etapa: 2.000 a 8.000 tokens (1.300 a 1.600 de identidade e roteamento, mais 500 a 2.000 de referências). Abordagem monolítica: 30.000 a 50.000 tokens, faixa em que a literatura documenta degradação ("perdido no meio", Liu et al.).
- De 33 praticantes, 30 relatam padrão de edição em U: 92% editam a etapa 1 (direção), 30% as etapas do meio, 78% a etapa final (verificação de alinhamento).
- 52 membros da comunidade; três pessoas sem experiência em programação criaram e rodaram fluxos completos de animação de dez minutos.
- Usuários não técnicos mudaram o comportamento do sistema editando `CONTEXT.md`, sem ajuda de desenvolvedor.
- Duplicar um espaço existente é o modo preferido de iterar, em vez de construir do zero.

**Onde foi usado.** Neuropolitics Lab (Edinburgh), ICR Research, Academy of International Affairs (Bonn), em pesquisa acadêmica, análise de políticas e produção de conteúdo.

**Direções futuras.** Etapas como passes de compilação; "depuração semântica" (rastrear uma saída até sua fonte); integridade de fonte (corrigir a fonte, não o produto).

## O que aproveitamos

- **A frase-síntese para a oficina:** "a pasta vira um agente com instruções claras, em texto, dentro dela". Marquito e Elton chegaram a isso sozinhos na conversa de 02/09; o artigo dá o nome e a citação.
- **Princípio 5 é o argumento central:** "configure a fábrica, não o produto" é exatamente a distinção "resultado específico versus resultado genérico" da conversa. Quem faz fichamento de 50 artigos não quer 50 prompts, quer uma fábrica de fichamentos que melhora com o uso.
- **Etapas e saídas intermediárias** justificam o "voltar para a etapa 4, não para a zero" que Marquito descreveu com o exemplo do PDF que vira slides.
- **Os números de contexto** (2 a 8 mil contra 30 a 50 mil tokens) dão base para falar de janela de contexto sem demonstrar ao vivo.
- **O padrão em U** orienta onde o pesquisador deve gastar atenção: definir bem a etapa 1 e verificar a final.
- **Usuários não técnicos editam CONTEXT.md**: é a evidência de que o público do Secim consegue, desde que atravesse a abstração "pastas e arquivos".
- **O kit para participantes** (`biblioteca/kits/kit-pesquisa/`) segue a estrutura, simplificada: três etapas, `_referencias/`, `saida/` por etapa, e um registro de auditoria que o ICM não tem mas que a Portaria CNPq pede.

## Cuidados e limites

- Os próprios autores: dados informais, comunidade autosselecionada, testes só com Claude Opus 4.6 e Sonnet 4.6, sem comparação controlada.
- Não serve para colaboração multiagente em tempo real, execução concorrente ou ramificação complexa. Para pesquisa de pós-graduação isso raramente importa.
- O workspace-builder confundiu participantes na oficina dos NTEs ("muito meta"). Para o Secim, não usar ao vivo: entregar a pasta pronta e o prompt único que cria uma estrutura mínima.

## A confirmar

- Se a versão v2 do artigo continua sendo a mais recente na data da oficina.
- Se o repositório mudou a estrutura de pastas (o resumo acima é de 02/09/2026).
