from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from .models import User


class UserCreationForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm):
        model = User
        fields = (
            'name',
            'email',
        )


class UserChangeForm(DjangoUserChangeForm):

    class Meta(DjangoUserChangeForm):
        model = User
        fields = (
            'name',
            'email',
            'password',
        )