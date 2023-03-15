from django.shortcuts import redirect
from django.conf import settings


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Prevent non-authenticated users from accessing the profile page
        if request.path.startswith('/profile'):
            if not request.user.is_authenticated:
                return redirect(settings.LOGIN_URL)
        else:
            return None
