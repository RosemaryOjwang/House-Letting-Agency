# Generated by Django 4.1.7 on 2023-04-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0002_alter_house_details_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_details',
            name='slug',
            field=models.SlugField(max_length=155),
        ),
    ]
