from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Emprestimo
from .serializers import EmprestimoSerializer
from rest_framework.authtoken.models import Token
from datetime import date
from .models import Livro
from usuario.models import Usuario

class EmprestimoListCreateAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste que serão usados em todos os métodos de teste
        user = User.objects.create_user(username='testuser', password='testpassword')
        usuario = Usuario.objects.create(user=user)
        livro = Livro.objects.create(titulo='Livro Teste', autor='Autor Teste', ano_publicacao=2021)
        
        # Cria um empréstimo de teste
        emprestimo = Emprestimo.objects.create(usuario=usuario, livro=livro, data_inicio=date.today(), data_devolucao=date.today())

    def setUp(self):
        # Obtém o usuário de teste existente
        self.user = User.objects.get(username='testuser')
        self.usuario = Usuario.objects.get(user=self.user)

        # Gera o token de autenticação para o usuário de teste
        self.token = Token.objects.create(user=self.user)

    def test_emprestimo_list(self):
        # Cria um cliente de teste da API
        client = APIClient()

        # Configura o cliente de teste para usar o token de autenticação
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Faz uma requisição GET para a lista de empréstimos
        response = client.get(reverse('emprestimo-list-create'))

        # Verifica se a resposta tem o status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta da API é igual aos empréstimos serializados
        emprestimos = Emprestimo.objects.all()
        serializer = EmprestimoSerializer(emprestimos, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_emprestimo_create(self):
        # Cria um cliente de teste da API
        client = APIClient()

        # Configura o cliente de teste para usar o token de autenticação
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Dados do empréstimo a ser criado
        data = {'usuario': self.usuario.id, 'livro': 1, 'data_inicio': date.today(), 'data_devolucao': date.today()}

        # Faz uma requisição POST para criar um novo empréstimo
        response = client.post(reverse('emprestimo-list-create'), data, format='json')

        # Verifica se a resposta tem o status HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o empréstimo foi criado corretamente
        emprestimo = Emprestimo.objects.get(id=response.data['id'])
        self.assertEqual(emprestimo.usuario, self.usuario)
        self.assertEqual(emprestimo.livro.id, 1)
        self.assertEqual(emprestimo.data_inicio, date.today())
        self.assertEqual(emprestimo.data_devolucao, date.today())