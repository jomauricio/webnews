from django.shortcuts import render
from .models import Autor
# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar(request):
    autores = Autor.objects.all().order_by('-nome')
    return render(request, 'listar.html', {'autores':autores})

def detalhar(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, 'detalhar.html', {'autor':autor})
