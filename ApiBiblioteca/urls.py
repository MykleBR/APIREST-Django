from django.contrib import admin
from django.urls import path
from estoque.views import LivroListCreateAPIView, LivroRetrieveUpdateDestroyAPIView
from usuario.views import UsuarioListCreateAPIView, UsuarioRetrieveUpdateDestroyAPIView
from estoque.views import gerar_token_usuario

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel de administração do Django
    path('api/token/', gerar_token_usuario, name='gerar_token_usuario'),  # URL para gerar token de autenticação
    path('livros/', LivroListCreateAPIView.as_view(), name='livro-list-create'),  # URL para listar e criar livros
    path('livros/<int:pk>/', LivroRetrieveUpdateDestroyAPIView.as_view(), name='livro-retrieve-update-destroy'),  # URL para recuperar, atualizar e excluir um livro específico
    path('usuarios/', UsuarioListCreateAPIView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyAPIView.as_view(), name='usuario-retrieve-destroy'),
]
