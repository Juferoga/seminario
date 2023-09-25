from django.db import models

class PaymentTypeChoices(models.IntegerChoices):
  CREDIT  = 0, 'Tarjeta de crédito'
  DEBIT   = 1, 'Tarjeta de débito'
  CASH    = 2, 'Efectivo'
  OTHERS  = 3, 'Otros'