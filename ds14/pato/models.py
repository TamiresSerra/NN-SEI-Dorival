from django.db import models
from django.contrib.auth.models import AbstractUser

class Pato(models.Model):
    nome = models.CharField(max_length=20)
    especie = models.CharField(max_length=150)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    cor = models.CharField(max_length=200)
    superPoder = models.CharField(max_length=200)
    cagaTorrada = models.BooleanField(null = True, blank=True)

    def __str__(self):
        if self.cagaTorrada:
            return f'{self.nome} caga torradas perfeitas'
        return f'{self.nome}não caga torradas perfeitas'

class DonoPato(AbstractUser):
    nome =models.CharField(max_length=10, blank=True, null=True)
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username