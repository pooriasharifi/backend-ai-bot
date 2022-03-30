from django.db import models
from profiles.models import Profiles
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profiles,related_name='posts',on_delete=models.CASCADE)
