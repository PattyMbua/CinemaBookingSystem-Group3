from django.db import models

# Entities: Movie, CinemaHall, Show, Customer, Booking.

# Relationships:
#================
# Show links Movie and CinemaHall.
# Booking links Show and Customer.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # duration in minutes
    release_date = models.DateField()

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name='shows')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} in {self.cinema_hall.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.customer.name} ({self.seats} seats)"