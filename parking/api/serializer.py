from parking.models import Veiculo
from rest_framework import serializers


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = (
            'placa',
            'data_entrada',
            )
                
