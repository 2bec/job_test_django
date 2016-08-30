#Desenvolvimento
Iniciei o desenvolvimento direto codificando, depois de ler o cenário, fui primeiro desenvolvendo os models depois urls, views, forms e templates.

Meu primeiro modelo foi esse, para revenda:

```
class Revenda(models.Model):
    cnpj = models.CharField(
        max_length=20, 
        help_text='CNPJ', 
        blank=True, 
        null=True)
    inscricao_estadual = models.CharField(
        max_length=30, 
        help_text='Inscrição Estadual', 
        blank=True, 
        null=True)
    email = models.CharField(
        max_length=150, 
        help_text='Email principal', 
        blank=True, 
        null=True)
    clientes = models.ManyToManyField(
        Cliente, 
        blank=True)
    produtos = models.ManyToManyField(
        Produto, 
        blank=True)
    usuarios = models.ManyToManyField(User)
```

O modelo de cliente ficou apenas com informações básicas:

```
class Cliente(models.Model):
    nome_completo = models.CharField(
        max_length=200, 
        help_text='Nome completo', 
        blank=False)
    cpf = models.CharField(
        max_length=11, 
        help_text='CPF', 
        blank=True, 
        null=True)
    email = models.CharField(
        max_length=150, 
        help_text='Email principal', 
        blank=True, 
        null=True)
```

Mas quando cheguei nas views percebi que esses modelos não eram os mais adequados, pois um cliente não deveria pertencer a mais de uma revenda, muito menos  os usuários devem pertencer a mais de uma revenda ou cliente. Resolvi então ler sobre models [nas páginas do django](https://docs.djangoproject.com/en/1.10/ref/models/), me aprofundei nos campos [many-to-many](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.ManyToManyField), [many-to-one](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.ForeignKey), [one-to-one](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.OneToOneField) e cheguei a esses novos modelos:


```
class Usuario(models.Model):
    user = models.ForeignKey(User)
    revenda = models.ForeignKey(Revenda)
    cliente = models.ForeignKey(
        Cliente, 
        blank=True, 
        null=True)

    class Meta:
    	unique_together = (('user', 'revenda'), ('user', 'cliente'))

class Revenda(models.Model):
    razao_social = models.CharField(
        max_length=200, 
        help_text='Razão Social', 
        blank=False)
    nome_fantasia = models.CharField(
        max_length=200, 
        help_text='Nome Fantasia', 
        blank=True, 
        null=True)
    cnpj = models.CharField(
        max_length=20, 
        help_text='CNPJ', 
        blank=True, 
        null=True)
    inscricao_estadual = models.CharField(
        max_length=30, 
        help_text='Inscrição Estadual', 
        blank=True, 
        null=True)
    email = models.CharField(
        max_length=150, 
        help_text='Email principal', 
        blank=True, 
        null=True)
    produtos = models.ManyToManyField(
        Produto, 
        blank=True)

class Cliente(models.Model):
    revenda = models.ForeignKey(Revenda) # ManyToOneField
    nome_completo = models.CharField(
        max_length=200, 
        help_text='Nome completo', 
        blank=False)
    cpf = models.CharField(
        max_length=11, 
        help_text='CPF', 
        blank=True, 
        null=True)
    email = models.CharField(
        max_length=150, 
        help_text='Email principal', 
        blank=True, 
        null=True)
    produtos = models.ManyToManyField(
        Produto, 
        blank=True)
```

Sei que ainda poderia se melhorado, como incluir [tradução](https://docs.djangoproject.com/pt-br/1.10/topics/i18n/translation/) nos help_text, nos campos [ManyToMany utilizar through](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.ManyToManyField.through) para controlar a tabela intermediária e incluir novos campos, talvez até no model Usuarios incluir OneToOneField para user ao invés de [unique_together](https://docs.djangoproject.com/en/1.10/ref/models/options/#unique-together) e incluir as [permissões diretamente nos models](https://docs.djangoproject.com/en/1.10/ref/models/options/#permissions) para utilizar nas views com [decorators](https://docs.djangoproject.com/pt-br/1.10/topics/http/decorators/), por exemplo.

No model Usuario deixei as permissões para o model do django User gerenciar, as permissões serão usadas para controlar o que cada Usuario pode fazer na revenda ou no cliente, como: listar, criar, apagar ou editar revendas, clientes, produtos, etc. Será necessário criar um [manager customizado](https://docs.djangoproject.com/pt-br/1.10/topics/db/managers/#custom-managers-and-model-inheritance).

Com os modelos definidos fui escrever as views. Utilizei [class-based views](https://docs.djangoproject.com/pt-br/1.10/topics/class-based-views/) para codificar menos, assim somente sobrescrevo alguns métodos caso precise. Listar, criar, modificar e apagar, além de um dashboard. Essa parte não foi tão penosa, mas aproveitei para reler sobre class-based views, [based views](https://docs.djangoproject.com/el/1.10/ref/class-based-views/base/) e [decorators](https://docs.djangoproject.com/pt-br/1.10/topics/class-based-views/intro/#decorating-the-class). Utilizei o decorator login_required para controlar o acesso, em uma primeira versão utilizei login_required direto nas urls, mas achei melhor manter nas views, então utilizei o method_decorator para controlar o dispatch (TODO: [ler mais sobre](https://docs.djangoproject.com/pt-br/1.10/topics/class-based-views/intro/#decorating-the-class))

Conforme fui escrevendo as views já desenvolvi os forms, pensando na produção dos templates depois. Evitei incluir styles e html nos forms ou nas views para deixar esse controle somente para os templates mesmo. Por isso escolhi utilizar [django-bootstratp-form](https://github.com/tzangms/django-bootstrap-form).

Para os formulários retornarem somente os produtos disponíveis para cada revenda ou cliente, sobrescrevi o método [get_form_kwargs](https://docs.djangoproject.com/pt-br/1.10/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form_kwargs) para passar um argumento (user) para [__init__](https://docs.djangoproject.com/pt-br/1.10/topics/forms/modelforms/#changing-the-queryset), onde sobrescrevi para retornar somente os produtos de acordo com a revenda ou cliente do usuário. [ TODO: Preciso melhorar o seguinte self.request.user.usuario_set.all().first().id. Como? Fazendo a alteração para [one-to-one](https://docs.djangoproject.com/pt-br/1.10/topics/db/examples/one_to_one/) consigo eliminar usuario_set.all().first().id e incluir algo mais fácil de ler e entender. ]

Para as views dos Usuários foi necessário sobrescrever o método save para que gravasse as permissões “certas” para aquele novo usuário. Depois através do [method_decorator](https://docs.djangoproject.com/pt-br/1.10/topics/class-based-views/intro/#decorating-the-class) com [permission_required](https://docs.djangoproject.com/pt-br/1.10/topics/auth/default/#the-permission-required-decorator) controlamos as permissões para cada view da aplicação. Por exemplo, na view create um cliente ou usuário só pode ter acesso caso seu usuário tenha essa permissão.

Os templates foram simples, acho que não cheguei na melhor solução mas funciona. Criei um tema base com bootstrap e parti daí para o restante deles.

Para os testes resolvi partir para os testes unitarios, foi uma ótima oportunidade para aprender mais sobre os testes, coisa que não tenho muito domínio. Estou lendo muita coisa sobre [unittest](https://docs.python.org/3/library/unittest.html#module-unittest), [TestCase](https://docs.djangoproject.com/pt-br/1.10/topics/testing/tools/#django.test.TestCase) e [selemiun](http://www.seleniumhq.org/). Também me interessei por [TDD](http://chimera.labs.oreilly.com/books/1234000000754/pt01.html) e outras metodologias que estou estudando novamente na faculdade também.  