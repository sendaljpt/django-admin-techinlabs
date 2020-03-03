import random
from datetime import datetime

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('sku')
        return self.readonly_fields

    def save(self):
        if not self.id:
            self.sku = generate_sku()
        super(Product, self).save()

    def __str__(self):
        return self.name


def random_number():
    t = datetime.now()
    str_time = t.strftime('%Y%m%d%H%I%S%f')
    rand_int = random.randint(1, int(str_time))

    return str(rand_int)

def generate_sku():
    prefix_so = 'SKU'
    year_month = datetime.now().strftime('%y%m')
    sku = '{}{}{}'.format(prefix_so, year_month, random_number()[:3])

    return sku