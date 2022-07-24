from django.db import models
from django.contrib.auth.models import User
# Create your models here.
  
  
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    records = models.ManyToManyField(Record, on_delete=Models.CASCADE)

class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rec_format = models.CharField(max_length=50)
    released = models.IntegerField()
    genre = models.CharField(max_length=50)
    style = models.CharField(max_length=50)

class Rating(models.Model):
    rating = models.CharField()