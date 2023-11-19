from django.test import TestCase
from .models import Place
from .serializers import PlaceSerializer
from .choices import PlaceTypeChoices
from datetime import datetime

class PlaceModelTestCase(TestCase):
    def setUp(self):
        self.place = Place.objects.create(
            t_name='Sala de Reuniones 1',
            t_description='Descripción de la sala de reuniones',
            n_type=PlaceTypeChoices.MEETING_ROOM,
            t_observation='Observaciones sobre la sala',
            n_price=100.0,
        )

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

class PlaceSerializerTestCase(TestCase):
    def setUp(self):
        self.place_data = {
            't_name': 'Sala de Reuniones 2',
            't_description': 'Descripción de la sala de reuniones 2',
            'n_type': PlaceTypeChoices.MEETING_ROOM,
            't_observation': 'Observaciones sobre la sala 2',
            'n_price': 150.0,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_place_serializer(self):
        serializer = PlaceSerializer(instance=self.place)
        self.assertEqual(serializer.data['t_name'], 'Sala de Reuniones 2')
        self.assertEqual(serializer.data['t_description'], 'Descripción de la sala de reuniones 2')
        self.assertEqual(serializer.data['n_type'], PlaceTypeChoices.MEETING_ROOM)
        self.assertEqual(serializer.data['t_observation'], 'Observaciones sobre la sala 2')
        self.assertEqual(serializer.data['n_price'], '150.00')
