from django.db import models
from django.contrib.auth.models import AbstractUser
from bookings.models import Restaurant
import datetime

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to="users_media", blank=True)


class Booking(models.Model):
    time = models.DateTimeField()
    peoples = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=16, default="Простаивает")
    booking_time = models.TextField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
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

