# To-do list

Aplicação web de gerenciamento de tarefas desenvolvida como projeto de estudo para colocar em prática conceitos de desenvolvimento web com Python e Flask.

O projeto permite que usuários criem uma conta, façam login e gerenciem suas próprias tarefas através de uma interface simples.

## Funcionalidades

- Cadastro de usuários
- Login e logout
- Sistema de sessões
- Criação de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Conclusão de tarefas
- Filtro de tarefas por status
- Separação das tarefas por usuário
- Armazenamento das informações em banco de dados
- Validação de acesso às tarefas de cada usuário

## Tecnologias utilizadas

- Backend
- Python
- Flask
- Flask-SQLAlchemy
- Banco de dados
- SQLite
- Frontend
- HTML5
- CSS3

## Estrutura do projeto

site_to_do_list/
│
├── codigo/
│   ├── app.py
│   ├── config.py
│   ├── extentions.py
│   ├── models.py
│   │
│   ├── routes/
│   │   ├── usuarios.py
│   │   └── tarefas.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── imagens/
│   │
│   └── templates/
│       ├── cadastro.html
│       ├── login.html
│       ├── tarefas.html
│       └── adicionar_tarefa.html
│
├── instance/
│   └── site_to_do_list.db
│
├── LICENSE
└── README.md

## Como executar

1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
2. Entre na pasta do projeto
cd site_to_do_list
3. Instale as dependências
pip install flask flask-sqlalchemy
4. Execute a aplicação
python codigo/app.py

Depois, acesse no navegador:

http://127.0.0.1:5000

## Objetivo do projeto

Desenvolvido principalmente para aprender e praticar desenvolvimento web, unindo conhecimentos de Python, Flask, banco de dados, HTML e CSS em uma aplicação funcional.

Mais do que criar uma lista de tarefas, o objetivo foi entender como diferentes partes de uma aplicação web trabalham juntas:
