from rest_framework import generics
from .models import Emprestimo
from .serializers import EmprestimoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

# Classe de view para listar e criar empréstimos
class EmprestimoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação por token
    permission_classes = [IsAuthenticated]  # Exige autenticação

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Classe de view para recuperar, atualizar e excluir empréstimos individuais
class EmprestimoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação por token
    permission_classes = [IsAuthenticated]  # Exige autenticação
