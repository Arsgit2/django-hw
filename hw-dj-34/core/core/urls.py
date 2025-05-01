from django.urls import path
from . import views

urlpatterns = [
    path("articles/new/", views.create_article, name="create_article"),
    path("articles/", views.article_list, name="article_list"),
]
