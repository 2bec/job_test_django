# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Usuario


class UpdateUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('cliente',)

class CreateUsuarioForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email',)