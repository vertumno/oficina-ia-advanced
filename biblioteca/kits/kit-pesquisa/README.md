# Kit Pesquisa — assistente de revisão de literatura com rastro auditável

Esta pasta é um assistente de pesquisa. Não é um programa: é um conjunto de instruções em texto que uma IA lê quando você a abre aqui dentro. Você conversa com a pasta; a IA faz o trabalho; tudo fica registrado.

Ela faz três coisas, em ordem:

1. **Ficha artigos** que você coloca em `00-entrada/` (referência, objetivo, método, achados, citações literais com página, relação com seu tema).
2. **Correlaciona** as fichas com o seu tema de pesquisa (tabela, convergências, divergências, lacunas).
3. **Relata o que fez e escreve o rascunho da sua declaração de uso de IA**, nos termos da Portaria CNPq 2.664/2026 (ferramenta, finalidade, fase).

Feito pela CGTE/Cefor (Ifes) para a oficina "IA além do chat" (Secim, 17/09/2026), com base na metodologia ICM de Jake Van Clief e David McDermott (2026). Licença MIT: use, altere, compartilhe.

## O que você precisa

- Um computador com o **VS Code** instalado (https://code.visualstudio.com), ou outro editor que abra pastas.
- Um **agente de IA que trabalhe em pastas**. Opções, em 14/09/2026 (confirme preços e limites, mudam com frequência). Na dúvida, escolha pela conta que você já tem: conta Google, Antigravity; conta no GitHub, Copilot.

| Ferramenta | Como instalar | Custo |
|---|---|---|
| Google Antigravity | https://antigravity.google (editor com agente embutido; não precisa do VS Code) | Plano individual gratuito com conta Google, com limite de uso semanal |
| Gemini CLI (Google) | https://github.com/google-gemini/gemini-cli | Gratuito com conta Google pessoal (cerca de 1.000 pedidos por dia) |
| GitHub Copilot, modo agente no VS Code | Extensão "GitHub Copilot" no VS Code | Plano gratuito limitado; plano Student gratuito para estudantes verificados (GitHub Education) |
| Claude Code (Anthropic) | https://claude.com/claude-code | Precisa de plano pago (Pro ou superior) |
| Codex CLI (OpenAI) | https://github.com/openai/codex | Incluído em planos pagos do ChatGPT |

Qualquer uma funciona com esta pasta. As instruções para a IA estão em `AGENTS.md`; os arquivos `CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md` só apontam para ele, cada um no nome que a sua ferramenta procura.

## Como usar, em seis passos

1. **Descompacte** o kit em um lugar que você encontre depois (ex.: `Documentos/pesquisa-ia/kit-pesquisa`).
2. **Abra a pasta no VS Code:** Arquivo → Abrir Pasta → escolha `kit-pesquisa`.
3. **Abra o seu agente de IA dentro dessa pasta** (no terminal do VS Code, digite o comando da ferramenta, ex.: `gemini`, `claude`, `codex`; ou abra o chat do Copilot e escolha o modo agente). No Antigravity, abra a pasta direto nele e use o painel do agente.
4. **Primeiro pedido, sempre este:**
   ```
   Leia README.md, CONTEXT.md e AGENTS.md desta pasta e me explique, em português, o que ela faz e como começar. Não execute nada ainda.
   ```
   Leia a resposta. Se algo não bater com este README, é a IA que está errada; diga a ela.
5. **Preencha `_referencias/minha-pesquisa.md`** com seu tema e sua pergunta (pode pedir ajuda à IA, mas o conteúdo é seu). **Coloque dois ou três artigos** (PDF ou texto) em `00-entrada/`.
6. **Execute uma etapa por vez:**
   ```
   Leia 01-fichamento/CONTEXT.md e execute a etapa para os artigos em 00-entrada/.
   ```
   Abra os arquivos que ela criou em `01-fichamento/saida/`. Leia. Corrija o que precisar. Só então:
   ```
   Leia 02-correlacao/CONTEXT.md e execute a etapa.
   ```
   E depois a etapa 03. Ao final, você terá em `03-relatorio-e-declaracao/saida/` o relatório do processo e o rascunho da declaração.

## Três regras de segurança

1. **Leia o que a IA pede permissão para fazer.** Ela vai pedir para ler e escrever arquivos. Dentro desta pasta, tudo bem. Fora dela, ou para apagar algo, diga não e pergunte por quê.
2. **Não ative modos que dispensam permissão** ("bypass", "yolo", "auto-approve") enquanto não souber o que está fazendo. É rápido e é perigoso.
3. **Não coloque em `00-entrada/` dados de participantes de pesquisa, prontuários ou material sigiloso** sem saber para onde a sua ferramenta envia o conteúdo. Ferramentas na nuvem enviam para a empresa. Para dados sensíveis, procure modelos locais (Ollama) ou não use IA.

## Dicas de sobrevivência no VS Code (aprendidas em oficinas)

- **Shift+Enter** quebra linha no chat. **Enter envia** e, no Copilot gratuito, gasta um dos seus créditos do mês.
- Copilot gratuito dá cerca de 50 interações por mês. Uma mensagem completa vale mais que cinco curtas. O saldo aparece no ícone do Copilot, no canto inferior direito. Quando acabar: espere o mês virar, ou troque de ferramenta (Gemini CLI é gratuito).
- No Copilot, o chat precisa estar no modo **Agent** para criar e editar arquivos. No modo "Ask" ele só conversa.
- Ao abrir a pasta, o VS Code pergunta **"Do you trust this folder?"**. Sim, é a sua pasta.
- **O arquivo aberto na aba do editor vira contexto do chat.** Antes de cada pedido, feche o que não é da etapa; senão a IA mistura.
- Se o painel de arquivos sumiu, clique no primeiro ícone da barra da esquerda (o explorador).

## Quando algo der errado

- A IA inventou uma referência ou uma página: aponte, peça correção, e anote no `registro/LOG-IA.md` que isso aconteceu. Foi para isso que o registro existe.
- A IA escreveu fora de `saida/` ou alterou suas instruções: peça para desfazer e reforce a regra. Se insistir, reinicie a conversa.
- A IA não lê PDF: peça "converta os PDFs de 00-entrada em .txt dentro da mesma pasta" ou converta você antes.
- Ficou confuso: apague tudo dentro das pastas `saida/`, limpe o `LOG-IA.md` (mantenha o cabeçalho) e comece de novo. As instruções continuam intactas.

## Depois de usar

- Guarde a pasta inteira junto com a pesquisa. Ela é o caderno de laboratório do seu uso de IA.
- Quer outra pasta para outra tarefa (revisar ABNT, preparar submissão para um congresso)? Copie esta e mude as instruções. É assim que se cresce: duplicando, não recomeçando.
- Melhorou alguma instrução? Compartilhe com os colegas. Uma pasta boa se troca.

## Arquivos que começam com ponto

Se aparecer algum arquivo chamado `.gitkeep`, ignore. Ele só existe para que as pastas vazias sejam preservadas.
