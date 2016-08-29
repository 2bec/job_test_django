from django.test import TestCase

from revendas.models import Revenda

# Create your tests here.

def create_revenda(nome):
	"""
	Creates an revenda with the given `razao_social`
	"""
	return Revenda.objects.create(razao_social=nome)