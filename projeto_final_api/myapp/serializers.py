from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()

class ColorObjectSerializer(serializers.Serializer):
    path = serializers.CharField()
    average_rgb = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=255)
    )