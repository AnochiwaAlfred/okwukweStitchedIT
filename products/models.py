from django.db import models

# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.BooleanField(default=False)
    discountedPrice = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    available = models.BooleanField(default=False)
    quantityAvailable = models.IntegerField()
    

    def __str__(self):
        return self.name
