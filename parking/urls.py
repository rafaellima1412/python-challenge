
from parking.views import EntradaCreateView
from django.urls import path

app_name = 'parking'

urlpatterns = [
    path('entrada/', EntradaCreateView.as_view(), name='entrada'),
    ]