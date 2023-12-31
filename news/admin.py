from django.contrib import admin
from .models import Article, Comment, ProductFamily
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    """
    This class allows admin to manage articles on the admin panel.
    """
    list_display = ('title', 'slug',
                    'status', 'created_on', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'product_name')
    search_fields = ['title', 'article_body', 'product_name']
    summernote_fields = ('article_body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage comments on the admin panel.
    """
    list_display = ('user', 'message', 'article',
                    'created_on', 'updated_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(ProductFamily)
class ProductFamilyAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage Product Family on the admin panel.
    It displays the product name, creation date and update date.
    """
    list_display = ('product_name', 'created_at', 'updated_at')
