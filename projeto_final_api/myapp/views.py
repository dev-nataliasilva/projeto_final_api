from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ColorObjectSerializer
import requests  # Importa o módulo requests para fazer chamadas HTTP

@api_view(['POST'])
def receive_color_objects(request):
    serializer = ColorObjectSerializer(data=request.data, many=True)  # Supondo que você enviará um array
    if serializer.is_valid():
        # Aqui você pode processar os dados recebidos
        color_objects = serializer.validated_data

        results = []
        
        # Loop através de cada objeto de cor recebido
        for color_object in color_objects:
            path = color_object['path']
            average_rgb = color_object['average_rgb']

            # Chama o endpoint da IA para prever a cor
            predicted_color = get_predicted_color(average_rgb)

            # Adiciona o resultado ao array de resultados
            results.append({
                'path': path,
                'average_rgb': average_rgb,
                'predicted_color': predicted_color
            })

        # Imprime a resposta da IA no console
        print("Resposta da IA:", results)
        return Response(results, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_predicted_color(average_rgb):
    # URL do endpoint da sua IA (ajuste conforme necessário)
    url = 'http://localhost:7070/api/predict-color/'  # Exemplo de URL

    # Ajusta o JSON enviado para o formato esperado pela IA
    response = requests.post(url, json={'rgb': average_rgb})  # Faz a requisição POST
    
    if response.status_code == 200:
        # Supondo que a resposta contenha um campo 'predicted_color'
        return response.json().get('predicted_color', 'Cor não prevista')
    else:
        return 'Erro na previsão'
