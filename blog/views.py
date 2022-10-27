from django.db.models import F, Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views import generic
# from django.views.generic import TemplateView, ListView

from . models import Category, Article


# @cache_page(60 * 2)
def index(request):
    title = 'Hlavni stranka'
    context = {
        'title': title,
    }
    return render(request, 'blog/index.html', context)


# @cache_page(60)
def blog(request):
    title = 'Blog'
    articles = Article.objects.filter(is_published=True).select_related()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blog.html', context)


# @cache_page(60)
def get_category(request, category_id):
    # category = Category.objects.raw('SELECT * FROM category')
    articles = Article.objects.filter(category=category_id,
                                      is_published=True).select_related('category')
    context = {
        # 'category': category,
        'articles': articles,
    }
    return render(request, 'blog/category.html', context)


# @cache_page(60)
def get_article(request, article_id):
    article = get_object_or_404(Article.objects.select_related(),
                                id=article_id,
                                is_published=True,
                                )
    article.views = F('views') + 1
    article.save()
    context = {
        'article': article,
    }
    return render(request, 'blog/article.html', context)


# class ViewArticle(generic.DetailView):
#     model = Article
    

# @cache_page(60 * 2)
def about(request):
    title = 'O Mne'
    return render(request, 'blog/about.html', {'title': title})


# @cache_page(60 * 2)
def contacts(request):
    title = 'Kontakty'
    return render(request, 'blog/contacts.html', {'title': title})


def certificates(request):
    title = 'Certifikáty'
    return render(request, 'blog/certificates.html', {'title': title})


def search_page(request):
    if request.method == 'POST':
        q = request.POST.get('search') if request.POST.get('search') is not None else ''

        articles = Article.objects.filter(Q(title__icontains=q, is_published=True) |
                                          Q(category__title__icontains=q, is_published=True) |
                                          Q(content__icontains=q, is_published=True)
                                          )

        return render(request,
                      'blog/search_page.html',
                      {'articles': articles, 'q': q}
                      )
    else:
        return render(request,
                      'blog/search_page.html',
                      # context
                      )

    