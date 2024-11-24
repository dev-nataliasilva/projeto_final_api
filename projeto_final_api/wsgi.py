"""
Configuração WSGI para o projeto 'projeto_final_api'.

Este arquivo expõe a chamada WSGI como uma variável de nível de módulo chamada ``application``.

Para mais informações sobre este arquivo, consulte:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Importa o módulo 'os' que fornece uma maneira de interagir com o sistema operacional.
import os

# Importa a função 'get_wsgi_application' do Django, que cria a aplicação WSGI.
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE', que aponta para as configurações do projeto Django.
# A variável 'projeto_final_api.settings' informa ao Django qual arquivo de configurações deve ser usado.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final_api.settings')

# Chama a função 'get_wsgi_application', que retorna a aplicação WSGI que será utilizada pelo servidor web.
application = get_wsgi_application()