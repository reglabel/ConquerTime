"""site_bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from app_LPB.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('cronometro/<int:id>/',cronometro, name="cronometro"),
    path('relatorioTarefa/',relatorioTarefa, name="relatorioTarefa"),
    
    path('cadastroTarefa/', cadastroTarefa, name="cadastroTarefa"),
    path('excluirTarefa/<int:id>/', excluirTarefa, name="excluirTarefa"),
    #path('editarTarefa/<int:id>/', editarTarefa, name="editarTarefa"),
    #path('listaTarefa/<int:id>/', listaTarefa, name="listaTarefa"),
    #path('cadastroCategoria/', cadastroCategoria, name="cadastroCategoria"),
    #path('excluirCategoria/<int:id>/', excluirCategoria, name="excluirCategoria"),
    #path('editarCategoria/<int:id>/', editarCategoria, name="editarCategoria"),
    #path('listaCategoria/<int:id>/', listaCategoria, name="listaCategoria"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
