from django.shortcuts import render 

def home(request):
    return render(request, 'core/index.html')
def viajes(request):
    return render(request, 'core/viajes.html')
def recomendaciones(request):
    return render(request, 'core/recomendaciones.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def nosotros(request):
    return render(request, 'core/nosotros.html')