from django.shortcuts import render, HttpResponseRedirect
from bookings.models import Restaurant, RestaurantCategory, Booking, Feedback
from bookings.forms import BookingForm, FeedbackForm
from django.urls import reverse


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


def booking(request, restaurant_id):
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('restaurants:booking'))
    else:
        form = BookingForm()

    context = {
        "title": "Сеть моно-ресторанов | Бронирование",
        "restaurant": Restaurant.objects.get(id=restaurant_id),
        "feedbacks": Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(id=restaurant_id)),
        "form": form
    }

    avg = lambda lst: sum(lst) / len(lst)
    if context["feedbacks"]:
        context["rating"] = round(avg(list(map(lambda fb: fb.mark, context["feedbacks"]))), 1)
    else:
        context["rating"] = 0

    return render(request, "users/booking.html", context=context)


def feedback(request):
    avg = lambda lst: sum(lst) / len(lst)
    context = {
        "title": "Сеть моно-ресторанов | Отзыв",
        "restaurant": Restaurant.objects.get(address="Приморский бульвар, д. 67"),
        "feedbacks": Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(address="Приморский бульвар, д. 67"))
    }

    if context["feedbacks"]:
        context["rating"] = round(avg(list(map(lambda fb: fb.mark, Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(pk=context["restaurant"].pk))))), 1)
    else:
        context["rating"] = 0

    return render(request, "bookings/feedback.html", context=context)


def basket(request):
    context = {
        "basket": Booking.objects.filter(user=request.user)
    }
    return render(request, "bookings/basket.html", context)


def basket_add(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    user_basket = Booking.objects.filter(user=request.user, restaurant=restaurant)

    if not user_basket.exists():
        Booking.objects.craete(user=request.user, restaurant=restaurant)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_delete(request, booking_id):
    booking1 = Booking.objects.get(id=booking_id)
    booking1.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
