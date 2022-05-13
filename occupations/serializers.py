from rest_framework import serializers
from .models import Education, Institution, InstitutionType

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'name'
        ]

class InstitutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionType
        fields = [
            'id',
            'name'
        ]

class InstitutionSerializer(serializers.ModelSerializer):
    institution_type = InstitutionTypeSerializer()

    class Meta:
        model = Institution
        fields = [
            'id',
            'name',
            'institution_type'
        ]

