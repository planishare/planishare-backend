from rest_framework import serializers
from .models import Like, View

from firebase_admin import auth

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

class ViewSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = View
        fields = [
            'id',
            'firebaseUserUUID',
            'post',
            'created_at',
        ]

    def validate(self, attrs):
        try:
            firebaseUserUUID = auth.verify_id_token(attrs["firebaseUserUUID"])
            print(firebaseUserUUID)
        except Exception:
            raise serializers.ValidationError("Invalid FirebaseUserUUID")
        return super().validate(attrs)

    # TODO: Register user if is auth
