from django.contrib.admin import ModelAdmin, register

from website.videos.models import Vimeo


@register(Vimeo)
class VideoAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'created', 'vimeo_id')
    ordering = ('created',)
    prepopulated_fields = {'slug': ('title',)}
