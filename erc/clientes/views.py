# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView
from django.utils.decorators import method_decorator

from clientes.models import Cliente
from clientes.forms import UpdateClienteForm

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ListaClientesView(ListView):

	model = Cliente
	template_name = "cliente_list.html"
	context_object_name = "clientes"

	def get_queryset(self):
		"""Returns Clientes that belong to the current revenda"""
		usuario = get_object_or_404(Usuario, user=self.request.user) # get usuario
		revenda = usuario.revenda # get specified revenda to usuario
		return Cliente.objects.filter(revenda=revenda)


@method_decorator(login_required, name='dispatch')
class UpdateClienteView(UpdateView):

	model = Cliente
	form_class = UpdateClienteForm
	template_name="cliente_update.html"
	success_url = "/clientes/list"

	def form_valid(self, form):
		messages.add_message(
			self.request,
			messages.SUCCESS,
			"Dados do cliente atualizados com sucesso!"
		)
		return super(UpdateClienteView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CreateClienteView(CreateView):
	
	model = Cliente
	form_class = UpdateClienteForm
	template_name="cliente_create.html"
	success_url = "/clientes/list"

	def form_valid(self, form):
		self.update_perfil(form) # put revenda on save form
		messages.add_message(
			self.request,
			messages.SUCCESS,
			"Cliente criado com sucesso!"
		)
		return super(CreateClienteView, self).form_valid(form)

	def update_perfil(self, form):
		usuario = get_object_or_404(Usuario, user=self.request.user) # get usuario
		form.instance.revenda = usuario.revenda # define revenda for cliente from the usuario