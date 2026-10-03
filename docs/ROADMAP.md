# Roadmap

## Fase 0 — Fundação

- [x] Criar repositório
- [x] Definir arquitetura
- [x] Criar documentação inicial
- [ ] Criar ambiente local
- [ ] Configurar FastAPI
- [ ] Configurar variáveis de ambiente
- [ ] Configurar testes

## V1 — Comentários de Página

### 1. Meta App e autenticação
- [ ] Criar/configurar Meta App
- [ ] Configurar Facebook Login quando necessário
- [ ] Obter User Access Token de desenvolvimento
- [ ] Descobrir Páginas administradas
- [ ] Obter Page Access Token
- [ ] Validar permissões mínimas
- [ ] Definir estratégia de renovação/expiração de tokens

### 2. Leitura
- [ ] Listar Páginas
- [ ] Listar posts
- [ ] Listar comentários
- [ ] Paginação
- [ ] Obter contexto do comentário
- [ ] Identificar comentários sem resposta

### 3. Escrita
- [ ] Responder comentário de teste
- [ ] Validar autoria da resposta
- [ ] Tratar erros da Graph API
- [ ] Implementar idempotência
- [ ] Criar auditoria de respostas

### 4. Webhooks
- [ ] Criar endpoint de verificação
- [ ] Validar assinatura
- [ ] Assinar Página/eventos necessários
- [ ] Persistir eventos recebidos
- [ ] Deduplicar eventos
- [ ] Processar eventos com segurança

### 5. Banco e auditoria
- [ ] PostgreSQL
- [ ] migrations
- [ ] Comment / Reply / WebhookEvent
- [ ] AuditLog
- [ ] correlação request/event/action

### 6. Integração com ChatGPT
- [ ] Definir contrato MCP/conector
- [ ] Ferramenta de listar pendências
- [ ] Ferramenta de obter contexto
- [ ] Ferramenta de responder comentário
- [ ] Aprovação humana antes da publicação

## V2 — Messenger

Somente após a V1 estar estável:
- conversas privadas;
- regras de janela de mensagens;
- respostas;
- escalonamento humano;
- auditoria.

## V3 — Moderação

- ocultar comentário;
- excluir quando permitido;
- spam;
- classificação;
- fila de revisão;
- políticas de moderação.

## V4 — Automação

- respostas assistidas por IA;
- regras por intenção;
- respostas automáticas de baixo risco;
- analytics;
- dashboards;
- alertas;
- políticas de escalonamento.

## Critério de conclusão da V1

A V1 estará tecnicamente provada quando conseguirmos executar de ponta a ponta:

```text
Comentário no Facebook
        ↓
Evento/consulta pela Meta
        ↓
Nossa API identifica o comentário
        ↓
Usuário/ChatGPT recebe contexto
        ↓
Resposta é aprovada
        ↓
Nossa API publica pela Meta
        ↓
Ação fica registrada em auditoria
```
