__author__ = 'Андрей'
from django import forms

class URLForm(forms.Form): #форма для ввода URL
    url = forms.URLField(label='URL')