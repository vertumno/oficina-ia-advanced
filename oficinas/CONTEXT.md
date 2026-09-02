# CONTEXT.md — oficinas

## O que há aqui

Uma pasta por evento, nomeada `AAAA-MM-DD-nome`. Cada pasta é autossuficiente para preparar, dar e registrar a oficina; o que for reutilizável entre eventos vive em `biblioteca/`, não aqui.

| Pasta | Evento | Estado |
|---|---|---|
| `2026-09-17-secim/` | Oficina "IA além do chat", Secim, Ifes campus Vitória, 17/09/2026, 16h às 17h30 | Em preparação |

Oficinas anteriores que vivem em outro repositório: "IA além do chat", VIII Concefor, 20/08/2026, em `C:\dev\oficina-concefor-icm\oficina\` (ficha em `referencias/oficina-concefor-2026-08-20.md`).

## Estrutura padrão de uma pasta de oficina

| Arquivo | O que é |
|---|---|
| `CONTEXT.md` | Estado, roteamento, decisões abertas |
| `00-briefing.md` | O convite, o público, a logística, as restrições, tudo que veio de fora |
| `01-plano-da-oficina.md` | Roteiro minuto a minuto, materiais, papéis, critérios de sucesso, planos B. Dono único do roteiro |
| `02-analise-e-melhorias.md` | O que a conversa de planejamento decidiu, o que os dados anteriores mostram, o que propomos mudar e por quê |
| `03-divulgacao-*.md` | Título, descrição, minibios, necessidades, no formato que o organizador pediu |
| `04-pre-oficina.md` | Checklist datado do que precisa acontecer antes, incluindo a comunicação com inscritos |
| `05-roteiro-demonstracao.md` | Script da demonstração ao vivo, com prompts exatos e plano B |
| `06-pos-oficina.md` | O que acontece depois: envio, coleta, medição, e a seção "Lições aprendidas" a preencher |
| `referencias-*.html` e `.md` | A página que fica com os participantes |

## Convenções

- **Versionamento:** a edição realizada congela. Mudanças para uma nova edição vão para `v2/` dentro da pasta do evento (como no Concefor).
- **Dono único:** o roteiro vive no plano; a análise, no arquivo de análise; as decisões abertas, no `CONTEXT.md`. Os outros apontam, não duplicam.
- **Fontes brutas** do evento (transcrições, avaliações, fotos) vão para `fontes/AAAA-MM-DD-...` na raiz do repositório, com linha em `fontes/CONTEXT.md`.
- **Lições aprendidas** que valem para qualquer oficina sobem para `biblioteca/` ou `referencias/` depois do evento.
