# Importe o módulo 'serializers' do Django Rest Framework
from rest_framework import serializers
# Importe o modelo 'Livro' do seu aplicativo
from .models import Livro

# Define a classe 'LivroSerializer' que herda de 'ModelSerializer'
class LivroSerializer(serializers.ModelSerializer):
    # Classe Meta é usada para fornecer metadados à classe do serializador
    class Meta:
        # Especifica o modelo a ser serializado, que é o 'Livro'
        model = Livro
        # Especifica quais campos do modelo devem ser incluídos na serialização
        # Aqui, o '__all__' significa incluir todos os campos do modelo
        fields = '__all__'

