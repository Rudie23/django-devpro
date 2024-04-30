import pytest
from django.urls import reverse

from website.videos.models import Vimeo
from website.django_assertions import assert_contains


# @pytest.fixture
# def videos(db):
#     v = [
#         Vimeo(slug='motivation', title='Motivation', vimeo_id='695001664'),
#         Vimeo(slug='windows-installation', title='Windows Installation', vimeo_id='251497668'),
#     ]
#     for video in v:
#         video.save()
#     return video
#
# def test_status_code(resp):
#     assert resp.status_code == 200
#
#
# @pytest.mark.parametrize(
#     'title',
#     [
#         'Motivation',
#         'Windows installation',
#     ]
# )
# def test_title_video(resp, title):
#     assert_contains(resp, title)
#
#
# @pytest.mark.parametrize(
#     'slug',
#     [
#         'motivation',
#         'windows-installation',
#     ]
# )
# def test_link_video(resp, slug):
#     video_link = reverse('videos:video', args=(slug,))
#     assert_contains(resp, f'href="{video_link}"')
