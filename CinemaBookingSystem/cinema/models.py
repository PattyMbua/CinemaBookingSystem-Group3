from django.db import models

# Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()  # Movie duration (e.g., "02:30:00")
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g., 4.5/5

    def __str__(self):
        return self.title

# Showtime Model
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_seats = models.PositiveIntegerField(default=50)  # Limit seats per showtime

    def __str__(self):
        return f'{self.movie.title} at {self.start_time}'

# Seat Model
class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.showtime.seats.count() >= self.showtime.max_seats:
            raise ValueError("Maximum seat capacity reached.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Seat {self.seat_number} for {self.showtime.movie.title}'

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Booking Model
class Booking(models.Model):
    customer = models.ForeignKey(Customer, related_name='bookings', on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, related_name='bookings', on_delete=models.CASCADE)
    booked_seats = models.ManyToManyField(Seat)

    def __str__(self):
        return f'Booking by {self.customer.name} for {self.showtime}'
