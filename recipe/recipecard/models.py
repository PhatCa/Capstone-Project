from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredient = models.TextField()
    instructions = models.TextField()
    picture = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT,default=None)


    def __str__(self):
        return self.name