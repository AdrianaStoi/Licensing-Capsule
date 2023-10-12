from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Article, ProductFamily, Comment 
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages



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
        product_id = self.request.GET.get('product_name__id__exact')
        return Article.objects.filter(product_name=product_id, status=1).order_by('-created_on')

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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment.user = request.user
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "singlearticle.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "commented_form": comment_form,
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


def editComment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = None
    article_slug= comment.article.slug

    if request.user == comment.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return redirect('singlearticle', slug=article_slug)
            else:
                comment_form = CommentForm(instance=comment)
                
    return render(request, 'editcomment.html', {'comment_form':comment_form, 'comment':comment})

def deleteComment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    article_slug= comment.article.slug

    if request.method == 'POST':
        if request.user == comment.user:
            comment.delete()
            messages.success(request, 'Comment deleted successfully.')
            return redirect('singlearticle', slug=article_slug)

    return render(request, 'confirmdeletecomment.html', {'comment':comment})