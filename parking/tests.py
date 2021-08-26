from parking.models import Valor, Veiculo
from django.test import TestCase

# from parking.behavior import Parking

class VeiculoModelTestCase(TestCase):
    def setUp(self) -> None:
        self.veiculo = Veiculo.objects.create(placa='ABC1234', modelo='fusca', cor='azul')
        self.valor = Valor.objects.create(periodoManha = 3.5, periodoTarde=4.0, periodoFDS=5.0)

    def test_placa_object(self):
        """Teste para validar se objeto de veiculo é criado."""
        self.assertEqual(self.veiculo.placa, 'ABC1234')

    def test_periodoTarde_object(self):
        """Teste para validar se objeto de valor é criado."""
        self.assertEqual(self.valor.periodoTarde_currency,  'BRL')

class ValorTestCase(TestCase):
    def test_periodo_max_length(self):
        valor = Valor.objects.get(id=1)
        max_length = valor._meta.get_field('periodoFDS').max_length
        self.assertEquals(max_length, 14)
