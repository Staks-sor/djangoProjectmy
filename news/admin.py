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

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="25">')
        else:
            return 'Рандомное фото'


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

admin.site.site_title = 'Админка епт'
admin.site.site_header = 'Какая то хуйня)'
