from django.http import HttpResponseNotFound
from django.shortcuts import render
from . models import Article, Category, Comment
from django.db.models import Q

# Create your views here.

def home_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    articles = Article.objects.filter(
        Q(title__icontains=q) |
        Q(content__icontains=q) |
        Q(category__name__icontains=q)
    )

    categories = Category.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, "blog/index.html", context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    """
    Handles GET and POST requests for article page.
    If GET, renders article page with all comments.
    If POST, creates a new comment and renders article page with all comments.
    """
    if request.method == 'POST':
        comment = request.POST.get('comment')    # Get comment from POST data
        Comment.objects.create(article=article, content=comment)     # Create a new comment
    
    comments = Comment.objects.filter(article=article)  # Get all comments for article

    context = {
        'article': article,
        'comments': comments
    }
    return render(request, "blog/article.html", context)

def create_article(request):
    return render(request, "blog/create.html")

def update_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return render(request, "blog/update.html", {'article': article})
    except Article.DoesNotExist:
        return HttpResponseNotFound('Article not found.')

def delete_article(request, article_id):
    return render(request, "blog/delete.html")

