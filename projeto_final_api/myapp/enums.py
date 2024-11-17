from enum import Enum

class Color(Enum):
    Branco = 'Branco'
    Preto = 'Preto'
    Azul = 'Azul'
    Vermelho = 'Vermelho'
    Verde = 'Verde'
    Laranja = 'Laranja'
    Amarelo = 'Amarelo'
    Roxo = 'Roxo'
    Marrom = 'Marrom'

COLOR_CATEGORIES = {color.value: color.name for color in Color}