# Registro de decisões

## ADR-001 — Backend em Python/FastAPI

**Status:** aprovado

A API será implementada em Python com FastAPI, aproveitando tipagem, Pydantic, ecossistema HTTP e facilidade de integração futura com ferramentas de IA.

## ADR-002 — Meta desacoplada dos clientes

**Status:** aprovado

Clientes não acessarão a Graph API diretamente. Toda comunicação passa pelo backend.

## ADR-003 — V1 limitada a comentários

**Status:** aprovado

Messenger, moderação avançada e automação ficam fora da primeira entrega. O objetivo é provar leitura, contexto, resposta e Webhook de comentários.

## ADR-004 — Aprovação humana na V1

**Status:** aprovado

Respostas sugeridas por IA não serão publicadas automaticamente na primeira versão.

## ADR-005 — Versão da Graph API configurável

**Status:** aprovado

A versão será definida por variável de ambiente e atualizada deliberadamente após testes.

## ADR-006 — Auditoria de qualquer escrita

**Status:** aprovado

Toda ação que altere conteúdo no Facebook deverá gerar registro de auditoria.
