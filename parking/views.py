
from django.views.generic import CreateView

from parking.forms import InsereVeiculoForm
from parking.models import Veiculo
from django.urls import reverse_lazy

class EntradaCreateView(CreateView):
    model = Veiculo
    form_class = InsereVeiculoForm
    template_name = 'entrada.html'
    success_url = reverse_lazy('parking:entrada')
