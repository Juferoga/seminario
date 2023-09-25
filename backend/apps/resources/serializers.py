from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resource
    fields = (
      'pk_id', 't_name', 't_description', 
      'd_created_at', 'd_updated_at', 
      'n_price', 'b_status'
    )
    read_only_fields = ('pk_id', 'd_created_at', 'd_updated_at')
