# API de Chamados de Suporte

## GET /chamados

Consulta todos os chamados cadastrados.

### Resposta

Status:

200 OK

Exemplo:

```json
[
    {
        "id": "1",
        "titulo": "Não consigo acessar o sistema",
        "descricao": "A tela de autenticação informa que minhas credenciais são inválidas.",
        "prioridade": "alta"
    }
]

POST /chamados

Cadastra um novo chamado.

Requisição
{
    "titulo": "Não consigo acessar o sistema",
    "descricao": "A tela de autenticação informa que minhas credenciais são inválidas.",
    "prioridade": "alta"
}
Resposta

Status:

201 Created

{
    "id": "1",
    "titulo": "Não consigo acessar o sistema",
    "descricao": "A tela de autenticação informa que minhas credenciais são inválidas.",
    "prioridade": "alta"
}
Prioridades permitidas
baixa
media
alta
Erro de validação

Status:

400 Bad Request

{
    "erro": "DADOS_INVALIDOS",
    "mensagem": "Não foi possível cadastrar o chamado.",
    "campos": {
        "prioridade": "Use baixa, media ou alta."
    }
}

---

# 13. Testando a API

No PowerShell, entre na pasta `backend`:

```powershell
cd backend