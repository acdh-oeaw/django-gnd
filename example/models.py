from django.db import models
from django.urls import reverse

from gnd.models import GndBaseModel


class MyText(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Person(GndBaseModel):
    title = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.id})
