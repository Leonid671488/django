from django.db import models

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
