from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListCreateAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste que serão usados em todos os métodos de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        Usuario.objects.create(nome='John Doe', email='johndoe@example.com', telefone='123456789', user=user)

    def setUp(self):
        # Cria um cliente de teste da API
        self.client = APIClient()

        # Cria um usuário de teste
        self.user = User.objects.create_user(username='testuser1', password='testpassword1')

        # Gera o token de autenticação para o usuário de teste
        self.token = Token.objects.create(user=self.user)

    def test_list_usuarios(self):
        # Configura o cliente de teste para usar o token de autenticação
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Faz uma requisição GET para a lista de usuários
        url = reverse('usuario-list-create')
        response = self.client.get(url)

        # Verifica se a resposta tem o status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta da API é igual aos usuários serializados
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        self.assertEqual(response.data, serializer.data)

    