from users.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

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
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user