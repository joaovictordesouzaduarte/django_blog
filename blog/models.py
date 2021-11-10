from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length= 255, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
