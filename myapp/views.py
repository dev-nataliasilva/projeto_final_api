from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .enums import Color
from .serializers import ColorObjectSerializer
from enum import Enum

@api_view(['POST'])
def receive_color_objects(request):
    # Obtendo a lista de categorias de cores do corpo da requisição
    color_categories = request.data.get('categories', [])  # Pegando as categorias enviadas no payload
    
    # Exibindo a lista de categorias de cores no console
    print("Lista de categorias de cores recebida:", color_categories)

    # Validando os objetos de cor
    serializer = ColorObjectSerializer(data=request.data.get('colors', []), many=True)  # Usando o 'colors' enviado
    if serializer.is_valid():
        color_objects = serializer.validated_data

        results = []
        
        # Loop através de cada objeto de cor recebido
        for color_object in color_objects:
            path = color_object['path']
            average_rgb = color_object['average_rgb']

            # Chama o endpoint da IA para prever a cor
            predicted_color = get_predicted_color(average_rgb)

            # Verifica se a cor prevista está no Enum e se está nas categorias fornecidas
            if predicted_color in [color.name for color in Color] and predicted_color in color_categories:
                predicted_color_enum = predicted_color  # Já é o nome da cor
                # Adiciona o resultado ao array de resultados
                results.append({
                    'path': path,
                    'average_rgb': average_rgb,
                    'predicted_color': predicted_color_enum
                })

        return Response(results, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_predicted_color(average_rgb):
    # URL do endpoint da sua IA (ajuste conforme necessário)
    url = 'http://localhost:7070/api/predict-color/'  # Exemplo de URL

    # Faz a requisição POST para o endpoint da IA
    response = requests.post(url, json={'rgb': average_rgb})
    
    if response.status_code == 200:
        # Supondo que a resposta contenha um campo 'predicted_color'
        return response.json().get('predicted_color', 'Cor não prevista')
    else:
        return 'Erro na previsão'
