from django.db import models
from django.utils import timezone

# Create your models here.


class notes(models.Model):
    title = models.CharField(max_length=30)
    details = models.TextField(max_length=100)

    def __str__(self):
        return self.title
