from django.db import models
from accounts.models import MyUser

# Create your models here.

class OrderHistory(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    orderHistory = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)