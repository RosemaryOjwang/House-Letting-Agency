from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Pay(models.Model):
    user = models.ForeignKey(User, default=999, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500, default=1)
 
@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        Pay.objects.create(user=instance)