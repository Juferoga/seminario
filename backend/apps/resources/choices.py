from django.db import models

class ResourcesStatusChoices(models.IntegerChoices):
  ACTIVE = 0, 'Activo'
  DESACTIVE = 1, 'Inactivo'
  REPAIR = 2, 'En reparación'
  OTHERS = 3, 'Otros'