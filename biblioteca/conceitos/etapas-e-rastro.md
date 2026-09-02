# Etapas e rastro auditável

## Em uma frase

Dividir o trabalho em etapas com saídas intermediárias visíveis permite corrigir onde o erro aconteceu (e não recomeçar do zero) e produz, de graça, o registro do que a IA fez, que é o que você precisa para declarar e defender.

## Como explicar em dois minutos

1. Um prompt que faz tudo é uma caixa-preta grande: entra PDF, sai apresentação. Se a apresentação ficou ruim, você mexe no pedido inicial e torce.
2. Divida em etapas: extrair conteúdo do PDF → organizar em tópicos → definir slides → montar o arquivo final. Agora são quatro caixinhas, e entre elas há arquivos que você pode abrir.
3. Se a etapa 4 saiu errada, você olha a saída da 3. Se ela estava certa, o problema é na 4; se estava errada, corrige a 3 e reprocessa só dali. Muito menos trabalho que refazer tudo.
4. Como cada etapa deixa um arquivo, você tem um rastro: o que entrou, o que saiu, o que a IA fez, o que você mudou. É a diferença entre "usei IA" e "a IA fez X na etapa Y, com a ferramenta Z, e eu verifiquei W".
5. A pesquisa com ICM mostra onde as pessoas gastam atenção: 92% editam a primeira etapa (definir a direção), 30% as do meio, 78% a última (verificar alinhamento). Ou seja: capriche na entrada, confie no meio, verifique a saída.

## Analogia ou imagem

Uma linha de montagem com estações. Em cada estação há uma bandeja com o que saiu. Se o produto final tem defeito, você anda pela linha olhando as bandejas até achar em qual estação ele apareceu.

Para a banca: o rastro é o caderno de laboratório da pesquisa com IA.

## Fala-chave

"A gente dividiu a caixa-pretona em seis caixinhas pretas."

"Se na quinta etapa deu problema, a gente não volta para a etapa zero. Volta para a quarta."

"Não só fazer, mas fazer e dizer o que fez. Aí você consegue defender numa banca: eu fiz X, a IA me ajudou em Y, a fonte é esta."

## Erro comum que o conceito corrige

Usar IA na última hora, com prompt mal feito, jogar tudo na conversa, receber um resultado razoável e esconder que foi feito com IA. "Qual a chance de entregar uma coisa ruim, ser percebido que foi feito por IA, sem ter dito que foi? Ninguém quer isso."

E, do outro lado, o repositório com 750 inserções feitas por bot que a pessoa não sabe mais onde estão: perdeu o controle porque não conseguia auditar o que a IA fazia. "A IA é amplificadora: de organização ou de desorganização."

## Fonte

- Van Clief e McDermott (2026): princípio 4 ("every output is an edit surface"), padrão em U, observabilidade como padrão, direções futuras ("semantic debugging").
- Portaria CNPq 2.664/2026: declarar ferramenta, finalidade e fase. O rastro por etapa entrega exatamente esses três dados. Ficha em `referencias/normas-uso-ia-pesquisa-brasil.md`.
- Conversa Marquito e Elton, 02/09/2026, trechos 00:15 a 00:16, 00:27, 00:44 e 01:00 a 01:02.

## Onde já foi usado

- Secim (17/09/2026): é o conceito que une o bloco de ética (declarar) ao bloco de método (pastas). Ver `oficinas/2026-09-17-secim/02-analise-e-melhorias.md`.
