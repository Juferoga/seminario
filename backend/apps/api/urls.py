from django.urls import path, include
from ..authuser import views

urlpatterns = [
  path('auth/generate_token/',views.CustomAuthToken.as_view()),
  path('user/',         include('apps.authuser.urls')),
  path("resource/",     include('apps.resources.urls')),
  path("artifact/",     include('apps.artifacts.urls')),
  path("place/",        include('apps.places.urls')),
  path("payment/",      include('apps.payments.urls')),
  path("reservation/",  include('apps.reservation.urls')),

]