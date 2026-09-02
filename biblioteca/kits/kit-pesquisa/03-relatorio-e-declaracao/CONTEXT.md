# CONTEXT.md — Etapa 03: Relatório do processo e declaração de uso de IA

## Objetivo

Transformar o registro de ações e as saídas das etapas em dois documentos: um relatório do que a IA fez (para a pesquisadora, a orientação e a banca) e um rascunho da declaração de uso de IA generativa, nos termos da Portaria CNPq nº 2.664/2026 (ferramenta, finalidade, fase; responsabilidade do autor; IA não é autora).

## Entradas

- `../registro/LOG-IA.md` (todas as entradas).
- `../01-fichamento/saida/` e `../02-correlacao/saida/` (para contar o que foi produzido e o que foi revisado).
- `../_referencias/minha-pesquisa.md` (identificação, programa, fase da pesquisa).
- `../_referencias/normas-e-voz.md` (onde a declaração vai ficar; exigências do veículo).

Não ler: `../00-entrada/`.

## Processo

1. Ler o registro inteiro. Agrupar as entradas por etapa e por tipo de ação (leitura, conversão, fichamento, correlação, correção após revisão humana).
2. Escrever o relatório do processo: o que a IA fez, em que ordem, com quais arquivos, e o que a pessoa revisou ou corrigiu (o registro deve ter isso; se não tiver, dizer que não consta).
3. Escrever o rascunho da declaração preenchendo, a partir do registro, os campos ferramenta, finalidade e fase. Usar a fase da pesquisa informada em `minha-pesquisa.md`. Se o veículo-alvo tiver modelo próprio (em `normas-e-voz.md`), seguir o modelo do veículo.
4. Listar o que a IA **não** fez, para que a declaração não infle nem esconda.
5. Registrar a ação em `../registro/LOG-IA.md`.

## Saídas

`saida/relatorio-do-processo.md`:

```
# Relatório do processo com IA

Etapa 03 · [data] · [ferramenta e modelo]

## Resumo
[quantos artigos, quantas fichas, quantas correções humanas registradas, período]

## Linha do tempo
| Data | Etapa | Ação | Arquivos | Verificação humana registrada |
|---|---|---|---|---|

## O que a IA fez
## O que a pessoa fez (conforme o registro)
## O que a IA não fez
## Problemas registrados (invenções corrigidas, arquivos não lidos, conversões)

Verificar:
- [se a linha do tempo bate com a lembrança da pessoa]
```

`saida/declaracao-uso-ia.md`:

```
# Declaração de uso de inteligência artificial generativa (rascunho)

Base: Portaria CNPq nº 2.664/2026. Posição sugerida: parte pré-textual, após os agradecimentos (confirmar com o programa).

DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL GENERATIVA

Declaro que, na elaboração deste trabalho, utilizei ferramentas de inteligência artificial generativa nas seguintes fases e finalidades:

- Fase: [fase] — Ferramenta: [ferramenta, modelo, período] — Finalidade: [finalidade concreta]. [Como foi verificado.]
- ...

Nenhuma ferramenta de IA foi usada para [o que o registro mostra que não foi feito]. As ferramentas de IA não são autoras deste trabalho. Assumo integral responsabilidade pelo conteúdo, pela exatidão das referências e pela originalidade do texto.

O registro das interações está disponível em [registro/LOG-IA.md desta pasta] e pode ser consultado pela banca.

[Cidade], [data]. [Nome]

Verificar:
- Cada linha da declaração contra o registro.
- Se o programa, a banca ou o periódico exigem modelo próprio.
- Cortar o que não se aplica; não deixar colchetes.
```

## Verificação

A pessoa lê os dois documentos, corrige, assina a declaração. O rascunho não é a declaração: a declaração é o que a pessoa assina.

## Encerramento da etapa

Resumo em três partes. Sugerir, se fizer sentido, que a pessoa guarde a pasta inteira junto com a pesquisa.
