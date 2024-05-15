from django.db import models

# Create your models here.

class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    Descricao = models.TextField(max_length=255)
    Prioridade = models.IntegerField()
    Categoria = models.TextField(max_length=255)