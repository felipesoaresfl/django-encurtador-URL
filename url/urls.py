from django.contrib import admin
from django.urls import path

from . import views

#insere a url curta na rota 
urlpatterns = [
    path("ache/<url_curta>", views.acha_minha_url),
    path('', views.pagina_inicial),
]
