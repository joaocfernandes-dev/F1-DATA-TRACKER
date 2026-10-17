# F1 Data Tracker 🏎️

Sistema de gerenciamento e análise de dados da Fórmula 1, desenvolvido em Python como projeto do Bootcamp II.

## 🎯 Objetivo

Organizar informações de corridas, pilotos, equipes e resultados, permitindo consultar classificações e pontuações de forma simples por meio de um menu interativo no terminal.

## ⚙️ Funcionalidades

- Cadastro de corridas, com nome, circuito, data e temporada.
- Cadastro de equipes.
- Cadastro de pilotos, com número e equipe.
- Registro de resultados por corrida.
- Consulta de corridas e resultados.
- Classificação de pilotos por pontuação acumulada.
- Classificação de equipes por pontuação acumulada.
- Validação de campos obrigatórios e valores numéricos.
- Persistência de dados em arquivo JSON, por meio do módulo de armazenamento.

## 🛠️ Tecnologias

- Python 3
- JSON para armazenamento local
- Git e GitHub para versionamento do código

## 📁 Estrutura do projeto

```text
F1-DATA-TRACKER/
├── data/
│   └── f1_data.json
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── storage.py
├── .gitignore
└── README.md
```

O arquivo `data/f1_data.json` é criado durante a execução quando os dados são salvos.

## ▶️ Como executar

1. Instale o Python 3.
2. Clone o repositório ou abra a pasta do projeto.
3. No terminal, entre na pasta raiz `F1-DATA-TRACKER`.
4. Execute:

```bash
py -m src.main
```
## 🧪 Testes automatizados

O projeto utiliza a biblioteca `unittest`, incluída no Python, para verificar regras importantes do sistema.

Os testes cobrem:

- Cadastro de equipes.
- Prevenção de equipes duplicadas.
- Validação de campos obrigatórios.
- Rejeição de pontuações negativas.
- Ordenação da classificação de pilotos por pontuação.

Para executar os testes na raiz do projeto, utilize:

```bash
py -m unittest src.test_main -v
```

Os testes utilizam entradas simuladas para verificar o comportamento das funções sem exigir interação manual com o menu.

## 📊 Como utilizar

Ao iniciar, o sistema apresenta um menu interativo para cadastrar e consultar informações.

Cadastre uma equipe antes de associá-la a um piloto. Cadastre uma corrida e um piloto antes de registrar um resultado. Os resultados registrados são utilizados para calcular as classificações.

## 💾 Armazenamento

Os dados são armazenados localmente em `data/f1_data.json`, permitindo que sejam recuperados em execuções posteriores, desde que o salvamento tenha ocorrido corretamente.

## 🔮 Próximas melhorias

- Aprimorar os testes automatizados.
- Melhorar o tratamento de erros.
- Validar formatos de data.
- Desenvolver uma interface visual.
- Avaliar a utilização de Docker em uma etapa futura.

## 👨‍💻 Projeto acadêmico

Desenvolvido para a entrega intermediária do Bootcamp II.
