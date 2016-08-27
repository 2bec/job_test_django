# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from revendas.views import RevendaDashboardView

urlpatterns = [
    url(r'^dashboard/$', RevendaDashboardView.as_view(), name="dashboard"),
]