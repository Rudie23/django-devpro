from typing import List
from website.modules.models import Module


def list_ordered_modules() -> List[Module]:
    return list(Module.objects.order_by('title').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)
