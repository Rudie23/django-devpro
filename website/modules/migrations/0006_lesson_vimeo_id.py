# Generated by Django 5.0.6 on 2024-05-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='vimeo_id',
            field=models.CharField(default=1, max_length=32),
        ),
    ]
