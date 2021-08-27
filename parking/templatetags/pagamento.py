import json
from datetime import datetime, time, timedelta

from django import template
from parking.models import Valor, Veiculo

register = template.Library()

@register.simple_tag
def pagamento(placa):

    veiculo = Veiculo.objects.get(placa=placa)
    valor = Valor.objects.get(id=1)
    entrada = veiculo.data_entrada
    now = datetime.now()
    diferenca = now - timedelta(hours=entrada.hour,
                                minutes=entrada.minute, seconds=entrada.second)
    saida = (diferenca.hour * 60) + diferenca.minute

    """Se for final de semana"""
    if now.weekday() >= 6:
        """Se passou de uma hora """
        if diferenca.hour >= 1:
            valor_final = ((valor.periodoFDS/60) * saida)
            return valor_final
        else:
            valor_final = valor.periodoFDS
            return valor_final
    else:
        """Nao e fds qual periodo do dia"""
        if now.time() >= time(8, 00) and now.time() < time(12, 00):
            if diferenca.hour >= 1:
                valor_final = ((valor.periodoManha/60) * saida)
                return valor_final
            else:
                valor_final = valor.periodoManha
                return valor_final
        elif now.time() > time(12, 00) and now.time() < time(18, 00):
            if diferenca.hour >= 1:
                valor_final = ((valor.periodoTarde/60) * saida)
                return valor_final
            else:
                valor_final = valor.periodoTarde
                return valor_final
