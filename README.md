
# 🚗 **Sistema de Venda de Carros — Django**

Aplicação web desenvolvida com Django para gerenciamento e venda de veículos. O sistema permite cadastrar, visualizar, editar e excluir carros, além de manter um controle automático de estoque e valor total dos veículos disponíveis.

## 📌 Sobre o projeto

Este projeto simula um sistema utilizado por lojas de veículos para gerenciar seu estoque de carros. O foco principal está no desenvolvimento do backend com Django, utilizando templates HTML simples para o frontend.

A aplicação implementa operações completas de CRUD e utiliza recursos do Django como ORM, Class-Based Views e signals para automação de processos.

    ⚙️ Funcionalidades
    🚘 Cadastro de veículos
    📋 Listagem de carros disponíveis
    🔍 Busca por modelo
    ✏️ Edição de informações
    ❌ Exclusão de veículos

## 📊 Controle automático de estoque:

* Quantidade total de carros
* Valor total do inventário

🖥️ ***Interface simples com templates HTML***

## 🛠️ Tecnologias utilizadas

* Python 3
* Django
* SQLite3
* HTML5
* CSS3

## 🗂️ Estrutura do projeto

    carros/
    │
    ├── app/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    │
    ├── cars/
    │   ├── models.py
    │   ├── views.py
    │   ├── signals.py
    │   ├── forms.py
    │   ├── templates/
    │   └── ...
    │
    ├── db.sqlite3
    └── manage.py

## 🚀 Como executar o projeto


# Clone o repositório
git clone 

# Entre na pasta
cd carros

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver

🌐 **Acesso**

    http://127.0.0.1:8000/

📊 **Diferenciais do projeto**

* Uso de signals (post_save e post_delete) para atualização automática do inventário
* Aplicação de boas práticas com Django ORM
* Estrutura organizada e escalável

# 👨‍💻 Autor

# **Leonardo Sales**
