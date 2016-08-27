# -*- coding: utf-8 -*-

from django import forms

from clientes.models import Cliente

class UpdateClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ('nome_completo','cpf','email', 'produtos')
		# or exclude ('revenda',)