from django.contrib import admin

# Register your models here.

from bookings.models import *

admin.site.register(RestaurantCategory)
admin.site.register(Restaurant)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Feedback)
