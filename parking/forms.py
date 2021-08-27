from django import forms

from .models import Veiculo


class InsereVeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = [
            'modelo',
            'cor',
            'placa',
        ]
