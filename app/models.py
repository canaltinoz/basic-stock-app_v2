from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    balance=models.PositiveIntegerField(default=100000)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)

    def __str__(self):
        return self.username
    

class Flavour(models.Model):

    def __str__(self):
        return self.title
    
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=20)
    quantity=models.PositiveIntegerField(default=0)

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
