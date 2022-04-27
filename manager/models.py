from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    pass

    # add additional fields in here

    def __str__(self):
        return self.username


class Level(models.IntegerChoices):
    low = 0, 'Low'
    medium = 1, 'Medium'
    high = 2, 'High'


class Lead(models.Model):
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    finance = models.IntegerField(choices=Level.choices)
    family = models.IntegerField(choices=Level.choices)
    english = models.IntegerField(choices=Level.choices)
    note = models.TextField()
    status = models.BooleanField(default=False)


class Task(models.Model):
    date = models.DateTimeField()
    description = models.TextField()
    staff = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(default=False)
