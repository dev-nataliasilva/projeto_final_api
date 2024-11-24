#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Esta linha indica que o script deve ser executado com o interpretador Python.

import os
import sys

def main():
    """Run administrative tasks."""
    # A função 'main' é o ponto de entrada do script.
    # Ela é responsável por configurar o ambiente e executar as tarefas administrativas do Django.

    # Define a variável de ambiente DJANGO_SETTINGS_MODULE para apontar para o arquivo de configurações.
    # Isso é necessário para que o Django saiba qual arquivo de configurações usar durante a execução dos comandos.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final_api.settings')

    try:
        # Tenta importar a função execute_from_command_line do Django, que permite executar comandos administrativos.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Caso a importação falhe (se o Django não estiver instalado ou configurado corretamente), lança um erro informando a falha.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Chama a função execute_from_command_line, passando os argumentos da linha de comando (sys.argv),
    # que permite a execução dos comandos administrativos do Django.
    execute_from_command_line(sys.argv)

# Quando o script é executado diretamente, a função main() será chamada.
if __name__ == '__main__':
    main()