from django.shortcuts import render
from django.views import generic
from .models import Article


class RecentArticle(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')[:3]
    template_name = 'index.html' 
    context_object_name = 'recent_articles'

class ListArticle(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')
    template_name = 'news.html' 
    context_object_name = 'all_articles'
    paginate_by = 5