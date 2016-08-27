# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Usuario


class UpdateUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('user','revenda','cliente')
		widgets = {
			'user': forms.TextInput(attrs={'readonly':'readonly'}),
			'revenda': forms.TextInput(attrs={'readonly':'readonly'}),
			'cliente': forms.TextInput(attrs={'readonly':'readonly'})
		}