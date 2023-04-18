from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User,
                                related_name='userprofile',
                                on_delete=models.CASCADE)
    user_amount = models.IntegerField(default=300)
    verbose_name = 'userprofile'
    def __str__(self):
        return self.user.username
    
