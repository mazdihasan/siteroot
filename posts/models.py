from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=150, null=True)
    post_slug = models.SlugField(null=True)
    post_body = models.TextField(null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    post_author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    post_views = models.IntegerField(default=1)
    post_image = models.ImageField()
