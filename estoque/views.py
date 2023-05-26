from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

# Define uma função de view usando o decorador @api_view e o método HTTP POST
@api_view(['POST'])
def gerar_token_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Autenticar o usuário com base nas credenciais fornecidas
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Gerar ou obter o token de autenticação
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    

# Define a classe de view 'LivroListCreateAPIView' que herda de 'generics.ListCreateAPIView'
class LivroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação por token
    permission_classes = [IsAuthenticated]  # Exige autenticação
    

# Define a classe de view 'LivroRetrieveUpdateDestroyAPIView' que herda de 'generics.RetrieveUpdateDestroyAPIView'
class LivroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação por token
    permission_classes = [IsAuthenticated]  # Exige autenticação
