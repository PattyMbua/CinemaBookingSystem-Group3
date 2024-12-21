from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CinemaHallViewSet, ShowViewSet, CustomerViewSet, BookingViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('cinema-halls', CinemaHallViewSet)
router.register('shows', ShowViewSet)
router.register('customers', CustomerViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]