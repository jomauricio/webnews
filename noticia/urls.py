from django.contrib import admin
from django.urls import path
from .views import detalhar, listar


urlpatterns = [
    path('', listar, name='listar'),
    path('<int:id>', detalhar, name='detalhar')
]