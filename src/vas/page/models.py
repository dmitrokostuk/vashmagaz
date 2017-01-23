from django.db import models

# Create your models here.

class Apartment(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=250)

    def __unicode__(self):
        return u"%s "%(self.title)

    def __str__(self):
        return u"%s %s "%(self.link,self.title)