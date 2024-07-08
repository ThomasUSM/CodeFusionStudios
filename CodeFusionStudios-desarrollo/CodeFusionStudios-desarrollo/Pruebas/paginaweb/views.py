from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def crear_cuenta(request):
    return render(request, 'crear_cuenta.html')

def recuperacion_cuenta(request):
    return render(request, 'recuperacion_cuenta.html')