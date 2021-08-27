from parking.api.viewsSet import VeiculoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', VeiculoViewSet)
