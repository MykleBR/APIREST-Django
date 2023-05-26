from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome