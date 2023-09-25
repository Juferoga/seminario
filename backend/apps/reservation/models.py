from django.db import models
from django.utils import timezone
from ..authuser.models import Employee, Student, Customer

class Reservation(models.Model):
    pk_id = models.AutoField(
      verbose_name='Llave primaria pago',
      primary_key=True
    )
    d_reservation = models.DateTimeField(
      null=True,
      verbose_name='Fecha de creación del registro'
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
    fk_student = models.ForeignKey(
      Student, 
      verbose_name=("Llave foránea estudiante"), 
      on_delete=models.CASCADE,
      null=True
    )
    fk_employee = models.ForeignKey(
      Employee, 
      verbose_name=("Llave foránea empleado"), 
      on_delete=models.CASCADE,
      null=True
    )

    def __str__(self):
      return f"Reservation {self.pk_id}"

    class Meta:
      verbose_name = 'Medio de pago'
      verbose_name_plural = 'Medios de pagos'
