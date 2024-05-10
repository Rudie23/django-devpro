from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    begin = models.DateTimeField()
    end = models.DateTimeField()
    students = models.ManyToManyField(get_user_model(), through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'grade'),)
        ordering = ('grade', 'date',)
