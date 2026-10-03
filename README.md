# API de gerenciamento do Facebook

Camada própria de integração entre uma Página do Facebook, a Meta Graph API e clientes autorizados (incluindo, futuramente, ChatGPT via conector/MCP).

## Objetivo

Permitir que operações de atendimento e moderação sejam executadas de forma controlada, auditável e segura, sem expor tokens da Meta ao cliente consumidor.

## Escopo

### V1 — Comentários de Página
- autenticação com a Meta;
- listar páginas autorizadas;
- listar posts da Página;
- listar comentários;
- identificar comentários sem resposta;
- obter contexto de um comentário;
- responder a comentários;
- receber eventos via Webhooks;
- registrar logs e auditoria.

### V2 — Messenger
- leitura de conversas elegíveis;
- respostas privadas;
- regras específicas da Messenger Platform.

### V3 — Moderação
- ocultar/excluir comentários quando permitido;
- classificação de spam;
- filas de revisão;
- políticas de escalonamento humano.

### V4 — Automação e ChatGPT
- conector/MCP;
- geração assistida de respostas;
- regras de automação;
- analytics e monitoramento.

## Arquitetura inicial

```text
Facebook Page
    |
    v
Meta Graph API
    |
    v
API FastAPI
 ├─ OAuth / tokens
 ├─ Pages / Posts / Comments
 ├─ Webhooks
 ├─ Auditoria
 └─ PostgreSQL
    |
    v
Conector / MCP
    |
    v
ChatGPT
```

## Stack

- Python 3.12+
- FastAPI
- Pydantic
- HTTPX
- SQLAlchemy
- PostgreSQL
- Docker

## Estrutura

```text
app/
  api/
  core/
  models/
  schemas/
  services/
  main.py
docs/
  ARQUITETURA.md
  ROADMAP.md
  META_GRAPH_API.md
  AUTENTICACAO.md
  WEBHOOKS.md
  SEGURANCA.md
  DECISOES.md
tests/
```

## Segurança

Nunca commitar App Secret, Page Access Token, User Access Token ou qualquer credencial. Use `.env` local/secret manager. O arquivo `.env.example` contém somente nomes de variáveis.

## Status

Planejamento e estrutura inicial em andamento. A primeira prova técnica será:

1. autenticar na Meta;
2. obter uma Página autorizada;
3. ler comentários;
4. responder a um comentário de teste;
5. validar o recebimento de Webhook.

Consulte [docs/ROADMAP.md](docs/ROADMAP.md) para o plano detalhado.
