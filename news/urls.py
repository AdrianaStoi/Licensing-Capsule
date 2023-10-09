from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecentArticle.as_view(), name="home"),
    path("news/", views.ListArticle.as_view(), name="news"),
    path("<slug:slug>/", views.SingleArticle.as_view(), name="singlearticle"),
    path("search", views.SearchArticle.as_view(), name="search"),
    path('product/<str:product_name>/', views.ArticlesByProductFamily.as_view(), name='articlesbyproductfamily'),
]
