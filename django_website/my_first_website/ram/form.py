from django import forms
from .models import Pokemon
from .models import UserInfo
from django.contrib.auth.models import User


class PokemonForm (forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"



class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')