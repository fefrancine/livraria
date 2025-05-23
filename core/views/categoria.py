from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AutorSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer # para pegar todos os campos que estão na classe CategoriaSerializer