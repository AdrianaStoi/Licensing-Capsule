from django.shortcuts import render
from django.views import generic
from .models import Article


def basePreview(request):
    return render(request, 'base.html')


class RecentArticle(generic.ListView):
    model= Article
    queryset = Article.objects.filter(
        status=1).order_by('created_on')[0:3]
    template_name = 'index.html'

