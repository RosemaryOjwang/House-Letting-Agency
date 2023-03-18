from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class House_Location(models.Model):
    location = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
