/**
 * Cria o formulário de avaliação da oficina "IA além do chat" (Secim, 17/09/2026).
 *
 * Como usar:
 *   1. Abra https://script.google.com e crie um projeto novo.
 *   2. Apague o conteúdo do Code.gs, cole este arquivo inteiro e salve.
 *   3. Escolha a função criarFormulario e clique em Executar.
 *      Na primeira vez o Google pede autorização: é o seu próprio script
 *      criando um formulário na sua conta.
 *   4. Veja os dois links no Registro de execução (Ctrl+Enter):
 *      o de edição, para você, e o de resposta, que vira o QR do slide 34.
 *
 * São sete perguntas; obrigatórias apenas a nota e o nível alcançado (ambas
 * de um clique). O formulário não coleta e-mail automaticamente, não exige
 * login e não limita uma resposta por pessoa: quem não preencher o campo de
 * contato no fim responde de forma anônima.
 */

var TITULO = 'IA além do chat — avaliação da oficina';

var DESCRICAO = [
  'Oficina do Secim, 17 de setembro de 2026. Leva dois minutos.',
  '',
  'Não pedimos seu nome nem seu e-mail: só no fim, se você quiser continuar',
  'conosco, há um campo opcional de contato. Deixando-o em branco, sua',
  'resposta é anônima. Responda com franqueza — é o que nos ajuda a melhorar',
  'a próxima edição.'
].join('\n');

// A página final do formulário leva ao material da oficina.
// Se a página do Portal IA.IA entrar no ar com link curto, troque aqui.
var LINK_MATERIAL = 'https://claude.ai/artifact/LXwpGNo9FbotQ4Pp8CkaWN';

function criarFormulario() {
  var form = FormApp.create(TITULO);

  form.setDescription(DESCRICAO);
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setAllowResponseEdits(false);
  form.setPublishingSummary(false);
  form.setProgressBar(false);
  form.setConfirmationMessage(
    'Obrigado! Todo o material da oficina (kit, prompts, modelo de declaração ' +
    'e referências) está em ' + LINK_MATERIAL
  );

  // setRequireLogin só existe em contas do Google Workspace; em conta comum,
  // ignorar o erro mantém o formulário aberto a qualquer pessoa.
  try {
    form.setRequireLogin(false);
  } catch (e) {
    Logger.log('setRequireLogin não se aplica a esta conta: ' + e.message);
  }

  // 1. NPS
  form.addScaleItem()
    .setTitle('De 0 a 10, o quanto você recomendaria esta oficina a um colega?')
    .setBounds(0, 10)
    .setLabels('Não recomendaria', 'Recomendaria com certeza')
    .setRequired(true);

  // 2. Nível alcançado. Mede o entregável em três níveis (01-plano, 3.4):
  // todos são sucesso, e é isto que preenche a linha "Nível 0 / 1 / 2" da
  // retrospectiva. Um clique, por isso obrigatória.
  form.addMultipleChoiceItem()
    .setTitle('Até onde você foi hoje?')
    .setHelpText('Não existe resposta certa: assistir já era um dos caminhos previstos.')
    .setChoiceValues([
      'Assisti (levo a página, o modelo de declaração e o kit)',
      'Fiz no navegador (rodei o prompt com um artigo meu)',
      'Fiz no computador (criei a pasta com a ferramenta instalada)',
      'Sentei à máquina como voluntário'
    ])
    .setRequired(true);

  // 3 a 6. Quatro perguntas abertas, todas opcionais.
  var abertas = [
    {
      titulo: 'O que você mais gostou?',
      ajuda: 'Um momento, uma parte ou uma ideia que valeu a pena.'
    },
    {
      titulo: 'O que você tiraria da oficina?',
      ajuda: 'O que sobrou, atrasou ou não serviu para você.'
    },
    {
      titulo: 'O que você acrescentaria?',
      ajuda: 'O que faltou: um assunto, mais prática, mais tempo em algo.'
    },
    {
      titulo: 'O que melhoraria na próxima edição?',
      ajuda: 'Ritmo, explicações, material, sala, horário — o que vier à cabeça.'
    }
  ];

  abertas.forEach(function (pergunta) {
    form.addParagraphTextItem()
      .setTitle(pergunta.titulo)
      .setHelpText(pergunta.ajuda)
      .setRequired(false);
  });

  // 7. Continuidade. Fica no fim, depois de tudo o que é anônimo, e o aviso
  // deixa explícito que preencher o contato identifica a resposta.
  form.addSectionHeaderItem()
    .setTitle('Quer continuar depois de hoje?')
    .setHelpText(
      'Esta parte é opcional. Se você escrever seu e-mail, ele chega junto ' +
      'com as respostas acima e elas deixam de ser anônimas. Prefere manter ' +
      'o anonimato? Deixe em branco e escreva seu contato na folha de tema ' +
      'ou fale com a gente no coffee break.'
    );

  form.addCheckboxItem()
    .setTitle('Tenho interesse em:')
    .setChoiceValues([
      'Ser multiplicador de IA no meu programa',
      'Participar do Papo com IA.IÁ (quintas, 15h às 15h45, online)',
      'Saber do curso de extensão "Inteligência de Contexto Pedagógica com IA" (2027)'
    ])
    .setRequired(false);

  form.addTextItem()
    .setTitle('Seu e-mail (só se você marcou algo acima)')
    .setHelpText('Usamos apenas para o convite combinado. Nada além disso.')
    .setValidation(
      FormApp.createTextValidation()
        .setHelpText('Escreva um e-mail válido ou deixe o campo em branco.')
        .requireTextIsEmail()
        .build()
    )
    .setRequired(false);

  Logger.log('Formulário criado: ' + TITULO);
  Logger.log('Editar:    ' + form.getEditUrl());
  Logger.log('Responder: ' + form.getPublishedUrl());

  return form.getPublishedUrl();
}
