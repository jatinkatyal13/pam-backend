from django.http import HttpResponse
from django.shortcuts import render

from rest_framework_json_api.views import (
  ModelViewSet
)

from api import models
from api import serializers

import requests
import json

# Create your views here.

class PatientListView(ModelViewSet):
  serializer_class = serializers.PatientSerializer

  def get_queryset(self):
    return models.Patient.objects.all()

def MLText(request):
  if request.method == "POST":
    endpoint = "http://localhost:1212/api/text"
    data = {
      'text' : request.POST['text']
    }
    result = requests.post(endpoint, data = data)

    return HttpResponse(result.content)

  else:
    return json.dumps({
      "error": "POST only"
    })
