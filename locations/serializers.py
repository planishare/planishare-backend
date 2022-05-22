from rest_framework import serializers

from .models import Commune, Region

class SimpleCommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = [
            'id',
            'name'
        ]

class RegionSerializer(serializers.ModelSerializer):
    communes = SimpleCommuneSerializer(many=True)
    class Meta:
        model = Region
        fields = [
            'id',
            'number',
            'name',
            'communes'
        ]

class SimpleRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id',
            'number',
            'name'
        ]

class CommuneSerializer(serializers.ModelSerializer):
    region = SimpleRegionSerializer()

    class Meta:
        model = Commune
        fields = [
            'id',
            'name',
            'region',
        ]