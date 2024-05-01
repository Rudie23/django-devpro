import pytest
from django.urls import reverse
from django.test import Client
from model_bakery import baker

from website.django_assertions import assert_contains
from website.videos.models import Vimeo


@pytest.fixture
def video(db):
    # The make method also accepts a parameter _bulk_create to use Django’s bulk_create method instead of calling
    # obj.save() for each created instance.
    return baker.make(Vimeo)


@pytest.fixture
def resp(client: Client, video):
    return client.get(reverse('videos:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.title)


def test_content(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')


@pytest.fixture
def resp_video_not_found(client: Client, video):
    return client.get(reverse('videos:video', args=(video.slug + '-video-not-found',)))


def test_status_code_video_not_found(resp_video_not_found):
    assert resp_video_not_found.status_code == 404
