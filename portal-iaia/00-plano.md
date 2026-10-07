# Plano: atualização do Portal IA.IÁ

Rascunho de 07/10/2026 para Marquito e Elton ajustarem; revisado no mesmo dia com a divisão de papéis entre o portal e a página "Ações de IA no Cefor" (seção 2). Nada aqui foi publicado. O que está marcado *a confirmar* não foi verificado; as decisões abertas estão na seção 7.

Portal: https://sites.google.com/view/iaia-educa (Google Sites, CGTE/Cefor/Ifes).
Catálogo: https://cefor.ifes.edu.br/index.php/component/content/article/2-uncategorised/17587-acoes-de-inteligencia-artificial-no-cefor (site do Cefor, oito subpáginas, atualizada em 26/08/2026).

## 1. Objetivo

Fazer o portal mostrar o que a CGTE já faz em IA, não só o que fez em 2024. Em concreto:

1. Publicar as oficinas de 2026 (Secim, VIII Concefor, NTEs), começando pelo Secim, que tem prazo.
2. Transformar "Professor + IA: Oficinas", hoje vazia, em um índice com linha do tempo.
3. Mandar quem procura ferramentas e serviços para "Ações de IA no Cefor", que já é o catálogo, e dar ao portal conteúdo prático sobre ética e declaração de uso de IA.
4. Corrigir o que está quebrado, desatualizado ou copiado por engano.
5. Combinar uma rotina para que cada oficina nova entre no portal sem depender de lembrança.

**Fora do escopo:** trocar de plataforma, redesenhar a identidade visual, produzir conteúdo novo que não venha de uma oficina ou de um recurso que já existe.

## 2. Princípios e divisão entre os dois sites

**"Ações de IA no Cefor" é o catálogo; o Portal IA.IÁ é a prática.** A página do Cefor diz o que existe e distribui para os serviços (GPTs, Papo, podcasts e palestras, Base de Conhecimento, Manual, redes sociais, portal). O portal mostra como se faz: oficinas com roteiro, experimentos, prompts, kits, e o Papo. O portal não repete o catálogo; aponta para ele.

```
Site do Cefor: Ações de IA no Cefor  (o que existe)
  ├─ GPTs ──────────────────────► Base de Conhecimento (um artigo por GPT, com o link)
  ├─ Papo com IA.IÁ ────────────► Portal: Papo
  ├─ Podcast, palestras, oficinas ► YouTube e Spotify   (proposta: também Portal: Oficinas)
  ├─ Base de Conhecimento
  ├─ Manual de Uso Ético ───────► Drive (bit.ly/manual-etica-IA)
  ├─ Ações nas redes sociais ───► Instagram
  └─ Portal IA.IA ──────────────► Portal: Início       (proposta: texto que diga o que o portal tem)

Portal IA.IÁ  (como se faz)
  ├─ Início · Papo · Oficinas e formações · Ética e declaração · Links & Refs
  └─ Ferramentas ↗ ─────────────► Ações de IA no Cefor (volta ao catálogo)
```

**Quem é dono de cada informação:**

| Informação | Dono | Os outros |
|---|---|---|
| Lista de GPTs, o que cada um faz, link de cada um | Ações (subpágina GPTs) → artigo da Base de Conhecimento | O portal aponta. Em listas, linka o artigo da Base; só dentro do passo a passo de um experimento linka o GPT direto |
| Manual de Uso Ético | Ações (subpágina Manual) → Drive | O portal linka o Manual; não resume nem copia |
| Gravações de podcasts, palestras e lives | Playlists do YouTube e Spotify (Ações, subpágina Podcast) | A página de cada oficina incorpora a própria gravação, se houver |
| Papo com IA.IÁ (horário, Meet, anotações) | Portal | Ações já aponta para o portal |
| Oficinas (o que foi, material, prática, lições) | Portal | Ações deveria apontar (hoje a subpágina Podcast, Palestras e Oficinas só leva ao YouTube) |
| Grupo de WhatsApp | Os dois, com o mesmo link | |

**Outros princípios:**

- **O repositório é a fonte; o portal é a vitrine.** O texto de cada página nasce em `portal-iaia/paginas/` e é colado no Sites. Se mudar no Sites, muda aqui também.
- **Uma página por oficina, sempre com o mesmo molde** (seção 4).
- **Repositório público:** pessoas de fora da CGTE aparecem pelo papel, não pelo nome (ver `CONTEXT.md` da raiz).
- **Links conferidos e datados:** cada lista de links termina com "revisado em DD/MM/AAAA".

## 3. Diagnóstico (navegação de 07/10/2026)

| Página | Situação | O que fazer |
|---|---|---|
| Página inicial | WhatsApp (botão repetido duas vezes), chamada para o Papo, cartões das oficinas de 2024, live sobre ética | Reorganizar em "três portas" (seção 5) e trocar os cartões pelos destaques de 2026 |
| Papo com IA.IÁ | Funciona: horário, Meet, documento de anotações com uma aba por encontro | Acrescentar desde quando existe, o artigo do ESUD 2025 e os próximos temas |
| Professor + IA: Oficinas | **Vazia** (só título e rodapé) | Virar o índice "Oficinas e formações" |
| Workday Online (10/09/2024) | Conteúdo descrito, sem link da gravação | Pôr a gravação, se existir (*a confirmar*), e aplicar o molde |
| Oficina Ifes + Moodle (VII Concefor, 2024) | Completa | Corrigir "Oficina IFEs"; avisar que a sala 9403 exige login |
| Oficina Escolas (2024) | Rica, mas no fim traz um bloco copiado da página do Moodle (VII Concefor, sala 9403, justificativa) e o formulário de certificado de 2024 ainda aberto | Tirar o bloco copiado; decidir sobre o certificado e sobre o laudo de exemplo (seção 7) |
| Makey Makey | Três jogos em `claude.site`, sem dizer quando, onde nem para quem | Contextualizar ou mudar de lugar (seção 7) |
| Links & Refs | Lista de 2024, sem data de revisão; links com problema (seção 8); a seção "GPTs específicos" repete o catálogo do Cefor e tem só três dos cinco GPTs | Revisar, cortar, datar; trocar os GPTs por um link para o catálogo |

Não vimos: o visual do site (só o texto) e o documento incorporado na página do Papo.

## 4. Molde de página de oficina

Inspirado nos quatro blocos da sala Moodle dos NTEs (`referencias/sala-moodle-ntes-blocos-html.md`).

1. **Cabeçalho:** título, data, local, público, facilitadores, carga horária.
2. **Em uma frase:** o que a oficina propôs.
3. **O que fizemos:** de três a cinco itens.
4. **Material para levar:** botões com link (slides, kit, prompts, sala, repositório).
5. **O que aprendemos:** duas ou três lições (sem dados pessoais, sem nomes de participantes).
6. **Próximo passo:** Papo com IA.IÁ, curso de extensão de 2027, contato.

## 5. Nova estrutura proposta

```
Início                     três portas: Quero começar · Quero conversar · Quero me aprofundar
Papo com IA.IÁ             como está, mais história, artigo e próximos temas
Oficinas e formações       índice em linha do tempo
  ├─ IA além do chat (2026)
  │    ├─ Secim (17/09/2026)
  │    ├─ VIII Concefor (20/08/2026)
  │    └─ NTEs (2026, data a confirmar)
  └─ Criar com o chat (2023–2025)
       ├─ Workday Online (10/09/2024)
       ├─ Oficina Ifes + Moodle (VII Concefor, 2024)
       ├─ Oficina Escolas (2024)
       ├─ Makey Makey (data a confirmar)
       └─ outras do histórico (seção 6, Fase 4)
Ética e declaração         prática: como declarar (Portaria CNPq, modelo de declaração, Protocolo, live);
                           o Manual é linkado, não reproduzido
Links & Refs               curada, com "revisado em"; sem a lista de GPTs
Ferramentas ↗              item de menu que leva direto a "Ações de IA no Cefor" (sem página no portal)
```

Por que trocar "Professor + IA" por "Oficinas e formações": o Secim foi para mestrandos e doutorandos, não para professores.

Por que "Ferramentas" é só um link: o catálogo de GPTs e serviços já vive no site do Cefor (seção 2). Uma página de ferramentas no portal duplicaria a lista e envelheceria antes da outra.

## 6. Inventário: o que entra e de onde vem

### Oficinas de 2026 (material neste repositório)

| Página | Fonte aqui | Material para linkar | Falta |
|---|---|---|---|
| Secim, 17/09/2026 | `oficinas/2026-09-17-secim/referencias-secim.html` e `.md` (prontas, com um item "a definir") | Drive do kit, prompts, modelo de declaração, Manual, Protocolo | Fechar o item "a definir" (curso de extensão); números do dia, se houver (`06-pos-oficina.md` está em branco) |
| VIII Concefor, 20/08/2026 | `referencias/oficina-concefor-2026-08-20.md`; repositório `oficina-concefor-icm` | Repositório público dos participantes: https://github.com/marcosaccioly/oficina-concefor-icm-participantes | Confirmar se algum slide ou folha pode ser publicado |
| NTEs, 2026 | `referencias/sala-moodle-ntes-blocos-html.md`; `biblioteca/paginas/modelo-blocos-moodle-ntes.html` | Sala Moodle (exige login?) | Data, local, público, quantos NTEs (*a confirmar*) |

### Histórico de 2023 a 2025 (cards do board da CGTE, levantados no `cerebro-cgte`; tudo *a confirmar*)

| Formação | Ano | Card |
|---|---|---|
| Workday "ChatGPT: 10 dicas para uso em sala de aula (e 5 desafios)" | 2023 | #7139, #7143 |
| Workday "Inteligência Artificial no Ifes" | 2023 | #7279 |
| Workshop "Canva avançado com IA" | 2024–25 | #7479, #7594 |
| Palestra "5 Anos em 1" (11/12, YouTube do Cefor) | 2024 | #7543 |
| Tutorial de ChatGPT em Libras | 2024 | #7397 |
| Oficina de IA no Trilha Cefor | 2025 | #7656, relatório em #7678 |
| "IA para Salas Virtuais: do Zero à Sala Pronta no Moodle", Jornada de Colatina | 2025 | #7670 |
| Formação com o GPT Gerador de Questionário, UAB | 2025 | #7706 |

### Conteúdo que ainda não está no portal

| Recurso | Link | Vai para |
|---|---|---|
| Protocolo de Atenção para Criação de Conteúdos Educacionais com IA (Rutinelli Fávero) | https://rpfweb.github.io/Protocolo-para-Uso-de-IA/ | Ética e declaração |
| Portaria CNPq 2.664/2026 e modelo de declaração de uso de IA | ver `referencias/normas-uso-ia-pesquisa-brasil.md` e `biblioteca/prompts/modelo-declaracao-uso-ia.md` | Ética e declaração |
| Artigo do ESUD 2025 sobre o Papo | https://submissoes.netel.ufabc.edu.br/index.php/esud2025/article/view/193 | Papo com IA.IÁ |
| Kit Pesquisa | pasta do Drive do Secim | Página do Secim |
| Curso de extensão "Inteligência de Contexto Pedagógica com IA" (2027) | informação *a definir* | Rodapé das páginas de oficina |

### O que já está no catálogo do Cefor (o portal só aponta)

| Recurso | Onde está | Como o portal usa |
|---|---|---|
| Cinco GPTs (DeIA, Gerador de Questionários, H5P Summary, Video Summarizer, Gerador de Rubricas) | Ações, subpágina GPTs (`?start=1`), cada um com artigo na Base de Conhecimento | Menu "Ferramentas ↗"; nas páginas de oficina, link do artigo da Base de cada GPT usado |
| Manual Prático de Uso Ético (atualizado em 26/08/2026) | Ações, subpágina Manual (`?start=5`) | Link na página Ética e declaração |
| Playlists de vídeos e de podcasts (YouTube e Spotify) | Ações, subpágina Podcast, Palestras e Oficinas (`?start=3`) | Página de cada oficina incorpora a própria gravação; Início pode trazer um destaque |
| Percurso "Inteligência Artificial" da Base de Conhecimento | Ações, subpágina Base (`?start=4`) | Link nas páginas de oficina quando um tutorial for usado na prática |
| Posts do Instagram | Ações, subpágina Redes Sociais (`?start=6`) | Não entram no portal |

## 7. Decisões abertas

| # | Decisão | Opções | Proposta | Quem |
|---|---|---|---|---|
| D1 | Nome do menu de oficinas | "Professor + IA: Oficinas" · "Oficinas e formações" · outro | "Oficinas e formações" | Ambos |
| D2 | Como publicar a página do Secim | Incorporar o HTML pronto ("Incorporar > Código", com rolagem própria) · refazer em blocos nativos do Sites | Blocos nativos (fica com cara de portal e funciona bem no celular); o HTML continua valendo para o Moodle | Elton |
| D3 | Quanto do histórico de 2023 a 2025 entra | Tudo, com página própria · só uma linha no índice · nada | Uma linha no índice por formação; página só para quem tiver material | Elton (tem o board) |
| D4 | Makey Makey | Fica em Oficinas, com contexto · vai para uma seção "Experimentos" | Fica, se houve oficina; senão vai para "Experimentos" | Ambos |
| D5 | Laudo de exemplo da Oficina Escolas | Manter como está · dizer "caso fictício" · trocar o nome | Dizer "caso fictício" na página (se for) | Elton |
| D6 | Formulário de certificado de 2024 | Fechar · manter | Fechar | Elton |
| D7 | Ferramentas comerciais em Links & Refs (Teachy, Mettzer, Eureca etc.) | Manter · cortar · separar como "ferramentas de mercado" | Separar, com data de revisão | Ambos |
| D8 | Nome da coordenadoria no rodapé | "Coordenadoria de Tecnologias Educacionais" (portal) · "Coordenadoria Geral de Tecnologias Educacionais" (site do Cefor, subpágina do Papo; artigo do ecossistema) | Alinhar com o site do Cefor | Elton |
| D9 | Quem mantém o portal depois | Elton · rodízio · CGTE | Elton publica; o texto nasce aqui | Ambos |
| D10 | Para onde e com que rótulo vai o menu "Ferramentas ↗" | Raiz de Ações (índice completo) · subpágina GPTs (`?start=1`) | Raiz de Ações, com o rótulo "Ferramentas e serviços ↗" para quem clica saber que vai sair do portal | Ambos |
| D11 | Fechar o caminho de volta no site do Cefor | Pedir dois ajustes em Ações: a subpágina "Podcast, Palestras e Oficinas" passa a apontar também para "Oficinas e formações" do portal; a subpágina "Portal IA.IA" troca o texto genérico por um que diga o que o portal tem (oficinas com prática, Papo, materiais) · deixar como está | Pedir os dois ajustes; quem edita o site do Cefor *a confirmar* | Elton |

## 8. Correções rápidas (independem das decisões)

- [ ] Início: tirar o botão de WhatsApp repetido; corrigir "Ética e Ia".
- [ ] Início: corrigir "Conheças as Oficinas em Escolas".
- [ ] Ifes + Moodle: corrigir "Oficina IFEs: IA + moodle".
- [ ] Ifes + Moodle e Escolas: avisar que a sala de teste (`ava3…id=9403`) pede login, ou abrir para visitante.
- [ ] Escolas: remover o bloco "Informações sobre a Oficina" copiado da página do VII Concefor.
- [ ] Links & Refs: o Classcraft não respondeu no teste de 07/10 (o serviço pode ter sido encerrado; *a confirmar*); remover ou substituir.
- [ ] Links & Refs: a Mesinha Digital ADA mudou de `quinyx.com.br` para `quinyxcompany.com`.
- [ ] Links & Refs: três itens (MelhorIA, Laboratórios Interdisciplinares, Olimpíada de IA) apontam para o mesmo artigo do Porvir; dar o link próprio de cada um ou juntar em um item.
- [ ] Links & Refs e Escolas: trocar `chat.openai.com` por `chatgpt.com`.
- [ ] Links & Refs: o Groq é infraestrutura de inferência, não um chat para professores; avaliar se sai.
- [ ] Links & Refs: trocar a seção "GPTs específicos" por um link para Ações de IA no Cefor, subpágina GPTs.
- [ ] Video Summarizer: o endereço agora redireciona para `…-noyoutube-video-summarizer-noyoutube-unaffiliated`. Conferir se ainda é o GPT da CGTE e se funciona; se mudou, corrigir no artigo da Base de Conhecimento (dono do link) e nos experimentos das oficinas de 2024.
- [ ] Links & Refs: acrescentar "revisado em DD/MM/AAAA".

## 9. Fases e prazos

Hoje é quarta, 07/10. O formulário de 30 dias do Secim sai em 17/10 e aponta para a página de referências; por isso o Secim vem primeiro.

| Fase | O que | Quem | Até |
|---|---|---|---|
| 0 | Ajustar este plano; fechar D1, D2, D9 e D10 | Marquito e Elton | sex 09/10 |
| 1 | **Secim:** texto da página no molde (`paginas/oficina-secim-2026.md`), publicar no Sites e pôr o link no formulário de 30 dias e no e-mail de pós-oficina | Claude redige; Marquito revisa; Elton publica | qua 14/10 |
| 1 | Correções rápidas (seção 8) | Elton | qua 14/10 |
| 1 | Anunciar a página no Papo | Elton | qui 15/10 |
| 2 | Índice "Oficinas e formações", página do VIII Concefor, página dos NTEs | Claude redige; Elton completa os dados dos NTEs e publica | sex 23/10 |
| 3 | Menu "Ferramentas ↗" apontando para o catálogo; "Ética e declaração" (prática); Links & Refs revisada; Início em três portas; Papo com história e artigo | Claude redige; Elton publica | sex 30/10 |
| 3 | Ajustes no catálogo do Cefor (D11): texto da subpágina "Portal IA.IA" e link para "Oficinas e formações" | Claude redige; quem edita o site do Cefor publica | sex 30/10 |
| 4 | Histórico de 2023 a 2025 (conforme D3) | Elton levanta no board; Claude redige | a combinar |
| 5 | Rotina: incluir "publicar a página no Portal IA.IÁ" no `06-pos-oficina.md` de toda oficina; revisar Links & Refs a cada trimestre | Ambos | depois da Fase 3 |

## 10. Como o conteúdo vai ser entregue

- Um arquivo por página em `portal-iaia/paginas/`, com nome `secao-assunto.md` (exemplo: `oficina-secim-2026.md`).
- Cada arquivo segue a ordem dos blocos do Sites: título, texto, botão (rótulo e URL), imagem (descrição), para o Elton colar sem precisar interpretar.
- No topo de cada arquivo: endereço da página no Sites, estado (rascunho, revisado, publicado) e data.
- Depois de publicar, o Elton marca "publicado em DD/MM" no arquivo.

## 11. Riscos

- **O portal volta a parar no tempo.** Sem a rotina da Fase 5, a próxima oficina também fica de fora. Mitigação: o passo entra no checklist de pós-oficina.
- **O histórico de 2023 a 2025 consome a energia das fases 1 a 3.** Mitigação: a Fase 4 vem por último, e uma linha no índice basta.
- **Duas versões do mesmo texto (repositório e Sites) divergem.** Mitigação: editar primeiro aqui, depois no Sites, e registrar a data.
- **Links de Drive e de GPTs mudam de permissão ou de endereço.** Mitigação: "revisado em" e revisão trimestral; o link de cada GPT tem um dono só (o artigo da Base de Conhecimento).
- **Catálogo e portal voltam a se repetir.** Mitigação: a tabela de donos da seção 2. Antes de pôr uma lista no portal, ver se ela já existe em Ações.
