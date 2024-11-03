from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()
