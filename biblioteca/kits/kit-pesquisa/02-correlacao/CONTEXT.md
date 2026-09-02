# CONTEXT.md — Etapa 02: Correlação com o tema

## Objetivo

Cruzar as fichas da etapa 01 com o tema e as dimensões da pesquisa, para mostrar convergências, divergências e lacunas, sempre apontando para a ficha e a página de origem.

## Entradas

- Todas as fichas em `../01-fichamento/saida/` (já revisadas pela pessoa).
- `../_referencias/minha-pesquisa.md` (dimensões, pergunta, o que quero descobrir).
- `../_referencias/bases-de-busca.md` (só para a seção de sugestões de busca).

Não ler: os artigos originais em `../00-entrada/` (a etapa trabalha sobre as fichas revisadas; se uma ficha estiver insuficiente, dizer isso em vez de voltar ao artigo), `../03-relatorio-e-declaracao/`.

## Processo

1. Ler todas as fichas. Se alguma estiver marcada com muitos "a confirmar" ou "[inferência]", avisar no início da saída e prosseguir com cautela.
2. Montar a tabela de correlação: uma linha por artigo, uma coluna por dimensão do tema. Nas células, uma frase curta e a referência à ficha (ex.: "ficha-silva-2023, p. 7").
3. Listar convergências entre os artigos e com a pesquisa; divergências; e lacunas (o que nenhum artigo trata e a pesquisa precisa).
4. Para cada lacuna, sugerir de uma a três buscas (base, termos, por quê), usando `bases-de-busca.md`. Não afirmar que artigos existem.
5. Não responder à pergunta de pesquisa. Não propor mudanças no tema ou no referencial. Se notar algo que pareça importante, colocar em "Observações para a pesquisadora", como pergunta.
6. Registrar a ação em `../registro/LOG-IA.md`.

## Saídas

Um arquivo `saida/correlacao.md`:

```
# Correlação: artigos × tema

Etapa 02 · [data] · [ferramenta e modelo] · Entradas: [lista das fichas]

## Aviso sobre a qualidade das fichas (se houver)

## Tabela de correlação
| Artigo | Dimensão 1 | Dimensão 2 | ... |
|---|---|---|---|
| [ficha-x] | [frase, p. N] | ... | ... |

## Convergências
- [item] (ficha-a, p. N; ficha-b, p. M)

## Divergências
- [item] (fichas e páginas)

## Lacunas
- [o que nenhum artigo trata] → buscas sugeridas: [base: termos] porque [motivo]

## Observações para a pesquisadora
- [perguntas, não conclusões]

Verificar:
- [cada célula da tabela que a pessoa deve conferir contra a ficha]
- [lacunas: confirmar que de fato nenhum artigo trata]
```

## Verificação (antes de seguir para a etapa 03)

- Conferir a tabela linha a linha contra as fichas.
- Decidir o que fazer com as lacunas (buscar mais artigos e repetir a etapa 01 para eles, ou seguir).
- Editar o arquivo à vontade: o que ficar é o que a etapa 03 vai relatar.

## Encerramento da etapa

Resumo em três partes. Não iniciar a etapa 03.
