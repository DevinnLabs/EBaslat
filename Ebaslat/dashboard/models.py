from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    created_on = models.DateTimeField(auto_now_add = True)
    vendor = models.OneToOneField(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Store'

    def __str__(self):
        return self.name

# class ProductVariant(models.Model):
#     size = models.CharField(max_length = 20)
#     color = models.CharField(max_length = 20)
#     model = models.CharField(max_length = 20)

#     class Meta:
#         db_table = 'ProductVariant'

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits = 1000, decimal_places = 2)
#     image = models.ImageField()
#     notes = models.TextField()
#     productVariants = models.ManyToManyField(ProductVariant)
#     store = models.ManyToManyField(Store, through= ProductDetails)

#     class Meta:
#         db_table = 'Product'

#     def __str__(self):
#         return self.name

# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length = 254)
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'Customer'

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     date = models.DateTimeField(auto_now_add = True)
#     shipping_address = models.TextField()
#     billing_address = models.TextField()
#     final_price = models.PositiveIntegerField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'Order'

# class Cart(models.Model):
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'Cart'

# class Brand(models.Model):
#     name = models.CharField(max_length = 20)
#     image = models.ImageField()

#     class Meta:
#         db_table = 'Brand'

# class Category(models.Model):
#     name = models.CharField(max_length = 25)
#     parent_category = models.ForeignKey('self', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'Category'

# class ProductDetails(models.Model):
#     inventory = models.PositiveIntegerField()
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL)
#     order = models.ManyToManyField(Order, through=OrderDetails)

#     class Meta:
#         db_table = 'ProductDetails'

# class OrderDetails(models.Model):
#     discount = models.PositiveIntegerField()
#     order_quantity = models.PositiveIntegerField()
#     review = models.TextField()
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = 'OrderDetails'

