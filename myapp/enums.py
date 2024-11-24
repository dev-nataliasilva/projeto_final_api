# Importa a classe 'Enum' do módulo 'enum', que permite criar tipos de dados enumerados
from enum import Enum

# Define a classe 'Color', que é um Enum que lista as cores possíveis
class Color(Enum):
    # Cada cor é um valor do Enum com nome e valor definidos explicitamente
    Branco = 'Branco'
    Preto = 'Preto'
    Azul = 'Azul'
    Vermelho = 'Vermelho'
    Verde = 'Verde'
    Laranja = 'Laranja'
    Amarelo = 'Amarelo'
    Roxo = 'Roxo'
    Marrom = 'Marrom'

# Cria um dicionário 'COLOR_CATEGORIES' que mapeia o valor da cor para o nome da cor.
# Esse dicionário será usado para facilitar o acesso às cores por seu nome ou valor.
COLOR_CATEGORIES = {color.value: color.name for color in Color}