# Generated by Django 4.0.3 on 2022-03-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='services',
            field=models.ManyToManyField(blank=True, to='mainapp.service'),
        ),
    ]
