from django.contrib.auth.models import User
from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    prix = models.IntegerField(default=0, )

    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name


class Gestionaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields for Gestionaire here


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=255)


class Livreur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilite = models.BooleanField(default=True)
    matriculeMoto = models.CharField(max_length=50)
