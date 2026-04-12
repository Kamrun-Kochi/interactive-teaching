from django.contrib import admin
from .models import Article, MediaItem, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ['title', 'created_at']
    help_text = "In body, use [word|media_id] to make a word clickable."


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'order']