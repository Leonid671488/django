from django.urls import path
from bookings.views import *

app_name = "restaurants"

urlpatterns = [
    path('', catalog, name='index'),
    path('booking/', booking, name='booking'),
    path('feedback/', feedback, name='feedback'),
    path('basket/', basket, name='basket'),
    path('basket-add/<int:restaurant_id>', basket_add, name='basket_add'),
    path('basket-delete/<int:booking_id>', basket_delete, name='basket_delete'),
]
