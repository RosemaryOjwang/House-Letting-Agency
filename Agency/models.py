from django.db import models

class UserRegister(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=6)
    confirm_password = models.CharField(max_length=10)

def __str__(self):
    return self.email
