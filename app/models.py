from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    balance=models.PositiveIntegerField(default=100000)

class Flavour(models.Model):
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=20)
    quantity=models.PositiveIntegerField(default=0)

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
