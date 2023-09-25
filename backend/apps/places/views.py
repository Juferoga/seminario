from .models import Place
from rest_framework import viewsets, permissions
from .serializers import PlaceSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PlaceSerializer