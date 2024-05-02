from django.db import models
from django.urls import reverse


# Create your models here.

class Module(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, max_length=64)
    public = models.TextField(max_length=128)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:detail', kwargs={'slug': self.slug})
