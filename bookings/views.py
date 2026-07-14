from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "Сеть моно-ресторанов | Главная"
    }

    return render(request, "bookings/index.html", context=context)


def restaurants(request):
    context = {
        "title": "Сеть моно-ресторанов | Выбор ресторана",
        "restaurants": [
            {"cuisine": "Рыба", "rating": 4.9, "address": "...", "image": "https://img.freepik.com/premium-photo/beautiful-old-bildings-marseille_948265-267099.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "...", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Азия", "rating": 5.0, "address": "...", "image": "https://avatars.mds.yandex.net/i?id=50fcdc06bacd4542e321b8d5b0aff052_l-5254479-images-thumbs&n=13"},
        ]
    }

    return render(request, "bookings/restaurants.html", context=context)
