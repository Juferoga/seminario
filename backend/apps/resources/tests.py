from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Resource

class ResourceTestCase(TestCase): 
    def setUp(self): 
        self.client = APIClient() 
        self.resource_data = { 
            't_name': 'Recurso de prueba', 
            't_description': 'Descripción del recurso de prueba', 
            'n_price': 10.99, 
            'b_status': 1 
            } 
        self.resource = Resource.objects.create(**self.resource_data) 
    
    def test_create_resource(self): 
        url = reverse('resource-list') 
        response = self.client.post(url, self.resource_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Resource.objects.count(), 2) 

    def test_update_resource(self): 
        url = reverse('resource-detail', kwargs={'pk': self.resource.pk}) 
        updated_data = { 
            't_name': 'Recurso actualizado', 
            't_description': 
            'Descripción actualizada del recurso', 
            'n_price': 14.99, 
            'b_status': 2 
        } 
        response = self.client.put(url, updated_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.resource.refresh_from_db() 
        self.assertEqual(self.resource.t_name, updated_data['t_name']) 
        
    def test_delete_resource(self): 
        url = reverse('resource-detail', kwargs={'pk': self.resource.pk}) 
        response = self.client.delete(url) 

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        self.assertEqual(Resource.objects.count(), 0)
        
    def test_retrieve_resource(self): 
        url = reverse('resource-detail', kwargs={'pk': self.resource.pk}) 
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data['t_name'], self.resource.t_name) 
        self.assertEqual(response.data['n_price'], str(self.resource.n_price))