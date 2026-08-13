from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User
from bookings.models import Booking, Feedback, Restaurant
from django.contrib import auth
from django.urls import reverse

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


def personal_account(request):
    avg = lambda lst: sum(lst) / len(lst)
    context = {
        "title": "Сеть моно-ресторанов | Личный кабинет",
        "restaurants": []
    }

    # restaurants = list(map(lambda bk: bk.restaurant, Booking.objects.filter(user=User.objects.get(email="burmalda67@gmail.com"))))
    # for restaurant in restaurants:
    #     feedbacks = list(map(lambda fb: fb.mark, Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(pk=restaurant.pk))))
    #     if feedbacks:
    #         context["restaurants"].append((restaurant, round(avg(feedbacks), 1)))
    #     else:
    #         context["restaurants"].append((restaurant, 0))

    return render(request, "users/personal_account.html", context=context)


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
