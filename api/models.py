from django.contrib.postgres.fields import (
  JSONField
)
from django.db import models

# Create your models here.

class Patient(models.Model):
  name = models.CharField(max_length = 256)

  def __str__ (self):
    return self.name

class Session(models.Model):
  patient = models.ForeignKey('Patient', on_delete = models.CASCADE)
  text_sentiment_analysis = JSONField()
  text_emotion_analysis = JSONField()
  image_emotion_analysis = JSONField()

  def __str__ (self):
    return self.id