from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Departamento(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    nome = models.CharField(max_length=128, null=True)
    funcao = models.CharField(max_length=128, null=True)
    idade = models.PositiveSmallIntegerField(null=True)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True,
    )

    def __str__(self):
        return self.nome


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Funcionario.objects.create(user=instance)
    instance.funcionario.save()
