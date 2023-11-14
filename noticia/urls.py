from django.contrib import admin
from django.urls import path
from .views import AutorListView, AutorDetailView, AutorCreateView, AutorUpdateView, AutorDeleteView, NoticiaListView, NoticiaDetailView, NoticiaCreateView, NoticiaDeleteView, NoticiaUpdateView

urlpatterns = [
    path('autor', AutorListView.as_view(), name='listar-autor'),
    path('autor/<int:id>', AutorDetailView.as_view(), name='detalhar-autor'),
    path('autor/cadastrar/', AutorCreateView.as_view(), name='cadastrar-autor'),
    path('autor/atualizar/<int:id>', AutorUpdateView.as_view(), name='atualizar-autor'),
    path('autor/deletar/<int:id>', AutorDeleteView.as_view(), name='deletar-autor'),
    path('noticia', NoticiaListView.as_view(), name='listar-noticia'),
    path('noticia/<int:pk>', NoticiaDetailView.as_view(), name='detalhar-noticia'),
    path('noticia/cadastrar/', NoticiaCreateView.as_view(), name='cadastrar-noticia'),
    path('noticia/atualizar/<int:pk>', NoticiaUpdateView.as_view(), name='atualizar-noticia'),
    path('noticia/deletar/<int:pk>', NoticiaDeleteView.as_view(), name='deletar-noticia'),
]