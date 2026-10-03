# Autenticação

## Objetivo

Garantir que credenciais da Meta permaneçam no backend e nunca sejam expostas ao ChatGPT, frontend, logs ou repositório.

## Tipos de credenciais

### App ID
Identifica o Meta App. Pode aparecer em configuração, mas ainda deve ser tratado como dado de configuração.

### App Secret
Segredo crítico. Nunca commitar ou enviar ao cliente.

### User Access Token
Usado no fluxo de autorização do usuário e obtenção de recursos permitidos.

### Page Access Token
Usado para operações da Página conforme permissões/tarefas concedidas.

## Fluxo planejado

```text
Usuário autoriza Meta App
        ↓
User Access Token
        ↓
Consulta Páginas autorizadas
        ↓
Page Access Token
        ↓
Backend guarda/referencia com segurança
        ↓
Serviços internos fazem chamadas à Meta
```

## Regras

1. Nenhum token em Git.
2. Nenhum token em prompts.
3. Nenhum token em respostas da API.
4. Nenhum token em logs.
5. Segredos em secret manager/variáveis seguras.
6. Rotação e expiração devem ser tratadas explicitamente.
7. Toda operação deve validar qual Página o chamador está autorizado a utilizar.

## Desenvolvimento

O arquivo `.env.example` contém apenas placeholders.

Arquivo real:
```text
.env
```

deve permanecer ignorado pelo Git.
