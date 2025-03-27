from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'mensaje': 'Hola Mundo! Bienvenido a la guía de Django.'
    }
    return render(request, "guia/index.html", context)