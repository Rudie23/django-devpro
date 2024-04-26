import pytest
from django.test import Client
from django.urls import reverse
from website.django_assertions import assert_contains


@pytest.fixture
def response(client):
    resp = client.get(reverse('base:index'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Bootstrap 5</title>')


def test_home_link(response):
    assert_contains(response, f'<a class="navbar-brand" href="{reverse('base:index')}">Dev Pro</a>')
