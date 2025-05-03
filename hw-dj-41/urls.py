
from django.contrib import admin
from django.urls import path
from notifications import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('custom/', views.custom_message_view),
    path('sign/', views.signed_data_view),
    path('verify/<signed_value>/', views.verify_signed_data_view),
]
