from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class LottoDraw(models.Model):
    numbers = models.CharField(max_length=255)
