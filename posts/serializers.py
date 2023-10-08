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

class SimpleAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
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

class SubjectWithAxisSerializer(serializers.ModelSerializer):
    axis = SimpleAxisSerializer(many=True)

    class Meta:
        model = Subject
        fields = [
            'id',
            'name',
            'axis'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleDetailSerializer()
    academic_level = AcademicLevelSerializer()
    axis = AxisSerializer()

    already_liked = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

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
            'updated_at',
            'total_likes',
            'total_views',
            'already_liked',
            'is_owner'
        ]

    def get_already_liked(self, instance):
        user = self.context['request'].user
        if (user != None):
            try:
                like = instance.likes.get(user=user.id)
                return like.id
            except Exception:
                return None
        return None

    def get_is_owner(self, instance):
        user = self.context['request'].user
        if (user != None):
            return user.id == instance.user.id
        return False

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
            'description': {'allow_null': True, 'required': False}
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

