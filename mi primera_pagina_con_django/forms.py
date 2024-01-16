from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categorias', 'publicacion']

class BusquedaForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100)
