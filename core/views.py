from django.shortcuts import render

# Create your views here.
def saludo(request):
    contexto = {
        'mensaje': 'Hola Mundo!'
    }
    return render(request, "core/index.html", contexto)