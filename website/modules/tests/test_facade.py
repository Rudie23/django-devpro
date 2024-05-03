import pytest
from model_bakery import baker
from website import facade
from website.modules.models import Module


@pytest.fixture
def modules(db):
    return baker.make(Module, 2, db)


def test_list_ordered_modules(modules):
    assert list(sorted(modules, key=lambda module: module.title)) == facade.list_ordered_modules()
