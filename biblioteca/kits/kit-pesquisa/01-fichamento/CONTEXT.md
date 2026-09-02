# CONTEXT.md — Etapa 01: Fichamento

## Objetivo

Produzir uma ficha de leitura por artigo, fiel ao texto, com citações localizáveis e uma primeira leitura da relação com o tema da pesquisa.

## Entradas

- Artigos em `../00-entrada/` (todos, ou os que a pessoa indicar).
- `../_referencias/minha-pesquisa.md` (tema, pergunta, dimensões, o que não fazer).
- `../_referencias/normas-e-voz.md` (formato da referência e das citações).

Não ler: `../02-correlacao/`, `../03-relatorio-e-declaracao/`, `bases-de-busca.md`.

## Processo

Para cada artigo, na ordem alfabética dos nomes de arquivo:

1. Ler o artigo inteiro. Se não conseguir ler (formato, tamanho, proteção), registrar e seguir para o próximo.
2. Escrever a ficha com as seções abaixo. Cada afirmação sobre o artigo precisa ser sustentável pelo texto; se for inferência sua, marcar como "[inferência]".
3. Citações literais: transcrever exatamente, entre aspas, com número de página. Se o arquivo não tiver paginação, indicar a seção e a posição aproximada e marcar "[página a confirmar]".
4. Relação com o tema: usar as "Dimensões do tema" de `minha-pesquisa.md` como roteiro. Para cada dimensão, dizer se o artigo trata, como trata, ou se não trata.
5. Registrar a ação em `../registro/LOG-IA.md`.

## Saídas

Um arquivo por artigo em `saida/`, nomeado `ficha-<nome-do-arquivo-de-entrada>.md`, com esta estrutura:

```
# Ficha: [título do artigo]

Etapa 01 · [data] · [ferramenta e modelo] · Entrada: [nome do arquivo]

## Referência
[no formato de normas-e-voz.md]

## Objetivo do artigo
## Contexto e participantes (se houver)
## Método
## Principais achados
[três a seis itens, cada um com a página onde aparece]

## Citações literais
1. "[trecho exato]" (p. X)
2. "[trecho exato]" (p. Y)

## Relação com o meu tema
| Dimensão | Trata? | Como |
|---|---|---|
[uma linha por dimensão de minha-pesquisa.md]

## Convergências e divergências com a minha pesquisa
## Limites que o próprio artigo reconhece
## O que eu ainda preciso ler ou confirmar

Verificar:
- [lista do que a pessoa deve conferir: páginas, referência completa, afirmações marcadas como inferência]
```

## Verificação (antes de seguir para a etapa 02)

A pessoa deve:
- Abrir cada ficha e conferir ao menos as duas citações literais contra o artigo.
- Conferir a referência completa (autores, ano, periódico, volume, páginas, DOI).
- Corrigir ou apagar o que estiver errado. A ficha corrigida é a entrada da etapa 02.

## Encerramento da etapa

Resumo em três partes: o que foi fichado; o que não foi possível (e por quê); o que verificar. Não iniciar a etapa 02.
