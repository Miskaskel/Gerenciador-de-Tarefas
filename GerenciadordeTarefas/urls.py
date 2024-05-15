"""
URL configuration for GerenciadordeTarefas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_Cadastro import views

urlpatterns = [
    path('Cadastrar/', views.Cadastro,name='Cadastro'),
    path('Tarefas/',views.Cadastrar,name='Cadastrar'),
    path('home/', views.tarefa,name='Tarefa'),
    path('Delete/<int:id_tarefa>', views.ExcluirTarefa,name='ExcluirTarefa'),
    path('Editar/<int:id_tarefa>', views.EditarTarefa, name='EditarTarefa'),
    path('Editar/<int:id_tarefa>/Update', views.Editar, name='Editar')
]
