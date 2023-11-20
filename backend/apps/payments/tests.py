from django.test import TestCase
from .models import Payment
from .serializers import PaymentSerializer
from .choices import PaymentTypeChoices
from datetime import datetime
from ..authuser.models import Customer

class PaymentModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='test_user',
            email='test@example.com',
            password='test_password'
        )

        self.payment = Payment.objects.create(
            n_type=PaymentTypeChoices.CREDIT,
            fk_customer=self.customer
        )

    def test_payment_str_representation(self):
        self.assertEqual(
            str(self.payment),
            f"Payment {self.payment.pk_id} - Type: {self.payment.get_n_type_display()}"
        )

    def test_payment_model_fields(self):
        self.assertEqual(self.payment.n_type, PaymentTypeChoices.CREDIT)
        self.assertEqual(self.payment.fk_customer, self.customer)
