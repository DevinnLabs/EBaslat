from django.contrib import admin

# Register your models here.
from .models import * #Store #ProductVariant, Product, Customer, Order, Cart, Brand, Category, ProductDetails, OrderDetails

admin.site.register(Store)
# admin.site.register(ProductVariant)
# admin.site.register(Product)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(Cart)
# admin.site.register(Brand)
# admin.site.register(Category)
# admin.site.register(ProductDetails)
# admin.site.register(OrderDetails)