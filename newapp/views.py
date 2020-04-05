from django.shortcuts import render
from rest_framework import viewsets
from newapp.models import Gateway, Route
from newapp.serializers import GatewaySerializer, RouteSerializer
# Create your views here.


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
