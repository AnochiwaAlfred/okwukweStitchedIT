from django.db import models

# Create your models here.

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(blank=True, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.product.name

    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    def add(self):
        self.product.add(self.quantity)
        self.save()
            
    def reduce(self):
        self.product.reduce(self.quantity)
        self.save()
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


