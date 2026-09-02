# Oficina "IA além do chat" (VIII Concefor, 20/08/2026) — o que aprendemos na prática

**Fonte:** repositório `C:\dev\oficina-concefor-icm`, pasta `oficina/`. Ler nesta ordem: `oficina/v2/aprendizados.md` (decisões), `oficina/v2/plano-v2.md` (roteiro atual), `oficina/retrospectiva-2026-08-20.md` (análise bloco a bloco), `oficina/fontes/2026-08-20/` (transcrição da manhã e avaliação). Repositório dos participantes: https://github.com/marcosaccioly/oficina-concefor-icm-participantes
**Consultado em:** 02/09/2026.

## Em uma frase

A única oficina de "IA no computador com pastas" que já demos: dois turnos, cerca de 40 professores de sete campi, NPS 90, e uma lista precisa do que faltou (ambientação, créditos, metáfora, erro nº 1) e do que não vimos (artefatos não coletados, avaliação no pico do entusiasmo, continuidade não absorvida).

## O que foi

- VIII Concefor, 20/08/2026, manhã (3h) e tarde (2h30), laboratório com 20 máquinas por turno.
- Público: professores e servidores do Ifes (Cefor, Santa Teresa, São Mateus, Guarapari, Vila Velha, Cariacica, Serra).
- Ferramenta: VS Code + GitHub Copilot na cota gratuita, login com conta do GitHub (é o GitHub que libera os créditos; login com Google não serve).
- Método: workspace-builder do ICM adaptado para pt-BR e para o contexto da oficina; dinâmica começa no papel (folha de mapeamento em duplas), depois `setup`, discovery, mapping, scaffolding.
- Resultado: média 9,7 em 20 respostas, 19 promotores, 1 detrator (nota 6, "requer conhecimento prévio"). Tarde (2h30) foi melhor avaliada que a manhã (3h).

## Os aprendizados que valem para qualquer oficina nossa

1. **Faltou um bloco inteiro: a ambientação.** Criar conta no GitHub, conectar no VS Code, baixar o zip, descompactar, abrir a pasta, ler o README, digitar `setup`. Sete passos, nenhum previsto. "Tinha que ter uma pré-oficina." Na v2, o Bloco 0 sai da preparação prévia (e-mail com 3 dias de antecedência, máquinas prontas), não do relógio da sala.
2. **Os créditos são o limite real do desenho.** Copilot gratuito: cerca de 50 interações por mês. O percurso inteiro precisa caber em ~30 mensagens. Ensinar Shift+Enter (Enter envia e queima crédito), onde ver o saldo, e o que fazer quando acabar. Entregar isso em papel, porque o crédito acaba em casa, sem nós do lado.
3. **A metáfora que funcionou foi a máquina de sorvete.** "A gente está montando a máquina de sorvete; no meio, alguém diz 'faz logo o sorvete'. Sai um sorvete errado. Aí a pessoa fica melhorando o sorvete. Não: você volta e melhora a máquina." A metáfora biológica planejada (célula-tronco) não foi usada nenhuma vez.
4. **O erro nº 1 é pular para o produto final.** "Faz logo a atividade." Mais provável em quem tem mais traquejo técnico. O aviso e a metáfora precisam vir **antes** da primeira interação com a IA.
5. **A regra de facilitação:** quando alguém reclamar do resultado, não corrija o resultado; mande voltar e corrigir a instrução. "Se você acertar esse HTML, nos próximos 15 você acerta todos."
6. **O que funcionou e deve ser preservado:** explicar o README como "o arquivo que a IA lê primeiro", com a provocação "como seria se toda pasta do seu computador tivesse um leia-me?"; recapitulações periódicas (planejadas, não como socorro); rodízio de teclado nas duplas; gestão explícita de expectativa ("não pensem que vão sair daqui fazendo tudo sozinhos"). Uma pessoa deu nota 10 dizendo que não conseguiu produzir nada.
7. **Detalhes de interface que consomem tempo:** as três colunas do VS Code; o botão do explorer; Open Preview para ler Markdown; o diálogo "trust this folder"; **o arquivo aberto na aba vira contexto involuntário do chat**.
8. **Defeitos do workspace-builder:** cria o workspace em lugar imprevisível; falta o passo de abrir o workspace novo em janela própria. Confirmam a decisão de, no Secim, não usar o builder ao vivo.

## Os pontos cegos (o que os dados mostraram e ninguém tinha visto)

- **Ninguém guardou os workspaces criados.** Entre 20 e 40 artefatos, nenhum coletado. Perdeu-se o acervo, a prova de valor e a base de comparação. Custo de evitar: uma pasta compartilhada e uma frase no encerramento.
- **A avaliação foi colhida no pico do entusiasmo.** NPS 90 responde "a oficina foi boa?", não "a oficina funcionou?". Isso só se responde em 30 dias, com outra pergunta (você voltou a abrir? produziu algo? o que travou?).
- **"Acabou cedo" não é pedido de oficina mais longa.** A tarde teve 30 min a menos e foi melhor avaliada. É pedido de **próxima** oficina (módulo 2, MOOC).
- **O certificado é o único e-mail que 100% abrem.** Mandar o material junto dele.
- **A habilidade foi ensinada em dupla; em casa a pessoa está sozinha.** A resposta está no método: em casa, quem entrevista é a IA. Dizer isso em voz alta.
- **Ninguém citou o Papo com IA.IÁ.** Público multicampi, quinta às 15h. Confirmar que é online (é: Google Meet) e dizer com todas as letras.
- **As folhas de mapeamento foram jogadas fora.** Recolher: são o registro de como a pessoa descreve o próprio trabalho antes da IA.
- **Ruído no repositório causou dano.** Workspaces de exemplo que não seriam usados confundiram quem procurava a própria pasta.
- **Um participante abriu uma porta institucional:** "o Ifes não usa essas ferramentas para processos administrativos". Gancho para levar o método para dentro da instituição.

## Casos reais colhidos (matéria-prima para aberturas)

- Dupla de pesquisadores: preparar artigo, escolher revista, aplicar normas e **responder parecer de banca sem sair do padrão**. É o caso mais próximo do público do Secim.
- Equipe do planetário: conteúdo de ensino médio em história para crianças.
- Slides acessíveis por desenho universal.
- Elaboração de atividades de disciplina.
- Ideia levantada na sala: um workspace para criar MOOC.

## Critérios de sucesso em níveis (adotar sempre)

| Nível | Concefor v2 |
|---|---|
| Mínimo (todos) | Dor mapeada no papel, entrevista com a IA respondida, discovery iniciado |
| Bom | Workspace gerado e aberto em janela própria |
| Ótimo | Rodou a máquina uma vez, viu o resultado ruim e melhorou a máquina |

Regra: quem estiver travado, garanta o mínimo dele em vez de empurrar para o seguinte.

## Convenções de organização que valem para esta pasta

- Edição realizada congela (v1); mudanças vivem em `v2/`.
- Material bruto em `fontes/AAAA-MM-DD/` com `leia-me.md` de proveniência e limitações; não se edita fonte bruta.
- "Dono único da informação": o roteiro vive no plano, a análise na retrospectiva, as decisões nos aprendizados; os outros apontam, não duplicam.

## O que aproveitamos no Secim

Quase tudo, adaptado a 90 minutos sem laboratório. Detalhe em `oficinas/2026-09-17-secim/02-analise-e-melhorias.md`. Em resumo: Bloco 0 fora do relógio (e-mail prévio e clínica de instalação no credenciamento); VS Code + Copilot com conta do GitHub como caminho gratuito já testado; conceitual antes da primeira interação; máquina de sorvete e erro nº 1; README como "arquivo que a IA lê primeiro"; níveis de sucesso; coleta de artefatos e da folha; QR duplo; material junto do certificado; formulário de 30 dias; "acabou cedo" respondido com a próxima oficina, não com mais minutos.

## A confirmar

- Se as ações de janela curta da v2 (e-mail único até 27/08, pasta compartilhada, formulário de 30 dias até 20/09) foram feitas. Se não, o Secim pode reaproveitar o mesmo formulário.
- Se os dois defeitos do workspace-builder foram corrigidos (irrelevante para o Secim, relevante para o curso de extensão).
- Se a oficina dada aos NTEs (sala Moodle em `fontes/2026-08-sala-moodle-ia-ntes-blocos.html`) é a mesma do Concefor ou uma edição à parte.
