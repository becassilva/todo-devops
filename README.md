# Todo DevOps

Aplicação simples de gerenciamento de tarefas desenvolvida em Python como parte da atividade prática da disciplina de DevOps e Integração Contínua da Uninter.

## Descrição do projeto

O projeto consiste em uma aplicação de linha de comando para gerenciamento de tarefas. A aplicação permite cadastrar tarefas, listar as tarefas cadastradas e indicar se uma tarefa foi concluída ou permanece pendente.

Além da aplicação, o projeto foi estruturado utilizando práticas de DevOps, incluindo versionamento com Git e GitHub, desenvolvimento baseado em branches, Pull Requests, testes automatizados com Pytest e containerização utilizando Docker.

## Objetivo

Demonstrar, na prática, a aplicação de conceitos e ferramentas de DevOps e Integração Contínua em um projeto de software, buscando organização, automação e melhoria contínua.

## Tecnologias utilizadas

- Python 3.13
- Git
- GitHub
- Pytest
- Docker
- GitHub Actions

## Estrutura do projeto

```text
todo-devops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
└── README.md
```

## Requisitos

Para executar o projeto localmente, é necessário ter instalado:

- Python 3.13 ou superior
- Git

Para executar utilizando Docker:

- Docker Desktop

## Instalação

Clone o repositório:

```bash
git clone https://github.com/becassilva/todo-devops.git
```

Entre na pasta do projeto:

```bash
cd todo-devops
```

A aplicação principal não possui dependências externas obrigatórias.

Para executar os testes automatizados, instale o Pytest:

```bash
python -m pip install pytest
```

## Execução local

Para executar a aplicação localmente, utilize:

```bash
python src/main.py
```

A aplicação apresentará as tarefas cadastradas e seus respectivos status.

Exemplo de saída:

```text
Tarefas:
1. Estudar DevOps - Concluída
2. Configurar Docker - Pendente
```

## Testes automatizados

Os testes automatizados foram implementados utilizando Pytest.

Para executar os testes, utilize:

```bash
python -m pytest
```

O resultado esperado é a aprovação dos testes automatizados da aplicação.

## Docker

A aplicação também pode ser executada utilizando Docker.

Para construir a imagem Docker:

```bash
docker build -t todo-devops .
```

Para executar o container:

```bash
docker run --name todo-devops-container todo-devops:latest
```

A aplicação será executada dentro do container Docker.

A utilização de containers permite padronizar o ambiente de execução da aplicação, reduzindo diferenças entre ambientes e facilitando a implantação e a execução do projeto.

## Versionamento

O projeto utiliza Git para controle de versão e GitHub para armazenamento remoto do código-fonte.

As principais branches utilizadas são:

- `main`: branch principal e estável do projeto;
- `development`: branch destinada à integração das funcionalidades;
- `feature/tarefas`: branch destinada ao desenvolvimento das funcionalidades relacionadas às tarefas.

As alterações são organizadas por meio de commits descritivos e Pull Requests.

## Pull Requests

As funcionalidades são desenvolvidas em branches específicas e posteriormente integradas por meio de Pull Requests.

Esse processo permite revisar as alterações antes da integração com a branch `development`, contribuindo para a organização e a qualidade do código.

## Integração Contínua

O projeto utiliza uma pipeline de Integração Contínua utilizando GitHub Actions.

A pipeline é executada automaticamente quando novas alterações são enviadas ao repositório ou quando um Pull Request é criado ou atualizado nas branches configuradas.

Durante a execução, a pipeline realiza o download do código, configura o ambiente Python, instala o Pytest e executa os testes automatizados do projeto.

A automação permite identificar problemas no código antes da integração das alterações, contribuindo para a qualidade e a confiabilidade do processo de desenvolvimento.

## Organização do projeto

O projeto utiliza recursos do GitHub para facilitar a organização e o acompanhamento do desenvolvimento, incluindo:

- Issues;
- Labels;
- Milestones;
- Projects;
- Wiki;
- Pull Requests;
- Insights.

Esses recursos permitem organizar tarefas, acompanhar o desenvolvimento e visualizar informações relacionadas ao projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.