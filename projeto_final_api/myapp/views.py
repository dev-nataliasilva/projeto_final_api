from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberSerializer

@api_view(['POST'])
def double_number(request):
    serializer = NumberSerializer(data=request.data)
    if serializer.is_valid():
        number = serializer.validated_data['number']
        result = number * 2
        return Response({'result': result}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
