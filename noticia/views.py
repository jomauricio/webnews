from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Autor
from .forms import AutorForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='home.html'

# def home(request):
#     return render(request, 'home.html')

class AutorListView(ListView):
    model=Autor
    template_name='listar.html'
    context_object_name='autores'
    ordering='-nome'


# def listar(request):
#     autores = Autor.objects.all().order_by('-nome')
#     return render(request, 'listar.html', {'autores':autores})

class AutorDetailView(DetailView):
    model=Autor
    template_name='detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'


# def detalhar(request, id):
#     autor = Autor.objects.get(id=id)
#     return render(request, 'detalhar.html', {'autor':autor})


class AutorCreateView(CreateView):
    model=Autor
    template_name='cadastrar.html'
    form_class=AutorForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar')



# def cadastrar(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Autor cadastrado com sucesso!")
#             return redirect("listar")
#     else:
#          form = AutorForm()
#          return render(request, 'cadastrar.html', {'form': form})


class AutorUpdateView(UpdateView):
    model=Autor
    template_name='atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar')


# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES, instance=autor)
#         if form.is_valid():
#             form.save()
#             return redirect("atualizar", id=id)
#         else:
#             return render(request, 'atualizar.html', {'form': form})
#     else:
#          return render(request, 'atualizar.html', {'form': form})

class AutorDeleteView(DeleteView):
    model=Autor
    template_name='autor_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar')


# def deletar(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('listar')
