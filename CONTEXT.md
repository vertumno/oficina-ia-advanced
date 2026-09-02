# CONTEXT.md — oficina-ia-advanced

## Identidade

Espaço de trabalho da CGTE/Cefor (Ifes) para preparar oficinas de IA aplicada à pesquisa e à educação. Responsáveis: Marquito (Marcos) e Elton. Língua de trabalho: português.

Objetivo primário: preparar e registrar oficinas (a próxima é o Secim, 17/09/2026).
Objetivo secundário: acumular blocos reutilizáveis para o curso de extensão de 2027 e para um MOOC.

## Camadas (inspirado no ICM)

| Camada | Onde | Natureza |
|---|---|---|
| Identidade e roteamento | `README.md`, este `CONTEXT.md` | Estável |
| Contratos por área | `CONTEXT.md` de cada pasta | Estável |
| Referências | `referencias/`, `biblioteca/` | Estável, cresce devagar |
| Trabalho em andamento | `oficinas/<evento>/`, `futuro/` | Muda a cada evento |
| Bruto processado | `fontes/` | Originais renomeados, com índice; não se edita |
| Bruto recém-chegado | `_inbox/` | Só entra; sai quando processado |

## Roteamento: onde cada tarefa acontece

| Tarefa | Vá para |
|---|---|
| Entender uma fonte (artigo, transcrição, norma) | `referencias/` |
| Buscar um conceito, prompt, kit ou modelo de página | `biblioteca/` |
| Preparar, dar ou registrar uma oficina | `oficinas/<evento>/` |
| Pensar o curso de extensão ou o MOOC | `futuro/` |
| Consultar o material original | `fontes/` (somente leitura; índice em `fontes/CONTEXT.md`) |
| Depositar algo que acabou de chegar | `_inbox/` (e processar: ficha em `referencias/`, original para `fontes/`) |

## Regras para agentes de IA trabalhando nesta pasta

1. Leia o `CONTEXT.md` da pasta onde vai trabalhar antes de criar ou alterar arquivos.
2. Nunca edite ou apague arquivos em `_inbox/` e `fontes/`. Se precisar de uma versão processada, escreva-a em `referencias/`. Renomear só ao mover da inbox para `fontes/`, seguindo a convenção `AAAA-MM-DD-descricao.ext`.
3. Não invente fontes, links, normas ou números. O que não foi verificado recebe a marca *a confirmar*.
4. Um bloco que serve a mais de uma oficina pertence a `biblioteca/`, não a `oficinas/`.
5. Prefira editar a fonte (ficha, conceito, kit) a corrigir uma cópia. Se corrigiu uma cópia, avise que a fonte também precisa mudar.
6. Ao terminar uma tarefa, diga o que fez, quais arquivos tocou e o que a pessoa deve verificar.
7. Registre no `README.md` (seção "Estado atual") mudanças que alteram o rumo do projeto.

## Pessoas e nomes que aparecem no material

- **Marquito (Marcos)** e **Elton**: CGTE/Cefor, ministram a oficina.
- **A organizadora do Secim**: mestranda do Ifes; nome omitido neste repositório público. Contato institucional pelo e-mail cgte.cefor@ifes.edu.br.
- **Rutinelli (Ruth) da Penha Fávero**: CGTE/Cefor; autora do Protocolo de Atenção para Criação de Conteúdos Educacionais com IA; docente convidada do curso de extensão de 2027; deu palestra recente sobre autoria e declaração de uso de IA e tem pastas de pesquisa começadas. Fonte a resgatar.
- **Hugo Cristo Sant'Anna**: professor do PPGP/UFES; seu seminário de IA para pesquisa é fonte de vários blocos (ficha em `referencias/`).
- **Jake Van Clief**: autor do ICM, base metodológica das pastas.
- **Silvio Meira**: autor do artigo-provocação sobre os 29.000 papers.
