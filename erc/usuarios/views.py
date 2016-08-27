# -*- coding: utf-8 -*-

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView

from usuarios.forms import UpdateUsuarioForm
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


@method_decorator(login_required, name='dispatch')
class UpdateUsuarioView(UpdateView):

	model = Usuario
	form_class = UpdateUsuarioForm
	template_name="usuario_update.html"
	success_url = "/usuarios/list"

	def form_valid(self, form):
		messages.add_message(
			self.request,
			messages.SUCCESS,
			"Dados do usuário atualizados com sucesso!"
		)
		return super(UpdateUsuarioView, self).form_valid(form)

	# TEST THIS!
	# def get_object(self, *args, **kwargs):
	# 	usuario = super(UpdateUsuarioView, self).get_object(*args, **kwargs)
	# 	cliente = usuario.cliente
	# 	r = self.request.user.usuario_set.all()
	# VERY CONFUSE :(
	# 	if not r or r.first().cliente != cliente:
	# 		raise PermissionDenied() #or Http404
	# 	return usuario


@method_decorator(login_required, name='dispatch')
class CreateUsuarioView(CreateView):

	model = Usuario
	form_class = UpdateUsuarioForm
	template_name="usuario_create.html"
	success_url = "/usuarios/list"

	def form_valid(self, form):
		self.update_perfil(form) # save and set new user infos with the owner infos
		messages.add_message(
			self.request,
			messages.SUCCESS,
			"Usuário criado com sucesso!"
		)
		return super(CreateUsuarioView, self).form_valid(form)

	def update_perfil(self, form):
		user = form.save() # save new user
		owner = Usuario.objects.get(user=self.request.user) # get info the owner
		revenda = owner.revenda
		cliente = owner.cliente
		return Usuario.objects.create(user=user,revenda=revenda,cliente=cliente)