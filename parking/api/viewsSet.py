
from parking.api.serializer import VeiculoSerializer
from parking.models import Veiculo
from rest_framework import viewsets


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    # permission_classes = (IsAuthenticated, )
