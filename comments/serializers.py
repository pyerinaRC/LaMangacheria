from rest_framework import serializers
from .models import Comentario
from .utils.censura import censurar_lenguaje

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

    def validate_contenido(self, value):
        if not value.strip():
            raise serializers.ValidationError("El comentario no puede estar vacío.")
        return censurar_lenguaje(value)
