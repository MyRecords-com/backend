from django.db import models
from django.contrib.auth.models import User
# Create your models here.
  
  
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)
    usr_type = models.CharField(max_length=50)
    setup = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return f'{self.user}'

class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rec_format = models.CharField(max_length=50)
    released = models.IntegerField()
    genre = models.CharField(max_length=50)
    style = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.name}'

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    records = models.ManyToManyField(Record)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    rating = models.CharField(max_length=20)
    comment = models.TextField()
