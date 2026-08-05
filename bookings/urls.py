from django.urls import path
from bookings.views import *

app_name = "restaurants"

urlpatterns = [
    path('', catalog, name='index'),
    path('booking/', booking, name='booking'),
    path('feedback/', feedback, name='feedback'),
]
