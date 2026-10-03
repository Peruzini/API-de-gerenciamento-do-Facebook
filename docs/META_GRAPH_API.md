# Meta Graph API

## Objetivo

Concentrar aqui os contratos e decisões relacionados à integração com a Meta. A versão da Graph API deve ser configurável por ambiente para evitar espalhar uma versão fixa pelo código.

Exemplo:

```env
META_GRAPH_VERSION=vXX.X
META_GRAPH_BASE_URL=https://graph.facebook.com
```

## Permissões esperadas para a V1

A lista final deve ser validada no painel e na documentação oficial da Meta no momento da configuração do App.

Permissões candidatas:
- `pages_show_list`
- `pages_read_engagement`
- `pages_manage_engagement`
- `pages_manage_metadata` para recursos ligados à assinatura/configuração da Página e Webhooks, quando aplicável

Solicitar somente permissões efetivamente necessárias.

## Descoberta de Páginas

Fluxo planejado:

```http
GET /{graph-version}/me/accounts
```

Campos desejados:
- id
- name
- access_token
- tasks

O Page Access Token retornado nunca deve ser enviado ao cliente final.

## Comentários

A implementação deve encapsular endpoints da Meta em um `MetaGraphClient`.

Operações da nossa camada:
- listar comentários;
- paginação;
- consultar respostas;
- responder comentário;
- tratamento uniforme de erros.

## Resposta a comentário

Fluxo conceitual:

```text
POST /{comment-id}/comments
message=<texto>
```

A chamada real deve usar o Page Access Token correspondente à Página autorizada.

## Erros

O cliente deverá normalizar:
- token inválido/expirado;
- permissão insuficiente;
- objeto não encontrado;
- rate limiting;
- falha transitória;
- erro de validação;
- indisponibilidade da Meta.

## Paginação

Nunca assumir que uma resposta contém todos os registros. A camada de serviço deve suportar cursores `before` / `after` conforme retornados pela Graph API.

## Política de versão

- versão da Graph API em variável de ambiente;
- atualização deliberada, nunca automática;
- registrar mudança em `docs/DECISOES.md`;
- executar testes de regressão antes de trocar versão.

## Referências

Documentação oficial:
- https://developers.facebook.com/docs/graph-api/
- https://developers.facebook.com/docs/pages-api/
- https://developers.facebook.com/docs/graph-api/webhooks/
