from django.shortcuts import render,redirect
from .models import Tarefa
from .forms import TarefaForm

def home(request):    
    Tarefas = {
        'Tarefas': Tarefa.objects.all().order_by("Prioridade")
    }

    return render(request,'Tarefas\home.html',Tarefas)

def Cadastrar(request):
    novaTarefa = Tarefa()
    novaTarefa.nome = request.POST.get('NomeTarefa')
    novaTarefa.Descricao = request.POST.get('DescriTarefa')
    novaTarefa.Prioridade = request.POST.get('PrioridadeTarefa')
    novaTarefa.Categoria = request.POST.get('CategoriaTarefa')
    novaTarefa.save()    
    url_executar = "/home/"

    return redirect(url_executar)    

def Cadastro(request):

    return render(request, 'Tarefas\Cadastro.html')
   


def tarefa(request):    
    
    Tarefas = {
        'Tarefas': Tarefa.objects.all().order_by("Prioridade")
    }

    return render(request,'Tarefas\home.html',Tarefas)


def ExcluirTarefa(request, id_tarefa):    
    dataTarefa = Tarefa.objects.get(id_tarefa=id_tarefa)
    dataTarefa.delete()

    return redirect(tarefa)

def EditarTarefa(request, id_tarefa):
    data = Tarefa.objects.get(id_tarefa=id_tarefa)

    return render(request, 'Tarefas\Editar.html', {'data':data})

def Editar(request, id_tarefa):
    nome = request.POST.get('NomeTarefa')
    Descricao = request.POST.get('DescriTarefa')
    Prioridade = request.POST.get('PrioridadeTarefa')
    Categoria = request.POST.get('CategoriaTarefa')
    Taf = Tarefa.objects.get(id_tarefa=id_tarefa)
    Taf.nome = nome
    Taf.Descricao = Descricao
    Taf.Prioridade = Prioridade
    Taf.Categoria = Categoria
    Taf.save()
    url_executar = "/home/"
    return redirect(url_executar)


    
