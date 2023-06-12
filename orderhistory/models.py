from django.db import models

# Create your models here.

class OrderHistory(models.Model):
    orders = models.ManyToManyField('orders.Order', blank=True, related_name='orders')
    timeStamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Order History'
    
    def addOrder(self, order):
        self.orders.add(order)
        self.save()   
    
    def __str__(self):
        from accounts.models import MyUser
        user=MyUser.objects.get(orderHistory=self)
        return f"{user}'s Order History".upper()