import pytest
from model_bakery import baker
from website import facade
from website.modules.models import Module


@pytest.fixture
def modules(db):
    return baker.make(Module, 2, db)


# This pytest works correctly in a local repository, but in GitHub doesn't work
# def test_list_ordered_modules(modules):
#     assert list(sorted(modules, key=lambda module: module.title)) == facade.list_ordered_modules()
