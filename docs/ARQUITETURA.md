# Arquitetura

## Princípio central

A Meta Graph API não será acessada diretamente pelo ChatGPT. A aplicação mantém credenciais e regras de autorização no servidor e expõe somente operações de negócio estritamente necessárias.

## Fluxo principal

```text
Usuário do Facebook
        |
        v
Facebook Page
        |
        v
Meta Graph API
        |
        +------> Webhooks ------+
        |                       |
        v                       v
                API FastAPI
        ├─ autenticação
        ├─ Meta client
        ├─ comentários
        ├─ regras de negócio
        ├─ auditoria
        └─ persistência
                |
                v
            PostgreSQL
                |
                v
        Conector / MCP
                |
                v
             ChatGPT
```

## Camadas

### app/api
Rotas HTTP públicas da nossa API.

### app/core
Configuração, segurança, logging e dependências centrais.

### app/services
Integrações externas e regras de negócio. O cliente da Meta ficará isolado aqui.

### app/models
Modelos persistidos no banco.

### app/schemas
Contratos Pydantic de entrada e saída.

## Operações previstas na V1

- `GET /health`
- `GET /pages`
- `GET /pages/{page_id}/posts`
- `GET /posts/{post_id}/comments`
- `GET /pages/{page_id}/comments/unanswered`
- `GET /comments/{comment_id}/context`
- `POST /comments/{comment_id}/replies`
- `GET /webhooks/meta` — verificação do webhook
- `POST /webhooks/meta` — recebimento de eventos

## Persistência mínima

Entidades previstas:
- Page
- Post
- Comment
- Reply
- WebhookEvent
- AuditLog
- CredentialReference

Tokens não devem ser armazenados em texto puro no banco.

## Integração futura com ChatGPT

O ChatGPT consumirá um conector/MCP que oferecerá ferramentas de alto nível, por exemplo:
- `facebook.list_unanswered_comments`
- `facebook.get_comment_context`
- `facebook.reply_comment`

O conector não receberá App Secret nem Page Access Token.
