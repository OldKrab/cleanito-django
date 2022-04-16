from django.contrib import admin

# Register your models here.
from .models import User, Service, Ad

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Ad)
