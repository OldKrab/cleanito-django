from .models import User


def current_user(request):
    return {'user': User.objects.first()}
