from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    desdription = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
