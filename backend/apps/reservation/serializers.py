from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reservation
    fields = (
      'pk_id', 'd_reservation',
      'd_created_at', 'b_status',
      'fk_customer', 'fk_student',
      'fk_employee'
    )
    read_only_fields = ('pk_id', 'd_created_at')