from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, ProductFamily, Comment
from django.db.models import Q, Count
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class RecentArticle(generic.ListView):
    """
    This view lists 3 of the most recent articles.
    It includes also an extra_context
    that lists all Product Family names.
    """
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')[:3]
    template_name = 'index.html'
    context_object_name = 'recent_articles'
    extra_context = {"product_family": ProductFamily.objects.all()}

    def get_context_data(self, **kwargs):
        """
        The function will count likes and comments
        and display 2 of the most liked articles
        and 1 of the most comment article.
        """
        context = super().get_context_data(**kwargs)

        most_liked_articles = (
            Article.objects
            .annotate(like_count=Count('likes'))
            .order_by('-like_count')[:2]
        )

        most_commented_articles = (
            Article.objects
            .annotate(comment_count=Count('comments'))
            .order_by('-comment_count')[:1]
        )

        context['most_liked_articles'] = most_liked_articles
        context['most_commented_articles'] = most_commented_articles
        return context


class ArticlesByProductFamily(generic.ListView):
    """
    This view will display the articles by product name.
    """
    model = Article
    template_name = 'productfamily.html'
    context_object_name = 'articles'

    def get_queryset(self):
        product_id = self.request.GET.get('product_name__id__exact')
        return Article.objects.filter(
            product_name=product_id,
            status=1
        ).order_by('-created_on')


class ListArticle(generic.ListView):
    """
    This view will display all articles available on the site
    paginate by 3 articles.
    """
    model = Article
    queryset = Article.objects.filter(
        status=1).order_by('-created_on')
    template_name = 'news.html'
    context_object_name = 'all_articles'
    paginate_by = 3


class SingleArticle(View, LoginRequiredMixin):
    """
    This view will display a single article with status 1-'Published'.
    It will also display the approved comments and likes.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = (
            article
            .comments
            .filter(approved=True)
            .order_by("-created_on")
        )
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
        """
        This method invoked when a POST request is initiated
        on the view through the comment form
        The comment form is displayed
        when user is logged in.
        """
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = (
            article
            .comments
            .filter(approved=True)
            .order_by("-created_on")
        )
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
    """
    This view will search by the query input
    and list articles if any available.
    """
    model = Article
    template_name = 'search.html'
    context_object_name = 'search_articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) |
                Q(excerpt__icontains=query) |
                Q(article_body__icontains=query, status=1)
            ).order_by('-created_on')
        else:
            return Article.objects.none()


@login_required
def editComment(request, comment_id):
    """
    This function will allow comment owner
    to edit their comment and save it.
    User must be logged in to access it.
    """
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    comment_form = None
    article_slug = comment.article.slug

    if request.user == comment.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(
                    request,
                    'You have edited the comment successfully.'
                )
                return redirect('singlearticle', slug=article_slug)
            else:
                comment_form = CommentForm(instance=comment)

    context = {
        'comment_form': comment_form,
        'comment': comment,
    }
    return render(request, 'editcomment.html', context)


@login_required
def deleteComment(request, comment_id):
    """
    This function will allow comment owner
    to delete their comment and save it.
    User must be logged in to access it.
    """
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    article_slug = comment.article.slug

    if request.method == 'POST':
        if request.user == comment.user:
            comment.delete()
            messages.success(
                request,
                'You have deleted the comment successfully.'
            )
        return redirect('singlearticle', slug=article_slug)

    return render(request, 'confirmdeletecomment.html', {'comment': comment})


class ArticleLike(View, LoginRequiredMixin):
    """
    This view will allow logged in users to
    like or unlike an article.
    """
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)

        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(reverse('singlearticle', args=[slug]))
