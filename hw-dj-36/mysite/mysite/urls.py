from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.article_list, name='article_list'),
    path('articles/new/', views.create_article, name='create_article'),
]
