from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "Сеть моно-ресторанов | Главная"
    }

    return render(request, "bookings/index.html", context=context)


def catalog(request):
    context = {
        "title": "Сеть моно-ресторанов | Выбор ресторана",
        "restaurants": [
            {"cuisine": "Рыба", "rating": 4.9, "address": "Приморский бульвар, д. 8", "image": "https://img.freepik.com/premium-photo/beautiful-old-bildings-marseille_948265-267099.jpg?semt=ais_hybrid"},
            {"cuisine": "Рыба", "rating": 4.9, "address": "Приморский бульвар, д. 8", "image": "https://img.freepik.com/premium-photo/beautiful-old-bildings-marseille_948265-267099.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "пр. Просвещения, д. 45", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "пр. Просвещения, д. 45", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "пр. Просвещения, д. 45", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "пр. Просвещения, д. 45", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Гриль", "rating": 4.8, "address": "пр. Просвещения, д. 45", "image": "https://img.freepik.com/free-photo/luxury-dining-room-with-elegant-decor-lighting-generated-by-ai_24640-84695.jpg?semt=ais_hybrid"},
            {"cuisine": "Азия", "rating": 5.0, "address": "ул. Набережная, д. 12", "image": "https://avatars.mds.yandex.net/i?id=50fcdc06bacd4542e321b8d5b0aff052_l-5254479-images-thumbs&n=13"}
        ]
    }
    context["cuisine_types"] = list(map(lambda restaurant: restaurant["cuisine"], context["restaurants"]))

    return render(request, "bookings/catalog.html", context=context)


def register(request):
    context = {
        "title": "Сеть моно-ресторанов | Регистрация"
    }

    return render(request, "bookings/register.html", context=context)


def login(request):
    context = {
        "title": "Сеть моно-ресторанов | Вход"
    }

    return render(request, "bookings/login.html", context=context)


def booking(request):
    context = {
        "title": "Сеть моно-ресторанов | Бронирование",
        "restaurant": {"cuisine": "Азия", "rating": 5.0, "address": "ул. Набережная, д. 12", "image": "https://avatars.mds.yandex.net/i?id=50fcdc06bacd4542e321b8d5b0aff052_l-5254479-images-thumbs&n=13"}
    }

    return render(request, "bookings/booking.html", context=context)
