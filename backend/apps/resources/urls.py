from django.urls import include, path
from rest_framework import routers
from .views import ResourceViewSet

router = routers.DefaultRouter()

router.register("", ResourceViewSet)

urlpatterns = [
    path('',include(router.urls))
]