from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload='post/', default='default.png')
    like = models.ManyToManyField('users.User')
    published_date = models.DateTimeField(default=timezone.now)