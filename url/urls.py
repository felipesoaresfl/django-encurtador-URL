from django.urls import path

from . import views

# insere a url curta na rota
urlpatterns = [
    path("<url_inserida>", views.acha_minha_url),
    path('', views.pagina_inicial),
]
