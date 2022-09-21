from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=50) 
    title = models.CharField(max_length=100) 
    rating = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    review = models.TextField()
