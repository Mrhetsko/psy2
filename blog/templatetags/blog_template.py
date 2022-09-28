from django import template
from django.shortcuts import get_object_or_404
from blog.models import Category, Article

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_articles():
    return Article.objects.filter(is_published=True)


@register.inclusion_tag('inc/_show_categories.html')
def show_all_categories():
    categories = Category.objects.all()
    return {'categories': categories}

