from rest_framework import generics
from .models import Categoria, Pregunta
from .serializers import CategoriaSerializer, PreguntaSerializer

class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PreguntaPorCategoriaListView(generics.ListAPIView):
    serializer_class = PreguntaSerializer

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        return Pregunta.objects.filter(categoria_id=categoria_id)
