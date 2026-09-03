# Sistema de Chamados

## Integrantes

1. Ângelo Mateus - 202323348
2. Esequias Ferraz De Andrade - 202411248
3. Felipe Ramos Da Silva - 202221884
4. Thiago Marsol Almeida Baião - 202323232
5. Juberto Junior Marques Coutinho - 202321179
6. Wallace Gustavo Da Silva - 202411248

## Objetivo

Criar uma aplicação web para registrar e acompanhar chamados de suporte técnico em um só lugar, substituindo o uso de planilhas e mensagens espalhadas.

# API de Chamados

API REST desenvolvida com Python e FastAPI para gerenciamento de chamados.

## Tecnologias

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Pytest

## Organização do projeto

```text
projeto-chamados/
├── backend/
│   ├── controllers/
│   ├── data/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
├── database/
├── docs/
│   ├── planejamento-semana-1.md
│   ├── diagrama-arquitetura.md
|   └── contrato-api-chamados.md
├── tests/
├── frontend/
└── README.md
```

## Documentação

A documentação do projeto está organizada na pasta `docs/`:

* `planejamento-semana-1.md` — planejamento inicial, definição do problema, escopo, usuários, requisitos e fluxo principal.
* `diagrama-arquitetura.md` — representação inicial da arquitetura do sistema.
* `contrato-api-chamados.md` — contrato inicial da API de chamados, contendo os recursos, endpoints, métodos HTTP, parâmetros, formatos JSON, respostas e principais códigos de status.

## Desenvolvimento

- **Semana 1:** Planejamento inicial do sistema, definição do problema, escopo, usuários, requisitos, fluxo e arquitetura.

- **Semana 2:** Definição do contrato inicial da API, com atributos, endpoints, métodos HTTP, respostas e cenários de erro.

- **Semana 3:** Início da implementação da API, com criação das rotas, controladores e serviços, além dos primeiros endpoints para consulta e cadastro de chamados e validação dos dados.