from . import views
from django.urls import path
from django.views.defaults import page_not_found

urlpatterns = [
    path("", views.RecentArticle.as_view(), name="home"),
    path("news/", views.ListArticle.as_view(), name="news"),
    path("<slug:slug>/", views.SingleArticle.as_view(), name="singlearticle"),
    path("search", views.SearchArticle.as_view(), name="search"),
    path('product/article/', views.ArticlesByProductFamily.as_view(), name='articlesbyproductfamily'),
    path("editcomment/<int:comment_id>", views.editComment, name="editcomment"),
    path("deletecomment/<int:comment_id>", views.deleteComment, name="deletecomment"),
    path("confirmdeletecomment/<int:comment_id>", views.deleteComment, name="confirmdeletecomment"),
    path("like/<slug:slug>", views.ArticleLike.as_view(), name="articlelike"),
    path("<path:path>", page_not_found, name="page_not_found"),
]
