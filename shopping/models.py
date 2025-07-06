from django.db import models
from products.models import Products
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    
    def calculate_price(self):
        total = 0
        for item in self.items.all():
            total += (item.product.price * item.quantity)
        self.total_price = total
    
    def save(self, *args, **kwargs):
        self.calculate_total()
        super().save(*args, **kwargs)

