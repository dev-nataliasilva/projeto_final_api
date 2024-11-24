# Importa a classe base 'serializers' do Django Rest Framework, que facilita a serialização e desserialização de dados
from rest_framework import serializers

# Define o serializer para validar e transformar os dados do objeto de cor
class ColorObjectSerializer(serializers.Serializer):
    # Define o campo 'path' como uma string (CharField), representando o caminho do arquivo ou imagem
    path = serializers.CharField()

    # Define o campo 'average_rgb' como uma lista de inteiros (ListField), onde cada item da lista é um valor entre 0 e 255.
    # Isso representa a média de valores RGB de uma imagem ou objeto.
    average_rgb = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=255)  # Cada valor na lista é um inteiro entre 0 e 255
    )