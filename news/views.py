from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article, ProductFamily 
from django.db.models import Q
from .forms import CommentForm


class RecentArticle(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')[:3]
    template_name = 'index.html' 
    context_object_name = 'recent_articles'
    extra_context = {"product_family": ProductFamily.objects.all()}

class ArticlesByProductFamily(generic.ListView):
    model = Article
    template_name = 'productfamily.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        product_name = self.kwargs['product_name']
        return Article.objects.filter(product_name=product_name)


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
                "article": article,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class SearchArticle(generic.ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'search_articles'


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter( Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(article_body__icontains=query, status=1)).order_by('-created_on')
        else:
            return Article.objects.none()


