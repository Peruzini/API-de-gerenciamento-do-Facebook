# Segurança

## Princípio

A API deve operar com privilégio mínimo e manter uma separação rígida entre credenciais da Meta e consumidores da nossa API.

## Regras obrigatórias

- segredos fora do Git;
- HTTPS em produção;
- tokens nunca retornados ao ChatGPT/cliente;
- logs sem segredos;
- validação de assinatura de Webhooks;
- controle de acesso por Página;
- trilha de auditoria para qualquer escrita;
- rate limit na nossa API;
- validação de tamanho e conteúdo de entrada;
- idempotência em operações de escrita;
- rotação de segredos;
- dependências atualizadas e verificadas.

## Publicação de respostas

Na V1, o padrão será:

```text
comentário
    ↓
geração/análise
    ↓
revisão/aprovação humana
    ↓
publicação
    ↓
auditoria
```

Automação sem aprovação humana somente será considerada em fase posterior e para classes de baixo risco definidas explicitamente.

## Dados de auditoria

Registrar no mínimo:
- ator;
- ação;
- Page ID;
- Comment ID;
- horário;
- resultado;
- correlation ID;
- origem da solicitação.

Evitar armazenar conteúdo pessoal além do necessário para a finalidade operacional.

## Repositório público

Como este repositório pode ser público, todo exemplo deve usar placeholders. Nunca adicionar tokens reais nem arquivos `.env`.
