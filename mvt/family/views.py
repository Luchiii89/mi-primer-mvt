'''n este archivo donde vamos a crear las vistas/pantallas que se enviarán al browser'''

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from family.models import Relative


def welcome(request):
	return HttpResponse("Hola Bienvenido a mi primer MVT")


def listRelatives(request):
    context = {
        "relatives" : Relative.objects.all(),
    }
    return render(request,"family/relatives.html",context)

