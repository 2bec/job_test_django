# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from produtos.models import Produto

# Create your models here.

class Revenda(models.Model):
    razao_social = models.CharField(max_length=200, help_text='Razão Social', blank=False)
    nome_fantasia = models.CharField(max_length=200, help_text='Nome Fantasia', blank=True, null=True)
    cnpj = models.CharField(max_length=20, help_text='CNPJ', blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=30, help_text='Inscrição Estadual', blank=True, null=True)
    email = models.CharField(max_length=150, help_text='Email principal', blank=True, null=True)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.razao_social