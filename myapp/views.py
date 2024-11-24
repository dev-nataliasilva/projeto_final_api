# Importação dos módulos necessários da biblioteca do Django e do DRF
from rest_framework.decorators import api_view  # Decorator para definir uma view de API
from rest_framework.response import Response  # Para criar uma resposta HTTP
from rest_framework import status  # Para definir os códigos de status HTTP
import requests  # Para realizar requisições HTTP a outros serviços
from .enums import Color  # Enum com as cores válidas que a IA pode prever
from .serializers import ColorObjectSerializer  # Serializador para validar os objetos de cor
from enum import Enum  # Importação para trabalhar com o tipo Enum

# A view recebe requisições POST na rota associada
@api_view(['POST'])
def receive_color_objects(request):
    """
    Esta view recebe uma lista de objetos de cor e categorias, 
    e utiliza um modelo de IA para prever a cor dominante baseada em dados RGB.
    """
    # Obtém as categorias de cores que foram enviadas no corpo da requisição
    color_categories = request.data.get('categories', [])  # 'categories' é uma chave no JSON

    # Exibe no console as categorias de cores que foram recebidas
    print("Lista de categorias de cores recebida:", color_categories)

    # Valida os objetos de cor com base no serializador
    serializer = ColorObjectSerializer(data=request.data.get('colors', []), many=True)  # 'colors' é outra chave no JSON
    
    if serializer.is_valid():
        # Se os dados são válidos, recupera os dados validados (os objetos de cor)
        color_objects = serializer.validated_data

        results = []  # Lista onde os resultados das previsões serão armazenados
        
        # Loop que percorre todos os objetos de cor recebidos
        for color_object in color_objects:
            path = color_object['path']  # Caminho ou identificador do objeto de cor
            average_rgb = color_object['average_rgb']  # Valor RGB médio para a cor

            # Chama a função que faz uma requisição para a IA para prever a cor baseada no valor RGB
            predicted_color = get_predicted_color(average_rgb)

            # Verifica se a cor prevista existe no Enum 'Color' e se ela está nas categorias enviadas
            if predicted_color in [color.name for color in Color] and predicted_color in color_categories:
                # Se a cor prevista for válida e estiver nas categorias, cria um dicionário com os resultados
                predicted_color_enum = predicted_color  # A cor prevista já está em formato de string
                results.append({
                    'path': path,
                    'average_rgb': average_rgb,
                    'predicted_color': predicted_color_enum
                })

        # Retorna os resultados encontrados com código HTTP 200 (sucesso)
        return Response(results, status=status.HTTP_200_OK)
    
    # Se o serializador não for válido (erros de validação), retorna um erro 400 com os detalhes
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_predicted_color(average_rgb):
    """
    Esta função envia os dados RGB para um endpoint da IA e retorna a cor prevista.
    """
    # URL do serviço de IA (ajuste conforme o endpoint real)
    url = 'https://ondesalvei-ia-f31a49c64a2d.herokuapp.com/api/predict-color/'  # Exemplo de URL do endpoint de IA

    # Realiza uma requisição POST para a IA, enviando os dados RGB no corpo da requisição
    response = requests.post(url, json={'rgb': average_rgb})
    
    # Verifica se a resposta foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Se a IA retornar uma previsão, extrai a cor prevista do JSON
        return response.json().get('predicted_color', 'Cor não prevista')
    else:
        # Caso a requisição falhe, retorna uma mensagem de erro
        return 'Erro na previsão'