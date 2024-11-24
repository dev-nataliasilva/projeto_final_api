# Importação das funções e classes necessárias do Django para roteamento de URLs
from django.urls import path  # Função para mapear URLs para views
from .views import receive_color_objects  # Importa a view que será associada à URL

# A lista de URLs da aplicação
urlpatterns = [
    # Define a URL padrão 'receive-colors/' que será associada à view 'receive_color_objects'
    path('receive-colors/', receive_color_objects, name='receive_color_objects'),
]
