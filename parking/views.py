
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from parking.forms import InsereVeiculoForm
from parking.models import Veiculo

# Index - Pagina Principal


def index(request):
    return render(request, 'index.html')

class EntradaCreateView(CreateView):
    model = Veiculo
    form_class = InsereVeiculoForm
    template_name = 'entrada.html'
    success_url = reverse_lazy('parking:entrada')

def pagar(request, placa):
    veiculo = Veiculo.objects.filter(placa=placa)
    context = {'placa': placa, 'veiculos': veiculo}
    return render(request, 'saida.html', context=context)

def placa(request):
    if request.method == "POST":
        placa = request.POST.get("placa", "") 
        if not placa:
            return render(request, 'index.html')
        veiculo = Veiculo.objects.filter(placa=placa)
        context = {'placa': placa, 'veiculos': veiculo}
        return render(request, 'saida.html', context=context)
