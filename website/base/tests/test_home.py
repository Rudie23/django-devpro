import pytest
from django.test import Client
from django.urls import reverse
from website.django_assertions import assert_contains


@pytest.fixture
def response(client: Client, db):
    resp = client.get(reverse('base:home'), db)
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Bootstrap 5</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Dev Pro</a>')
