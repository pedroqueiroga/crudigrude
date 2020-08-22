from django.contrib.auth.models import User
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    nome = models.CharField(max_length=128)
    funcao = models.CharField(max_length=128)
    idade = models.PositiveSmallIntegerField()
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True,
    )

    def __str__(self):
        return self.nome
