from rest_framework import serializers

from .models import Commune, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id',
            'number',
            'name',
        ]

class CommuneSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Commune
        fields = [
            'id',
            'name',
            'region',
        ]