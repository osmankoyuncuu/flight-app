from django.urls import path
from rest_framework import routers
from .views import FlightView, ReservationView

router = routers.DefaultRouter()
router.register("flights", FlightView, basename="flights")
router.register("reservations", ReservationView)

urlpatterns = [
]
urlpatterns += router.urls