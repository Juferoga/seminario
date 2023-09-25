from django.db import models

class ArtifactTypeChoices(models.IntegerChoices):
  FURNITURE = 0, 'Inmobiliario'
  TECH = 1, 'Tecnología'
  OFFICE = 2, 'Artículos de oficina'
  OTHERS = 3, 'Otros'