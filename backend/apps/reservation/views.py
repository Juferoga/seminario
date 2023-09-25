from .models import Reservation
from rest_framework import viewsets, permissions
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ReservationSerializer