# Generated by Django 4.1.7 on 2023-03-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0011_image_delete_multipleimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_details',
            name='thumbnail',
            field=models.ImageField(upload_to='img'),
        ),
    ]
