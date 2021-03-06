"""erc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^revendas/', include("revendas.urls", namespace='revendas')),
    url(r'^clientes/', include("clientes.urls", namespace='clientes')),
    url(r'^usuarios/', include("usuarios.urls", namespace='usuarios')),
    url(r'^produtos/', include("produtos.urls", namespace='produtos')),
    url(r'^faq/', auth_views.login, name="faq"),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, name="logout"),
]
