
# F1 Data Tracker — Sistema de Gerenciamento e Análise de Dados da Fórmula 1

## 1. Descrição do Projeto

O F1 Data Tracker é uma aplicação desenvolvida em Python para organizar e consultar informações relacionadas à Fórmula 1.

O projeto tem como objetivo facilitar o gerenciamento de dados de corridas, pilotos, equipes e resultados, permitindo acompanhar classificações e pontuações ao longo de uma temporada.

Esta aplicação faz parte do Bootcamp II do curso de Engenharia de Dados e Machine Learning e dá continuidade ao planejamento desenvolvido na entrega inicial.

## 2. Objetivos

- Cadastrar corridas e seus dados principais.
- Cadastrar pilotos e associá-los às respectivas equipes.
- Cadastrar equipes participantes.
- Registrar os resultados das corridas.
- Consultar corridas e resultados cadastrados.
- Calcular a classificação dos pilotos por pontuação.
- Consultar a pontuação acumulada das equipes.
- Aplicar validações para garantir a consistência dos dados.

## 3. Funcionalidades

A aplicação contará com um menu interativo no terminal, permitindo ao usuário selecionar as operações disponíveis.

As funcionalidades previstas são:

1. Cadastrar corrida.
2. Cadastrar piloto.
3. Cadastrar equipe.
4. Registrar resultado.
5. Consultar corridas.
6. Consultar resultados.
7. Consultar classificação dos pilotos.
8. Consultar pontuação das equipes.
9. Sair da aplicação.

## 4. Tecnologias Utilizadas

- Python 3 — desenvolvimento da aplicação.
- Git — controle de versão do código.
- GitHub — hospedagem do repositório e acompanhamento do histórico de desenvolvimento.
- Docker — tecnologia prevista para a etapa final do projeto.

## 5. Estrutura do Projeto

```text
F1-DATA-TRACKER/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## 6. Requisitos

- Python 3 instalado.
- Git instalado para versionamento do projeto.

## 7. Como Executar

No terminal, acesse a pasta raiz do projeto e execute:

```bash
python src/main.py
```

No Windows, caso o comando `python` não funcione, tente:

```powershell
py src/main.py
```

## 8. Regras de Negócio

- Corridas devem possuir nome, circuito, data e temporada.
- Pilotos devem possuir nome, número e equipe.
- Pilotos devem estar associados a equipes cadastradas.
- Resultados devem estar associados a corridas e pilotos existentes.
- A pontuação deve ser numérica e válida.
- A classificação dos pilotos deve considerar a soma dos pontos registrados.
- A pontuação das equipes deve considerar os pontos obtidos por seus pilotos.

## 9. Desenvolvimento

O projeto está sendo desenvolvido de maneira incremental:

- **Fase 1 — Planejamento:** definição do problema, objetivos, funcionalidades, regras de negócio e arquitetura inicial.
- **Fase 2 — Implementação:** desenvolvimento da aplicação em Python, validação das regras de negócio e versionamento com Git e GitHub.
- **Fase 3 — Evolução:** preparação da aplicação para execução em Docker, realização de testes e deploy, conforme os requisitos da etapa final.

## 10. Autor

João Coelho

Curso: Engenharia de Dados e Machine Learning  
Disciplina: Bootcamp II  
Turma/Polo: B
