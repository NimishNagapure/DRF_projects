from pydoc import describe
from django.db import models

# Create your models here.

class Movie(models.Model):
    name= models.CharField(max_length=70)
    description = models.CharField(max_length=300)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name