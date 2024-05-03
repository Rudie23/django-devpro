from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from website.modules.models import Module
# Register your models here.


@admin.register(Module)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
