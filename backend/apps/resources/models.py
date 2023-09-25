from django.db import models
from django.utils import timezone
from abc import abstractmethod, ABC
from .choices import ResourcesStatusChoices

class Resource(models.Model):
  pk_id = models.AutoField(
    verbose_name='Llave primaria artefacto',
    primary_key=True
  )
  t_name = models.CharField(
    max_length=255,
    verbose_name="Nombre del recurso"
  )
  d_created_at = models.DateTimeField(
    default=timezone.now,
    verbose_name='Fecha de creación del registro'
  )
  d_updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name='Fecha de última actualización del registro'
  )
  t_description = models.TextField(
    null=True,
    blank=True,
    verbose_name='Descripción del artefacto'
  )
  n_price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    null=True,
    blank=True,
    verbose_name='Precio del artefacto'
  )
  b_status = models.IntegerField(
    choices=ResourcesStatusChoices.choices,
    default=ResourcesStatusChoices.ACTIVE,
    verbose_name="Estado del recurso"
  )

  def is_active(self):
    return self.b_status

  def update_status(self, status):
    self.b_status = status
    self.save()

  class Meta:
    verbose_name = 'Recurso'
    verbose_name_plural = 'Recursos'