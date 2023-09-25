from rest_framework import serializers
from .models import Artifact

class ArtifactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artifact
    fields = (
      'pk_id', 't_name', 'n_stock', 'n_type',
      'd_created_at', 'd_updated_at', 't_description', 
      'n_price', 'b_status'
    )
    read_only_fields = ('pk_id', 'd_created_at', 'd_updated_at')
