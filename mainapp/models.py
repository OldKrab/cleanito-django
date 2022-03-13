from django.db import models


class Image(models.Model):
    path = models.TextField()

    def __str__(self):
        return self.path


class Service(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.TextField()
    login = models.TextField()
    password = models.TextField()
    phone = models.TextField()
    is_individual = models.BooleanField()
    image = models.ForeignKey(Image, models.RESTRICT)

    def __str__(self):
        return self.name


class Ad(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    images = models.ManyToManyField(Image)
    services = models.ManyToManyField(Service)
    name = models.TextField()
    description = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    price = models.IntegerField()
    city = models.TextField()

    def __str__(self):
        return self.name
