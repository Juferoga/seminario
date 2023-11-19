import json
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..authuser.models import Employee, Student, Customer
from ..payments.models import Payment
from .models import Reservation
from rest_framework import status
from rest_framework.test import APIClient


class ReservationModelTest(TestCase):
    def setUp(self):
        # Crear instancias necesarias para las pruebas
        customer = Customer.objects.create(name='Cliente de prueba', email='casasas@gm.com')
        student = Student.objects.create(name='Estudiante de prueba', email='casaqwes@gm.com')
        employee = Employee.objects.create(name='Empleado de prueba', email='crfdasas@gm.com')
        payment = Payment.objects.create(pk_id=1)
        
        self.client = APIClient()
        self.reservation_data = {
            'd_reservation': timezone.now().isoformat(),
            'b_status': True,
            'fk_employee_id': 3,
            'fk_payment_id': 1
            }
        self.reservation = Reservation.objects.create(**self.reservation_data) 

    def test_create_reservation(self): 
        url = reverse('reservation-list') 
        response = self.client.post(url, self.reservation_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Reservation.objects.count(), 2) 
    
    def test_update_reservation(self): 
        url = reverse('reservation-detail', kwargs={'pk': self.reservation.pk}) 
        updated_data = {
            'd_reservation': timezone.now().isoformat(),
            'b_status': False,
            'fk_employee_id': 3,
            'fk_payment_id': 1
            }
        response = self.client.put(url, updated_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.reservation.refresh_from_db() 

        expected_datetime = timezone.datetime.fromisoformat(updated_data['d_reservation'])

        self.assertEqual(self.reservation.d_reservation, expected_datetime)

    def test_delete_reservation(self): 
        url = reverse('reservation-detail', kwargs={'pk': self.reservation.pk}) 
        response = self.client.delete(url) 

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        self.assertEqual(Reservation.objects.count(), 0)
    
    def test_retrieve_resource(self): 
        url = reverse('reservation-detail', kwargs={'pk': self.reservation.pk}) 
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        #self.assertEqual(response.data['d_reservation'], self.reservation.d_reservation) 
        #self.assertEqual(response.data['fk_employee_id'], str(self.reservation.fk_employee))

