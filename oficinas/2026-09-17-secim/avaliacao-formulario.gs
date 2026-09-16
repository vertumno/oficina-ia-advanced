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
 * O formulário é anônimo: não coleta e-mail, não exige login e não limita
 * uma resposta por pessoa. São cinco perguntas; só a nota é obrigatória.
 */

var TITULO = 'IA além do chat — avaliação da oficina';

var DESCRICAO = [
  'Oficina do Secim, 17 de setembro de 2026. Leva dois minutos.',
  '',
  'É anônimo: não pedimos seu nome nem seu e-mail. Responda com franqueza —',
  'é o que nos ajuda a melhorar a próxima edição.'
].join('\n');

// A página final do formulário leva ao material da oficina.
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

  // 2 a 5. Quatro perguntas abertas, todas opcionais.
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

  Logger.log('Formulário criado: ' + TITULO);
  Logger.log('Editar:    ' + form.getEditUrl());
  Logger.log('Responder: ' + form.getPublishedUrl());

  return form.getPublishedUrl();
}
