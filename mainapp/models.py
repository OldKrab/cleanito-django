import datetime

from django.db import models
from PIL import Image


class Service(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    def user_directory_path(self, filename):
        return 'user_{0}/{1}'.format(self.id, filename)

    name = models.TextField()
    login = models.TextField()
    password = models.TextField()
    phone = models.TextField()
    is_individual = models.BooleanField()
    image = models.ImageField(blank=True, upload_to=user_directory_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        img.thumbnail((90, 90))
        img.save(self.image.path)


class Ad(models.Model):
    def ad_directory_path(self, filename):
        return 'ad_{0}/{1}'.format(self.id, filename)

    user = models.ForeignKey(User, models.CASCADE)
    services = models.ManyToManyField(Service, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    price = models.IntegerField()
    city = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to=ad_directory_path)

    def save(self, *args, **kwargs):
        self.creation_date = datetime.datetime.now()
        super().save()

    def __str__(self):
        return self.name


