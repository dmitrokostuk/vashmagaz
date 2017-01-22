from django.db import models

# Create your models here.

class Apartment(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=250)