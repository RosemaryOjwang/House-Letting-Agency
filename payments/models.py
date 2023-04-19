from django.db import models
from accounts.models import User_Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Pay(models.Model):
    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500, default=1)
 
@receiver(post_save, sender=User_Profile)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        Pay.objects.create(user=instance)