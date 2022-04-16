from rest_framework import serializers
from .models import Education, Institution

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'name'
        ]

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = [
            'id',
            'name',
            'institution_type'
        ]