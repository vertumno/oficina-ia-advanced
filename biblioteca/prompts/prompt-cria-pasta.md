# Prompt que cria a pasta

Prompt único para a IA, no computador, criar uma estrutura mínima de pasta-agente e explicar o que criou. É o momento "abriu um portal" da oficina: a pessoa vê a IA criando pastas e arquivos no computador dela, abre um arquivo e lê a instrução.

Diferente do workspace-builder do ICM, que faz perguntas e monta uma estrutura completa, este prompt é fechado: cria sempre a mesma estrutura pequena. A intenção é que a pessoa entenda que *ela* pode criar isso, com ou sem IA, e depois baixe o kit completo.

## Antes de colar

1. Crie uma pasta vazia no computador (por exemplo `minha-pesquisa-ia`).
2. Abra essa pasta no VS Code (Arquivo → Abrir Pasta).
3. Abra o seu agente de IA nessa pasta (Claude Code, Codex, Gemini CLI, Copilot em modo agente, ou outro).
4. Cole o prompt abaixo.

## O prompt

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

## O que deve acontecer

1. A IA cria as pastas e os arquivos (pode pedir permissão para escrever; conceda).
2. Mostra a árvore e explica cada arquivo.
3. Você abre `01-fichamento/CONTEXT.md` no VS Code e lê em voz alta: "a instrução está aqui, em texto, e você pode mudar".
4. Você abre `registro/LOG-IA.md` e mostra o formato vazio: "tudo que a IA fizer vai ficar registrado aqui".

Depois disso, o próximo passo natural é colocar um artigo em `00-entrada/` e dizer: "Leia o CONTEXT.md de 01-fichamento e execute a etapa para o artigo que está em 00-entrada."

## Se der errado

- A IA criou coisas a mais (scripts, `.gitignore`, pastas extras): peça "remova o que não estava na lista". Serve de exemplo de por que as instruções precisam ser fechadas.
- A IA não consegue escrever arquivos: verifique se a ferramenta está aberta na pasta certa e se você concedeu permissão.
- A IA escreveu em inglês: "reescreva todos os arquivos em português".

## Histórico

- 02/09/2026: escrito a partir da conversa Marquito e Elton (trechos 00:19 a 00:20, 00:33 a 00:34 e 00:53). Ainda não testado. Testar com Claude Code e com Gemini CLI antes de 10/09 e anotar o resultado aqui.
