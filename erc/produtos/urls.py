# -*- coding: utf-8 -*-

from django.conf.urls import url

from produtos.views import ProdutoDetailView

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)/$', ProdutoDetailView.as_view(), name='detail'),
]