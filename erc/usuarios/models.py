# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from revendas.models import Revenda

# Create your models here.

class Usuario(models.Model):
    user = models.ForeignKey(User)
    revenda = models.ForeignKey(Revenda)
    nome_completo = models.CharField(max_length=200, help_text='Nome completo', blank=True)

    class Meta:
    	unique_together = (('user', 'revenda')) # make sense o.0

    def __str__(self):
        return self.nome_completo