# pessoas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pessoa
from .forms import PessoaForm

def home(request):
    return render(request, 'home.html')

def list_pessoas(request):
    pessoas = Pessoa.objects.all()  # Obtém todas as pessoas
    return render(request, 'list_pessoas.html', {'pessoas': pessoas})

def add_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'add_pessoa.html', {'form': form})

def edit_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('list_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'edit_pessoa.html', {'form': form, 'pessoa': pessoa})

def delete_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa.delete()
    return redirect('list_pessoas')
