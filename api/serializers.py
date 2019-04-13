from rest_framework_json_api import serializers

from api import models

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Patient
    fields = "__all__"
