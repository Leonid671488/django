from django.db import models
from users.models import User
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
    menu = models.FileField(upload_to="restaurants_menu", blank=True)

    def __str__(self):
        return f"{self.category.name} | {self.address}"


class Booking(models.Model):
    time = models.DateTimeField()
    peoples = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=16, default="Простаивает")
    booking_time = models.TextField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} | {self.status}"


class Feedback(models.Model):
    mark = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booking.user.username} | {self.mark}"


