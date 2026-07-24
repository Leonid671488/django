from django.db import models
import datetime

# Create your models here.

class RestaurantCategory(models.Model):
    image = models.ImageField(upload_to="restaurants_media", blank=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    image = models.ImageField(upload_to="restaurants_media", blank=True)
    address = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} | {self.address}"


class User(models.Model):
    avatar = models.ImageField(upload_to="users_media", blank=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} | {self.phone}"


class Booking(models.Model):
    time = models.DateTimeField()
    peoples = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=16, default="Простаивает")
    booking_time = models.DateTimeField(default=datetime.datetime.now())
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} | {self.status}"


class Feedback(models.Model):
    mark = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booking.user.name} | {self.mark}"
