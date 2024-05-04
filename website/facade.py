from typing import List
from website.modules.models import Module, Lesson


def list_ordered_modules() -> List[Module]:
    return list(Module.objects.order_by('title').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_lessons_from_ordered_modules(module: Module):
    # return all lesson objects related to module
    return list(module.lesson_set.order_by('order').all())
