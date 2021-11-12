from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length= 255, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ("-create", )
    
    def __str__(self):
        return self.title
    

