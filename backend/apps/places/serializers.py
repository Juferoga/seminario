from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place
    fields = (
      'pk_id', 't_name', 't_observation', 'n_type',
      'd_created_at', 'd_updated_at', 't_description', 
      'n_price', 'b_status'
    )
    read_only_fields = ('pk_id', 'd_created_at', 'd_updated_at')
