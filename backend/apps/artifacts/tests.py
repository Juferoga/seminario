from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Artifact
from .choices import ArtifactTypeChoices

class ArtifactTestCase(TestCase): 
    def setUp(self): 
        self.client = APIClient() 
        self.artifact_data = { 
            't_name': 'Artifact de prueba', 
            't_description': 'Descripción del artifact de prueba', 
            'n_type': ArtifactTypeChoices.FURNITURE, 
            } 
        self.artifact = Artifact.objects.create(**self.artifact_data) 
    
    def test_create_artifact(self): 
        url = reverse('artifact-list') 
        response = self.client.post(url, self.artifact_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Artifact.objects.count(), 2) 

    def test_update_artifact(self): 
        url = reverse('artifact-detail', kwargs={'pk': self.artifact.pk}) 
        updated_data = { 
            't_name': 'Artifact actualizado', 
            't_description': 'Descripción del artifact actualizado', 
            'n_type': ArtifactTypeChoices.FURNITURE, 
            } 
        response = self.client.put(url, updated_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.artifact.refresh_from_db() 
        self.assertEqual(self.artifact.t_name, updated_data['t_name']) 
        
    def test_delete_artifact(self): 
        url = reverse('artifact-detail', kwargs={'pk': self.artifact.pk}) 
        response = self.client.delete(url) 

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        self.assertEqual(Artifact.objects.count(), 0)
        
    def test_retrieve_artifact(self): 
        url = reverse('artifact-detail', kwargs={'pk': self.artifact.pk}) 
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data['t_name'], self.artifact.t_name) 
        self.assertEqual(str(response.data['n_price']), str(self.artifact.n_price))
