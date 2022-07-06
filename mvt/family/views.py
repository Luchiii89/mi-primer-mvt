'''n este archivo donde vamos a crear las vistas/pantallas que se enviarán al browser'''

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from family.models import Relative


def welcome(request):
	return HttpResponse("Hola Bienvenido a mi primer MVT")


# def mostrar_mi_template(request):
#     return render(request,"family/index.html")
#mi-primer-mvt\mvt\family\templates\family\index.html


def listRelatives(request):
    context = {
        "relatives" : Relative.objects.all(),
    }
    return render(request,"family/relatives.html",context)