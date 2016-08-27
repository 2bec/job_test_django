# -*- coding: utf-8 -*-

from django.conf.urls import url

from clientes.views import ListaClientesView, UpdateClienteView, CreateClienteView

urlpatterns = [
    url(r'^list/$', ListaClientesView.as_view(), name="list"),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateClienteView.as_view(), name='update'),
    url(r'^create/$', CreateClienteView.as_view(), name='create'),
]