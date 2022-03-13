from mainapp.models import *

a = User.objects.get(name='boop')
print(a)