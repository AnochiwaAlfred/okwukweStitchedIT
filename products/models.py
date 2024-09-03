from django.db import models

# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='Description')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.BooleanField(default=False, null=True, blank=True)
    discountedPrice = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=0)
    image = models.ImageField(upload_to='product_images/')
    available = models.BooleanField(default=False)
    quantityAvailable = models.IntegerField()
    

    def __str__(self):
        return self.name

    def add(self, quantity):
        if quantity>0:
            self.quantityAvailable += quantity
            self.available=True
            self.save()
            
            
    
    def reduce(self, quantity):
        if self.quantityAvailable>=quantity:
            print(f"reducing {self} from {self.quantityAvailable} by {quantity}")
            self.quantityAvailable -= quantity
            self.save()
            if self.quantityAvailable==0:
                print(f"setting availability of  {self} from {self.available} to False")
                self.available=False
                self.save()
            