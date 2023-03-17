from django.db import models
from django.urls import reverse

# Create your models here.
class House_Location(models.Model):
    
    location_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True)

    class Meta:
        ordering = ['location_name']
        indexes = [
           models.Index(fields=['location_name']),
       ]
        verbose_name = 'location'
        verbose_name_plural = 'locations'


    def __str__(self):
        return self.location_name
    
    def get_absolute_url(self):
        return reverse('Agency:house_list_by_location',
                       args=[self.slug])
    
#class Image(models.Model):
#    images = models.FileField()
#
#    def __str__(self):
#        return self.images
#    
#    def get_absolute_url(self):
#        return reverse('Agency:house_images_detail',
#                        args=[self.id, self.slug])

    
class House_Details(models.Model):
    #CATEGORY_CHOICES = [
   #    ("beds", "Bedsitter"),
   #     ("1 br", "One bedroom"),
   #    ("2 br", "Two bedroom"),
   #     ("3 br", "Three bedroom"),
   #     ("4 br", "Four bedroom"),
   # ]
    location = models.ForeignKey(House_Location,
                                 related_name='details',
                                 db_constraint=True,
                                 on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)#, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=255)
    thumbnail = models.ImageField(upload_to='img')
    #images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='house_view')
    #image = models.ImageField(upload_to='products/%Y/%m/%d')

    description = models.TextField()
    rent_amount = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category_name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['category_name']),
            models.Index(fields=['-posted'])
        ]

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('Agency:house_detail',
                        args=[self.id, self.slug])

