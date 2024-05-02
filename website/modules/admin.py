from django.contrib import admin
from django.contrib.admin import ModelAdmin
from website.modules.models import Module
# Register your models here.


@admin.register(Module)
class ModuloAdmin(ModelAdmin):
    list_display = ('title', 'public')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
