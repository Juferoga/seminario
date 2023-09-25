from django.urls import include, path
from rest_framework import routers
from .views import ArtifactViewSet

router = routers.DefaultRouter()

router.register("", ArtifactViewSet)

urlpatterns = [
    path('',include(router.urls))
]