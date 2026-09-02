# CONTEXT.md — paginas

## O que há aqui

Modelos de "página que fica com o participante": blocos HTML com estilo inline, sem CSS externo nem JavaScript, feitos para colar no editor do Moodle ou publicar como página simples.

| Arquivo | Origem | Uso |
|---|---|---|
| `modelo-blocos-moodle-ntes.html` | Cópia fiel de `fontes/2026-08-sala-moodle-ia-ntes-blocos.html` (sala da oficina dos NTEs) | Modelo visual e estrutural: quatro blocos coloridos (comece aqui, uso responsável, organize seu trabalho, quero avançar) |

Páginas adaptadas para um evento ficam na pasta do evento (ex.: `oficinas/2026-09-17-secim/referencias-secim.html`). Se uma adaptação criar um bloco novo que serve para todos (como o bloco de declaração de uso de IA na pesquisa), trazer o bloco para cá como modelo.

## Padrão visual dos blocos

- Fonte Arial; texto `#23313f`; largura máxima 1100px; margem inferior 22px.
- Cabeçalho do bloco: borda esquerda de 6px na cor do bloco, fundo claro da mesma família, rótulo em maiúsculas pequenas, `h3` de 24px.
- Cartões internos brancos com borda de 1px e raio de 8px.
- Cores usadas: azul `#2e75b6`, amarelo `#f0bb14`, verde `#259b8a`, roxo `#7653b6`. Ao criar bloco novo, escolher uma cor distinta e manter a mesma estrutura.

## Regras

- Sem CSS externo, sem `<script>`, sem `<html>` ou `<body>`: o bloco é colado dentro de uma página existente.
- Todo link com `target="_blank" rel="noopener"`.
- Links verificados na data de publicação; anotar a data no arquivo da oficina.
