from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Autor, Noticia
from .forms import AutorForm, NoticiaForm, RegistrationForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()[:5]
        context["autores"] = Autor.objects.all()[:5]
        
        return context


# def home(request):
#     noticias = Noticia.objects.all()
#     return render(request, 'home.html', {"noticias": noticias})

class AutorListView(LoginRequiredMixin, ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'
    ordering='-nome'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get("q")
        
        if search:
            self.autores = Autor.objects.filter(nome__icontains=search)
        else:
            self.autores = Autor.objects.all()

        return self.autores


# def listar(request):
#     autores = Autor.objects.all().order_by('-nome')
#     return render(request, 'listar.html', {'autores':autores})

class AutorDetailView(LoginRequiredMixin, DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'


# def detalhar(request, id):
#     autor = Autor.objects.get(id=id)
#     return render(request, 'detalhar.html', {'autor':autor})


class AutorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm
    permission_required = 'noticia.add_autor'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar-autor')



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


class AutorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'
    permission_required = 'noticia.change_autor'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar-autor')


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

class AutorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Autor
    template_name='autor/autor_confirm_delete.html'
    pk_url_kwarg='id'
    permission_required = 'noticia.delete_autor'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar-autor')


# def deletar(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('listar')


class NoticiaListView(LoginRequiredMixin, ListView):
    model=Noticia
    template_name='noticia/listar.html'
    context_object_name='noticias'
    ordering='-titulo'
    paginate_by = 5


class NoticiaDetailView(LoginRequiredMixin, DetailView):
    model=Noticia
    template_name='noticia/detalhar.html'
    context_object_name='noticia'


class NoticiaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Noticia
    template_name='noticia/cadastrar.html'
    form_class=NoticiaForm
    permission_required = 'noticia.pode_publicar'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia cadastrada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model=Noticia
    template_name='noticia/atualizar.html'
    form_class=NoticiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia atualizada com sucesso!")
        return reverse('listar-noticia')
    

class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model=Noticia
    template_name='noticia/noticia_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia deletada com sucesso!")
        return reverse('listar-noticia')
    

class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')

