from django.contrib import admin

from website.grades.models import Grade


# Register your models here.

class EnrollmentInline(admin.TabularInline):
    model = Grade.students.through
    extra = 1
    readonly_fields = ('date',)
    autocomplete_fields = ('user',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
    list_display = ('name', 'slug', 'begin', 'end')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-begin',)
    search_fields = ('name',)
