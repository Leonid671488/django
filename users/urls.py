from django.urls import path
from users.views import *

app_name = "users"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('booking/', booking, name='booking'),
    path('feedback/', feedback, name='feedback'),
    path('personal_account/', personal_account, name='personal_account'),
]
