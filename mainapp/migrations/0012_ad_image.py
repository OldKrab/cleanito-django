# Generated by Django 4.0.3 on 2022-03-17 13:29

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_delete_adimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, upload_to=mainapp.models.Ad.ad_directory_path),
        ),
    ]
