from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.jpeg')
    like = models.ManyToManyField(User, related_name='like_posts', blank=True)
    published_date = models.DateTimeField(default=timezone.now)