from django.db import models
from django.urls import reverse


# Create your models here.

class Vimeo(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    vimeo_id = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('videos:video', args=(self.slug,))

    def __str__(self):
        return f'{self.title}'
