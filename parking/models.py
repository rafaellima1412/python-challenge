from django.db import models


class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=8, null=False)
    modelo = models.CharField('modelo', max_length=100, null=False)
    cor = models.CharField('cor', max_length=50, null=False)
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa

