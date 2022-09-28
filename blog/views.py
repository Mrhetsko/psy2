from django.db.models import F
from django.shortcuts import render, get_object_or_404
# from django.views.generic import TemplateView, ListView

from . models import Category, Article


def index(request):
    return render(request, 'blog/index.html')


def blog(request):
    return render(request, 'blog/blog.html')


def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category,
                                      is_published=True,
                                      )
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'blog/category.html', context)


def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id,
                                is_published=True,
                                )
    article.views = F('views') + 1
    article.save()
    context = {
        'article': article,
    }
    return render(request, 'blog/article.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contacts(request):
    return render(request, 'blog/contacts.html')





















