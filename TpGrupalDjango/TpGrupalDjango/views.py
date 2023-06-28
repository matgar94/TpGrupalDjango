from django.shortcuts import render 

def home(request):
    return render(request, 'index.html')
def viajes(request):
    return render(request, 'viajes.html')
def recomendaciones(request):
    return render(request, 'recomendaciones.html')
def contacto(request):
    return render(request, 'contacto.html')
def nosotros(request):
    return render(request, 'nosotros.html')