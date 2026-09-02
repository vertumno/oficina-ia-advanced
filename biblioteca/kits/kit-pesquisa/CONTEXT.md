# CONTEXT.md — Kit Pesquisa

## Identidade

Assistente de revisão de literatura com rastro auditável, para pós-graduandos. Uma IA trabalha dentro desta pasta seguindo as instruções escritas aqui. A pessoa dona da pesquisa decide, revisa e responde pelo resultado.

## Estrutura e roteamento

| Pasta ou arquivo | Camada | O que é |
|---|---|---|
| `README.md` | Para a pessoa | Como usar o kit |
| `CONTEXT.md` (este) | Roteamento | O que há e onde cada coisa acontece |
| `AGENTS.md` e `CLAUDE.md` | Regras para a IA | O que a IA pode e não pode fazer |
| `_referencias/` | Referência estável | O tema da pesquisa, as normas e a voz do autor, as bases de busca. A IA lê e obedece; não altera sem pedir |
| `00-entrada/` | Entrada | Artigos e textos que a pessoa coloca |
| `01-fichamento/` | Etapa 1 | Uma ficha por artigo → `01-fichamento/saida/` |
| `02-correlacao/` | Etapa 2 | Correlação das fichas com o tema → `02-correlacao/saida/` |
| `03-relatorio-e-declaracao/` | Etapa 3 | Relatório do processo e rascunho da declaração de uso de IA → `03-relatorio-e-declaracao/saida/` |
| `registro/LOG-IA.md` | Rastro | Registro de toda ação da IA: data, etapa, ferramenta, o que fez, o que a pessoa deve verificar |

## Fluxo

```
00-entrada/  →  01-fichamento/saida/  →  02-correlacao/saida/  →  03-relatorio-e-declaracao/saida/
                       ↑ revisão humana        ↑ revisão humana            ↑ revisão humana
registro/LOG-IA.md recebe uma entrada a cada ação, em todas as etapas
```

Cada etapa tem um `CONTEXT.md` com o contrato: **Entradas** (o que ler), **Processo** (o que fazer), **Saídas** (o que escrever e onde), **Verificação** (o que a pessoa confere antes de seguir).

## Como uma etapa é executada

1. A pessoa pede: "Leia `0N-.../CONTEXT.md` e execute a etapa".
2. A IA lê `AGENTS.md`, este arquivo, o `CONTEXT.md` da etapa e as referências listadas no contrato.
3. A IA executa, escreve só em `0N-.../saida/`, registra em `registro/LOG-IA.md`.
4. A IA termina com um resumo: o que fez, o que não conseguiu, o que a pessoa deve verificar.
5. A pessoa revisa e edita os arquivos em `saida/` antes de pedir a próxima etapa.

## Como crescer

- Nova etapa: copie a pasta de uma etapa, renumere, reescreva o `CONTEXT.md`. Atualize a tabela acima.
- Nova pasta para outra tarefa: copie o kit inteiro e reescreva as instruções.
- Mudou o jeito de fichar? Edite `01-fichamento/CONTEXT.md`, não a ficha. A próxima execução já sai do jeito novo.
