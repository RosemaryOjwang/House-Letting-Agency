# Generated by Django 4.1.7 on 2023-03-23 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0002_multipleimage_alter_house_details_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_details',
            name='multipleimages',
            field=models.ForeignKey(default='img/no_image.png', on_delete=django.db.models.deletion.CASCADE, related_name='multiple_images', to='Houses.multipleimage'),
        ),
        migrations.AlterField(
            model_name='multipleimage',
            name='images',
            field=models.FileField(blank=True, default='img/no_image.png', null=True, upload_to='img'),
        ),
    ]
