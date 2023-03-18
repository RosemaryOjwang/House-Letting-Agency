from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class House_Location(models.Model):
    location = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True)
    
    class Meta:
        ordering = ['location']
        indexes = [
            models.Index(fields=['location']),
        ]
        verbose_name = 'House Location'
        verbose_name_plural = 'House Locations'

    def __str__(self):
        return self.location
