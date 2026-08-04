from django.shortcuts import render
from bookings.models import Restaurant, RestaurantCategory
from users.models import Feedback

# Create your views here.

def index(request):
    context = {
        "title": "Сеть моно-ресторанов | Главная",
        "categories": RestaurantCategory.objects.all()
    }

    return render(request, "bookings/index.html", context=context)


def catalog(request):
    avg = lambda lst: sum(lst) / len(lst)
    context = {
        "title": "Сеть моно-ресторанов | Выбор ресторана",
        "restaurants": [],
        "categories": RestaurantCategory.objects.all()
    }

    for restaurant in Restaurant.objects.all():
        feedbacks = list(map(lambda fb: fb.mark, Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(pk=restaurant.pk))))
        if feedbacks:
            context["restaurants"].append((restaurant, round(avg(feedbacks), 1)))
        else:
            context["restaurants"].append((restaurant, 0))

    return render(request, "bookings/catalog.html", context=context)

