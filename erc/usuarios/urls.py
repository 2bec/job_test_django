# -*- coding: utf-8 -*-

from django.conf.urls import url

from usuarios.views import ListaUsuariosView, UpdateUsuarioView, CreateUsuarioView

urlpatterns = [
    url(r'^list/$', ListaUsuariosView.as_view(), name="list"),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateUsuarioView.as_view(), name='update'),
    url(r'^create/$', CreateUsuarioView.as_view(), name='create'),
]