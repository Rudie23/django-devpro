import pytest
from django.urls import reverse
from django.test import Client
from model_bakery import baker

from website.modules.models import Module
from website.django_assertions import assert_contains


@pytest.fixture
def modules(db):
    return baker.make(Module, 2, db)


@pytest.fixture
def response(client: Client, modules):
    return client.get(reverse('base:home'))


def test_modules_titles(response, modules):
    for module in modules:
        assert_contains(response, module.title)


def test_links_titles(response, modules):
    for module in modules:
        assert_contains(response, module.get_absolute_url())
