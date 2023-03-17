# Generated by Django 4.1.7 on 2023-03-07 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0002_rename_price_house_details_rent_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_details',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Agency.house_location'),
        ),
    ]