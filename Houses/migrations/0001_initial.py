# Generated by Django 4.1.7 on 2023-03-22 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=155, unique=True)),
                ('thumbnail', models.ImageField(upload_to='img')),
                ('description', models.TextField(max_length=1000)),
                ('monthly_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('owners_contact', models.DecimalField(decimal_places=0, max_digits=10)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='House_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'ordering': ['locationName'],
            },
        ),
        migrations.AddIndex(
            model_name='house_location',
            index=models.Index(fields=['locationName'], name='Houses_hous_locatio_c727ec_idx'),
        ),
        migrations.AddField(
            model_name='house_details',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Houses.house_location'),
        ),
        migrations.AddField(
            model_name='house_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
