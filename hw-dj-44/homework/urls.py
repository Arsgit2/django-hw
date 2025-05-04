from django.urls import path
from .views import HomeworkListView

urlpatterns = [
    path('', HomeworkListView.as_view(), name='homework_list'),
]
