from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

class SingleArticle(View):


    def get (self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "singlearticle.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )