from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Artifact
from .serializers import ArtifactSerializer

class ArtifactModelTestCase(TestCase):
    def setUp(self):
        Artifact.objects.create(t_string=1, n_stock=10, description="Test Artifact", price=100.00)

    def test_artifact_created(self):
        artifact = Artifact.objects.get(description="Test Artifact")
        self.assertEqual(artifact.n_stock, 10)

class ArtifactSerializerTestCase(TestCase):
    def setUp(self):
        self.artifact_attributes = {'t_string': 1, 'n_stock': 10, 'description': 'Test Artifact', 'price': 100.00}
        self.serializer_data = ArtifactSerializer(data=self.artifact_attributes)

    def test_artifact_serializer_valid(self):
        self.assertTrue(self.serializer_data.is_valid())

class ArtifactViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artifact_data = {'t_string': 1, 'n_stock': 10, 'description': 'Test Artifact', 'price': 100.00}
        self.response = self.client.post(
            reverse(''),
            self.artifact_data,
            format="json"
        )

    def test_api_can_create_artifact(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_artifact(self):
        artifact = Artifact.objects.get()
        response = self.client.get(
            reverse('', kwargs={'pk': artifact.pk_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, artifact)
