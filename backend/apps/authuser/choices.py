from django.db import models

class RoleChoices(models.IntegerChoices):
  SUPERADMIN = 0, 'Administrador Administrador'
  ADMINISTRATOR = 1, 'Administrador'
  EMPLOYEE = 2, 'Empleado'
  CLIENT = 3, 'Cliente'
  STUDENT = 4, 'Estudiante'

class TypeIdentificationChoices(models.IntegerChoices):
  CEDULA = 1, 'Cédula de ciudadanía'
  TI = 2, 'Tarjeta de identidad'
  CEDULAEXTRANJERA = 3, 'Cédula de extranjería'