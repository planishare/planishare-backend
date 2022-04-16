from rest_framework import serializers

from users.serializers import UserSimpleDetailSerializer
from .models import AcademicLevel, Axis, Subject, Post

class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = [
            'id',
            'name',
        ]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'name',
        ]

class AxisSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Axis
        fields = [
            'id',
            'name',
            'subject',
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleDetailSerializer()
    academic_level = AcademicLevelSerializer()
    axis = AxisSerializer()

    likes = serializers.SerializerMethodField()
    downloads = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'description',
            'image',
            'academic_level',
            'axis',
                # 'subject',
            'main_file',
            'suporting_material',
            'created_at',
            'updated_at',
            'likes',
            'downloads',
        ]
    
    def get_likes(self, instance):
        likes = instance.likes.all().count()
        return likes
    
    def get_downloads(self, instance):
        downloads = instance.downloads.all().count()
        return downloads

class PostCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'description',
            'image',
            'academic_level',
            'axis',
            'main_file',
            'suporting_material',

            'created_at',
        ]
        extra_kwargs = {
            'academic_level': {'allow_null': False, 'required': True},
            'axis': {'allow_null': False, 'required': True},
        } 

class PostUpdateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'academic_level',
            'axis',
            'updated_at',
        ] 

