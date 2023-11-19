from django.test import TestCase
from django.utils import timezone
from ..authuser.models import Employee, Student, Customer
from ..payments.models import Payment
from .models import Reservation
from rest_framework import status


class ReservationModelTest(TestCase):
    def setUp(self):
        # Crear instancias necesarias para las pruebas
        customer = Customer.objects.create(name='Cliente de prueba', email='casasas@gm.com')
        student = Student.objects.create(name='Estudiante de prueba', email='casaqwes@gm.com')
        employee = Employee.objects.create(name='Empleado de prueba', email='crfdasas@gm.com')
        payment = Payment.objects.create(pk_id=1)

        self.reservation = Reservation.objects.create(
            d_reservation=timezone.now(),
            b_status=True,
            fk_customer=customer,
            fk_student=student,
            fk_employee=employee,
            fk_payment=payment
        )

    def test_str_method(self):
        self.assertEqual(str(self.reservation), f"Reservation {self.reservation.pk_id}")

    def test_verbose_names(self):
        self.assertEqual(Reservation._meta.verbose_name, 'Reservación')
        self.assertEqual(Reservation._meta.verbose_name_plural, 'Reservaciones')

    # Agrega más pruebas según sea necesario
