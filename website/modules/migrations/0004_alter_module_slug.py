# Generated by Django 5.0.4 on 2024-05-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_filling_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
