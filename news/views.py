from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article, ProductFamily 
from django.db.models import Q


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
                "article": article,
                "comments": comments,
                "liked": liked
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


def product_family_list_view(request):
    product_names = ProductFamily.objects.all()

    context = {
        'product_names':product_names
    }
    return render(request, 'productfamilylist.html', context)

def article_by_product_family(request, product_name_id):
    product_family = ProductFamily.objects.get(pk=product_name_id)
    articles = Article.objects.filter(product_name=product_family)
    return render(request, 'productfamily.html', {'product_family':product_family, 'articles':articles})
