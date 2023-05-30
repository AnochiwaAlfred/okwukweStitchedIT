from django.db import models
from products.models import Product

# Create your models here.

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.product.name

    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


