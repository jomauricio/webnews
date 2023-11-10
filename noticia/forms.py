from django.forms import ModelForm
from .models import Autor, Noticia

class AutorForm(ModelForm):
   
    class Meta:
        model=Autor
        fields='__all__'

class NoticiaForm(ModelForm):
   
    class Meta:
        model=Noticia
        fields='__all__'