from django.contrib import admin

from .models import Veiculo, Valor


class VeiculoAdmin(admin.ModelAdmin):
    pass

class ValorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Valor, ValorAdmin)