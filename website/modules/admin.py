from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from website.modules.models import Module, Lesson
# Register your models here.


@admin.register(Module)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Lesson)
class LessonAdmin(OrderedModelAdmin):
    list_display = ('title', 'module', 'move_up_down_links')
    list_filter = ('module',)
    ordering = ('module', 'order')
    prepopulated_fields = {'slug': ('title',)}
