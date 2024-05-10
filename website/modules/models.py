from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse


# Create your models here.

class Module(OrderedModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    public = models.TextField(max_length=128)
    description = models.TextField(max_length=512)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:detail', kwargs={'slug': self.slug})


class Lesson(OrderedModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    order_with_respect_to = 'module'
    vimeo_id = models.CharField(max_length=32)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:lesson', kwargs={'slug': self.slug})
