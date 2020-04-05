from rest_framework import serializers
from newapp.models import Gateway, Route


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'prefix', 'gateway')
        depth = 1
