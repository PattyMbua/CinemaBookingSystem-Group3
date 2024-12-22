from rest_framework import viewsets  # For ViewSet functionality
from rest_framework.exceptions import ValidationError  # For custom validation
from .models import Movie, CinemaHall, Show, Customer, Booking  # Models
from .serializers import (  # Serializers
    MovieSerializer,
    CinemaHallSerializer,
    ShowSerializer,
    CustomerSerializer,
    BookingSerializer,
)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        show = serializer.validated_data['show']
        seats_requested = serializer.validated_data['seats']
        # Calculate total booked seats for the show
        total_seats = sum(booking.seats for booking in show.bookings.all())
        # Check if adding new seats exceeds the cinema hall capacity
        if total_seats + seats_requested > show.cinema_hall.capacity:
            raise ValidationError("Cannot book seats: Exceeds cinema hall capacity.")
        serializer.save()
