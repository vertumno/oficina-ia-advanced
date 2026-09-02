# Roteiro da demonstração ao vivo (bloco 5, 25 minutos)

Script para o Marquito na máquina, com o Elton circulando. Prompts exatos, o que dizer, o que mostrar, o que pode dar errado. Ensaiar em 14/09 e gravar como reserva.

## Preparação da máquina (antes das 15h15)

- Área de trabalho limpa. Duas pastas: `secim-demo/` (vazia) e `kit-pesquisa/` (o kit, com **um** artigo de exemplo em `00-entrada/`, nomeado `sobrenome-ano-tema.pdf`, e `_referencias/minha-pesquisa.md` preenchido com um tema de exemplo em Educação Matemática).
- Uma terceira pasta, `kit-pesquisa-ensaio/`, com as saídas geradas no ensaio (ficha, correlação, relatório, declaração, registro preenchido). É o plano B.
- VS Code aberto em `secim-demo/`, com o terminal integrado e o Claude Code logado. Fonte do editor e do terminal em 18 ou mais. Tema claro (projeta melhor). Barra lateral do explorador visível.
- Segunda janela do VS Code aberta em `kit-pesquisa/`, minimizada.
- Navegador com duas abas: as conversas "pedido versus processo" já rodadas. E uma terceira aba com a página de referências.
- Notificações desligadas. Wi-Fi conectado; hotspot 4G pronto.
- Vídeo de reserva aberto no reprodutor, pausado.

## Parte A: a pasta nasce (8 min)

**Dizer:** "Esta pasta está vazia. Vou pedir para a IA criar uma estrutura mínima. Reparem que eu digo exatamente o que quero, e digo para não fazer mais nada."

**Colar** (de `biblioteca/prompts/prompt-cria-pasta.md`):

```
Estamos em uma pasta vazia. Crie nela uma estrutura mínima para um assistente de pesquisa com rastro auditável, exatamente assim, sem acrescentar nada além disto:

minha-pesquisa-ia/
  README.md                 (o que é esta pasta e como usar, em 10 linhas)
  CONTEXT.md                (regras para a IA: ler antes de agir; não inventar referências; registrar toda ação em registro/LOG-IA.md; escrever só em pastas "saida"; perguntar antes de apagar qualquer coisa)
  _referencias/
    minha-pesquisa.md       (modelo em branco com: tema, pergunta de pesquisa, referencial teórico, público, o que já sei, o que quero descobrir)
  01-fichamento/
    CONTEXT.md              (contrato: entrada = artigos em 00-entrada; processo = ficha por artigo com referência, objetivo, método, achados, duas citações literais com página, relação com meu tema; saída = 01-fichamento/saida/ficha-<nome>.md; ao final, listar o que eu devo verificar)
    saida/
  00-entrada/               (onde eu coloco os artigos)
  registro/
    LOG-IA.md               (cabeçalho e formato: data, etapa, ferramenta e modelo, o que fez, arquivos lidos e escritos, o que o humano deve verificar)

Escreva todos os arquivos em português. Depois de criar, me mostre a árvore de pastas e explique, em uma frase por arquivo, para que serve cada um. Não execute nenhuma etapa ainda.
```

**Enquanto roda (1 a 2 min):** "Ela vai pedir permissão para criar arquivos. Leiam comigo o que ela pede. Eu autorizo porque é a minha pasta e é isso que eu pedi. É a primeira regra de segurança: ler o que ela quer fazer."

**Quando terminar:**
1. Apontar a árvore no explorador: "Isto são pastas e arquivos no meu computador. Nada de mágico."
2. **Abrir `01-fichamento/CONTEXT.md` e ler em voz alta** (30 segundos). "A instrução está aqui. Em texto. Se eu quiser três citações em vez de duas, eu mudo aqui, não peço de novo toda vez."
3. Abrir `registro/LOG-IA.md`: "Vazio. Tudo que a IA fizer vai ficar registrado aqui. Ferramenta, o que fez, o que eu tenho que verificar. Reparem: são os três dados que a norma pede."
4. "Isto é o esqueleto. Agora vou mostrar uma pasta que já está boa, que vocês vão levar."

**Se der errado:** a IA criou coisa a mais → "remova o que não estava na lista" (e comentar: instruções precisam ser fechadas). Escreveu em inglês → "reescreva em português". Travou → passar direto para a Parte B; o esqueleto está no kit.

## Parte B: a pasta trabalha (12 min)

**Trocar** para a janela do `kit-pesquisa/`. Mostrar a árvore por dez segundos: "mesma lógica, três etapas, um artigo já colocado na entrada".

**Primeiro pedido** (colar):

```
Leia README.md, CONTEXT.md e AGENTS.md desta pasta e me explique, em português, o que ela faz e como começar. Não execute nada ainda.
```

**Dizer, enquanto responde (1 min):** "Este é sempre o primeiro pedido. Em casa, sem a gente, é assim que vocês começam. A pasta se explica."

Ler dois ou três trechos da resposta. Não ler tudo.

**Etapa 01** (colar):

```
Leia 01-fichamento/CONTEXT.md e execute a etapa para o artigo em 00-entrada/.
```

**Enquanto roda (2 a 4 min), falar:**
- "Ela está lendo o contrato da etapa, o meu tema em `_referencias/minha-pesquisa.md`, e o artigo. Só isso. Não está lendo o resto da pasta. É o contexto em camadas: 2 a 8 mil tokens, não 40 mil."
- Ler as permissões em voz alta de novo.
- "Vai demorar um pouco. Fichar um artigo com citação de página é trabalho. Se eu tivesse pedido 'resume aí', sairia em dez segundos e sem página."

**Quando terminar:**
1. Abrir `01-fichamento/saida/ficha-....md`. Mostrar a referência, os achados com página, as duas citações literais, a tabela de relação com o tema, e a seção "Verificar" no fim. "Ela me diz o que eu tenho que conferir. Eu vou conferir a citação da página 7 contra o PDF. Se estiver errada, eu corrijo na ficha e anoto no registro."
2. Abrir `registro/LOG-IA.md`: mostrar a entrada. "Data, etapa, ferramenta, o que fez, o que eu devo verificar."

**Etapa 03** (pular a 02 por tempo, dizer isso):

"Vou pular a etapa 02, que cruza várias fichas, porque só temos um artigo. Vou direto para a que interessa hoje."

```
Leia 03-relatorio-e-declaracao/CONTEXT.md e execute a etapa com o que existe no registro até agora.
```

**Enquanto roda (1 a 2 min):** "Ela vai ler o registro e escrever duas coisas: o relatório do que fez, e o rascunho da declaração."

**Quando terminar:** abrir `03-relatorio-e-declaracao/saida/declaracao-uso-ia.md`. Ler a linha "Fase: ... Ferramenta: ... Finalidade: ...". **Dizer:** "A declaração não saiu da minha cabeça. Saiu do rastro. Eu reviso, corto o que não se aplica, assino. E se a banca perguntar o que a IA fez, o registro está aqui."

**Fechar a Parte B:** "Vocês não estão mais conversando com a web. Estão conversando com uma pasta que vocês sabem o que tem. Se o resultado ficar ruim, não briguem com o resultado: abram o `CONTEXT.md` da etapa e melhorem a instrução. Aí ele acerta nos próximos cinquenta."

**Se der errado:**
- Lento demais → abrir a pasta `kit-pesquisa-ensaio/` e mostrar as saídas prontas: "isto saiu no ensaio de segunda". Dizer que a IA não é determinística e que por isso o registro importa.
- Não leu o PDF → "converta o PDF em .txt em 00-entrada e execute de novo" (mostra o que o README diz). Se ainda assim, pasta de ensaio.
- Erro de permissão → mostrar o diálogo, autorizar, comentar. Se insistir, pasta de ensaio.
- Tudo falhou (rede) → vídeo de reserva, 5 minutos, com narração ao vivo.

## Parte C: eles trabalham (5 min)

**Projetar** o slide com os dois caminhos:

- **Nível 1 (navegador):** abra sua IA; cole o prompt "processo com rastro" (QR da página); anexe ou cole seu artigo; leia a saída até a seção "declaração".
- **Nível 2 (computador):** abra o kit no VS Code; primeiro pedido; coloque seu artigo (ou baixe um dos exemplos, link na página) em `00-entrada/`; execute a etapa 01.

**Facilitadores circulam.** Regras:
- Quem travou no nível 2, garantir o nível 1. Não empurrar.
- Quem reclama do resultado: "abre o CONTEXT.md da etapa e muda a instrução".
- Quem pede "me dá logo a revisão": "é o sorvete".
- Anotar os casos interessantes para a retrospectiva.

Aos 5 minutos, o Elton chama a recapitulação. Quem estiver no meio continua em silêncio; o plantão pega o resto.

## Gatilhos e detalhes de interface que atrapalham (do Concefor)

- O arquivo aberto na aba vira contexto do chat no Copilot. Fechar abas antes de cada pedido.
- "Do you trust this folder?" aparece ao abrir a pasta. Autorizar.
- Shift+Enter para quebrar linha; Enter envia.
- No Copilot, o modo tem que ser "Agent", não "Ask", para escrever arquivos.
- O explorador some se a pessoa clica no ícone errado; mostrar o ícone de volta.
- No Claude Code, as permissões aparecem no terminal; no Copilot, como botões no chat. Dizer que muda de ferramenta para ferramenta, mas a pergunta é a mesma.
