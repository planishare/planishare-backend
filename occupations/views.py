from rest_framework import generics, filters
from .models import Education, Institution
from .serializers import EducationSerializer, InstitutionSerializer
from api.utils import CustomPageNumberPagination

class EducationtListAPIView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class InstitutionListAPIView(generics.ListAPIView):
    queryset = Institution.objects.all().order_by('id')
    serializer_class = InstitutionSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = CustomPageNumberPagination
