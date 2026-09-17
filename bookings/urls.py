from django.urls import path
from bookings.views import *

app_name = "restaurants"

urlpatterns = [
    path('', catalog, name='index'),
    path('category/<int:category_id>', catalog, name='catalog'),
    path('page/<int:page_number>', catalog, name='page'),
    path('category/<int:category_id>/page/<int:page_number>', catalog, name='category_page'),
    path('booking/<int:restaurant_id>', booking, name='booking'),
    path('feedback/<int:restaurant_id>', feedback, name='feedback'),
    path('basket/', basket, name='basket'),
    path('basket-delete/<int:restaurant_id>', basket_delete, name='basket_delete'),
]
