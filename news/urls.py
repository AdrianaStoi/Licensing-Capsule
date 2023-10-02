from . import views
from django.urls import path

urlpatterns = [
    path('base.html/', views.basePreview, name='base.html'),
    path("", views.RecentArticle.as_view(), name="home"),
    path('news.html/', views.newsPreview, name='news.html'),
]
