from django.db import models
from products.models import Product
from addresses.models import Address
from orderitems.models import OrderItem

# Create your models here.

class Order(models.Model):
    PAYMENTMETHOD = (
        ('Card', 'Card'),
        ('Paypal', 'Paypal'),
        ('Bank', 'Bank')
    )
    orderID = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    paymentMethod = models.CharField(max_length=6, choices=PAYMENTMETHOD, blank=False)
    billingAddress = models.ForeignKey(Address, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    shippingAddress = models.ForeignKey(Address, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    orderItems = models.ManyToManyField(OrderItem)
    
    def __str__(self):
        return str(self.orderID)

    @property
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
# 
    
    
        