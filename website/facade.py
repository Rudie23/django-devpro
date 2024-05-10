from typing import List

from django.db.models import Prefetch

from website.modules.models import Module, Lesson


def list_ordered_modules() -> List[Module]:
    return list(Module.objects.order_by('title').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_lessons_from_ordered_modules(module: Module):
    # return all lesson objects related to module. The reason the reverse is a queryset is, ForeignKey is 1-to-many
    # relationship. Hence, the reverse is a queryset.
    return list(module.lesson_set.order_by('order').all())


def find_lesson(slug):
    # Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when
    # it executes its query. This is a performance booster which results in a single more complex query but means
    # later use of foreign-key relationships won’t require database queries.
    return Lesson.objects.select_related('module').get(slug=slug)


def list_modules_with_lessons():
    ordered_modules = Lesson.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(Prefetch('lesson_set', queryset=ordered_modules, to_attr='lessons')).all()
