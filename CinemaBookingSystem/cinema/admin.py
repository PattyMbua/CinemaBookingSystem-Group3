from django.contrib import admin

# Register your models here.
from .models import Movie, Showtime, Seat, Customer, Booking

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Seat)
admin.site.register(Customer)
admin.site.register(Booking)
