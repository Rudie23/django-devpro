from typing import List

import pytest
from django.urls import reverse
from django.test import Client
from model_bakery import baker

from website.django_assertions import assert_contains
from website.modules.models import Lesson, Module


@pytest.fixture
def modules(db):
    return baker.make(Module, 2, db)


@pytest.fixture
def lessons(modules):
    lessons_list = list()
    for module in modules:
        lessons_list.extend(baker.make(Lesson, 3, module=module))
    return lessons_list


@pytest.fixture
def resp(client: Client, modules, lessons):
    return client.get(reverse('modules:index'))


def test_index_available(resp):
    assert resp.status_code == 200


def test_title(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.title)


def test_description(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.description)


def test_public(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.public)


def test_lessons_titles(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.title)


def test_lessons_urls(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.get_absolute_url())
