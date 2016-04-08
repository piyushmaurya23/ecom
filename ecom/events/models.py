from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    organiser = models.CharField(max_length=120)
    venue = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})

