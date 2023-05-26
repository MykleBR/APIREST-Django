from django.db import models

# Define a classe 'Livro' que herda de 'models.Model'
class Livro(models.Model):
    # Define o campo 'titulo' como um CharField com no máximo 100 caracteres
    titulo = models.CharField(max_length=100)
    # Define o campo 'autor' como um CharField com no máximo 100 caracteres
    autor = models.CharField(max_length=100)
    # Define o campo 'ano_publicacao' como um IntegerField
    ano_publicacao = models.IntegerField()

    # Sobrescreva o método '__str__' para retornar uma representação em string do objeto
    def __str__(self):
        return self.titulo