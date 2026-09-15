---
paths:
  - oficinas/2026-09-17-secim/referencias-secim.html
---

# Sincronizar com o Artifact publicado

Toda alteração em `oficinas/2026-09-17-secim/referencias-secim.html` deve ser
republicada no Claude Artifact assim que a edição for concluída na mesma
sessão — não deixe a página só salva localmente.

**Artifact:** https://claude.ai/artifact/LXwpGNo9FbotQ4Pp8CkaWN

**Como republicar:**
1. Edite o arquivo normalmente.
2. Publique com a ferramenta Artifact usando `file_path` apontando para este
   HTML e `url` igual ao link acima, para atualizar a mesma página em vez de
   criar uma nova.
3. Inclua de novo, em `files`, os assets referenciados pelo HTML que não
   estão embutidos como `data:` URI:
   - `slides-visual/src/fonts/archivo-normal.woff2`
   - `slides-visual/src/fonts/archivo-italic.woff2`
   - `slides-visual/src/fonts/jetbrains-normal.woff2`
   - `biblioteca/fotos/silva-elton.png` (publicado como `biblioteca/fotos/silva-elton.png`)
   - `biblioteca/fotos/accioly-marcos.jpg` (publicado como `biblioteca/fotos/accioly-marcos.jpg`)

   Republicar sem `url` cria um artifact novo e separado — sempre passe o
   `url` acima para atualizar o mesmo link.

**Por quê:** o link do artifact é o que é compartilhado com os participantes
e colaboradores (inclusive quem não tem acesso de escrita a este
repositório); ele só reflete o conteúdo atual se for republicado a cada
edição do arquivo-fonte.
