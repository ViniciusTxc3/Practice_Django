from django.urls import path

from . import views

# Precisa apontar a raiz da URLconf para o módulo polls.urls (mysitte/urls.py)
urlpatterns = [
    path('', views.index, name='index'),
]