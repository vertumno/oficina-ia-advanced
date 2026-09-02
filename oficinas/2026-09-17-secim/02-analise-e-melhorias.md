# Análise da conversa de 02/09 e melhorias propostas

O que Marquito e Elton decidiram, o que deixaram aberto, o que os dados de outras fontes (Concefor, ICM, normas, Hugo, Meira) acrescentam, e o que propomos mudar. O plano resultante está em `01-plano-da-oficina.md`; este arquivo explica o porquê.

Fontes: `fontes/2026-09-02-transcricao-conversa-marquito-elton-secim.md`; `referencias/` (todas as fichas); `C:\dev\oficina-concefor-icm\oficina\v2\aprendizados.md`.

## 1. Resumo executivo

1. **Os dois eixos que a conversa identificou (ética e método) são um eixo só.** Declarar bem exige saber o que a IA fez; saber exige processo visível; processo visível exige organização; organização, no computador, é pastas e arquivos. A oficina inteira é essa frase, dita de quatro jeitos.
2. **O gargalo não é a ferramenta, é a abstração "pastas e arquivos".** O Concefor confirmou; a oficina precisa fazer a pessoa **abrir e ler** um arquivo de instruções antes de ver qualquer mágica.
3. **É uma palestra com demonstração e material, não uma oficina de construção.** Marquito tinha razão. A métrica é formar multiplicadores e garantir que ninguém saia sem entregável, em três níveis.
4. **O Bloco 0 tem que sair do relógio.** Mensagem prévia com instruções e uma clínica de instalação durante o credenciamento (15h às 16h), na própria sala.
5. **O que o Concefor não viu, o Secim já faz desde o desenho:** coleta de artefatos na sala, QR de continuidade ao lado do de avaliação, material junto do certificado, formulário de 30 dias, e a resposta ao "quero mais" é a próxima oficina, não mais minutos.

## 2. O que a conversa decidiu e o que deixou aberto

| Tema | O que foi dito | Estado no plano |
|---|---|---|
| Não levar a oficina do Concefor como está | "Avançado para uma galera que não está usando nem o uso normal bem feito" | Acatado. Nada de workspace-builder ao vivo. |
| Abrir com ética e provocação | Manual de ética, Silvio Meira, "todo mundo está usando, declarar é o caminho" | Acatado. Blocos 1 e 2. |
| Prompt ruim versus prompt bom | "Não só mostrar o bom; mostrar os dois"; usar o acrônimo do Hugo | Acatado. Bloco 3, com P.A.R.T.E. e as duas conversas prontas. |
| Janela de contexto | "Precisamos dizer; não dá para demonstrar" | Acatado. Visual e números do ICM. |
| Ir ao computador com um prompt único que cria pastas | "Para a pessoa entender que ela pode criar"; Elton: "não sei qual é mais complicado, o prompt ou o zip" | Acatado como Parte A da demonstração. O zip (kit) vem na Parte B. Os dois, porque cumprem funções diferentes: o prompt mostra que se pode criar; o kit mostra uma pasta boa. |
| Mostrar uma pasta pronta e disponibilizar | "Resgatar a pasta 08-ciência do cérebro da CGTE e simplificar" | Acatado. O kit é a simplificação; comparar com a 08-ciência antes do dia (pendência). |
| Entregável | Elton: "oficina tem que ter entregável"; Marquito: "a barreira de instalar é alta" | Resolvido com três níveis. Ninguém sai sem. |
| Riscos de dar acesso ao computador | "Não é bypass permissions"; "a IA amplifica o perigo também" | Acatado. Três regras de segurança, no bloco 7 e na folha. |
| Diagnóstico prévio | Elton quer; Marquito acha que não muda nada em uma hora | Compromisso: três perguntas na mensagem prévia (para decidir ferramenta e tamanho da clínica) e três de mão levantada na abertura (para calibrar falas). Nada além. |
| Custos | "Todo mundo deve estar assinando algum plano"; "será?" | Caminho gratuito explícito e testado (Copilot) e alternativo (Gemini CLI). |
| Multiplicadores e Papo com IA.IÁ | "Se um ou dois conseguirem, é vantagem"; convidar para o Papo | Acatado, com a correção do Concefor: dizer que o Papo é online e capturar o canal na sala. |
| Animação "a caixa é o agente" (Remotion) | "Uma animação que serve para todas as oficinas" | Proposto como sequência de três imagens estáticas para 17/09 (caixa → caixa com bilhete → dez caixas); animação fica para o curso de extensão. |
| Fable 5.1 para preparar | "A gente podia usar o Fable para isso" | Feito: esta pasta. |
| Serve para o curso de extensão | "Já é a base para o curso" | `futuro/curso-extensao-2027.md` mapeia. |

Deixado em aberto na conversa e decidido aqui (revisável): título; divisão de papéis; hospedagem da página; artigos de exemplo; o que fazer com o Papo de 17/09. Ver "Decisões abertas" no `CONTEXT.md`.

## 3. Insights

### 3.1. Os dois eixos são um só

Na conversa, Marquito nomeou "dois vieses diferentes": falar de ética e uso bem feito na web, ou mostrar IA no computador. A tensão se dissolve quando se percebe que a norma (CNPq 2.664/2026) pede exatamente o que a pasta produz: **ferramenta, finalidade e fase**. O `registro/LOG-IA.md` do kit guarda esses três dados a cada ação. A etapa 03 lê o registro e escreve o rascunho da declaração. A ética deixa de ser um bloco introdutório e vira a **razão** do método.

Meira dá a frase: a pergunta muda de "quem escreveu" para "isso se sustenta". Para responder "se sustenta", o pós-graduando precisa mostrar o que a IA fez e o que ele verificou. Isso é rastro. Rastro exige etapas. Etapas exigem organização. Organização, no computador, é pastas e arquivos.

**O que fazemos:** o bloco 2 termina com "a declaração não sai da cabeça, sai do rastro"; a demonstração termina com a declaração gerada a partir do registro; a recapitulação repete a cadeia.

### 3.2. O gargalo é a abstração, não a ferramenta

Marquito descreveu o caso da participante com doutorado que criou uma pasta, viu os arquivos e não entendeu que podia criar outra. "Quem vive no Drive, no e-mail e no WhatsApp não gerencia arquivos há anos; a IA chegou pela web e reforçou isso." O Concefor confirmou: o que destravou foi explicar o README como "o arquivo que a IA lê primeiro" e perguntar "como seria se toda pasta tivesse um leia-me?".

**O que fazemos:** o primeiro ato da demonstração depois de criar a pasta é **abrir o `CONTEXT.md` da etapa e ler em voz alta**. O primeiro pedido do kit é sempre "leia o README e me explique". O nível 2 começa lendo, não rodando. Isso é intocável na ordem de corte.

### 3.3. É palestra com demonstração; a métrica é a próxima

Marquito: "uma hora não dá tempo para oficina; é uma palestra com eles fazendo na máquina, quem conseguir". O Concefor mostra que o turno mais curto foi melhor avaliado e que "acabou cedo" é pedido de próxima oficina. **O que fazemos:** aceitar o formato, dizer em voz alta que ninguém sai operando sozinho, e responder ao "quero mais" com Papo, curso de extensão e uma segunda oficina, não com mais conteúdo.

### 3.4. O entregável em três níveis

O dilema "ou instala ou não tem entregável" é falso. Nível 0 (assiste) leva página, modelo e kit. Nível 1 (faz na web) leva o resultado do prompt bom com um artigo próprio, que já é ficha mais rascunho de declaração. Nível 2 (faz no computador) leva a pasta funcionando. Todos são sucesso; o formulário pergunta qual nível cada um alcançou.

### 3.5. O Bloco 0 fora do relógio

Aprendizado nº 1 do Concefor: sete passos de ambientação não previstos comeram o roteiro. No Secim é pior: notebook próprio, sem preparação de laboratório. **O que fazemos:** (a) mensagem aos inscritos com dez dias de antecedência, com instalação em seis passos e o pedido de conta no GitHub; (b) clínica de instalação das 15h15 às 16h na sala, durante o credenciamento, com os dois facilitadores; (c) folha de sobrevivência impressa. A hora da oficina começa com quem instalou já instalado.

### 3.6. Conceitual antes da primeira interação

Aprendizados nº 3 e nº 4 do Concefor: a máquina de sorvete foi a metáfora que funcionou, e o erro nº 1 (pedir logo o produto) acontece se o aviso vier depois. No Secim, o erro nº 1 tem cara própria: "me dá logo o texto da revisão de literatura". **O que fazemos:** bloco 4, cinco minutos, antes da demonstração, com a máquina de sorvete, o aviso e o README. Nunca cortar.

### 3.7. "Fábrica versus produto" tem citação

Marquito descreveu, com o exemplo do PDF que vira slides, a diferença entre resultado específico e genérico e o "voltar para a etapa 4, não para a zero". É, palavra por palavra, o princípio 5 do ICM ("configure the factory, not the product") e o princípio 4 ("every output is an edit surface"). Para um público de pesquisadores, ter um artigo com nome, data e arXiv vale mais que a intuição. **O que fazemos:** o bloco 7 mostra os cinco princípios em um slide e diz "leiam o artigo, está na página".

### 3.8. Janela de contexto: dizer, não demonstrar

Consenso na conversa. O ICM dá os números (2 a 8 mil tokens por etapa contra 30 a 50 mil no monolito) e a citação (Liu et al., "lost in the middle"). **O que fazemos:** um visual da barra que enche e os números; trinta segundos de "vocês já viveram isso".

### 3.9. Custos: caminho gratuito testado

A dúvida "todo mundo tem assinatura?" não se resolve com adivinhação. O Concefor já rodou uma oficina inteira em VS Code + Copilot gratuito com conta do GitHub (~50 interações por mês). O kit foi desenhado para caber em dez mensagens. Gemini CLI é a alternativa com mais crédito (cerca de 1.000 pedidos por dia com conta Google), mas é linha de comando. **O que fazemos:** recomendar Copilot como caminho primário na mensagem prévia (tem interface gráfica, já testado), Gemini CLI como alternativa, e ensinar a economia de créditos (Shift+Enter, mensagens completas) na folha. Testar o kit nas três ferramentas até 05/09 e decidir.

### 3.10. Segurança: três regras, não um sermão

Elton perguntou se vale falar dos riscos; Marquito: "difícil não falar; eles são pesquisadores". **O que fazemos:** três regras (leia as permissões; não use bypass; não suba dados sensíveis sem saber para onde vão), no bloco 7, no README do kit e na folha. Dois minutos. Sem lista de horrores.

### 3.11. Diagnóstico: o mínimo que muda uma decisão

Marquito tem razão que um questionário não muda uma oficina de uma hora; Elton tem razão que saber o perfil ajuda. O compromisso: perguntar só o que muda uma decisão. Três perguntas na mensagem prévia (usa IA toda semana? tem notebook e vem instalar? qual ferramenta já usa?) decidem quanto tempo reservar para a clínica e qual ferramenta priorizar. Três de mão levantada na abertura calibram as falas e viram dado para a retrospectiva.

### 3.12. Continuidade: o que o Concefor perdeu

Ninguém citou o Papo com IA.IÁ na avaliação do Concefor; ninguém coletou os workspaces; o certificado foi burocracia. **O que fazemos desde o desenho:** QR do canal ao lado do QR da avaliação; pasta "envie aqui" e frase de coleta antes de as pessoas levantarem; folha de tema recolhida; material junto do certificado (combinar com a organizadora); formulário de três perguntas em 30 dias; convite ao Papo dizendo que é online e o link. Um alerta: o Papo é às 15h de quinta, e a oficina é numa quinta, às 16h, com credenciamento às 15h. Decidir o que fazer com o Papo de 17/09.

### 3.13. Silvio Meira e Hugo: usar sem exceder

Meira entra na abertura (o número, a frase) e no fecho (julgamento). Não entra o resto: são dados de conferências de computação, e o público publica em periódicos de educação. Hugo entra em três pontos: P.A.R.T.E., a progressão chatbot → copiloto → agente, "ancorar, não inventar" (regra 1 do kit). O funil responsável vai para a página, não para a fala. Mostrar o repositório do seminário dele por vinte segundos: "o evento dele é pastas e arquivos".

### 3.14. Não usar o workspace-builder ao vivo

Ficou "muito meta" no Concefor; tem dois defeitos abertos (cria em lugar imprevisível; falta abrir o workspace novo em janela própria); e o Secim não tem tempo. O prompt único cria uma estrutura fechada e pequena; o kit é uma pasta boa e pronta. O builder e o artigo do ICM ficam na página, para quem quiser ir além.

### 3.15. A provocação "doideira com doideira"

"Vocês usam o computador de qualquer jeito e a IA de qualquer jeito; juntar as duas potencializa a bagunça." É forte, é verdadeira e é o momento em que a plateia se reconhece. Mantida no bloco 7, em versão construtiva: "a IA amplifica organização ou desorganização; escolham". Sem palavrão.

### 3.16. Um caso real do Ifes para abrir

O Concefor colheu, sem artefatos, o caso da dupla de pesquisadores: "preparar artigo, escolher revista, aplicar normas e responder parecer de banca sem sair do padrão". É o caso mais próximo do público do Secim. Se der tempo, uma frase no bloco 3: "colegas do Ifes já montaram pasta para isso". Se conseguirmos o contato, um depoimento de um minuto no plantão ou na próxima oficina.

## 4. Melhorias ao nosso processo de preparar oficinas

1. **Esta pasta é o processo.** Fontes brutas em `fontes/`, fichas em `referencias/`, blocos reutilizáveis em `biblioteca/`, uma pasta por evento. O Concefor tinha `oficina/` dentro do repositório do ICM; agora as oficinas têm casa própria e o material do Concefor é referência.
2. **Dono único da informação**, como no Concefor: roteiro no plano, análise aqui, decisões abertas no `CONTEXT.md`. Ninguém duplica; todos apontam.
3. **Kit testado com uma pessoa leiga antes do dia.** O Concefor não testou o `setup` com um professor simulado e pagou por isso. A organizadora do Secim é a testadora ideal: é o público (mestranda) e já fez oficina nossa.
4. **Ensaio cronometrado e vídeo de reserva.** A demonstração ao vivo é o momento de maior risco; gravar no ensaio custa dez minutos e salva a oficina.
5. **Coleta e medição fazem parte do desenho, não do pós.** Pasta compartilhada e formulário de 30 dias prontos antes do dia.
6. **Lições aprendidas obrigatórias em `06-pos-oficina.md`**, e o que valer para todas sobe para `biblioteca/`. A edição congela; a próxima nasce em `v2/`.
7. **Cada oficina alimenta o curso de extensão.** Os conceitos de `biblioteca/conceitos/` já são degraus da escada da ata. O kit de pesquisa vira modelo para os kits de plano de aula e de devolutivas.
8. **Uma rodada com a IA do "mais simples e mais efetivo"** antes de cada oficina, como Marquito propôs. Esta é a primeira. A pergunta que vale repetir: "o que sai daqui se sobrar só 45 minutos?"

## 5. Riscos e decisões pendentes

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Rede do campus bloqueia IA ou GitHub | Média (sem resposta da organização) | Perguntar hoje; hotspot 4G; nível 1 pelo celular |
| Poucos instalam antes; clínica lotada | Alta | Mensagem prévia clara; dois facilitadores; pendrive com instaladores; a oficina não depende disso |
| Copilot gratuito muda regras até o dia | Média | Testar em 05/09 e em 15/09; Gemini CLI como alternativa; folha diz "confira" |
| Kit não testado tem defeito | Alta | Testar nas três ferramentas (05/09) e com pessoa leiga (09/09) |
| Programa tem regra própria sobre IA que contradiz o que dizemos | Baixa | Perguntar à organizadora; dizer "o piso é a norma nacional" |
| Papo com IA.IÁ de 17/09 conflita | Certa | Decidir até 04/09 |
| Divulgação atrasada compromete inscrições | Alta se não enviar hoje | Enviar 02/09 |

## 6. O que não fazer

- Não usar o workspace-builder ao vivo.
- Não demonstrar a janela de contexto enchendo.
- Não prometer que sairão operando o método.
- Não esticar a oficina para caber mais; cortar na ordem definida.
- Não corrigir o resultado de ninguém; mandar corrigir a instrução.
- Não deixar a sala sem coletar: fichas, folhas, contatos de multiplicadores.
- Não citar o Ofício-Circular da CAPES pelo número como se tivéssemos o documento; dizer "a CAPES orientou os programas a usar a Portaria como referência".
