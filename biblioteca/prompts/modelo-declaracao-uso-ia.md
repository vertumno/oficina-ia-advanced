# Modelo de declaração de uso de IA generativa

Base normativa: Portaria CNPq nº 2.664/2026 (declarar **ferramenta**, **finalidade** e **fase** da pesquisa; responsabilidade integral do autor; IA não é autora). Posição no documento, conforme orientação da UFRRJ (Memorando 93/2026): parte pré-textual, após os agradecimentos. Verifique se o seu programa, banca ou periódico tem modelo próprio; se tiver, ele prevalece.

Ficha com as fontes: `referencias/normas-uso-ia-pesquisa-brasil.md`.

## Princípios que a declaração precisa refletir

1. Diz **o que** foi usado (ferramenta, versão ou data de uso).
2. Diz **para quê** (finalidade concreta: fichamento, revisão gramatical, tradução, geração de código, análise de dados, organização de referências).
3. Diz **em que fase** (concepção, levantamento bibliográfico, coleta, análise, redação, revisão, submissão).
4. Afirma que **o conteúdo foi revisado e é de responsabilidade do autor**, e que **a IA não é autora**.
5. Não esconde nem infla. Quem usou só para revisar gramática declara só isso.

## Variante A: dissertação ou tese

```
DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL GENERATIVA

Declaro que, na elaboração desta [dissertação/tese], utilizei ferramentas de inteligência artificial generativa nas seguintes fases e finalidades:

- [Fase: levantamento bibliográfico] — [Ferramenta e versão, ex.: Claude Sonnet 4.6, via Claude Code, em agosto de 2026] — [Finalidade: fichamento preliminar de artigos e elaboração de matriz de correlação entre os artigos e o tema da pesquisa]. Todas as fichas foram conferidas por mim contra os textos originais.
- [Fase: redação] — [Ferramenta] — [Finalidade: revisão gramatical e sugestões de clareza em trechos do capítulo 3]. As sugestões foram aceitas ou rejeitadas por mim, uma a uma.
- [Fase: análise de dados] — [Ferramenta] — [Finalidade: geração de scripts em R para as análises descritas na seção 4.2]. Os scripts foram revisados e executados por mim; os resultados foram verificados [descrever como].

Nenhuma ferramenta de IA foi usada para [ex.: gerar dados, produzir a interpretação dos resultados, redigir as conclusões], salvo o indicado acima. As ferramentas de IA não são autoras deste trabalho. Assumo integral responsabilidade pelo conteúdo, pela exatidão das referências e pela originalidade do texto.

O registro detalhado das interações com IA está disponível em [ex.: apêndice X / repositório / arquivo registro/LOG-IA.md], e pode ser consultado pela banca.

[Cidade], [data]. [Nome]
```

## Variante B: artigo ou trabalho para evento

```
Uso de inteligência artificial generativa. Os autores utilizaram [ferramenta e versão] para [finalidade(s)] na fase de [fase(s)]. Todo o conteúdo gerado foi revisado e editado pelos autores, que assumem integral responsabilidade pelo texto. A ferramenta não é autora e não foi usada para [o que não foi feito, se relevante].
```

Colocar na seção indicada pelo periódico ou evento (geralmente "Declarações" ou nota antes das referências). Se o veículo tem modelo próprio, use o dele.

## Variante C: trabalho de disciplina

```
Declaro que usei [ferramenta] para [finalidade] neste trabalho, em [fase]. Revisei o conteúdo gerado e respondo por ele. Não usei IA para [o que não foi feito]. Registro das interações disponível em [onde], se o professor solicitar.
```

## Como o kit gera isso

No `kit-pesquisa`, a etapa `03-relatorio-e-declaracao` lê o `registro/LOG-IA.md` e as saídas das etapas anteriores e escreve um rascunho da Variante A com os campos preenchidos a partir do registro. O autor revisa, corta o que não se aplica e assina. A declaração não sai da cabeça: sai do rastro.

## Histórico

- 02/09/2026: escrito com base nas fichas de normas. Confirmar o texto integral da Portaria antes da oficina para citar o artigo correto.
