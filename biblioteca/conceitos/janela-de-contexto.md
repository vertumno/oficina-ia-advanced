# Janela de contexto

## Em uma frase

A IA só "vê" o que cabe na conversa atual; quando a conversa cresce demais, ela perde o fio, e os resultados pioram sem que você perceba o motivo.

## Como explicar em dois minutos

1. Toda IA generativa trabalha com uma janela: o texto que ela consegue considerar de uma vez (instruções, o que você colou, o que ela mesma já respondeu).
2. Você começa uma conversa, cola três artigos, pede uma coisa, depois outra, depois outra. Em algum ponto a janela enche. A ferramenta corta o começo, resume, ou simplesmente perde precisão. Você não vê isso acontecer.
3. Sintoma: "ela estava indo bem e de repente ficou burra". Não ficou. Ela deixou de ver o que importava.
4. Mesmo antes de encher, há degradação: a pesquisa mostra que modelos vão pior quando a informação relevante está no meio de um contexto longo.
5. Soluções, em ordem de esforço: conversas curtas por tarefa; "projetos" ou instruções fixas nas ferramentas web; no computador, pastas em que cada etapa carrega só o que precisa. No ICM, uma etapa usa de 2 a 8 mil tokens; uma conversa "faz tudo" chega a 30 a 50 mil.

## Analogia ou imagem

Uma mesa de trabalho. Cabe um certo número de papéis abertos. Você vai empilhando; em algum momento o papel que importa está no fundo da pilha e você trabalha olhando a folha errada. A pasta é o arquivo ao lado da mesa: você tira da mesa o que não é desta etapa e guarda onde consegue achar de novo.

Visual: barra que enche; quando passa de um ponto, a resposta fica cinza.

## Fala-chave

"Tem uma coisa acontecendo por baixo dos panos que vocês não estão vendo. Por isso os resultados ficam ruins depois de um tempo."

"Não demonstro isso ao vivo porque leva tempo demais para encher a janela. Mas vocês já viveram isso."

## Erro comum que o conceito corrige

Tentar resolver tudo em uma conversa só, cada vez maior, e culpar a ferramenta. Ou jogar "tudo" em uma pasta genérica que faz tudo: a IA precisa ler um contexto enorme antes de começar e já entra consumindo a janela.

## Fonte

- Van Clief e McDermott (2026), seção sobre eficiência de contexto: 2.000 a 8.000 tokens por etapa contra 30.000 a 50.000 na abordagem monolítica; cita Liu et al. ("lost in the middle").
- Conversa Marquito e Elton, 02/09/2026, trechos 00:16, 00:28 e 01:09 (o caso do carregamento de 45 skills com 80.000 tokens).

## Onde já foi usado

- Secim (17/09/2026), bloco "pedido versus processo", como visual, sem demonstração ao vivo.
