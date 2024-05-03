# Generated by Django 5.0.4 on 2024-05-03 15:41

from django.db import migrations
from django.utils.text import slugify


def fill_slug(apps, schema_editor):
    Module = apps.get_model('modules', 'Module')
    for module in Module.objects.all():
        module.slug = slugify(module.title)
        module.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_module_slug'),
    ]

    operations = [
        migrations.RunPython(fill_slug),
    ]
