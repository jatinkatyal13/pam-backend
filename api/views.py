from django.shortcuts import render

from rest_framework_json_api.views import (
  ModelViewSet
)

from api import models
from api import serializers

# Create your views here.

class PatientListView(ModelViewSet):
  serializer_class = serializers.PatientSerializer

  def get_queryset(self):
    return models.Patient.objects.all()
