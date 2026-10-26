# F1 Data Tracker — Bootcamp II

Sistema interativo em Python para cadastrar e consultar informações de corridas, pilotos, equipes e resultados da Fórmula 1.

O projeto utiliza armazenamento em JSON e pode ser executado localmente ou em um contêiner Docker. O Docker Compose facilita a construção e a inicialização do ambiente.

## Objetivos

- Organizar dados de corridas, pilotos e equipes.
- Registrar resultados e consultar classificações.
- Validar informações inseridas pelo usuário.
- Persistir os dados em arquivo JSON.
- Facilitar a execução do sistema com Docker e Docker Compose.

## Funcionalidades

- Cadastro de corridas, com nome, circuito, data e temporada.
- Cadastro de equipes e pilotos.
- Registro e consulta de resultados.
- Classificação de pilotos e equipes por pontuação.
- Validação dos dados informados.
- Persistência em arquivo JSON.
- Testes automatizados com `unittest`.
- Execução em contêiner Docker.
- Orquestração com Docker Compose.

## Tecnologias

- Python
- JSON
- `unittest`
- Docker
- Docker Compose
- Git e GitHub

## Estrutura do projeto

```text
F1-DATA-TRACKER/
├── data/
│   └── f1_data.json
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── storage.py
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

O arquivo `data/f1_data.json` armazena os dados salvos pelo sistema.

## Pré-requisitos

Para execução local, é necessário Python instalado.

Para execução em contêiner, é necessário Docker Desktop em execução, com suporte ao Docker Compose.

## Execução local

Na raiz do projeto, execute:

```powershell
py -m src.main
```

## Testes automatizados

Para executar os testes na raiz do projeto:

```powershell
py -m unittest src.test_main -v
```

Os testes verificam regras de cadastro, validações e ordenação de classificações.

## Execução com Docker

### 1. Construir a imagem

```powershell
docker build -t f1-data-tracker .
```

### 2. Executar o sistema

