# Importa a classe 'AppConfig' do módulo 'django.apps'.
# A classe 'AppConfig' é usada para configurar a aplicação Django.
from django.apps import AppConfig

# Define a classe 'MyappConfig', que herda de 'AppConfig'.
# Esta classe configura a aplicação 'myapp'.
class MyappConfig(AppConfig):
    # Define o campo padrão para o tipo de campo de chave primária.
    # 'BigAutoField' é um campo de auto-incremento, adequado para grandes volumes de dados.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # O nome da aplicação Django, que é o nome do pacote ou módulo da aplicação.
    # Esse nome é usado em várias configurações no Django.
    name = 'myapp'