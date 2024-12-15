from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        app_label = 'blog'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
