from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class House_Location(models.Model):
    locationName = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True)
    
    class Meta:
        ordering = ['locationName']
        indexes = [
            models.Index(fields=['locationName']),
        ]
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.locationName
    
    def get_absolute_url(self):
        return reverse('Agency:house_list_by_Location',
                       args=[self.slug])
    
    
class House_Details(models.Model):
    user = models.ForeignKey(User, 
                             related_name='houses',
                             on_delete=models.CASCADE)
    location = models.ForeignKey(House_Location,
                                 related_name='houses',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=155, unique=True) 
    thumbnail = models.ImageField(upload_to='img')
    
    description = models.TextField(max_length=1000)
    monthly_rent = models.DecimalField(max_digits=10,
                                       decimal_places=2)
    available = models.BooleanField(default=True)
    owners_contact = models.DecimalField(max_digits=10,
                                         decimal_places=0)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Houses:house_detail', args=[self.id, self.slug])
    
class MultipleImage(models.Model):
    house = models.ForeignKey(House_Details, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='img')

    def __str__(self):
        return self.house.title
    