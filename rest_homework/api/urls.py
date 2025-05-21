from django.urls import path
from .views import ProtectedView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='api-login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
