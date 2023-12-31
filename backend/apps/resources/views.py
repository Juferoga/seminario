from .models import Resource
from rest_framework import viewsets, permissions
from .serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResourceSerializer