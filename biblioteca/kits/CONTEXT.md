# CONTEXT.md — kits

## O que há aqui

Pastas completas que o participante baixa, descompacta e abre com a IA dele no computador. Cada kit é um exemplo funcional de "pasta como agente".

| Kit | Para quem | O que faz |
|---|---|---|
| `kit-pesquisa/` | Pós-graduandos e pesquisadores | Assistente de revisão de literatura com rastro auditável: ficha artigos, correlaciona com o tema, gera relatório do processo e rascunho de declaração de uso de IA |

## Princípios de desenho de um kit

1. **Pequeno.** Três etapas é o máximo para uma primeira experiência. Quem quiser mais, duplica e amplia.
2. **Independente de ferramenta.** Tem `AGENTS.md` (lido por Codex, Gemini CLI, Copilot, Cursor e outros) e `CLAUDE.md` (lido pelo Claude Code) com o mesmo conteúdo essencial.
3. **Legível antes de rodar.** O primeiro ato do participante é ler o `README.md`; o segundo é pedir à IA que explique a pasta. Só depois executa.
4. **Rastro por padrão.** Toda ação da IA vai para `registro/LOG-IA.md` com ferramenta, finalidade e etapa, os três dados que a Portaria CNPq 2.664/2026 pede.
5. **Só escreve em `saida/`.** As instruções e referências são da pessoa; a IA não as altera sem pedir.
6. **Em português.** Tudo, inclusive os nomes de arquivo.
7. **Ancorar, não inventar.** Regra número 1 das instruções para a IA.

## Como empacotar para distribuição

```
cd biblioteca/kits
zip -r kit-pesquisa.zip kit-pesquisa -x "*/saida/.gitkeep" "*/.gitkeep"
```

Testar o zip em uma máquina limpa antes de distribuir. Guardar o zip fora do repositório (Drive ou Base de Conhecimento do Cefor) e anotar o link em `oficinas/<evento>/06-pos-oficina.md`.

## Regras para agentes

- Ao alterar um kit, manter a compatibilidade com o `README.md` dele (os passos descritos precisam continuar funcionando).
- Não acrescentar dependências (scripts, bibliotecas, ferramentas externas) sem registrar no `README.md` do kit.
- Não colocar exemplos de artigos com direitos autorais dentro do kit; indicar fontes de acesso aberto.
