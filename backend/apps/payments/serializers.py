from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = (
      'pk_id', 'n_type',
      'd_created_at',  
      'b_status'
    )
    read_only_fields = ('pk_id', 'd_created_at')