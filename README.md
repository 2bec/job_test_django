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
Para saber mais sobre o desenvolvimento acesse o [arquivo de desenvolvimento](https://github.com/2bec/job_test_django/blob/master/Desenvolvimento.md), criei para documentar a experiência e gravar refências.

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
Acesse o diretório do repositório ` cd job_test_django ` e então instale os requisitos pelo arquivo ` pip install -r requirements.txt `

# Setup em 4 passos
Acesse o diretório da aplicação ` cd job_test_django/erc `, inicie o banco (se for o primeiro acesso) ` python manage.py migrate `, crie um usuário adiministrativo ` python manage.py createsuperuser ` e inicie o servidor ` python manage.py runserver 8080 `.

Agora você pode fazer login no admin http://127.0.0.1:8080/admin/, crie uma revenda e crie um usuário para essa revenda. Opicionalmente você pode relacionar um cliente para o mesmo usuário. Se tiver cliente, o usuário é um cliente senão ele é um usuário da revenda. Acesse http://127.0.0.1:8080/ faça o login com o usuário da revenda para acessar o dashboard.

# Use shell
```
>>> from django.contrib.auth.models import User
>>> u = User.objects.create_user('revenda','revenda@email.com','password1234')
>>> u
<User: revenda>
>>> from revendas.models import Revenda
>>> r = Revenda.objects.create(razao_social="Nova Revenda")
>>> r
<Revenda: Nova Revenda>
>>> from usuarios.models import Usuario
>>> usuario = Usuario.objects.create(user=u, revenda=r)
>>> usuario
<Usuario: >
>>> usuario.nome_completo = "Manoel Augusto"
>>> usuario.save()
>>> usuario
<Usuario: Manoel Augusto>
>>> usuario.__dict__
{'cliente_id': None, 'user_id': 3, '_revenda_cache': <Revenda: Nova Revenda>, '_user_cache': <User: revenda>, '_state': <django.db.models.base.ModelState object at 0x7f5983ad0fd0>, '_cliente_cache': None, 'nome_completo': 'Manoel Augusto', 'id': 2, 'revenda_id': 2}
>>> usuario.revenda
<Revenda: Nova Revenda>
>>> usuario.revenda.produtos.all()
<QuerySet []>
>>> from produtos.models import Produto
>>> Produto.objects.all()
<QuerySet [<Produto: Produto A>, <Produto: Produto B>, <Produto: Produto C>]>
>>> p = Produto.objects.get(pk=2)
>>> p
<Produto: Produto B>
>>> r.produtos.add(p)
>>> r.produtos.all()
<QuerySet [<Produto: Produto B>]>
>>> usuario.revenda.produtos.all()
<QuerySet [<Produto: Produto B>]>
>>> from clientes.models import Cliente
>>> c = Cliente.objects.create(revenda=r,nome_completo='Cliente Norte')
>>> c
<Cliente: Cliente Norte>
>>> c.usuario_set.all()
<QuerySet []>
>>> u2 = User.objects.create_user('cliente','cliente@email.com','password1234')
>>> usuario2 = Usuario.objects.create(user=u2, revenda=r, cliente=c)
>>> usuario2
<Usuario: >
>>> usuario2.nome_completo = 'Leonardo W'
>>> usuario2.save()
>>> usuario2
<Usuario: Leonardo W>
>>> usuario2.cliente.produtos.all()
<QuerySet []>
>>> usuario2.revenda.produtos.all()
<QuerySet [<Produto: Produto B>]>
>>> c.produtos.add(Produto.objects.get(pk=2))
>>> usuario2.revenda.cliente_set.all().first().produtos.all()
<QuerySet [<Produto: Produto B>]>
>>> c.produtos.add(Produto.objects.get(pk=3)) # BUG
>>> usuario2.revenda.cliente_set.all().first().produtos.all()
<QuerySet [<Produto: Produto B>, <Produto: Produto C>]>
>>> usuario2.revenda.cliente_set.all()
<QuerySet [<Cliente: Cliente Norte>]>
```