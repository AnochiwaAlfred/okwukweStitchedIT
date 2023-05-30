from django.db import models
# from accounts.models import MyUser

# Create your models here.
class Address(models.Model):
    streetAddress = models.CharField(max_length=255)
    apartmentAddress = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='Nigeria')
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Address"

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'