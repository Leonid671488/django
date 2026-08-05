from django.shortcuts import render
from users.models import User
from bookings.models import Booking, Feedback, Restaurant


# Create your views here.

def register(request):
    context = {
        "title": "Сеть моно-ресторанов | Регистрация"
    }

    return render(request, "users/register.html", context=context)


def login(request):
    context = {
        "title": "Сеть моно-ресторанов | Вход"
    }

    return render(request, "users/login.html", context=context)


def personal_account(request):
    avg = lambda lst: sum(lst) / len(lst)
    context = {
        "title": "Сеть моно-ресторанов | Личный кабинет",
        "user": User.objects.get(phone="+7 999 123-45-67"),
        "restaurants": []
    }

    restaurants = list(map(lambda bk: bk.restaurant, Booking.objects.filter(user=User.objects.get(email="burmalda67@gmail.com"))))
    for restaurant in restaurants:
        feedbacks = list(map(lambda fb: fb.mark, Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(pk=restaurant.pk))))
        if feedbacks:
            context["restaurants"].append((restaurant, round(avg(feedbacks), 1)))
        else:
            context["restaurants"].append((restaurant, 0))

    return render(request, "users/personal_account.html", context=context)
