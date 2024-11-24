# Importa 'path' para definir rotas e 'include' para incluir outras configurações de URLs
from django.urls import path, include

# Definindo a lista de URLs para o projeto
urlpatterns = [
    # A URL base 'api/' é mapeada para as URLs definidas em 'myapp.urls'.
    # Isso permite que todas as URLs definidas dentro de 'myapp.urls' sejam acessíveis com o prefixo 'api/'.
    path('api/', include('myapp.urls')),
]