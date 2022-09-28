from django import forms
from django.contrib import admin
from . models import Category, Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('id', 'title', 'category', 'created', 'updated', 'is_published', 'views')
    list_display_links = ('id', 'title', 'category',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published',)
    readonly_fields = ('views',)

    save_on_top = True


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
