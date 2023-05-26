from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.authtoken.models import Token

class GerarTokenUsuarioViewTest(TestCase):
    def test_gerar_token_usuario(self):
        # Cria um usuário de teste
        username = 'testuser'
        password = 'testpassword'
        User.objects.create_user(username=username, password=password)

        # Cria um cliente de teste da API
        client = APIClient()

        # Faz uma requisição POST para gerar um token de autenticação
        response = client.post(reverse('gerar_token_usuario'), {'username': username, 'password': password}, format='json')

        # Verifica se a resposta tem o status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta da API contém um token
        self.assertIn('token', response.data)

        # Obtém o token gerado
        token = response.data['token']

        # Configura o cliente de teste para usar o token de autenticação nas próximas requisições
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)


class LivroListCreateAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste que serão usados em todos os métodos de teste
        Livro.objects.create(titulo='Livro Teste', autor='Autor Teste', ano_publicacao=2021)

    def setUp(self):
        # Cria um usuário de teste
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        # Gera o token de autenticação para o usuário de teste
        self.token = Token.objects.create(user=self.user)

    def test_livro_list(self):
        # Cria um cliente de teste da API
        client = APIClient()

        # Configura o cliente de teste para usar o token de autenticação
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Faz uma requisição GET para a lista de livros
        response = client.get(reverse('livro-list-create'))

        # Verifica se a resposta tem o status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta da API é igual aos livros serializados
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_livro_create(self):
        # Cria um cliente de teste da API
        client = APIClient()

        # Configura o cliente de teste para usar o token de autenticação
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Dados do livro a ser criado
        data = {'titulo': 'Novo Livro', 'autor': 'Autor Teste', 'ano_publicacao': 2022}

        # Faz uma requisição POST para criar um novo livro
        response = client.post(reverse('livro-list-create'), data, format='json')

        # Verifica se a resposta tem o status HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o livro foi criado corretamente no banco de dados
        livro = Livro.objects.get(pk=response.data['id'])
        self.assertEqual(livro.titulo, data['titulo'])
        self.assertEqual(livro.autor, data['autor'])
        self.assertEqual(livro.ano_publicacao, data['ano_publicacao'])