from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    def _str_(self):
        return self.description