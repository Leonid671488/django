from django.urls import path
from bookings.views import *

app_name = "restaurants"

urlpatterns = [
    path('', catalog, name='index'),
    path('booking/<int:restaurant_id>', booking, name='booking'),
    path('feedback/<int:restaurant_id>', feedback, name='feedback'),
    path('basket/', basket, name='basket'),
    path('basket-delete/<int:restaurant_id>', basket_delete, name='basket_delete'),
]
