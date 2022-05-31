from turtle import position
from django import forms
from django.forms import ModelForm
from app_1.models import Players


class CategoryForm(forms.Form):
    category = forms.CharField(max_length=40, min_length=3, label='Nombre de la categoria')
    n_category = forms.IntegerField(label='Numero de la categoria')


class PlayersForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    position = forms.CharField(max_length=40, label='Posición')


class WinnersForm(forms.Form):
    name_couple = forms.CharField(max_length=40, label='Nombre de la pareja')