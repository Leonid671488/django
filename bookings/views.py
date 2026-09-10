from django.shortcuts import render, HttpResponseRedirect
from bookings.models import Restaurant, RestaurantCategory, Booking, Feedback
from bookings.forms import BookingForm, FeedbackForm
from django.contrib.auth.decorators import login_required
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


@login_required()
def booking(request, restaurant_id):
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.restaurant = Restaurant.objects.get(id=restaurant_id)
            booking_instance.user =  request.user
            booking_instance.save()

            return HttpResponseRedirect(reverse('restaurants:basket'))
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

    return render(request, "bookings/booking.html", context=context)


@login_required()
def feedback(request, restaurant_id):
    if request.method == "POST":
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback_instance = form.save(commit=False)
            feedback_instance.booking = Booking.objects.get(user=request.user, restaurant=Restaurant.objects.get(id=restaurant_id))
            feedback_instance.save()

            return HttpResponseRedirect(reverse('users:personal_account'))
    else:
        form = FeedbackForm()

    context = {
        "title": "Сеть моно-ресторанов | Отзыв",
        "restaurant": Restaurant.objects.get(id=restaurant_id),
        "feedbacks": Feedback.objects.filter(booking__restaurant=Restaurant.objects.get(id=restaurant_id)),
        "form": form
    }

    avg = lambda lst: sum(lst) / len(lst)
    if context["feedbacks"]:
        context["rating"] = round(avg(list(map(lambda fb: fb.mark, context["feedbacks"]))), 1)
    else:
        context["rating"] = 0

    return render(request, "bookings/feedback.html", context=context)


@login_required()
def basket(request):
    context = {
        "basket": Booking.objects.filter(user=request.user)
    }
    return render(request, "bookings/basket.html", context)
