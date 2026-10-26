# F1 Data Tracker — Bootcamp II

Sistema interativo em Python para cadastrar e consultar informações de corridas, pilotos, equipes e resultados da Fórmula 1.

O projeto utiliza armazenamento em JSON e pode ser executado localmente ou em contêineres Docker. O Docker Compose facilita a construção e a execução interativa da aplicação.

## 1. Objetivos

- Organizar dados de corridas, pilotos e equipes.
- Registrar resultados e consultar classificações.
- Validar informações inseridas pelo usuário.
- Persistir os dados em arquivo JSON.
- Facilitar a execução da aplicação em diferentes ambientes por meio do Docker.
- Utilizar Docker Compose para orquestrar a execução interativa do sistema.

## 2. Funcionalidades

- Cadastro de corridas, com nome, circuito, data e temporada.
- Cadastro de equipes.
- Cadastro de pilotos, com número e equipe.
- Registro e consulta de resultados.
- Classificação de pilotos por pontuação acumulada.
- Classificação de equipes por pontuação acumulada.
- Validação de campos obrigatórios e valores numéricos.
- Persistência dos dados em arquivo JSON.
- Testes automatizados com `unittest`.
- Execução por meio de Docker e Docker Compose.

## 3. Tecnologias utilizadas

- **Python 3:** linguagem de programação da aplicação.
- **JSON:** armazenamento local dos dados.
- **unittest:** execução de testes automatizados.
- **Docker:** construção de imagens e execução em contêineres.
- **Docker Compose:** configuração e execução do serviço.
- **Git e GitHub:** versionamento e hospedagem do código-fonte.

## 4. Estrutura do projeto

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

O arquivo `data/f1_data.json` armazena os dados salvos pela aplicação. A pasta `docs/` contém o planejamento lógico elaborado nas etapas anteriores.

## 5. Pré-requisitos

Para executar o projeto, é necessário ter:

- Python instalado, para execução local.
- Docker Desktop instalado e em execução.
- Docker Compose disponível por meio do comando `docker compose`.
- Git, caso deseje clonar o repositório.

## 6. Execução local

Na raiz do projeto, execute:

```powershell
py -m src.main
```

A aplicação apresenta um menu interativo para cadastrar e consultar as informações.

## 7. Testes automatizados

Para executar os testes automatizados na raiz do projeto, utilize:

```powershell
py -m unittest src.test_main -v
```

Os testes verificam regras de cadastro, validações e ordenação de classificações.

## 8. Conteinerização com Docker

### 8.1. Construir a imagem

Na raiz do projeto, execute o comando:

```bash
docker build -t f1-data-tracker .
```

Esse comando constrói uma imagem Docker chamada `f1-data-tracker` a partir do `Dockerfile`.

### 8.2. Executar o contêiner

Para iniciar a aplicação de maneira interativa, utilize o comando exigido nesta etapa:

```bash
docker run -it f1-data-tracker
```

O parâmetro `-it` permite que o usuário interaja com o menu pelo terminal.

**Execução alternativa com persistência dos dados no computador:**

No PowerShell, utilize:

```powershell
docker run --rm -it -v "${PWD}/data:/app/data" f1-data-tracker
```

Esse comando compartilha a pasta `data` local com `/app/data` no contêiner, permitindo manter os dados salvos no computador mesmo após o encerramento do contêiner.

## 9. Orquestração com Docker Compose

O arquivo `docker-compose.yml` define o serviço `tasktracker`, a construção da imagem, o terminal interativo e o compartilhamento da pasta de dados.

Para executar a aplicação por meio do Docker Compose, utilize:

```bash
docker compose run --build tasktracker
```

Esse comando constrói a imagem, quando necessário, e inicia o serviço `tasktracker` de maneira interativa.

A configuração inclui `stdin_open: true` e `tty: true`, permitindo que a aplicação continue recebendo entradas do usuário pelo terminal.

## 10. Persistência dos dados

Os dados da aplicação são armazenados no arquivo `data/f1_data.json`.

Quando a execução utiliza o volume configurado no Docker Compose ou o comando alternativo com `-v`, a pasta de dados local é compartilhada com o contêiner.

Para validar a persistência, cadastre e salve um registro, encerre a aplicação e inicie uma nova execução. Em seguida, consulte o registro para verificar se continua disponível.

## 11. Planejamento e rastreabilidade

O planejamento lógico elaborado na etapa inicial está disponível em:

`docs/planejamento_logico.pdf`

A estrutura do projeto preserva a documentação e o código desenvolvidos nas etapas anteriores, acrescentando os artefatos de conteinerização e orquestração necessários para a fase final.

## 12. Conclusão

O F1 Data Tracker reúne funcionalidades de cadastro, consulta, classificação e armazenamento de dados relacionados à Fórmula 1.

Nesta etapa final, o projeto foi preparado para execução por meio de Docker e Docker Compose, mantendo a interação pelo terminal e documentando os comandos necessários para construção e execução da aplicação.

A conteinerização facilita a reprodução do ambiente de execução, enquanto o Docker Compose centraliza as configurações necessárias para iniciar o serviço.

## 13. Repositório

**GitHub:**  
https://github.com/joaocfernandes-dev/F1-DATA-TRACKER

**Projeto:** F1 Data Tracker — Bootcamp II

**Entrega:** Fase final — Conteinerização, Orquestração e Deploy do TaskTracker.
