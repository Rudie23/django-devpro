from model_bakery import baker
from django.urls import reverse
from website.django_assertions import assert_contains
from website.modules.models import Module, Lesson
import pytest


@pytest.fixture
def module(db):
    return baker.make(Module)


@pytest.fixture
def lessons(module):
    return baker.make(Lesson, 3, module=module)


@pytest.fixture
def response(client, module, lessons):
    resp = client.get(reverse('modules:detail', kwargs={'slug': module.slug}))
    return resp


def test_title(response, module: Module):
    assert_contains(response, module.title)


def test_description(response, module: Module):
    assert_contains(response, module.description)


def test_public(response, module: Module):
    assert_contains(response, module.public)


def test_titles_of_lessons(response, lessons):
    for lesson in lessons:
        assert_contains(response, lesson.title)


def test_links_of_lessons(response, lessons):
    for lesson in lessons:
        assert_contains(response, lesson.get_absolute_url())
