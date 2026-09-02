# Sala Moodle da oficina dos NTEs — blocos HTML de referência

**Fonte:** `fontes/2026-08-sala-moodle-ia-ntes-blocos.html` (HTML com estilo inline, feito para colar em rótulos ou páginas do Moodle; chegou como `ref-sala-IA-NTEs.txt`). Cópia editável em `biblioteca/paginas/modelo-blocos-moodle-ntes.html`.
**Origem:** oficina de IA dada aos Núcleos de Tecnologia Educacional (NTEs) atendidos pelo Cefor, em 2026, com foco em docentes e uso de IA no computador (projetos, pastas, ICM, workspace-builder).
**Consultado em:** 02/09/2026.

## Em uma frase

Quatro blocos coloridos, autocontidos, que funcionam como "página que fica com o participante": comece aqui, uso responsável, organize seu trabalho, quero avançar.

## Estrutura dos blocos

| Bloco | Cor | Conteúdo | Links |
|---|---|---|---|
| Comece aqui | Azul (#2e75b6) | "Não é preciso dominar todas as ferramentas. Comece por uma necessidade real do seu trabalho." Sugestão: escolha uma tarefa concreta. | Ações de IA no Cefor; Base de Conhecimento |
| Uso responsável | Amarelo (#f0bb14) | Quatro perguntas antes de usar IA: posso compartilhar estes dados? consigo verificar? está claro onde a IA foi usada? a decisão e a responsabilidade continuam minhas? | Manual de ética; Protocolo de Atenção (Fávero) |
| Organize seu trabalho com IA | Verde (#259b8a) | Quatro cartões: contexto, referências, continuidade, verificação. Progressão: conversa avulsa → contexto bem definido → projeto organizado → assistente especializado. Comentário `EDITE AQUI` para projetos, pastas, contexto, ICM. | GPTs do Cefor |
| Quero avançar | Roxo (#7653b6) | Aprofundar repertório, comunidades. Comentário `EDITE AQUI` para materiais avançados, ICM, automações. | Portal IA.IA; Papo com IA.IÁ; Podcasts, palestras e oficinas |

Padrão visual: fonte Arial; borda esquerda de 6px na cor do bloco; fundo claro da mesma família; título em `h3` 24px; cartões brancos com borda de 1px; largura máxima 1100px. Sem CSS externo, sem JavaScript: cola direto no editor do Moodle.

## O que aproveitamos

- **A página de referências do Secim** (`oficinas/2026-09-17-secim/referencias-secim.html`) usa a mesma linguagem visual e acrescenta o que os comentários `EDITE AQUI` pediam: pastas como agentes, ICM, kit para baixar, além de um bloco novo sobre declaração de uso de IA na pesquisa e um bloco de ferramentas por etapa (funil do Hugo).
- **As quatro perguntas do bloco amarelo** ganham versão para pesquisa: posso subir estes dados de participantes? consigo verificar cada referência? saberei dizer à banca o que a IA fez? a interpretação continua minha?
- **A progressão do bloco verde** ganha um passo a mais: "assistente especializado" vira "pasta que vira agente".

## Cuidados e limites

- O HTML original não tem os links de projetos e ICM (só os comentários pedindo). A versão do Secim preenche.
- Cores e contraste foram pensados para fundo claro do Moodle. Se a página for publicada fora do Moodle (GitHub Pages, artefato), incluir fundo explícito.
- O texto fala "seu trabalho" e "decisão pedagógica" (público docente). Para o Secim, trocar por "sua pesquisa" e "interpretação".

## A confirmar

- Onde a página do Secim será hospedada (sala Moodle aberta? página no Portal IA.IA? Base de Conhecimento?). Isso define se entregamos HTML inline (Moodle) ou página completa.
