"""
Django settings for projeto_final_api project.
"""

from pathlib import Path
import os
from enum import Enum

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = 'django-insecure-yv@x#6%1vaup^vcw6wsp6zcds$an8a+3a^upbo0hm3u_a*eq0r'
DEBUG = False
ALLOWED_HOSTS = [
    'ondesalvei-api-3e0bb38ffd71.herokuapp.com'  # API (própria aplicação) 
    'ondesalvei-afacdb17af64.herokuapp.com',  # Front     
    #'localhost',  # Para desenvolvimento local
    #'127.0.0.1',  # Para desenvolvimento local
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'rest_framework',    
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'projeto_final_api.urls'

WSGI_APPLICATION = 'projeto_final_api.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True