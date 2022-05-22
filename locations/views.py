from rest_framework import generics

from locations.models import Region
from locations.serializers import RegionSerializer

class RegionWithCommunesListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    authentication_classes = []
