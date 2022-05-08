from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from locations.serializers import CommuneSerializer

from .models import User
from reactions.models import Download, Like
from posts.models import Post

from occupations.serializers import EducationSerializer, InstitutionSerializer

class UserSimpleDetailSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    education = EducationSerializer()
    institution = InstitutionSerializer()

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'education',
            'institution',
        ]

class UserDetailSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    education = EducationSerializer()
    institution = InstitutionSerializer()
    commune = CommuneSerializer()

    total_likes = serializers.SerializerMethodField(read_only=True)
    total_downloads = serializers.SerializerMethodField(read_only=True)
    total_posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'education',
            'institution',
            'commune',
            'created_at',
            'updated_at',
            'total_likes',
            'total_downloads',
            'total_posts',
        ]
    
    def get_total_likes(self, obj):
        # likes = obj.user_likes.all()
        likes = Like.objects.filter(post__user=obj.id).count()
        # data = LikeSerializer(likes, many=True).data
        return likes
    
    def get_total_downloads(self, obj):
        downloads = Download.objects.filter(post__user=obj.id).count()
        return downloads

    def get_total_posts(self, obj):
        posts = Post.objects.filter(user=obj.id).count()
        return posts

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'education',
            'institution',
            'commune',
        ]

class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    email = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            'email',
            'updated_at',
            'password',
        ]
    
    def update(self, instance, validated_data):
        user = instance
        password = validated_data['password']
        user.password = make_password(password)
        user.save()
        return user
