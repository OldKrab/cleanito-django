# Generated by Django 4.0.3 on 2022-03-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_ad_creation_date_alter_ad_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='creation_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
