# Webhooks

## Objetivo

Receber eventos da Meta para reduzir polling e reagir a novos comentários de forma controlada.

## Endpoints

### Verificação

```http
GET /webhooks/meta
```

Responsável pelo handshake de verificação definido pela Meta.

### Eventos

```http
POST /webhooks/meta
```

Recebe notificações da Meta.

## Requisitos de segurança

- validar o token de verificação no handshake;
- validar assinatura da requisição conforme o mecanismo oficial da Meta;
- rejeitar payloads inválidos;
- nunca confiar apenas no corpo recebido;
- armazenar identificadores para deduplicação;
- responder rapidamente e processar trabalho pesado de forma desacoplada.

## Processamento

```text
Meta
  ↓
POST /webhooks/meta
  ↓
Validação
  ↓
Deduplicação
  ↓
Persistência do evento
  ↓
Fila/processamento
  ↓
Atualização de comentário/pendência
```

## Idempotência

Eventos podem ser repetidos. O processamento deverá ser seguro contra duplicidade.

## Observabilidade

Registrar:
- horário;
- tipo do evento;
- Page ID;
- objeto afetado;
- event/correlation ID;
- status do processamento;
- erro normalizado quando houver.

Nunca registrar tokens ou segredos.
