from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do produto', blank=False)

    def __str__(self):
        return self.nome