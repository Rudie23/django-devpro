from model_bakery import baker
from django.urls import reverse
from website.django_assertions import assert_contains
from website.modules.models import Module
import pytest


@pytest.fixture
def module(db):
    return baker.make(Module, db)


@pytest.fixture
def resp(client, module):
    resp = client.get(reverse('modules:detail', kwargs={'slug': module.slug}))
    return resp


def test_title(resp, module: Module):
    assert_contains(resp, module.title)


def test_description(resp, module: Module):
    assert_contains(resp, module.description)


def test_public(resp, module: Module):
    assert_contains(resp, module.public)
