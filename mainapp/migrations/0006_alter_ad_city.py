# Generated by Django 4.0.3 on 2022-03-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='city',
            field=models.CharField(max_length=200),
        ),
    ]
