# -*- coding: utf-8 -*-

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from usuarios.models import Usuario

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ListaUsuariosView(ListView):

	model = Usuario
	template_name = "usuario_list.html"
	context_object_name = "usuarios"

	def get_queryset(self):
		"""Returns Usarios that belong to the current cliente"""
		usuario = get_object_or_404(Usuario, user=self.request.user) # get usuario
		cliente = usuario.cliente # get specified cliente to usuario
		return Usuario.objects.filter(cliente=cliente)