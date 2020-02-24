from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    f_name = models.CharField(max_length=10)
    occupation = models.CharField(max_length=10)
    f_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.f_name

class Account(models.Model):
    pass
