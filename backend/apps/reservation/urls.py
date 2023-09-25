from django.urls import include, path
from rest_framework import routers
from .views import ReservationViewSet

router = routers.DefaultRouter()

router.register("", ReservationViewSet)

urlpatterns = [
  path('',include(router.urls))
]