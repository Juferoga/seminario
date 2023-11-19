# apps/authuser/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employee, Customer, Student
from django.contrib.auth import get_user_model

class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_employee(self):
        url = reverse('employee_create')
        data = {
            'n_id': 123,
            't_id': 1,
            'n_phone': 123456789,
            'email': 'employee@example.com',
            'name': 'John Doe',
            'password': 'securepassword',
            'n_salary': 50000.00,
            'd_start_contract': '2023-01-01T00:00:00Z',
            'd_end_contract': '2023-12-31T23:59:59Z',
            't_rol': 2,  
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().email, 'employee@example.com')

    def test_get_employee_list(self):
        url = reverse('employee_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


