# Skill "Integridade e IA na Pesquisa" (Cefor/Ifes)

**Fonte:** pacote de skill para Claude (SKILL.md + assets + references), recebido pronto de terceiros para
distribuição a mestrandos e doutorandos do Ifes. Versão 1.0, base normativa verificada em 15/09/2026.
Arquivo original: `fontes/2026-09-17-skill-integridade-ia-pesquisa-cnpq.zip`.
**Consultado em:** 17/09/2026.

## Em uma frase

Uma skill de Claude que responde, em linguagem simples e ancorada na Portaria CNPq nº 2.664/2026, às quatro
perguntas do pós-graduando sobre uso de IA generativa na pesquisa: pode usar, como registra, como declara e se
pode entregar tranquilo.

## O que diz (síntese fiel)

- Instalada em `.claude/skills/integridade-ia-pesquisa/` deste repositório (formato padrão de skill do Claude
  Code: `SKILL.md` com frontmatter `name`/`description`, mais `assets/` e `references/`).
- Estrutura em quatro perguntas + um caminho de socorro:
  1. **Posso usar IA nisso?** Semáforo (verde/amarelo/vermelho) por tipo de uso, com o artigo da portaria
     (`references/triagem-de-usos.md`).
  2. **Como registro o que usei?** Diário de Uso de IA de 5 campos, em `.md` e `.csv`
     (`assets/diario-uso-ia.md`, `assets/diario-uso-ia.csv`), mais Plano de Uso de IA com o orientador
     (`assets/plano-uso-ia.md`).
  3. **Como declaro?** Gera declaração (texto e quadro) a partir do diário, para dissertação, tese, artigo,
     relatório ou slides (`references/modelos-de-declaracao.md`).
  4. **Posso entregar tranquilo?** Checklist pré-entrega: citações, referências inexistentes, dados, autoria
     (`references/checklist-pre-entrega.md`, `references/autoria-e-colaboracao.md`).
  - **Socorro:** regularização de uso não declarado, conforme a etapa (seção "Regularização" em
    `references/modelos-de-declaracao.md`).
- Também cobre dados de participantes e sigilo (`references/dados-e-privacidade.md`), a portaria explicada em
  linguagem simples (`references/mapa-da-portaria.md`) e o texto de apoio da própria portaria
  (`references/portaria-cnpq-2664-2026.md`), além de contexto Ifes/CAPES/outras normas
  (`references/contexto-ifes-e-outras-normas.md`).
- Princípios inegociáveis: forma, não policia; nunca inventa artigo, prazo ou sanção (marca **[NORMA]**,
  **[BOA PRÁTICA]** ou **[INTERPRETAÇÃO]**); não é detector de IA; não substitui orientador, CEP ou PRPPG; nunca
  pede dados identificáveis de participantes; nunca usa travessão nos textos que gera.
- Vem com um guia para o estudante instalar a mesma skill na própria conta do claude.ai (dentro do zip original,
  não copiado ao repositório: ver "Cuidados e limites").

## O que aproveitamos

- Skill instalada e pronta para uso neste repositório ao trabalhar com Claude Code
  (`.claude/skills/integridade-ia-pesquisa/`).
- Reforça e opera o mesmo material da ficha `normas-uso-ia-pesquisa-brasil.md`: os três elementos da declaração
  (ferramenta, finalidade, fase) e "autoria exclusivamente humana, responsabilidade integral" aparecem aqui como
  regras vivas, com semáforo e modelos prontos, não só como síntese normativa.
- O Diário de Uso de IA e o Plano de Uso de IA (`assets/`) são candidatos a modelo para
  `biblioteca/kits/kit-pesquisa/registro/LOG-IA.md` e para `biblioteca/prompts/modelo-declaracao-uso-ia.md`, se
  quisermos alinhar os dois materiais.
- **Decisão de 17/09/2026:** a skill fica separada do Kit Pesquisa (natureza, público e manutenção diferentes) e é
  distribuída na página do participante do Secim (`oficinas/2026-09-17-secim/referencias-secim.html`, seção
  `#skill`), com download pela pasta da oficina no Drive (origem `oficinas/2026-09-17-secim/downloads/integridade-ia-pesquisa.zip`, cópia fiel do zip interno do pacote),
  instalação e exemplos adaptados do guia para estudantes. Ponte com o kit: levar `relatorio-do-processo.md` e
  `declaracao-uso-ia.md` da etapa 03 à skill.
- Pode virar um bloco de "continuidade pós-oficina" (como já fazemos com outras skills/kits): ensinar o
  participante a instalar a skill na própria conta do claude.ai usando o guia embutido no zip original.

## Cuidados e limites

- O conteúdo normativo (datas, artigos, sanções) tem a mesma ressalva da ficha `normas-uso-ia-pesquisa-brasil.md`:
  confirmar o texto integral da Portaria 2.664/2026 antes de citar artigo específico em material oficial da
  oficina.
- O guia de instalação para o estudante (`guia-da-skill-para-estudantes.md`, dentro do zip original em
  `fontes/`) não foi copiado para `biblioteca/`; se for usado num material de participante, extrair e adaptar a
  partir do zip, não reescrever de memória.
- A skill se autodeclara "bússola, não tribunal": não fiscaliza nem substitui orientador, CEP ou PRPPG. Manter
  esse enquadramento ao apresentá-la na oficina, para não sugerir que ela emite parecer oficial.

## A confirmar

- Autoria e licença de uso do pacote da skill (recebido pronto; autor e permissão de redistribuição a
  confirmar antes de oferecê-la a participantes fora deste repositório).
- Se o texto da Portaria em `references/portaria-cnpq-2664-2026.md` bate com o Diário Oficial (mesma checagem
  pendente na ficha `normas-uso-ia-pesquisa-brasil.md`).
