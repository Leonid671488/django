from django.contrib import admin

# Register your models here.

from bookings.models import *

admin.site.register(RestaurantCategory)
# admin.site.register(Restaurant)
admin.site.register(Booking)
admin.site.register(Feedback)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("category", "address")
    list_filter = ("category",)
    search_fields = ("address",)
    ordering = ("category",)
    fields = (("category", "address"), "image", "menu")


class BasketAdmin(admin.TabularInline):
    model = Booking
    readonly_fields = ("booking_time",)
