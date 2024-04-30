import pytest
from django.urls import reverse
from django.test import Client

from website.django_assertions import assert_contains
from website.videos.models import Vimeo


@pytest.fixture
def video(db):
    v = Vimeo(slug='motivation', title='Motivation', vimeo_id='695001664')
    v.save()
    return v


@pytest.fixture
def resp(client: Client, video):
    return client.get(reverse('videos:vimeo', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.title)


# def test_content(resp, video):
#     assert_contains(resp, f'<iframe src=f"https://player.vimeo.com/video/{video.vimeo_id}"')
