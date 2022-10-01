from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Категорія')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    content = models.TextField(max_length=10000, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    is_published = models.BooleanField(default=True, verbose_name='Показати/Сховати')
    views = models.IntegerField(default=0, verbose_name='Переглядів')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категорія')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
        ordering = ['-created']
