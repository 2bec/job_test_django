# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from revendas.models import Revenda
from produtos.models import Produto

# Create your models here.

class Cliente(models.Model):
    revenda = models.ForeignKey(Revenda) # ManyToOneField
    nome_completo = models.CharField(max_length=200, help_text='Nome completo', blank=False)
    cpf = models.CharField(max_length=11, help_text='CPF', blank=True, null=True)
    email = models.CharField(max_length=150, help_text='Email principal', blank=True, null=True)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.nome_completo