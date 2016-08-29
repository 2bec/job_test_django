from django.test import TestCase

from clientes.models import Cliente

# Create your tests here.

def create_cliente(nome, revenda):
	"""
	Creates an cliente with the given `revenda` and `nome_completo`
	"""
	return Cliente.objects.create(nome_completo=nome, revenda=revenda)