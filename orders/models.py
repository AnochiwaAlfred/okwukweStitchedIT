<<<<<<< HEAD
from django.db import models
import uuid
from django_countries import countries
# Create your models here.

class Order(models.Model):
    PAYMENTMETHOD = (
        ('Card', 'Card'),
        ('Paypal', 'Paypal'),
        ('Bank', 'Bank')
    )
    COUNTRY = tuple([(code, name) for code, name in countries])
    
    orderID = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.UUIDField(unique=True, blank=True, null=True, default=uuid.uuid4)
    orderItems = models.ManyToManyField('orderitems.OrderItem', related_name='orderitems')

    paymentMethod = models.CharField(max_length=6, choices=PAYMENTMETHOD, blank=False)
    streetAddress = models.CharField(max_length=255)
    apartmentAddress = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(verbose_name='Country', max_length=200, choices=COUNTRY, null=True, blank=True)
    
    def __str__(self):
        return f"Order {self.orderID}"

    @property
    def get_order_total(self):
        orderitems = self.orderItems_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    

    
    
=======
from django.db import models
import uuid
from django_countries import countries
# Create your models here.

class Order(models.Model):
    PAYMENTMETHOD = (
        ('Card', 'Card'),
        ('Paypal', 'Paypal'),
        ('Bank', 'Bank')
    )
    COUNTRY = tuple([(code, name) for code, name in countries])
    
    orderID = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.UUIDField(unique=True, blank=True, null=True, default=uuid.uuid4)
    orderItems = models.ManyToManyField('orderitems.OrderItem', related_name='orderitems')

    paymentMethod = models.CharField(max_length=6, choices=PAYMENTMETHOD, blank=False)
    streetAddress = models.CharField(max_length=255)
    apartmentAddress = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(verbose_name='Country', max_length=200, choices=COUNTRY, null=True, blank=True)
    
    def __str__(self):
        return f"Order {self.orderID}"

    @property
    def get_order_total(self):
        orderitems = self.orderItems_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    

    
    
>>>>>>> 4a8e8a410c304b57e382320e48a01d181f4dd41f
        