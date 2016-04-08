from django.db import models
from django.core.urlresolvers import reverse
from ecom.events.models import Event

# Create your models here.

class Register(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("register:thanks", kwargs={"pk": self.pk})

