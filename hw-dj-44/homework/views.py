from django.shortcuts import render
from .models import HomeworkModel
from .mixins import CustomLoginRequiredMixin
from django.views.generic import ListView

class HomeworkListView(CustomLoginRequiredMixin, ListView):
    model = HomeworkModel
    template_name = 'homework/index.html'
    context_object_name = 'homework_items'
