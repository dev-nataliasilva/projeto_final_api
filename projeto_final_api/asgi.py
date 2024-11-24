"""
ASGI config for projeto_final_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Importa a biblioteca os, que fornece uma maneira de interagir com o sistema operacional
import os

# Importa a função get_asgi_application do Django para configurar o ASGI
from django.core.asgi import get_asgi_application

# Define a variável de ambiente DJANGO_SETTINGS_MODULE para apontar para o arquivo de configurações
# Isso é necessário para que o Django saiba qual arquivo de configurações utilizar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final_api.settings')

# A variável 'application' é definida como a instância ASGI do Django
# Essa variável será usada pelo servidor para interagir com a aplicação Django usando ASGI
application = get_asgi_application()