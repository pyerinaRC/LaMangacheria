from rest_framework import viewsets
from .models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-creado_en')
    serializer_class = ComentarioSerializer
