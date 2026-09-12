# Sistema de Chamados

## Integrantes

1. Ângelo Mateus - 202323348
2. Esequias Ferraz De Andrade - 202411248
3. Felipe Ramos Da Silva - 202221884
4. Thiago Marsol Almeida Baião - 202323232
5. Juberto Junior Marques Coutinho - 202321179
6. Wallace Gustavo Da Silva - 202411248

---

# Objetivo

Criar uma aplicação web para registrar e acompanhar chamados de suporte técnico em um só lugar, substituindo o uso de planilhas e mensagens espalhadas.

O sistema foi desenvolvido de forma incremental durante as atividades práticas da disciplina, começando pelo planejamento e definição do problema, passando pela definição da arquitetura e do contrato da API e, posteriormente, chegando à implementação do back-end e da persistência dos dados.

---

# Desenvolvimento

O desenvolvimento do projeto foi realizado de forma incremental, acompanhando as atividades propostas ao longo das semanas. Cada etapa acrescentou novos elementos ao sistema, permitindo que a aplicação evoluísse de uma definição inicial do problema para uma implementação funcional da API de gerenciamento de chamados.

## Semana 1 — Planejamento inicial

Na primeira etapa foi realizado o planejamento inicial do projeto. Foram definidos o problema a ser solucionado, o escopo da aplicação, os usuários envolvidos, os requisitos iniciais e o fluxo principal do sistema.

A proposta estabelecida foi desenvolver um sistema capaz de centralizar o registro e o acompanhamento de chamados de suporte técnico, evitando que essas solicitações permanecessem espalhadas por diferentes meios de comunicação, como mensagens e planilhas.

A documentação referente a essa etapa está disponível no diretório `docs/`, por meio do arquivo:

```text
docs/planejamento-semana-1.md
```

---

## Semana 2 — Arquitetura do sistema

Na segunda etapa foi definida a organização arquitetural inicial do projeto.

A aplicação foi estruturada considerando a separação entre as diferentes responsabilidades do sistema, permitindo que cada parte da aplicação possua uma função específica.

A documentação da arquitetura está disponível em:

```text
docs/diagrama-arquitetura.md
```

Essa definição serviu como base para a organização posterior do back-end, permitindo separar as rotas, regras de negócio, modelos e acesso aos dados.

---

## Semana 3 — Contrato da API

Na terceira etapa foi definido o contrato inicial da API de chamados.

Foram estabelecidos os principais recursos, endpoints, métodos HTTP, parâmetros, formatos das requisições e respostas e códigos de status esperados.

A documentação correspondente está disponível em:

```text
docs/contrato-api-chamados.md
```

Essa definição serviu como referência para a implementação posterior da API, permitindo que os endpoints fossem desenvolvidos de acordo com um contrato previamente estabelecido.

---

# Semana 4 — Persistência de Chamados

Na quarta semana foi realizada a implementação da persistência dos chamados.

A atividade teve como objetivo substituir o armazenamento exclusivamente em memória por uma estrutura persistente, permitindo que os chamados continuassem disponíveis mesmo depois que a aplicação fosse encerrada e executada novamente.

A atividade propôs a criação de uma estrutura persistente para os chamados e a integração dos endpoints de criação e consulta com o banco de dados. O resultado esperado era que um chamado criado por meio da API permanecesse disponível em uma consulta posterior.

Para essa etapa foi utilizado o **SQLite**, banco de dados relacional local que permite armazenar os chamados diretamente no projeto, sem necessidade de utilização de serviços externos ou provedores de nuvem.

## Modelagem do chamado

A entidade principal da aplicação é o `Chamado`.

A estrutura utilizada possui os seguintes campos:

| Campo | Descrição |
|---|---|
| `id` | Identificador único do chamado |
| `titulo` | Título do chamado |
| `descricao` | Descrição detalhada do problema |
| `status` | Estado atual do chamado |
| `criado_em` | Data e hora em que o chamado foi criado |

O identificador é gerado automaticamente pelo banco de dados. O título e a descrição são obrigatórios, enquanto o campo `status` possui valores controlados.

Os estados aceitos são:

```text
aberto
em_andamento
fechado
```

Essa estrutura corresponde ao modelo definido na atividade da Semana 4.

## Banco de dados

A aplicação utiliza SQLite para realizar a persistência dos dados.

A tabela utilizada é denominada `chamados` e possui uma chave primária para identificação dos registros, campos obrigatórios para título e descrição, um valor padrão para o status e uma data de criação.

O projeto possui também um script SQL versionado em:

```text
backend/database/001_criar_tabela_chamados.sql
```

Esse arquivo contém a definição da tabela e a restrição que controla os valores permitidos para o campo `status`.

A atividade da Semana 4 determina que a estrutura do banco seja reproduzível e versionada por meio de script ou migração.

Além do script SQL, o projeto possui a implementação da criação automática da tabela utilizando SQLite. Dessa maneira, quando a aplicação é iniciada, o banco é inicializado caso a tabela ainda não exista.

## Persistência dos dados

O acesso ao banco foi concentrado no módulo:

```text
backend/data/chamados.py
```

Esse módulo é responsável por estabelecer a conexão com o SQLite e realizar as operações de inserção, consulta, atualização e exclusão.

A aplicação utiliza consultas parametrizadas para enviar os valores ao banco de dados. Dessa forma, os dados recebidos pelas requisições não são inseridos diretamente por concatenação de strings SQL.

Essa abordagem atende à orientação da atividade para que as consultas utilizem parâmetros, evitando a montagem direta de comandos SQL com valores recebidos nas requisições.

## Organização do back-end

A implementação da Semana 4 mantém a separação de responsabilidades definida durante as etapas anteriores.

A estrutura utilizada pode ser representada da seguinte forma:

```text
Cliente
   ↓
Router
   ↓
Controller
   ↓
Service
   ↓
Data / SQLite
```

O **Router** define os endpoints disponíveis na API e recebe as requisições HTTP.

O **Controller** coordena o fluxo das requisições, encaminhando os dados para os serviços e tratando situações como registros inexistentes e identificadores inválidos.

O **Service** concentra a lógica relacionada às operações dos chamados e faz a comunicação entre os controllers e a camada de acesso aos dados.

A camada **Data** é responsável pela comunicação direta com o SQLite, executando as consultas necessárias para inserir, listar, buscar, atualizar e excluir registros.

Os **Models** utilizam Pydantic para definir a estrutura dos dados recebidos e retornados pela API, além de realizar validações.

Essa organização evita concentrar as regras de negócio, SQL e detalhes HTTP em um único trecho de código, seguindo a orientação apresentada na atividade prática.

## Endpoints implementados

A API disponibiliza as seguintes operações:

| Operação | Método | Endpoint |
|---|---|---|
| Criar chamado | `POST` | `/chamados` |
| Listar chamados | `GET` | `/chamados` |
| Buscar chamado | `GET` | `/chamados/{id}` |
| Atualizar chamado | `PUT` | `/chamados/{id}` |
| Excluir chamado | `DELETE` | `/chamados/{id}` |

### Criar chamado

Para criar um chamado é utilizado:

```http
POST /chamados
```

Exemplo de requisição:

```json
{
    "titulo": "Acesso bloqueado",
    "descricao": "Não consigo acessar o painel de atendimento.",
    "status": "aberto"
}
```

Após a criação, o registro é gravado no banco SQLite e o recurso criado é retornado pela API.

A rota utiliza o código HTTP `201 Created` para indicar que o recurso foi criado com sucesso.

### Listar chamados

Para consultar os chamados persistidos:

```http
GET /chamados
```

A API consulta o banco de dados e retorna os registros existentes.

Dessa maneira, os dados não dependem apenas da memória do processo da aplicação.

### Buscar chamado por identificador

Para consultar um chamado específico:

```http
GET /chamados/{id}
```

Exemplo:

```http
GET /chamados/1
```

Quando o identificador existe, o chamado correspondente é retornado.

Quando o registro não existe, a API retorna:

```http
404 Not Found
```

com uma mensagem indicando que o chamado não foi encontrado.

### Atualizar chamado

Também foi implementada a atualização de registros:

```http
PUT /chamados/{id}
```

A operação permite modificar os dados existentes do chamado, mantendo os campos que não forem informados.

### Excluir chamado

A exclusão é realizada por:

```http
DELETE /chamados/{id}
```

Quando o chamado existe, ele é removido do banco de dados.

Caso o identificador não corresponda a um registro existente, a API retorna `404 Not Found`.

---

# Validações

A aplicação possui validações para garantir que os dados recebidos estejam de acordo com as regras definidas para o recurso.

O campo `titulo` possui tamanho mínimo e máximo definido.

O campo `descricao` também precisa possuir conteúdo válido.

O campo `status` utiliza valores controlados, aceitando somente:

```text
aberto
em_andamento
fechado
```

Além disso, os endpoints que recebem um identificador realizam uma validação para impedir valores menores ou iguais a zero.

Quando ocorre um erro de validação dos dados recebidos, a aplicação possui um tratamento específico que retorna uma resposta HTTP `400`.

A atividade da Semana 4 determina a realização de testes de criação válida, consulta, validação de dados obrigatórios e consulta de identificador inexistente.

---

# Semana 5 - Primeira API de Chamados com FastAPI

Na semana 5 foi construido uma versão executável do back-end do Sistema de Chamados utilizando **FastAPI**, **Uvicorn** e **Pydantic**. Nesta etapa, os dados são gerenciados temporariamente em memória.

---

## Instruções de Execução

1. Crie e ative o seu ambiente virtual Python (`.venv`):
   ```bash
   python -m venv .venv
   # No Windows: .venv\Scripts\activate
   # No Linux/Mac: source .venv/bin/activate
   ```
2. Instale as dependências listadas no projeto (`fastapi` e `uvicorn`):
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor de desenvolvimento com recarregamento automático (`--reload`):
   ```bash
   uvicorn main:app --reload
   ```
4. Abra o navegador e acesse a documentação interativa baseada no Swagger UI:
   **`http://127.0.0.1:8000/docs`**

---

## Endpoints Implementados
- `GET /` — Retorna a mensagem de boas-vindas informando que a API está ativa.
- `GET /chamados` — Lista todos os chamados cadastrados (inicialmente vazia).
- `POST /chamados` — Cadastra um novo chamado validando os campos obrigatórios (*título*, *descrição* e *prioridade*) via Pydantic.
- `GET /chamados/{id}` — Busca um chamado específico pelo seu identificador numérico.
- `GET /chamados/status/{status_chamado}` — *(Desafio Adicional)* Retorna apenas os chamados filtrados pelo status informado.

---

## Evidências dos Testes

| Rota / Teste Realizado |
| :--- |
| **GET /** (API Ativa) |
| **GET /chamados** (Lista Vazia) |
| **POST /chamados** (Sucesso 201 Created) |
| **GET /chamados/{id}** (Busca por ID) |
| **GET /chamados/999** (Erro 404 Not Found) |
| **Validação Automática Pydantic** (Erro de Corpo) |
| **Desafio Adicional** (Filtro por Status) |

---

# Tecnologias utilizadas

O projeto utiliza as seguintes tecnologias:

- Python 3.12
- FastAPI
- Uvicorn
- SQLite
- Pydantic
- Pytest
- HTTPX
- Git
- GitHub
- Swagger/OpenAPI
- HTML
- CSS
- JavaScript

O FastAPI também disponibiliza automaticamente a documentação interativa da API por meio do Swagger.

---

# Estrutura do projeto

A estrutura atual do projeto está organizada da seguinte maneira:

```text
projeto-chamados/
│
├── backend/
│   ├── controllers/
│   ├── data/
│   │   └── chamados.py
│   ├── models/
│   │   └── chamado.py
│   ├── routes/
│   ├── services/
│   │   └── service.py
│   ├── controller.py
│   ├── router.py
│   ├── semana-5-api-chamados
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── main.py
│   └── requirements.txt
│
├── backend/database/
│   ├── database
│   └── 001_criar_tabela_chamados.sql
│
├── docs/
│   ├──evidencias-semana-5/
│   │   ├──1get.png
│   │   ├──2get-chamados.png
│   │   ├──3post-json.png
│   │   ├──3post-resposta.png
│   │   ├──4busca1.png
│   │   ├──4busca2.png
│   │   ├──5busca-outro.png
│   │   ├──6validacao-pydantic1.png
│   │   ├──6validacao-pydantic2.png
│   │   ├──7desafio-adicional.png
│   │   ├──8busca-status-aberto.png
│   │   └──9busca-status-fechado.png
│   ├── API-CHAMADOS.md
│   ├── api-chamados.md
│   ├── contrato-api-chamados.md 
│   ├── diagrama-arquitetura.md
|   └── planejamento-semana-1.md
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── chamados.html
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── tests/
│   ├── test_chamados_get.py
│   ├── test_chamados_post.py
│   └── test_chamados_validacao.py
│
├── .gitignore
└── README.md
```

---

# Instalação

## 1. Clonar o projeto

```powershell
git clone https://github.com/aula-fullstack-univassouras/Projeto-Sistema-Chamados.git
```

Entrar na pasta:

```powershell
cd Projeto-Sistema-Chamados
```

## 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv venv
```

## 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Caso seja necessário alterar a política de execução:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois:

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Instalar as dependências

Com o ambiente virtual ativado:

```powershell
pip install -r requirements.txt
```

---

# Executando a API

Na pasta principal do projeto:

```powershell
python -m uvicorn main:app --reload
```

A API será disponibilizada em:

```text
http://127.0.0.1:8000
```

A documentação interativa do Swagger pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

Também está disponível a documentação alternativa:

```text
http://127.0.0.1:8000/redoc
```

---

# Códigos HTTP

A API utiliza códigos HTTP para representar o resultado das operações.

| Código | Significado |
|---|---|
| `200` | Operação realizada com sucesso |
| `201` | Recurso criado |
| `400` | Requisição inválida |
| `404` | Chamado não encontrado |
| `422` | Erro de validação padrão |

O tratamento específico da aplicação também converte os erros de validação de requisição para uma resposta `400`, fornecendo detalhes sobre os dados inválidos.

---

# Testes

A API pode ser testada utilizando o Swagger disponibilizado pelo FastAPI:

```text
http://127.0.0.1:8000/docs
```

Também podem ser utilizadas ferramentas como:

- Swagger;
- Postman;
- Insomnia;
- PowerShell;
- curl.

A atividade da Semana 4 define como verificações principais a criação de um chamado válido, a consulta da lista, a consulta pelo identificador, a tentativa de criação sem título e a consulta de um identificador inexistente.

O projeto possui arquivos destinados aos testes:

```text
tests/test_chamados_post.py
tests/test_chamados_get.py
tests/test_chamados_validacao.py
```

---

# Exemplos de chamados

## Chamado 1

```json
{
    "titulo": "Computador não liga",
    "descricao": "Computador do setor administrativo não liga.",
    "status": "aberto"
}
```

## Chamado 2

```json
{
    "titulo": "Problema na impressora",
    "descricao": "Impressora não está realizando as impressões.",
    "status": "aberto"
}
```

## Chamado 3

```json
{
    "titulo": "Internet lenta",
    "descricao": "A conexão de internet está apresentando lentidão.",
    "status": "aberto"
}
```

## Chamado 4

```json
{
    "titulo": "Sistema indisponível",
    "descricao": "O sistema interno não está acessível.",
    "status": "em_andamento"
}
```

## Chamado 5

```json
{
    "titulo": "Troca de teclado",
    "descricao": "Teclado do computador apresenta defeito.",
    "status": "fechado"
}
```

---

# Arquitetura

A arquitetura da aplicação pode ser representada da seguinte maneira:

```text
                 CLIENTE
                    │
                    ▼
                 ROUTER
                    │
                    ▼
               CONTROLLER
                    │
                    ▼
                 SERVICE
                    │
                    ▼
             DATA / DATABASE
                    │
                    ▼
                 SQLITE
```

Essa organização permite separar as responsabilidades da aplicação.

O Router é responsável pelo recebimento e direcionamento das requisições HTTP.

O Controller realiza o controle do fluxo das operações.

O Service concentra as regras relacionadas ao funcionamento dos chamados.

A camada Data realiza o acesso efetivo ao banco de dados.

O SQLite mantém os registros persistidos.

Os Models definem a estrutura dos dados e suas respectivas validações.

---

# Documentação

A documentação do projeto está organizada na pasta `docs/`.

Entre os documentos estão:

- `planejamento-semana-1.md` — planejamento inicial, definição do problema, escopo, usuários, requisitos e fluxo principal.
- `diagrama-arquitetura.md` — representação inicial da arquitetura do sistema.
- `contrato-api-chamados.md` — contrato inicial da API de chamados, contendo recursos, endpoints, métodos HTTP, parâmetros, formatos JSON, respostas e códigos de status.
- `API-CHAMADOS.md` — documentação relacionada à API implementada.
- `evidencias-semana-5` — capturas de tela sobre a semana 5

A documentação foi ampliada ao longo do desenvolvimento para acompanhar a evolução do projeto.

---

# Persistência e Semana 4

A implementação da Semana 4 representa uma evolução importante do projeto porque os chamados deixam de depender exclusivamente da memória da aplicação e passam a ser armazenados de maneira persistente.

O roteiro da atividade estabelece como resultado principal que um chamado criado pela API permaneça disponível em uma consulta posterior. Também determina a existência de uma tabela persistente, script ou migração versionada, integração dos endpoints, consultas parametrizadas, validações e documentação das decisões técnicas.

No projeto, essa persistência é realizada utilizando SQLite, com a tabela `chamados` e operações de inserção, consulta, atualização e exclusão.

O script de criação da tabela está versionado no projeto, permitindo que a estrutura do banco possa ser reproduzida por outros integrantes da equipe.

---

# Decisões técnicas

Durante a implementação da Semana 4, foi adotado o SQLite como banco de dados relacional local.

A escolha permite trabalhar com persistência real sem exigir a instalação de um servidor de banco de dados separado ou a utilização de serviços externos. A própria atividade permite a utilização de um banco relacional local e informa que não é necessário utilizar provedor de nuvem, serviço pago ou conta externa.

Também foi adotada a separação entre Router, Controller, Service e Data, evitando concentrar todas as responsabilidades em um único arquivo.

Outra decisão importante foi utilizar consultas parametrizadas no acesso ao SQLite, evitando a concatenação direta de valores recebidos das requisições com comandos SQL.

---
