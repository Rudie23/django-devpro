import pytest
from django.test import Client
from model_bakery import baker


@pytest.fixture
def user_logged(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='Fulano')
    return user_model


@pytest.fixture
def client_with_user_logged(user_logged, client: Client):
    client.force_login(user_logged)
    return client
