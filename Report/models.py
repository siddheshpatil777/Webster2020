from django.db import models
from Post.models import Post
from django.contrib.auth.models import User
# Create your models here.

class Report(models.Model):
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    Text=models.TextField(blank=False)
    Raised_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Raised_by