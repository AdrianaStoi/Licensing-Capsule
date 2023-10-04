from django.shortcuts import render
from django.views import generic
from .models import Article


def newsPreview(request):
    return render(request, 'news.html')

class RecentArticle(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')[:3]
    template_name = 'index.html' 
    context_object_name = 'recent_articles'
