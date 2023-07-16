from rest_framework import generics, permissions

from reports.models import Report
from reports.serializers import ReportSerializer

class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
