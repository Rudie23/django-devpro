from django.shortcuts import render, get_object_or_404

from website.videos.models import Vimeo


# Create your views here.

def index(request):
    videos = Vimeo.objects.order_by('created').all()
    return render(request, 'videos/index.html', context={'videos': videos})


def video_page(request, slug):
    video = get_object_or_404(Vimeo, slug=slug)
    return render(request, 'videos/video.html', context={'video': video})
