from django.contrib import admin
from .models import Movie, CinemaHall, Show, Customer, Booking  # Import your models

# Register your models
admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(Show)
admin.site.register(Customer)
admin.site.register(Booking)
