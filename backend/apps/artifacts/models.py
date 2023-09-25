from django.db import models
from .choices import ArtifactTypeChoices
from ..resources.models import Resource

class Artifact(Resource):
    n_type = models.IntegerField(
        choices=ArtifactTypeChoices.choices,
        default=ArtifactTypeChoices.OTHERS,
        verbose_name='Tipo de artefacto'
    )
    n_stock = models.PositiveIntegerField(
        default=0,
        verbose_name='Número de unidades en stock'
    )

    def __str__(self):
        return f"Artifact {self.pk_id} - Type: {self.get_n_type_display()}"

    def is_in_stock(self):
        return self.n_stock > 0

    def update_stock(self, quantity):
        self.n_stock += quantity
        self.save()

    class Meta:
        verbose_name = 'Artefacto'
        verbose_name_plural = 'Artefactos'
