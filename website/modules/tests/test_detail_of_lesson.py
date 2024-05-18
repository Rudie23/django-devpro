from model_bakery import baker
from django.urls import reverse
from website.django_assertions import assert_contains
from website.modules.models import Module, Lesson
import pytest


@pytest.fixture
def module(db):
    return baker.make(Module, db)


@pytest.fixture
def lesson(module):
    return baker.make(Lesson, module=module)


@pytest.fixture
def response(client_with_user_logged, lesson):
    return client_with_user_logged.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))


def test_title(response, lesson: Lesson):
    assert_contains(response, lesson.title)


def test_vimeo(response, lesson: Lesson):
    assert_contains(response, f'src="https://player.vimeo.com/video/{lesson.vimeo_id}"')


def test_module_breadcrumb(response, module: Module):
    assert_contains(response, f'<li class="breadcrumb-item"><a href="{module.get_absolute_url()}">{module.title}</a'
                              f'></li>')


@pytest.fixture
def resp_no_user_logged(client, lesson):
    resp = client.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_user_not_logged_redirect(resp_no_user_logged):
    assert resp_no_user_logged.status_code == 302
    assert resp_no_user_logged.url.startswith(reverse('login'))
