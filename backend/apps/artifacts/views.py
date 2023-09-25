from .models import Artifact
from rest_framework import viewsets, permissions
from .serializers import ArtifactSerializer

class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArtifactSerializer