from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from usuarios.models import Usuario
from clientes.tests import create_cliente
from revendas.tests import create_revenda

# Create your tests here.

def create_user(username, password):
	"""
	Creates a user with the given `username` and `password`
	"""
	return User.objects.create_user(username=username, password=password)

def create_usuario(user, nome, revenda, cliente=None):
	"""
	Creates a usuario with the given `user` and `nome` and `revenda` and `cliente`
	"""
	return Usuario.objects.create(
		nome_completo=nome,
		revenda=revenda,
		cliente=cliente,
		user=user
	)


class UsuarioViewTests(TestCase):
	def setUp(self):
		""" Every test needs a client """
		self.user = create_user('joe', 'joepassword')
		self.client = Client()
		self.assertTrue(self.client.login(username='joe', password='joepassword'))

	def test_list_view_user_whithout_usuario(self):
		"""
		If user without usuarios exists, 404
		"""
		response = self.client.get(reverse('usuarios:list'))
		self.assertEqual(response.status_code, 404)

	def test_list_view_user_whith_usuario(self):
		"""
		If user with usuarios exists, 200
		"""
		revenda = create_revenda("First One Revenda")
		create_usuario(self.user, "Usuario One", revenda)
		response = self.client.get(reverse('usuarios:list'))
		self.assertEqual(response.status_code, 200)

	def test_list_view_usuario_without_cliente(self):
		"""
		If usuarios list return just one user
		"""
		revenda = create_revenda("First One Revenda")
		usuario = create_usuario(self.user, "Usuario Two", revenda)
		response = self.client.get(reverse('usuarios:list'))
		self.assertQuerysetEqual(
			response.context['usuarios'],
			["<Usuario: Usuario Two>"]
		)

	def test_list_view_usuarios_without_cliente(self):
		"""
		If usuarios list return more than one with same revenda and without cliente
		"""
		revenda = create_revenda("First One Revenda")
		revenda2 = create_revenda("Second One Revenda")

		user2 = create_user('john', 'johnpassword')
		user3 = create_user('jony', 'jonypassword')

		usuario = create_usuario(self.user, "Usuario Three", revenda)
		usuario2 = create_usuario(user2, "Usuario Four", revenda)
		usuario3 = create_usuario(user3, "Usuario Five", revenda2)

		response = self.client.get(reverse('usuarios:list'))

		self.assertQuerysetEqual(
			response.context['usuarios'],
			["<Usuario: Usuario Four>", "<Usuario: Usuario Three>"]
		)

	def test_list_view_usuarios_with_cliente(self):
		"""
		If usuarios list return more than one with same revenda and with cliente
		"""
		revenda = create_revenda("First One Revenda")
		revenda2 = create_revenda("Second One Revenda")

		cliente = create_cliente("First Cliente", revenda)
		cliente2 = create_cliente("Second Cliente", revenda2)

		user2 = create_user('abert', 'abertpassword')
		user3 = create_user('jony', 'jonypassword')

		usuario = create_usuario(self.user, "Usuario Six", revenda)
		usuario2 = create_usuario(user2, "Usuario Seven", revenda, cliente)
		usuario3 = create_usuario(user3, "Usuario Eight", revenda2, cliente2)

		response = self.client.get(reverse('usuarios:list'))

		self.assertQuerysetEqual(
			response.context['usuarios'],
			["<Usuario: Usuario Seven>", "<Usuario: Usuario Six>"]
		)

	def test_list_view_usuario_with_cliente(self):
		"""
		If usuarios list return more than one with same revenda and with cliente
		"""
		revenda = create_revenda("First One Revenda")
		revenda2 = create_revenda("Second One Revenda")

		cliente = create_cliente("First Cliente", revenda)
		cliente2 = create_cliente("Second Cliente", revenda2)

		user2 = create_user('abert', 'abertpassword')
		user3 = create_user('jony', 'jonypassword')

		usuario = create_usuario(self.user, "Usuario Six", revenda, cliente2)
		usuario2 = create_usuario(user2, "Usuario Seven", revenda, cliente)
		usuario3 = create_usuario(user3, "Usuario Eight", revenda2, cliente2)

		response = self.client.get(reverse('usuarios:list'))

		self.assertQuerysetEqual(
			response.context['usuarios'],
			["<Usuario: Usuario Six>"]
		)

		# cliente = create_cliente("First Cliente", revenda)
		# usuario = create_usuario(self.user, "Usuario Two", revenda, cliente)
		# user2 = create_user('john', 'johnpassword')
		# usuario2 = create_usuario(user2, "Usuario One", revenda)
		# revenda2 = create_revenda("First One Revenda")
		# user3 = create_user('jony', 'jonypassword')
		# usuario2 = create_usuario(user3, "Usuario Tree", revenda2, cliente) # BUG