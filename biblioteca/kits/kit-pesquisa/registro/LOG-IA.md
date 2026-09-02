# LOG-IA — registro de ações da IA nesta pasta

Toda ação da IA dentro do Kit Pesquisa recebe uma entrada aqui, acrescentada ao final, sem apagar as anteriores. É o caderno de laboratório do uso de IA: dele saem o relatório do processo e a declaração de uso (etapa 03).

Campos obrigatórios em cada entrada: data e hora; etapa; ferramenta e modelo; o que fez; arquivos lidos; arquivos escritos; o que a pessoa deve verificar. Quando a pessoa corrigir algo, ela (ou a IA, a pedido) registra a correção também: é isso que mostra o humano no laço.

## Formato

```
## [AAAA-MM-DD HH:MM] · Etapa [00/01/02/03] · [Ferramenta, modelo]
- Ação: [o que fez, em uma ou duas frases]
- Leu: [arquivos]
- Escreveu: [arquivos]
- Verificar: [o que a pessoa deve conferir]
- Observações: [invenções detectadas e corrigidas, conversões, arquivos não lidos, dúvidas]
```

## Exemplo

```
## [2026-09-17 16:52] · Etapa 01 · Claude Code, Claude Sonnet 4.6
- Ação: fichamento do artigo silva-2023-geogebra.pdf conforme 01-fichamento/CONTEXT.md.
- Leu: 00-entrada/silva-2023-geogebra.pdf; _referencias/minha-pesquisa.md; _referencias/normas-e-voz.md
- Escreveu: 01-fichamento/saida/ficha-silva-2023-geogebra.md
- Verificar: citações das páginas 7 e 12; DOI não constava no PDF, marcado "a confirmar".
- Observações: o PDF não tem numeração nas duas últimas páginas; localização indicada por seção.

## [2026-09-17 17:05] · Revisão humana · [nome da pesquisadora]
- Ação: conferi as duas citações; a da p. 12 estava correta, a da p. 7 estava na p. 8. Corrigi na ficha.
- Escreveu: 01-fichamento/saida/ficha-silva-2023-geogebra.md
```

## Entradas

(as entradas começam abaixo desta linha)
