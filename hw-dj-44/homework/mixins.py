from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('You are not authorized to view this page')
        return super().dispatch(request, *args, **kwargs)
