from django.test import TestCase
from .models import Place
from .serializers import PlaceSerializer
from .choices import PlaceTypeChoices
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status



class PlaceModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.place_data = {
            't_name': 'Sala de Reuniones 1',
            't_description': 'Descripción de la sala de reuniones',
            'n_type': PlaceTypeChoices.MEETING_ROOM,
            't_observation': 'Observaciones sobre la sala',
            'n_price': 100.0,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_create_place(self): 
        url = reverse('place-list') 
        response = self.client.post(url, self.place_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Place.objects.count(), 2) 

    def test_update_place(self): 
        url = reverse('place-detail', kwargs={'pk': self.place.pk}) 
        updated_data = {
            't_name': 'Sala de Reuniones 1',
            't_description': 'Modificación de la descripción de la sala de reuniones',
            'n_type': PlaceTypeChoices.MEETING_ROOM,
            't_observation': 'Observaciones sobre la sala',
            'n_price': 100.0,
        }
        response = self.client.put(url, updated_data, format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.place.refresh_from_db() 

        self.assertEqual(self.place.t_name, updated_data['t_name'])

    def test_delete_place(self): 
        url = reverse('place-detail', kwargs={'pk': self.place.pk}) 
        response = self.client.delete(url) 

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        self.assertEqual(Place.objects.count(), 0)
    
    def test_retrieve_place(self): 
        url = reverse('place-detail', kwargs={'pk': self.place.pk}) 
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data['t_name'], self.place.t_name) 
        self.assertEqual(response.data['n_price'], str(self.place.n_price)+'0')

    def test_place_str_representation(self):
        self.assertEqual(
            str(self.place),
            f"Place {self.place.pk_id} - Type: {self.place.get_n_type_display()}"
        )

    def test_place_model_fields(self):
        self.assertEqual(self.place.t_name, 'Sala de Reuniones 1')
        self.assertEqual(self.place.t_description, 'Descripción de la sala de reuniones')
        self.assertEqual(self.place.n_type, PlaceTypeChoices.MEETING_ROOM)
        self.assertEqual(self.place.t_observation, 'Observaciones sobre la sala')
        self.assertEqual(self.place.n_price, 100.0)

    def test_place_serializer(self):
        serializer = PlaceSerializer(instance=self.place)
        self.assertEqual(serializer.data['t_name'], 'Sala de Reuniones 1')
        self.assertEqual(serializer.data['t_description'], 'Descripción de la sala de reuniones')
        self.assertEqual(serializer.data['n_type'], PlaceTypeChoices.MEETING_ROOM)
        self.assertEqual(serializer.data['t_observation'], 'Observaciones sobre la sala')
        self.assertEqual(serializer.data['n_price'], '100.00')
