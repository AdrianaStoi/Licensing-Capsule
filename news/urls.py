from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecentArticle.as_view(), name="home"),
    path("news/", views.ListArticle.as_view(), name="news"),
    path("<slug:slug>/", views.SingleArticle.as_view(), name="singlearticle"),
    path("search", views.SearchArticle.as_view(), name="search"),
    path("productfamilylist/", views.product_family_list_view, name="product-family-list"),
    path("productfamily/<int:product_name_id>", views.article_by_product_family, name="articlesbyproductfamily"),
]
