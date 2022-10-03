from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contscts', views.contacts, name='contacts'),
    path('search', views.search_page, name='search-page'),
    path('cetrificates', views.certificates, name='certificates'),
    path('blog/category/<int:category_id>/', views.get_category, name="category"),
    path('blog/article/<int:article_id>/', views.get_article, name="article"),
]
