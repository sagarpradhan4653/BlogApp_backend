from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogger(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='post_images', null=True, blank=True)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title



