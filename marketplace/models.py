from django.db import models

class Pencil(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
