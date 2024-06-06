import pytest
from django.test import Client
from django.urls import reverse

from website.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client, db):
    return client.get(reverse('base:sign-up'), db)


def test_login_form_page(resp):
    assert resp.status_code == 200


def test_button_login_available(resp):
    assert_contains(resp, 'Sign up')


def test_link_of_login_available(resp):
    assert_contains(resp, reverse('base:sign-up'))
