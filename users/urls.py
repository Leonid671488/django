from django.urls import path
from users.views import *

app_name = "users"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('personal_account/', personal_account, name='personal_account'),
]
