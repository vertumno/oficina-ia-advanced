# CONTEXT.md — _inbox

## O que é

Caixa de entrada. Tudo que chega (transcrição, conversa, PDF, HTML, ata, artigo) é colocado aqui como está, sem editar. A meta é a inbox ficar vazia: cada item é processado e sai daqui.

## O ciclo de um item

1. **Chegou:** coloque o arquivo aqui, com o nome que veio.
2. **Processe:** leia e escreva (ou peça à IA para escrever) uma ficha em `referencias/`, seguindo o modelo de `referencias/CONTEXT.md`. Se o item for de uma oficina específica, o processamento pode ir para `oficinas/<evento>/00-briefing.md`.
3. **Arquive:** mova o original para `fontes/` com nome `AAAA-MM-DD-descricao.ext` e acrescente uma linha na tabela de `fontes/CONTEXT.md`.
4. **Aponte:** a ficha cita o caminho em `fontes/`.

## Regras

- Nada aqui é editado. Se precisar de versão processada, ela nasce em `referencias/` ou `oficinas/`.
- Um item não fica aqui mais de uma sessão de trabalho sem ao menos uma linha de registro em `fontes/CONTEXT.md` dizendo o que é e quem vai processar.
- Estado em 17/09/2026: vazia. O zip da skill "Integridade IA Pesquisa CNPQ" foi processado: instalado em
  `.claude/skills/integridade-ia-pesquisa/`, arquivado em `fontes/` e fichado em `referencias/`.
