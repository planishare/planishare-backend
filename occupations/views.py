from rest_framework import generics
from .models import Education, Institution
from .serializers import EducationSerializer, InstitutionSerializer

class EducationtListAPIView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = []

class InstitutionListAPIView(generics.ListAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    authentication_classes = []