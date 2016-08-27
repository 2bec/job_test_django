# job_test_django

# Apresentação
O objetivo desta aplicação é demonstrar conhecimentos em Django. Não utilizar essa aplicação em ambiente de produção, não é um produto acabado.
Esta aplicação foi desenvolvida para gerenciar a criação das revendas, clientes, usuários e fazer o controle de permissões de acesso aos produtos pelos clientes.

###Empresa:
- A Empresa pode cadastrar revendedores, clientes e usuários.
- Pode associar qualquer um dos produtos para as revendas ou para seus clientes.

###Revenda:
- As revendas podem cadastrar clientes.
- As revendas só podem cadastrar usuários para os seus clientes.
- As revendas só podem associar produtos aos seus clientes.
- Os produtos disponíveis para associar, são aqueles que a Empresa disponibilizou para a revenda.
- A revenda só pode acessar as telas de produtos que possui.

###Cliente:
- O cliente só pode acessar as telas de produtos que possui.

# Desenvolvimento
Para saber mais sobre o desenvolvimento acesse o arquivo [desenvolvimento], criei para documentar a experiência e gravar refências.

# Requirements
- Django 1.10+
- Python 2.7+, support 3
- Virtualenv
- Django-bootstrap-form

```
pip install virtualenv

```

# Enviroment
Primeiro crie um diretório para trabalhar ` mkdir test_django ` e acesse ` cd test_django `.

# Virtualenv
Agora crie uma virtualenv ` virtualenv djangoenv ` depois ative sua nova virtualenv ` source djangoenv/bin/active `.

# Git clone
` git clone git@github.com:2bec/job_test_django.git `

# Install requirements.txt
` pip install -r requirements.txt `

# Setup em 4 passos
Acesse o diretório da aplicação ` cd job_test_django/erc `, inicie o banco ` python manage.py migrate `, crie um usuário adiministrativo ` python manage.py createsuperuser ` e inicie o servidor ` python manage.py runserver 8080 `.

Agora você deve fazer login no admin http://127.0.0.1:8080/admin/, criar uma revenda e criar um usuário responsável por essa revenda. Opicionalmente você pode relacionar um cliente ao mesmo usuário.