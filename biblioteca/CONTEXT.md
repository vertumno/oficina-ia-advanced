# CONTEXT.md — biblioteca

## O que há aqui

Blocos reutilizáveis para qualquer oficina, curso ou página sobre IA. Nada aqui é específico de um evento; o que é específico fica em `oficinas/<evento>/`.

| Subpasta | Conteúdo | Formato |
|---|---|---|
| `conceitos/` | Ideias-núcleo que explicamos em toda oficina, cada uma com "como explicar em dois minutos", analogia, fala-chave e fonte | Um `.md` por conceito |
| `prompts/` | Prompts prontos para demonstrar, copiar e colar, ou entregar; e o modelo de declaração de uso de IA | Um `.md` por prompt |
| `kits/` | Pastas completas para o participante baixar e usar com sua IA no computador | Uma pasta por kit |
| `paginas/` | Modelos de página "que fica com o participante" (HTML para Moodle) | `.html` |

## Como usar

- Ao montar uma oficina, escolha os conceitos e prompts que cabem no tempo e cite-os no plano (não copie o texto; aponte para cá).
- Se precisar adaptar um bloco para um público, escreva a adaptação em `oficinas/<evento>/` e anote aqui, no bloco original, que existe uma variante.
- Se a adaptação for melhor que o original, atualize o original.

## Regras para agentes

- Blocos são estáveis. Alterações precisam preservar o que já está sendo usado em oficinas passadas (ou registrar a mudança na seção "Histórico" do bloco).
- Cada conceito e prompt cita sua fonte. Sem fonte, marcar *a confirmar*.
- O kit tem regras próprias em `kits/CONTEXT.md`; respeitá-las.
