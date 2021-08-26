from django.db import models
from djmoney.models.fields import MoneyField

class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=8, null=False)
    modelo = models.CharField('modelo', max_length=100, null=False)
    cor = models.CharField('cor', max_length=50, null=False)
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa

class Valor(models.Model):
    periodoManha = MoneyField(max_digits=14, decimal_places=2,
                              default_currency='BRL', default='2')
    periodoTarde = MoneyField(max_digits=14, decimal_places=2,
                              default_currency='BRL', default='3')
    periodoFDS = MoneyField(max_digits=14, decimal_places=2,
                            default_currency='BRL', default='2.5')

    def __str__(self):
        return "Tabela de Valores"
