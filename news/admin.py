from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'update_at',
        'is_published',
        'get_photo',
    )
    list_display_links = (
        'id', 'title'
    )
    search_fields = (
        'title',
        'content'
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'is_published',
        'category'
    )

    fields = (
        'title',
        'category',
        'content',
        'photo',
        'get_photo',
        'is_published',
        'views',
        'created_at',
        'update_at',
    )

    readonly_fields = (
        'get_photo',
        'views',
        'created_at',
        'update_at',
    )
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="25">')
        else:
            return 'Рандомное фото'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = (
        'id',
        'title'
    )
    search_fields = (
        'title',
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
"""Костыль времени"""
from datetime import datetime
from pytz import timezone
admin.site.site_title = 'Админка епт'
tz = timezone('Europe/Moscow')
dt = datetime.now(tz=tz)
hh = dt.strftime('Время:  %H:%M Дата: %d.%m.%Y года')
admin.site.site_header = f'Админ панель   {hh}'

