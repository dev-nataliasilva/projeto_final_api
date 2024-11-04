from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberSerializer
from .serializers import ColorObjectSerializer

@api_view(['POST'])
def double_number(request):
    serializer = NumberSerializer(data=request.data)
    if serializer.is_valid():
        number = serializer.validated_data['number']
        result = number * 2
        return Response({'result': result}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def receive_color_objects(request):
    serializer = ColorObjectSerializer(data=request.data, many=True)  # Supondo que você enviará um array
    if serializer.is_valid():
        # Aqui você pode processar os dados recebidos
        color_objects = serializer.validated_data

        # Imprime os dados recebidos no console
        print("Dados recebidos:", color_objects)  

        return Response({'received': color_objects}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)