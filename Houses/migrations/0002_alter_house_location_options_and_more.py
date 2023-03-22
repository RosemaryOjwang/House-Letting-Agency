# Generated by Django 4.1.7 on 2023-03-21 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house_location',
            options={'ordering': ['locationName'], 'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterField(
            model_name='house_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
