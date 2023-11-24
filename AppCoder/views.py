from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_1.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/app/cursos/listar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoActualizacion(UpdateView):#
    model = Curso
    success_url = "/app/cursos/listar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoEliminar(DeleteView):
    model = Curso
    template_name = "AppCoder/eliminar_curso.html"
    success_url = "/app/cursos/listar"


# Create your views here.
def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Lucas",
        "form": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", contexto)


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47783)
    curso.save()

    return redirect("/app/cursos")  # get


def crear_curso_form(request):
    if request.method == "POST":
        # Crear curso
        curso_formulario = CursoForm(request.POST)
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()
            return redirect("/app/cursos/")

    curso_formulario = CursoForm()
    contexto = {
        "form": curso_formulario
    }

    return render(request, "AppCoder/crear_curso.html", contexto)


def busqueda_camada(request):
    try:

        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        contexto = {
            "cursos": cursos,
            "nombre": "Lucas",
            "form": BusquedaCursoForm(),
        }
        return render(request, "AppCoder/cursos.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/cursos/")

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Lucas"}
    return render(request, 'index.html', contexto)