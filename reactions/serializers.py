from requests import delete
from rest_framework import serializers

from posts.models import Post
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
    
    def create(self, validated_data):
        post = validated_data['post']
        post.total_likes += 1
        post.save()
        return super().create(validated_data)

class ViewSerializer(serializers.ModelSerializer):
    firebase_user_id = serializers.CharField(max_length=2000)

    class Meta:
        model = View
        fields = [
            'id',
            'firebase_user_id',
            'post',
            'user',
            'first_seen',
        ]

    def validate(self, attrs):
        try:
            user = self.context['request'].user
            if (user):
                attrs['user'] = user if user.is_authenticated else None
        except Exception:
            raise serializers.ValidationError('Failed getting authenticated user')
        return super().validate(attrs)
    
    def validate_firebase_user_id(self, value):
        # Verify token
        firebase_uid = None
        try:
            decoded_token = auth.verify_id_token(value)
            firebase_uid = decoded_token.get('user_id')
        except Exception:
            raise serializers.ValidationError('Invalid ID Token')
        return firebase_uid

    def create(self, validated_data):
        post = validated_data['post']
        post.total_views += 1
        post.save()
        return super().create(validated_data)