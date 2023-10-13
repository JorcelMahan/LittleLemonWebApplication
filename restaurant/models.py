from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    booking_date = models.DateField()
    number_of_guests = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title
