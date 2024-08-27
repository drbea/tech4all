from django.contrib import admin

from .models import Article, Category, Comment
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']

    def get_queryset(self, request):
        """
        Override the default get_queryset method to prefetch related category 
        to avoid database queries for each article in the list view.
        """
        return super().get_queryset(request).select_related('category')
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for Comment model. 
    This class is used to customize the admin interface for Comment model.
    """
    # list display fields in the admin interface
    list_display = ['content', 'created_at', 'updated_at', 'article']

    def get_queryset(self, request):
        """
        Override the default get_queryset method to prefetch related article 
        to avoid database queries for each comment in the list view.
        """
        return super().get_queryset(request).select_related('article')
    
    def article(self, obj):
        """
        Return the title of the article related to the comment.
        """
        return obj.article.title

    # set the short description of the article field in the admin interface
    article.short_description = 'Article'
