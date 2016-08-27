# -*- coding: utf-8 -*-

from django.conf.urls import url

from usuarios.views import ListaUsuariosView

urlpatterns = [
    url(r'^list/$', ListaUsuariosView.as_view(), name="list"),
]