from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


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
    
class House_Details(models.Model):
    user = models.ForeignKey(User,
                             related_name='locations',
                             on_delete=models.CASCADE)
    location = models.ForeignKey(House_Location,
                                 related_name='locations',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='img')
    description = models.TextField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10,
                                       decimal_places=2)
    available = models.BooleanField(default=True)
    owners_contact = PhoneField(help_text='Enter contact phone number')
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title