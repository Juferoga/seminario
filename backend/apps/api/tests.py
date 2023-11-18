from django.test import TestCase
from django.urls import reverse

class APITests(TestCase):
  
  def test_home_view(self):
    response = self.client.get(reverse(''))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "API")

  def test_integration_view(self):
    response = self.client.get(reverse('integration-test'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Lista de Recursos")
