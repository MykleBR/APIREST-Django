from django.db import models
from usuario.models import Usuario
from estoque.models import Livro


class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_devolucao = models.DateField()
