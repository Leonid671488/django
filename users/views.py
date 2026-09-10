from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User
from bookings.models import Booking, Feedback, Restaurant
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from project.bookings.views import feedback


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {
        "title": "Сеть моно-ресторанов | Регистрация",
        "form": form
    }

    return render(request, "users/register.html", context=context)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:personal_account'))
    else:
        form = UserLoginForm()

    context = {
        "title": "Сеть моно-ресторанов | Вход",
        "form": form
    }

    return render(request, "users/login.html", context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required()
def personal_account(request):
    avg = lambda lst: sum(lst) / len(lst)
    context = {
        "title": "Сеть моно-ресторанов | Личный кабинет",
        "restaurants": []
    }

    bookings = Booking.objects.filter(user=request.user)
    for booking in bookings:
        restaurant = booking.restaurant
        feedbacks = Feedback.objects.filter(booking=booking)
        if feedbacks:
            rating = round(avg(list(map(lambda fb: fb.mark, feedbacks))), 1)
        else:
            rating = 0
        context["restaurants"].append([restaurant, rating])

    return render(request, "users/personal_account.html", context=context)


@login_required()
def change_profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST ,instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:personal_account'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "title": "Сеть моно-ресторанов | Редактирование профиля",
        "form": form
    }

    return render(request, "users/change_profile.html", context=context)
