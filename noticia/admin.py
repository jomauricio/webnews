from django.contrib import admin
from .models import Autor, Noticia

# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nome", "email"]
    search_fields = ["nome"]

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "data_pub", "autor"]
    autocomplete_fields = ["autor"]
