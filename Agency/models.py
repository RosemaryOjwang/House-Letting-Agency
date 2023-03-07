from django.db import models

# Create your models here.
class House_Location(models.Model):
    
    location_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'location'
        verbose_name_plural = 'locations'


    def __str__(self):
        return self.location_name
    
class House_Details(models.Model):
    CATEGORY_CHOICES = [
        ("1 br", "One bedroom"),
        ("2 br", "Two bedroom"),
        ("3 br", "Three bedroom")
    ]
    AVAILABILITY_CHOICES = [
        ("Y", "Yes"),
        ("N", "No")
    ]
    location = models.ForeignKey(House_Location,
                                 related_name='locations',
                                 on_delete=models.CASCADE)
    category_name = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['category_name']),
            models.Index(fields=['-posted'])
        ]

    def __str__(self):
        return self.category_name