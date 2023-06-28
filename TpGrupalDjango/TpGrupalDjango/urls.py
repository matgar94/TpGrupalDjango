"""
URL configuration for TpGrupalDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TpGrupalDjango.views import home
from TpGrupalDjango.views import viajes
from TpGrupalDjango.views import recomendaciones
from TpGrupalDjango.views import contacto
from TpGrupalDjango.views import nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('viajes/', viajes),
    path('recomendaciones/', recomendaciones),
    path('nosotros/', nosotros),
    path('contacto/', contacto),
]
