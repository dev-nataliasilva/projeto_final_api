"""
Django settings for projeto_final_api project.
"""

# Importação de módulos necessários
from pathlib import Path
import os
from enum import Enum

# Definindo o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de arquivos estáticos
STATIC_URL = '/static/'  # URL para acessar os arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório onde os arquivos estáticos serão coletados para produção

# Chave secreta do Django (não deve ser compartilhada publicamente)
SECRET_KEY = 'django-insecure-yv@x#6%1vaup^vcw6wsp6zcds$an8a+3a^upbo0hm3u_a*eq0r'

# Modo de depuração do Django
DEBUG = False  # Quando em produção, o DEBUG deve ser False

# Lista de hosts permitidos para a aplicação (domínios onde a aplicação pode ser acessada)
ALLOWED_HOSTS = [
    'ondesalvei-api-3e0bb38ffd71.herokuapp.com',  # API (própria aplicação) 
    'ondesalvei-afacdb17af64.herokuapp.com',  # Front-end
    #'localhost',  # Para desenvolvimento local
    #'127.0.0.1',  # Para desenvolvimento local
]

# Aplicações instaladas no Django
INSTALLED_APPS = [
    'django.contrib.auth',  # Sistema de autenticação
    'django.contrib.contenttypes',  # Conteúdos genéricos de tipo
    'django.contrib.sessions',  # Sessões de usuário
    'rest_framework',  # Django REST Framework para criação de APIs
    'corsheaders',  # Permite configurar CORS (Cross-Origin Resource Sharing)
]

# Middleware utilizado pela aplicação
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Middleware para suportar CORS
    'django.middleware.security.SecurityMiddleware',  # Middleware de segurança
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware para servir arquivos estáticos de forma eficiente
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware comum
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticação
]

# Configuração de roteamento
ROOT_URLCONF = 'projeto_final_api.urls'  # Arquivo de URLs principal

# Configuração do WSGI (interface de gateway de servidor web)
WSGI_APPLICATION = 'projeto_final_api.wsgi.application'

# Configuração de banco de dados (comentada, já que não está usando banco de dados)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # Usando banco SQLite por padrão
#         'NAME': BASE_DIR / 'db.sqlite3',  # Caminho para o banco de dados
#     }
# }

# Validadores de senhas (não configurados para esta aplicação)
AUTH_PASSWORD_VALIDATORS = []

# Configurações de idioma e fuso horário
LANGUAGE_CODE = 'en-us'  # Código do idioma (Inglês dos Estados Unidos)
TIME_ZONE = 'UTC'  # Fuso horário (Tempo Universal Coordenado)
USE_I18N = True  # Ativa suporte a internacionalização
USE_TZ = True  # Ativa suporte a fusos horários

# Define o tipo de campo auto-incrementado para os modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de CORS
CORS_ALLOW_ALL_ORIGINS = True  # Permite requisições de qualquer origem (para facilitar durante o desenvolvimento)

# Configuração de arquivos estáticos usando o WhiteNoise para produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'