# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from produtos.models import Produto
from usuarios.models import Usuario

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProdutoDetailView(DetailView):

    model = Produto
    template_name = "produto_detail.html"

    def get_queryset(self):
		usuario = get_object_or_404(Usuario, user=self.request.user) # get usuario
		if usuario.cliente:
			return usuario.cliente.produtos.all()
		elif usuario.revenda:
			return usuario.revenda.produtos.all()