from django.db import models
from .validators import positive_integer


class  Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[positive_integer])
    in_stock = models.BooleanField(default=True)
    available_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{ self.name} - ${ self.price}"