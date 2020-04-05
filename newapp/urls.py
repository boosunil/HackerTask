from django.urls import path, include
from rest_framework import routers
from newapp.views import GatewayViewSet, RouteViewSet

router = routers.DefaultRouter()
router.register('gateway', GatewayViewSet)
router.register('route', RouteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
