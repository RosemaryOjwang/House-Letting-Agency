# Generated by Django 4.1.7 on 2023-03-23 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0004_alter_house_details_multipleimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house_details',
            name='multipleimages',
        ),
        migrations.DeleteModel(
            name='MultipleImage',
        ),
    ]
