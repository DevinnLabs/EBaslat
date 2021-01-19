from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits = 1000, decimal_places = 2)
    product_image = models.ImageField()
    product_notes = models.TextField()
