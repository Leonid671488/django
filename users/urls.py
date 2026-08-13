from django.urls import path
from users.views import *

app_name = "users"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change_profile/', change_profile, name='change_profile'),
    path('personal_account/', personal_account, name='personal_account'),
]
