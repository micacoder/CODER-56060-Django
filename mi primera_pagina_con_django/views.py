from django.shortcuts import render
from .models import Libro
from .forms import LibroForm, BusquedaForm

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'nombre_de_tu_aplicacion/libro_list.html', {'libros': libros})

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
    else:
        form = LibroForm()
    return render(request, 'nombre_de_tu_aplicacion/libro_edit.html', {'form': form})

def buscar_libro(request):
    if request.method == "POST":
        form = BusquedaForm(request.POST)
        if form.is_valid():
            titulo_buscar = form.cleaned_data['titulo']
            libros = Libro.objects.filter(titulo__icontains=titulo_buscar)
    else:
        form = BusquedaForm()
        libros = Libro.objects.all()
    return render(request, 'nombre_de_tu_aplicacion/buscar_libro.html', {'form': form, 'libros': libros})
