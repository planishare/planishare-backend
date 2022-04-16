from rest_framework import serializers
from .models import Like, Download

class LikeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = [
            'id',
            'user',
            'post',
            'created_at',
        ]

class DownloadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Download
        fields = [
            'id',
            'user',
            'post',
            'created_at',
        ]