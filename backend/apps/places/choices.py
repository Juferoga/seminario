from django.db import models

class PlaceTypeChoices(models.IntegerChoices):
  CLASSROOM = 0, 'Salón de clase'
  AUDITORIUM = 1, 'Auditorio'
  INFORMATICS_ROOM = 2, 'Sala de informática'
  MEETING_ROOM = 3, 'Sala de reuniones'
  OTHERS = 4, 'Otros'