from django.db import models
from .choices import PaymentTypeChoices
from django.utils import timezone
from ..authuser.models import Customer

class Payment(models.Model):
    pk_id = models.AutoField(
      verbose_name='Llave primaria pago',
      primary_key=True
    )
    n_type = models.IntegerField(
      choices=PaymentTypeChoices.choices,
      default=PaymentTypeChoices.OTHERS,
      verbose_name='Tipo de pago'
    )
    d_created_at = models.DateTimeField(
      default=timezone.now,
      verbose_name='Fecha de creación del registro'
    )
    b_status = models.BooleanField(
      auto_created=True,
      default=True,
      verbose_name="Estado del pago"
    )
    fk_customer = models.ForeignKey(
      Customer, 
      verbose_name=("Llave foránea cliente"), 
      on_delete=models.CASCADE,
      null=True
    )

    def __str__(self):
      return f"Payment {self.pk_id} - Type: {self.get_n_type_display()}"

    class Meta:
      verbose_name = 'Medio de pago'
      verbose_name_plural = 'Medios de pagos'
