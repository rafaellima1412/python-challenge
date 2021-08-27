from django.urls import path

from parking.views import EntradaCreateView

from . import views

app_name = 'parking'

urlpatterns = [
    path('', views.index, name='index'),
    path('entrada/', EntradaCreateView.as_view(), name='entrada'),
    path('saida/<str:placa>/',views.pagar, name='saida'),
    path('placa/',views.placa, name='saida'),
    ]
    