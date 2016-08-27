# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View

from usuarios.models import Usuario

# Create your views here.

@method_decorator(login_required, name='dispatch')
class RevendaDashboardView(View):

	template_name="revenda_dashboard.html"

	def get(self, request):
		usuario = get_object_or_404(Usuario, user=self.request.user)
		revenda = usuario.revenda
		cliente = usuario.cliente
		context = {'revenda': revenda, 'cliente': cliente, 'usuario': usuario}
		return render(request, self.template_name, context)

