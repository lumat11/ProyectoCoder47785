from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()
    contexto = {"curso": curso}

    return render(reques, 'index.html', contexto)


def show_html(request):
    curso = Curso.objects.firts()
    contexto = {"curso": curso}
    return render(request,  'index.html', contexto)
