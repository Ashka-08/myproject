from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_quant = models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)
    img = models.ImageField()

    def __str__(self):
        return f'ProductID: {self.pk} {self.name}, price: {self.price}'
    