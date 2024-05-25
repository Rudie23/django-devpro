import pytest
from django.urls import reverse
from django.test import Client
from model_bakery import baker
from website.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client: Client, db):
    return client.get(reverse('login'), db)


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model, db)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.password_plana = password
    return user_model


@pytest.fixture
def resp_post(client: Client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.password_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modules:index')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'), db)


def test_button_login_available(resp_home):
    assert_contains(resp_home, 'Sign in')


def test_link_of_login_available(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_with_user_logged(client_with_user_logged, db):
    return client_with_user_logged.get(reverse('base:home'), db)


def test_button_login_unavailable(resp_home_with_user_logged):
    assert_not_contains(resp_home_with_user_logged, 'Sign in')


def test_link_of_login_unavailable(resp_home_with_user_logged):
    assert_not_contains(resp_home_with_user_logged, reverse('login'))


def test_button_exit_available(resp_home_with_user_logged):
    assert_contains(resp_home_with_user_logged, 'logout')


def test_name_user_logged_available(resp_home_with_user_logged, user_logged):
    assert_contains(resp_home_with_user_logged, user_logged.first_name)


def test_link_of_logout_available(resp_home_with_user_logged):
    assert_contains(resp_home_with_user_logged, reverse('logout'))
