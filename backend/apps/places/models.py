from django.db import models
from .choices import PlaceTypeChoices
from ..resources.models import Resource

class Place(Resource):
    n_type = models.IntegerField(
      choices=PlaceTypeChoices.choices,
      default=PlaceTypeChoices.OTHERS,
      verbose_name='Tipo de lugar'
    )
    t_observation = models.CharField(
      max_length=255,
      verbose_name="Observaciones del lugar",
    )

    def __str__(self):
      return f"Place {self.pk_id} - Type: {self.get_n_type_display()}"

    class Meta:
      verbose_name = 'Lugar'
      verbose_name_plural = 'Lugares'
