from django.shortcuts import render


def inicio(request):
    return render(request,'core/inicio.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def informacion(request):
    return render(request,'core/informacion.html')
