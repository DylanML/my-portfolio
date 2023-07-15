from django.db import models
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(datetime.datetime.now())
    image = models.ImageField(upload_to="blog/images")
