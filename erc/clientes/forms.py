# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import get_object_or_404

from clientes.models import Cliente
from produtos.models import Produto
from usuarios.models import Usuario

class UpdateClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ('nome_completo','cpf','email', 'produtos',)
		# or exclude ('revenda',)

	def __init__(self, user, *args, **kwargs):
		# user = kwargs.pop('user', None)
		super(UpdateClienteForm, self).__init__(*args, **kwargs)
		usuario = get_object_or_404(Usuario, id=user) # get usuario
		if usuario.cliente: # get produtos for cliente
			self.fields['produtos'].queryset = Produto.objects.filter(cliente=usuario.cliente)
		elif usuario.revenda: # get produtos for revenda
			self.fields['produtos'].queryset = Produto.objects.filter(revenda=usuario.revenda)