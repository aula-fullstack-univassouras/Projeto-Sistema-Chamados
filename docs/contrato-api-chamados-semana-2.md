# Contrato inicial — API de Chamados

## 1. Recurso

- **Nome:** `chamados`
- **Finalidade:** registrar e acompanhar solicitações de suporte técnico.

O recurso `chamados` representa uma solicitação de suporte feita por uma pessoa usuária. Cada chamado possui informações sobre o problema, sua prioridade e seu status durante o atendimento.

## 2. Formato de dados

As requisições e respostas da API utilizarão **JSON**.

Para requisições que enviam dados ao servidor, será utilizado o cabeçalho:

```http
Content-Type: application/json
```

## 3. Atributos

| Campo | Tipo | Obrigatório na criação? | Descrição |
|---|---|---:|---|
| `id` | número inteiro | Não | Identificador único do chamado |
| `titulo` | texto | Sim | Resumo do problema ou solicitação |
| `descricao` | texto | Sim | Descrição detalhada do problema |
| `prioridade` | texto | Sim | Nível de prioridade do chamado |
| `status` | texto | Não | Situação atual do chamado |

### Valores previstos

**Prioridade:**

- `baixa`
- `media`
- `alta`

**Status:**

- `aberto`
- `em_andamento`
- `encerrado`

O `id` será gerado pelo sistema. Na criação de um chamado, o `status` poderá ser iniciado automaticamente como `aberto`.

## 4. Endpoints

| Método | URI | Finalidade | Parâmetros | Status previstos |
|---|---|---|---|---|
| `GET` | `/chamados` | Listar chamados | `status` opcional | `200` |
| `GET` | `/chamados/{id}` | Consultar um chamado específico | `id` na URI | `200`, `404` |
| `POST` | `/chamados` | Criar um chamado | Corpo JSON | `201`, `400` |
| `PATCH` | `/chamados/{id}` | Atualizar parcialmente um chamado | `id` e corpo JSON | `200`, `400`, `404` |
| `DELETE` | `/chamados/{id}` | Remover um chamado | `id` na URI | `204`, `404` |

As URIs representam os recursos e não ações. Por isso, serão utilizados caminhos como `/chamados` e `/chamados/{id}`, evitando formatos como `/criarChamado` ou `/buscarChamados`.

## 5. Listar chamados

### Requisição

```http
GET /chamados
```

Também poderá ser utilizado o parâmetro de consulta `status` para filtrar os chamados:

```http
GET /chamados?status=aberto
```

### Resposta

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
[
  {
    "id": 42,
    "titulo": "Tela sem acesso",
    "descricao": "Não consigo acessar a tela de consultas.",
    "prioridade": "alta",
    "status": "aberto"
  }
]
```

## 6. Consultar um chamado

### Requisição

```http
GET /chamados/42
```

### Resposta de sucesso

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta",
  "status": "aberto"
}
```

### Recurso inexistente

Caso não exista um chamado com o identificador informado:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json
```

```json
{
  "erro": "Recurso não encontrado",
  "mensagem": "O chamado informado não foi encontrado."
}
```

## 7. Criar chamado

### Requisição

```http
POST /chamados
Content-Type: application/json
```

```json
{
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta"
}
```

### Resposta de sucesso

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /chamados/42
```

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta",
  "status": "aberto"
}
```

O `status` é definido inicialmente como `aberto` quando não for informado na criação.

### Dado inválido

Caso o campo `titulo` não seja informado:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json
```

```json
{
  "erro": "Dado inválido",
  "detalhes": [
    {
      "campo": "titulo",
      "mensagem": "O título é obrigatório."
    }
  ]
}
```

A mesma estrutura poderá ser utilizada para outras validações de dados.

## 8. Atualizar chamado

A atualização será parcial e utilizará o método `PATCH`.

### Requisição

```http
PATCH /chamados/42
Content-Type: application/json
```

Exemplo de alteração de prioridade:

```json
{
  "prioridade": "media"
}
```

### Resposta de sucesso

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "media",
  "status": "aberto"
}
```

Caso o chamado não exista, será retornado:

```http
HTTP/1.1 404 Not Found
```

Caso os dados enviados sejam inválidos:

```http
HTTP/1.1 400 Bad Request
```

## 9. Remover chamado

### Requisição

```http
DELETE /chamados/42
```

### Resposta de sucesso

```http
HTTP/1.1 204 No Content
```

Não haverá corpo na resposta quando a remoção for realizada com sucesso.

Caso o chamado não exista:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json
```

```json
{
  "erro": "Recurso não encontrado",
  "mensagem": "O chamado informado não foi encontrado."
}
```

## 10. Códigos de status

| Código | Significado | Utilização no contrato |
|---|---|---|
| `200` | OK | Consultas e atualizações realizadas com sucesso |
| `201` | Created | Chamado criado com sucesso |
| `204` | No Content | Chamado removido com sucesso |
| `400` | Bad Request | Dados inválidos ou obrigatórios ausentes |
| `404` | Not Found | Chamado não encontrado |
| `500` | Internal Server Error | Erro inesperado no servidor |

Os códigos de status têm como objetivo permitir que o consumidor da API identifique o resultado da solicitação sem depender somente da mensagem retornada no corpo da resposta.

## 11. Estrutura dos erros

Os erros de validação utilizarão uma estrutura padronizada:

```json
{
  "erro": "Dado inválido",
  "detalhes": [
    {
      "campo": "titulo",
      "mensagem": "O título é obrigatório."
    }
  ]
}
```

Para erros relacionados a recursos inexistentes, será utilizada uma estrutura mais simples:

```json
{
  "erro": "Recurso não encontrado",
  "mensagem": "O chamado informado não foi encontrado."
}
```

As mensagens devem ser claras para que o front-end consiga apresentar uma informação compreensível para a pessoa usuária.

## 12. Decisões tomadas

- O recurso principal da primeira versão será `chamados`.
- As requisições e respostas utilizarão JSON.
- A coleção será acessada por `/chamados`.
- Um chamado individual será identificado por `/chamados/{id}`.
- `GET` será utilizado para consultas.
- `POST` será utilizado para criação.
- `PATCH` será utilizado para alterações parciais.
- `DELETE` será utilizado para remoção.
- O status inicial de um novo chamado será `aberto`.
- O parâmetro `status` poderá ser utilizado para filtrar a listagem.
- A estrutura de erros será padronizada para facilitar o tratamento pelo front-end.
- Os valores iniciais definidos para prioridade são `baixa`, `media` e `alta`.
- Os valores iniciais definidos para status são `aberto`, `em_andamento` e `encerrado`.

## 13. Dúvidas pendentes

- Definir posteriormente se apenas atendentes poderão alterar o status dos chamados.
- Definir como será realizada a autenticação dos usuários.
- Definir futuramente se um chamado encerrado poderá ser reaberto.
- Avaliar posteriormente a necessidade de novos filtros na listagem.
- Avaliar a necessidade de outros recursos, como usuários e categorias, conforme o desenvolvimento avançar.

## 14. Revisão

Este documento representa o contrato inicial da API e poderá ser atualizado conforme as decisões do projeto forem validadas durante as próximas etapas da disciplina.

Antes da implementação definitiva, o contrato deve ser revisado pela equipe para verificar se os endpoints, métodos, campos, exemplos e códigos de status continuam de acordo com o que será desenvolvido.

---

**Documento relacionado:**

- `planejamento-semana-1.md` — planejamento inicial do sistema.
- `diagrama-arquitetura.md` — arquitetura inicial do projeto.