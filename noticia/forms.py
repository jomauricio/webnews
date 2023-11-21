from django.forms import ModelForm, EmailField
from .models import Autor, Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AutorForm(ModelForm):
   
    class Meta:
        model=Autor
        fields='__all__'

class NoticiaForm(ModelForm):
   
    class Meta:
        model=Noticia
        fields='__all__'

class RegistrationForm(UserCreationForm):

    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'email', 'password1', 'password2' ]
